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

import itertools

from zun.api.controllers import link
from zun.common.policies import registry as policies


_basic_keys = (
    'uuid',
    'user_id',
    'project_id',
    'name',
    'domain',
    'username',
    'password',
    'links',
)


def format_registry(context, url, registry):
    def transform(key, value):
        if key not in _basic_keys:
            return
        # strip the key if it is not allowed by policy
        policy_action = policies.REGISTRY % ('get_one:%s' % key)
        if not context.can(policy_action, fatal=False, might_not_exist=True):
            return
        if key == 'uuid':
            yield ('uuid', value)
            if url:
                yield ('links', [link.make_link(
                    'self', url, 'registries', value),
                    link.make_link(
                        'bookmark', url,
                        'registries', value,
                        bookmark=True)])
        elif key == 'password':
            yield ('password', '***')
        else:
            yield (key, value)

    return dict(itertools.chain.from_iterable(
        transform(k, v) for k, v in registry.items()))
