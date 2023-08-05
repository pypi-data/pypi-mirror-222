# Copyright (c) 2017 Intel, Inc.
# Copyright (c) 2017 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import collections

from oslo_config import cfg
from oslo_log import log as logging
from oslo_serialization import jsonutils

from zun.common import exception
from zun import objects
from zun.objects import fields
from zun.pci import stats
from zun.pci import whitelist

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class PciDevTracker(object):
    """Manage pci devices in a compute node.

    This class fetches pci passthrough information from compute node
    and tracks the usage of these devices.

    It's called by compute node resource tracker to allocate and free
    devices to/from containers, and to update the available pci passthrough
    devices information from compute node periodically.

    `pci_devs` attribute of this class is the in-memory "master copy" of all
    devices on each compute node, and all data changes that happen when
    claiming/allocating/freeing
    devices HAVE TO be made against container contained in `pci_devs` list,
    because they are periodically flushed to the DB when the save()
    method is called.

    It is unsafe to fetch PciDevice objects elsewhere in the code for update
    purposes as those changes will end up being overwritten when the `pci_devs`
    are saved.
    """

    def __init__(self, context, node_id=None):
        """Create a pci device tracker.

        If a node_id is passed in, it will fetch pci devices information
        from database, otherwise, it will create an empty devices list
        and the resource tracker will update the node_id information later.
        """

        super(PciDevTracker, self).__init__()
        self.stale = {}
        self.node_id = node_id
        self.dev_filter = whitelist.Whitelist(CONF.pci.passthrough_whitelist)
        self.stats = stats.PciDeviceStats(dev_filter=self.dev_filter)
        self._context = context
        if node_id:
            self.pci_devs = objects.PciDevice.list_by_compute_node(
                context, node_id)
        else:
            self.pci_devs = []
        self._build_device_tree(self.pci_devs)
        self._initial_instance_usage()

    def _initial_instance_usage(self):
        self.allocations = collections.defaultdict(list)
        self.claims = collections.defaultdict(list)
        for dev in self.pci_devs:
            uuid = dev.container_uuid
            if dev.status == fields.PciDeviceStatus.CLAIMED:
                self.claims[uuid].append(dev)
            elif dev.status == fields.PciDeviceStatus.ALLOCATED:
                self.allocations[uuid].append(dev)
            elif dev.status == fields.PciDeviceStatus.AVAILABLE:
                self.stats.add_device(dev)

    def save(self):
        for dev in self.pci_devs:
            if dev.obj_what_changed():
                dev.save()
                if dev.status == fields.PciDeviceStatus.DELETED:
                    self.pci_devs.remove(dev)

    @property
    def pci_stats(self):
        return self.stats

    def update_devices_from_compute_resources(self, devices_json):
        """Sync the pci device tracker with compute node information.

        To support pci device hot plug, we sync with the compute node
        periodically, fetching all devices information from compute node,
        update the tracker and sync the DB information.

        Devices should not be hot-plugged when assigned to a container,
        but possibly the compute node has no such guarantee. The best
        we can do is to give a warning if a device is changed
        or removed while assigned.

        :param devices_json: The JSON-ified string of device information
                             that is returned from the compute node.
        """

        devices = []
        for dev in jsonutils.loads(devices_json):
            if self.dev_filter.device_assignable(dev):
                devices.append(dev)
        self._set_hvdevs(devices)

    @staticmethod
    def _build_device_tree(all_devs):
        """Build a tree of devices that represents parent-child relationships.

        We need to have the relationships set up so that we can easily make
        all the necessary changes to parent/child devices without having to
        figure it out at each call site.

        This method just adds references to relevant containers already found
        in `pci_devs` to `child_devices` and `parent_device` fields of each
        one.

        Currently relationships are considered for SR-IOV PFs/VFs only.
        """

        # Ensures that devices are ordered in ASC so VFs will come
        # after their PFs.
        all_devs.sort(key=lambda x: x.address)

        parents = {}
        for dev in all_devs:
            if dev.status in (fields.PciDeviceStatus.REMOVED,
                              fields.PciDeviceStatus.DELETED):
                # NOTE(ndipanov): Removed devs are pruned from
                # self.pci_devs on save() so we need to make sure we
                # are not looking at removed ones as we may build up
                # the tree sooner than they are pruned.
                continue
            if dev.dev_type == fields.PciDeviceType.SRIOV_PF:
                dev.child_devices = []
                parents[dev.address] = dev
            elif dev.dev_type == fields.PciDeviceType.SRIOV_VF:
                dev.parent_device = parents.get(dev.parent_addr)
                if dev.parent_device:
                    parents[dev.parent_addr].child_devices.append(dev)

    def _set_hvdevs(self, devices):
        exist_addrs = set([dev.address for dev in self.pci_devs])
        new_addrs = set([dev['address'] for dev in devices])

        for existed in self.pci_devs:
            if existed.address in exist_addrs - new_addrs:
                try:
                    existed.remove()
                except exception.PciDeviceInvalidStatus as e:
                    LOG.warning(("Trying to remove device with %(status)s "
                                 "ownership %(instance_uuid)s because of "
                                 "%(pci_exception)s"),
                                {'status': existed.status,
                                 'container_uuid': existed.container_uuid,
                                 'pci_exception': e.format_message()})
                    # Note(yjiang5): remove the device by force so that
                    # db entry is cleaned in next sync.
                    existed.status = fields.PciDeviceStatus.REMOVED
                else:
                    # Note(yjiang5): no need to update stats if an assigned
                    # device is hot removed.
                    self.stats.remove_device(existed)
            else:
                new_value = next((dev for dev in devices if
                                 dev['address'] == existed.address))
                new_value['compute_node_id'] = self.node_id
                if existed.status in (fields.PciDeviceStatus.CLAIMED,
                                      fields.PciDeviceStatus.ALLOCATED):
                    # Pci properties may change while assigned because of
                    # hotplug or config changes. Although normally this should
                    # not happen.

                    # As the devices have been assigned to a container,
                    # we defer the change till the container is destroyed.
                    # We will not sync the new properties with database
                    # before that.

                    # TODO(yjiang5): Not sure if this is a right policy, but
                    # at least it avoids some confusion and, if needed,
                    # we can add more action like killing the container
                    # by force in future.
                    self.stale[new_value['address']] = new_value
                else:
                    existed.update_device(new_value)

        for dev in [dev for dev in devices if
                    dev['address'] in new_addrs - exist_addrs]:
            dev['compute_node_uuid'] = self.node_id
            dev_obj = objects.PciDevice.create(self._context, dev)
            self.pci_devs.append(dev_obj)
            self.stats.add_device(dev_obj)

        self._build_device_tree(self.pci_devs)

    def _claim_container(self, context, container_uuid, pci_requests):
        devs = self.stats.consume_requests(pci_requests.requests)
        if not devs:
            return None

        for dev in devs:
            dev.claim(container_uuid)
        return devs

    def _allocate_container(self, container, devs):
        for dev in devs:
            dev.allocate(container)

    def allocate_container(self, container):
        devs = self.claims.pop(container.uuid, [])
        self._allocate_container(container, devs)
        if devs:
            self.allocations[container.uuid] += devs

    def claim_container(self, context, container_uuid, pci_requests):
        devs = []
        if self.pci_devs and pci_requests and pci_requests.requests:
            devs = self._claim_container(context, container_uuid, pci_requests)
            if devs:
                self.claims[container_uuid] = devs
        return devs

    def free_device(self, dev, container):
        """Free device from pci resource tracker

        :param dev: cloned pci device object that needs to be free
        :param container: the container that this pci device
                          is allocated to
        """
        for pci_dev in self.pci_devs:
            # Find the matching pci device in the pci resource tracker.
            # Once found, free it.
            if (dev.id == pci_dev.id and
                    dev.container_uuid == container.uuid):
                self._remove_device_from_pci_mapping(
                    container.uuid, pci_dev, self.allocations)
                self._remove_device_from_pci_mapping(
                    container.uuid, pci_dev, self.claims)
                self._free_device(pci_dev)
                break

    def _remove_device_from_pci_mapping(self, container_uuid,
                                        pci_device, pci_mapping):
        """Remove a PCI device from allocations or claims.

        If there are no more PCI devices, pop the uuid.
        """
        pci_devices = pci_mapping.get(container_uuid, [])
        if pci_device in pci_devices:
            pci_devices.remove(pci_device)
            if len(pci_devices) == 0:
                pci_mapping.pop(container_uuid, None)

    def _free_device(self, dev, container=None):
        freed_devs = dev.free(container)
        stale = self.stale.pop(dev.address, None)
        if stale:
            dev.update_device(stale)
        for dev in freed_devs:
            self.stats.add_device(dev)

    def _free_container(self, container):
        for dev in self.pci_devs:
            if dev.status in (fields.PciDeviceStatus.CLAIMED,
                              fields.PciDeviceStatus.ALLOCATED):
                if dev.container_uuid == container.uuid:
                    self._free_device(dev)

    def free_container(self, context, container):
        if self.allocations.pop(container.uuid, None):
            self._free_container(container)
        elif self.claims.pop(container.uuid, None):
            self._free_container(container)

    def update_pci_for_container(self, context, container, sign):
        """Update PCI usage information if devices are de/allocated."""
        if not self.pci_devs:
            return

        if sign == -1:
            self.free_container(context, container)
        if sign == 1:
            self.allocate_container(container)

    def clean_usage(self, containers, orphans):
        """Remove all usages for containers not passed in the parameter.

        The caller should hold the COMPUTE_RESOURCE_SEMAPHORE lock
        """
        existed = set(cnt['uuid'] for cnt in containers)
        existed |= set(cnt['uuid'] for cnt in orphans)

        # need to copy keys, because the dict is modified in the loop body
        for uuid in list(self.claims):
            if uuid not in existed:
                devs = self.claims.pop(uuid, [])
                for dev in devs:
                    self._free_device(dev)
        # need to copy keys, because the dict is modified in the loop body
        for uuid in list(self.allocations):
            if uuid not in existed:
                devs = self.allocations.pop(uuid, [])
                for dev in devs:
                    self._free_device(dev)


def get_container_pci_devs(cnt, request_id=None):
    """Get the devices allocated to one or all requests for a container.

    - For generic PCI request, the request id is None.
    - For sr-iov networking, the request id is a valid uuid
    - There are a couple of cases where all the PCI devices allocated to a
      container need to be returned.
    """
    pci_devices = cnt.pci_devices
    if pci_devices is None:
        return []
    return [device for device in pci_devices
            if device.request_id == request_id or request_id == 'all']
