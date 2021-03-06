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

from .fish import Fish


class Shark(Fish):
    """Shark.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Sawshark, Goblinshark, Cookiecuttershark

    All required parameters must be populated in order to send to Azure.

    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: datetime
    """

    _validation = {
        'length': {'required': True},
        'fishtype': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'age': {'key': 'age', 'type': 'int'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
    }

    _subtype_map = {
        'fishtype': {'sawshark': 'Sawshark', 'goblin': 'Goblinshark', 'cookiecuttershark': 'Cookiecuttershark'}
    }

    def __init__(self, **kwargs):
        super(Shark, self).__init__(**kwargs)
        self.age = kwargs.get('age', None)
        self.birthday = kwargs.get('birthday', None)
        self.fishtype = 'shark'
