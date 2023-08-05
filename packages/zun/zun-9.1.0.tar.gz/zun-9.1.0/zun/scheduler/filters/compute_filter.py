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

from oslo_log.log import logging

from zun.api import servicegroup
from zun.scheduler import filters

LOG = logging.getLogger(__name__)


class ComputeFilter(filters.BaseHostFilter):
    """Filter on active Compute nodes"""

    def __init__(self):
        self.servicegroup_api = servicegroup.ServiceGroup()
        super(ComputeFilter, self).__init__()

    # Host state does not change within a request
    run_filter_once_per_request = True

    def host_passes(self, host_state, container, extra_spec):
        """Returns True for only active compute nodes"""
        service = host_state.service
        if service.disabled:
            LOG.debug('%(host_state)s is disabled, reason: %(reason)s',
                      {'host_state': host_state.hostname,
                       'reason': service.disabled_reason or 'Unknow'})
            return False
        else:
            if not self.servicegroup_api.service_is_up(service):
                LOG.warning('%(host_state)s has not been heard from in '
                            'a while', {'host_state': host_state.hostname})
                return False
        return True
