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


class SignedIdentifier(Model):
    """signed identifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. a unique id
    :type id: str
    :param access_policy: Required. The access policy
    :type access_policy: ~xmlservice.models.AccessPolicy
    """

    _validation = {
        'id': {'required': True},
        'access_policy': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str', 'xml': {'name': 'Id'}},
        'access_policy': {'key': 'AccessPolicy', 'type': 'AccessPolicy', 'xml': {'name': 'AccessPolicy'}},
    }
    _xml_map = {
        'name': 'SignedIdentifier'
    }

    def __init__(self, *, id: str, access_policy, **kwargs) -> None:
        super(SignedIdentifier, self).__init__(**kwargs)
        self.id = id
        self.access_policy = access_policy
