# Copyright 2012 New Dream Network, LLC (DreamHost)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from oslo_middleware import request_id
from pecan import hooks

from zun.common import context
from zun.compute import api as compute_api
import zun.conf

CONF = zun.conf.CONF


class ContextHook(hooks.PecanHook):
    """Configures a request context and attaches it to the request.

    The following HTTP request headers are used:

    X-User-Name:
        Used for context.user_name.

    X-User-Id:
        Used for context.user_id.

    X-Project-Name:
        Used for context.project.

    X-Project-Id:
        Used for context.project_id.

    X-Auth-Token:
        Used for context.auth_token.

    X-Roles:
        Used for context.roles.
    """

    def before(self, state):
        headers = state.request.headers
        user_name = headers.get('X-User-Name')
        user_id = headers.get('X-User-Id')
        project = headers.get('X-Project-Name')
        project_id = headers.get('X-Project-Id')
        domain_id = headers.get('X-User-Domain-Id')
        domain_name = headers.get('X-User-Domain-Name')
        auth_token = headers.get('X-Auth-Token')
        roles = headers.get('X-Roles', '').split(',')
        auth_token_info = state.request.environ.get('keystone.token_info')
        req_id = state.request.environ.get(request_id.ENV_REQUEST_ID)

        state.request.context = context.make_context(
            auth_token=auth_token,
            auth_token_info=auth_token_info,
            request_id=req_id,
            user_name=user_name,
            user_id=user_id,
            project_name=project,
            project_id=project_id,
            domain_id=domain_id,
            domain_name=domain_name,
            roles=roles)


class RPCHook(hooks.PecanHook):
    """Attach the rpcapi object to the request so controllers can get to it."""

    def before(self, state):
        context = state.request.context
        state.request.compute_api = compute_api.API(context)


class NoExceptionTracebackHook(hooks.PecanHook):
    """Workaround rpc.common: deserialize_remote_exception.

    deserialize_remote_exception builds rpc exception traceback into error
    message which is then sent to the client. Such behavior is a security
    concern so this hook is aimed to cut-off traceback from the error message.
    """
    # NOTE(max_lobur): 'after' hook used instead of 'on_error' because
    # 'on_error' never fired for wsme+pecan pair. wsme @wsexpose decorator
    # catches and handles all the errors, so 'on_error' dedicated for unhandled
    # exceptions never fired.
    def after(self, state):
        # Omit empty body. Some errors may not have body at this level yet.
        if not state.response.body:
            return

        # Do nothing if there is no error.
        if 200 <= state.response.status_int < 400:
            return

        json_body = state.response.json
        # Do not remove traceback when server in debug mode (except 'Server'
        # errors when 'debuginfo' will be used for traces).
        if CONF.debug and json_body.get('faultcode') != 'Server':
            return

        title = json_body.get('title')
        traceback_marker = 'Traceback (most recent call last):'
        if title and (traceback_marker in title):
            # Cut-off traceback.
            title = title.split(traceback_marker, 1)[0]
            # Remove trailing newlines and spaces if any.
            json_body['title'] = title.rstrip()
            # Replace the whole json. Cannot change original one beacause it's
            # generated on the fly.
            state.response.json = json_body
