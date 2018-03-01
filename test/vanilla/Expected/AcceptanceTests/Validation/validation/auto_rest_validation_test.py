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
from .operations import AutoRestValidationTestOperationsMixin
from msrest.exceptions import HttpOperationError
from . import models


class AutoRestValidationTestConfiguration(Configuration):
    """Configuration for AutoRestValidationTest
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestValidationTestConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestvalidationtest/{}'.format(VERSION))

        self.subscription_id = subscription_id


class AutoRestValidationTest(AutoRestValidationTestOperationsMixin, object):
    """Test Infrastructure for AutoRest. No server backend exists for these tests.

    :ivar config: Configuration for client.
    :vartype config: AutoRestValidationTestConfiguration

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        self.config = AutoRestValidationTestConfiguration(subscription_id, base_url)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

