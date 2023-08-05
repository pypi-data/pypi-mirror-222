# Copyright 2013 Rackspace Hosting
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
from oslo_concurrency import processutils
from oslo_service import service as openstack_service

from trove.cmd.common import with_initialize
from trove.conductor import api as conductor_api


@with_initialize
def main(conf):
    from trove.common import notification
    from trove.common.rpc import conductor_host_serializer as sz
    from trove.common.rpc import service as rpc_service
    from trove.instance import models as inst_models

    notification.DBaaSAPINotification.register_notify_callback(
        inst_models.persist_instance_fault)
    topic = conf.conductor_queue
    server = rpc_service.RpcService(
        key=None, manager=conf.conductor_manager, topic=topic,
        rpc_api_version=conductor_api.API.API_LATEST_VERSION,
        secure_serializer=sz.ConductorHostSerializer)
    workers = conf.trove_conductor_workers or processutils.get_worker_count()
    launcher = openstack_service.launch(conf, server, workers=workers,
                                        restart_method='mutate')
    launcher.wait()
