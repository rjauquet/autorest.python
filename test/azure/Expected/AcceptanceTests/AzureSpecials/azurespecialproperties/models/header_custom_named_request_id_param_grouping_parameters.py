# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HeaderCustomNamedRequestIdParamGroupingParameters(Model):
    """Additional parameters for custom_named_request_id_param_grouping operation.

    All required parameters must be populated in order to send to Azure.

    :param foo_client_request_id: Required. The fooRequestId
    :type foo_client_request_id: str
    """

    _validation = {
        'foo_client_request_id': {'required': True},
    }

    _attribute_map = {
        'foo_client_request_id': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HeaderCustomNamedRequestIdParamGroupingParameters, self).__init__(**kwargs)
        self.foo_client_request_id = kwargs.get('foo_client_request_id', None)
