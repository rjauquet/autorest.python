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


class ListBlobsResponse(Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param container_name: Required.
    :type container_name: str
    :param prefix: Required.
    :type prefix: str
    :param marker: Required.
    :type marker: str
    :param max_results: Required.
    :type max_results: int
    :param delimiter: Required.
    :type delimiter: str
    :param blobs: Required.
    :type blobs: ~xmlservice.models.Blobs
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'container_name': {'required': True},
        'prefix': {'required': True},
        'marker': {'required': True},
        'max_results': {'required': True},
        'delimiter': {'required': True},
        'blobs': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'name': 'ServiceEndpoint', 'attr': True}},
        'container_name': {'key': 'ContainerName', 'type': 'str', 'xml': {'name': 'ContainerName', 'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str', 'xml': {'name': 'Prefix'}},
        'marker': {'key': 'Marker', 'type': 'str', 'xml': {'name': 'Marker'}},
        'max_results': {'key': 'MaxResults', 'type': 'int', 'xml': {'name': 'MaxResults'}},
        'delimiter': {'key': 'Delimiter', 'type': 'str', 'xml': {'name': 'Delimiter'}},
        'blobs': {'key': 'Blobs', 'type': 'Blobs', 'xml': {'name': 'Blobs'}},
        'next_marker': {'key': 'NextMarker', 'type': 'str', 'xml': {'name': 'NextMarker'}},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(self, *, service_endpoint: str, container_name: str, prefix: str, marker: str, max_results: int, delimiter: str, blobs, next_marker: str, **kwargs) -> None:
        super(ListBlobsResponse, self).__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.container_name = container_name
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.delimiter = delimiter
        self.blobs = blobs
        self.next_marker = next_marker