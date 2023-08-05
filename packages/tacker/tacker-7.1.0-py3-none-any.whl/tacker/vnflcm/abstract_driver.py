# Copyright (C) 2020 NTT DATA
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

import abc


class VnfInstanceAbstractDriver(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def instantiate_vnf(self, context, vnf_instance_id, instantiate_vnf_req):
        """instantiate vnf request.

        :param context: context
        :param vnf_instance_id: uuid of vnf_instance
        :param instantiate_vnf_req: object of InstantiateVnfRequest
        :return: None
        """
        pass

    @abc.abstractmethod
    def terminate_vnf(self, context, vnf_instance, terminate_vnf_req):
        """terminate vnf request.

        :param context: the request context
        :param vnf_instance: object of VnfInstance
        :param terminate_vnf_req: object of TerminateVnfRequest
        :return: None
        """
        pass
