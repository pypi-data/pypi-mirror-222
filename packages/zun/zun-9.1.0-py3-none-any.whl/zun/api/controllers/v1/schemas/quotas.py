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

common_quota = {
    'type': ['integer', 'string'],
    'pattern': '^-?[0-9]+$',
    # -1 is a flag value for unlimited
    'minimum': -1
}

quota_resources = {
    'containers': common_quota,
    'memory': common_quota,
    'cpu': common_quota,
    'disk': common_quota
}

query_param_update = {
    'type': 'object',
    'properties': quota_resources,
    'additionalProperties': False
}
