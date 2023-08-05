# Copyright 2017 Eayun, Inc.
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
#

from trove.extensions.common.views import UserView


class RedisRootCreatedView(UserView):
    def __init__(self, user, failed_slaves):
        self.failed_slaves = failed_slaves
        super(RedisRootCreatedView, self).__init__(user)

    def data(self):
        user_dict = {
            "name": self.user.name,
            "password": self.user.password
        }
        return {"user": user_dict, "failed_slaves": self.failed_slaves}
