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

from msrest.pipeline import ClientRawResponse

from .. import models


class PetsOperations(object):
    """PetsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create_ap_true(
            self, create_parameters, custom_headers=None, raw=False, **operation_config):
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PetAPTrue or ClientRawResponse if raw=true
        :rtype: ~additionalproperties.models.PetAPTrue or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<additionalproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.create_ap_true.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPTrue')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PetAPTrue', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_ap_true.metadata = {'url': '/additionalProperties/true'}

    def create_ap_object(
            self, create_parameters, custom_headers=None, raw=False, **operation_config):
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PetAPObject or ClientRawResponse if raw=true
        :rtype: ~additionalproperties.models.PetAPObject or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<additionalproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.create_ap_object.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPObject')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PetAPObject', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_ap_object.metadata = {'url': '/additionalProperties/type/object'}

    def create_ap_string(
            self, create_parameters, custom_headers=None, raw=False, **operation_config):
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: ~additionalproperties.models.PetAPString
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PetAPString or ClientRawResponse if raw=true
        :rtype: ~additionalproperties.models.PetAPString or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<additionalproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.create_ap_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPString')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PetAPString', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_ap_string.metadata = {'url': '/additionalProperties/type/string'}

    def create_ap_in_properties(
            self, create_parameters, custom_headers=None, raw=False, **operation_config):
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters:
         ~additionalproperties.models.PetAPInProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PetAPInProperties or ClientRawResponse if raw=true
        :rtype: ~additionalproperties.models.PetAPInProperties or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<additionalproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.create_ap_in_properties.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPInProperties')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PetAPInProperties', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_ap_in_properties.metadata = {'url': '/additionalProperties/in/properties'}

    def create_ap_in_properties_with_ap_string(
            self, create_parameters, custom_headers=None, raw=False, **operation_config):
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters:
         ~additionalproperties.models.PetAPInPropertiesWithAPString
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PetAPInPropertiesWithAPString or ClientRawResponse if
         raw=true
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<additionalproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.create_ap_in_properties_with_ap_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(create_parameters, 'PetAPInPropertiesWithAPString')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PetAPInPropertiesWithAPString', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_ap_in_properties_with_ap_string.metadata = {'url': '/additionalProperties/in/properties/with/additionalProperties/string'}
