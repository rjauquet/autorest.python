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

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from . import models
try:
    from .auto_rest_report_service_async import AutoRestReportServiceAsyncMixin
except (SyntaxError, ImportError):
    class AutoRestReportServiceAsyncMixin:
        pass


class AutoRestReportServiceConfiguration(Configuration):
    """Configuration for AutoRestReportService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestReportServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestreportservice/{}'.format(VERSION))


class AutoRestReportService(AutoRestReportServiceAsyncMixin, object):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestReportServiceConfiguration

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestReportServiceConfiguration(base_url)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def get_report(
            self, qualifier=None, custom_headers=None, raw=False, **operation_config):
        """Get test coverage report.

        :param qualifier: If specified, qualifies the generated report further
         (e.g. '2.7' vs '3.5' in for Python). The only effect is, that
         generators that run all tests several times, can distinguish the
         generated reports.
        :type qualifier: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: dict or ClientRawResponse if raw=true
        :rtype: dict[str, int] or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<report.models.ErrorException>`
        """
        # Construct URL
        url = self.get_report.metadata['url']

        # Construct parameters
        query_parameters = {}
        if qualifier is not None:
            query_parameters['qualifier'] = self._serialize.query("qualifier", qualifier, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('{int}', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_report.metadata = {'url': '/report'}
