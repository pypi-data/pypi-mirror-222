#    Copyright 2017 Linaro Limited
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

from oslo_log import log as logging
import sys

from zun.common import config
from zun.common import service as zun_service
import zun.conf
from zun.websocket import websocketproxy

CONF = zun.conf.CONF
LOG = logging.getLogger(__name__)


def main():
    zun_service.prepare_service(sys.argv)
    config.parse_args(sys.argv)
    LOG.info("start websocket proxy")

    host = CONF.websocket_proxy.wsproxy_host
    port = CONF.websocket_proxy.wsproxy_port
    websocketproxy.ZunWebSocketProxy(
        listen_host=host,
        listen_port=port,
        cert=CONF.websocket_proxy.cert,
        key=CONF.websocket_proxy.key,
        ssl_only=CONF.websocket_proxy.ssl_only,
        file_only=True,
        RequestHandlerClass=websocketproxy.ZunProxyRequestHandler
    ).start_server()
