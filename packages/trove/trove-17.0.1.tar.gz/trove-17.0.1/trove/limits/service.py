# Copyright 2013 OpenStack Foundation
# Copyright 2013 Hewlett-Packard Development Company, L.P.
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

from trove.common import policy
from trove.common import wsgi
from trove.limits import views
from trove.quota.quota import QUOTAS


class LimitsController(wsgi.Controller):
    """
    Controller for accessing limits in the OpenStack API.
    """

    def index(self, req, tenant_id):
        """
        Return all absolute and rate limit information.
        """
        context = req.environ[wsgi.CONTEXT_KEY]
        policy.authorize_on_tenant(context, 'limits:index')
        quotas = QUOTAS.get_all_quotas_by_tenant(tenant_id)
        abs_limits = {k: v['hard_limit'] for k, v in quotas.items()}
        rate_limits = req.environ.get("trove.limits", [])

        return wsgi.Result(views.LimitViews(abs_limits,
                                            rate_limits).data(), 200)
