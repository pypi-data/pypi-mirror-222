# Copyright 2015 Tesora Inc.
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

from oslo_log import log as logging

from trove.common.strategies.cluster import base
from trove.guestagent import api as guest_api


LOG = logging.getLogger(__name__)


class CassandraGuestAgentStrategy(base.BaseGuestAgentStrategy):

    @property
    def guest_client_class(self):
        return CassandraGuestAgentAPI


class CassandraGuestAgentAPI(guest_api.API):
    """Cluster Specific Datastore Guest API

    **** VERSION CONTROLLED API ****

    The methods in this class are subject to version control as
    coordinated by guestagent/api.py.  Whenever a change is made to
    any API method in this class, add a version number and comment
    to the top of guestagent/api.py and use the version number as
    appropriate in this file
    """

    def get_data_center(self):
        LOG.debug("Retrieving the data center for node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("get_data_center", self.agent_low_timeout,
                          version=version)

    def get_rack(self):
        LOG.debug("Retrieving the rack for node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("get_rack", self.agent_low_timeout,
                          version=version)

    def set_seeds(self, seeds):
        LOG.debug("Configuring the gossip seeds for node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("set_seeds", self.agent_low_timeout,
                          version=version, seeds=seeds)

    def get_seeds(self):
        LOG.debug("Retrieving the gossip seeds for node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("get_seeds", self.agent_low_timeout,
                          version=version)

    def set_auto_bootstrap(self, enabled):
        LOG.debug("Setting the auto-bootstrap to '%(enabled)s' "
                  "for node: %(id)s", {'enabled': enabled, 'id': self.id})
        version = guest_api.API.API_BASE_VERSION

        return self._call("set_auto_bootstrap", self.agent_low_timeout,
                          version=version, enabled=enabled)

    def cluster_complete(self):
        LOG.debug("Sending a setup completion notification for node: %s",
                  self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("cluster_complete", self.agent_high_timeout,
                          version=version)

    def node_cleanup_begin(self):
        LOG.debug("Signaling the node to prepare for cleanup: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("node_cleanup_begin", self.agent_low_timeout,
                          version=version)

    def node_cleanup(self):
        LOG.debug("Running cleanup on node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._cast('node_cleanup', version=version)

    def node_decommission(self):
        LOG.debug("Decommission node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._cast("node_decommission", version=version)

    def cluster_secure(self, password):
        LOG.debug("Securing the cluster via node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call(
            "cluster_secure", self.agent_high_timeout,
            version=version, password=password)

    def get_admin_credentials(self):
        LOG.debug("Retrieving the admin credentials from node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("get_admin_credentials", self.agent_low_timeout,
                          version=version)

    def store_admin_credentials(self, admin_credentials):
        LOG.debug("Storing the admin credentials on node: %s", self.id)
        version = guest_api.API.API_BASE_VERSION

        return self._call("store_admin_credentials",
                          self.agent_low_timeout,
                          version=version,
                          admin_credentials=admin_credentials)
