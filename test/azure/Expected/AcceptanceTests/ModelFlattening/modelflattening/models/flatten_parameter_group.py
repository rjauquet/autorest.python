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


class FlattenParameterGroup(Model):
    """Additional parameters for put_simple_product_with_grouping operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Product name with value 'groupproduct'
    :type name: str
    :param product_id: Required. Unique identifier representing a specific
     product for a given latitude & longitude. For example, uberX in San
     Francisco will have a different product_id than uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    :param max_product_display_name: Required. Display name of product.
    :type max_product_display_name: str
    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odatavalue: URL value.
    :type odatavalue: str
    """

    _validation = {
        'name': {'required': True},
        'product_id': {'required': True},
        'max_product_display_name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': '', 'type': 'str'},
        'product_id': {'key': '', 'type': 'str'},
        'description': {'key': '', 'type': 'str'},
        'max_product_display_name': {'key': '', 'type': 'str'},
        'generic_value': {'key': '', 'type': 'str'},
        'odatavalue': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FlattenParameterGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.product_id = kwargs.get('product_id', None)
        self.description = kwargs.get('description', None)
        self.max_product_display_name = kwargs.get('max_product_display_name', None)
        self.generic_value = kwargs.get('generic_value', None)
        self.odatavalue = kwargs.get('odatavalue', None)
