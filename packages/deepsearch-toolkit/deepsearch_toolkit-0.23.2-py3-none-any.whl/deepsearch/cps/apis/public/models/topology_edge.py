# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.public.configuration import Configuration


class TopologyEdge(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'source': 'list[str]',
        'target': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, name=None, source=None, target=None, local_vars_configuration=None):  # noqa: E501
        """TopologyEdge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._source = None
        self._target = None
        self.discriminator = None

        self.name = name
        self.source = source
        self.target = target

    @property
    def name(self):
        """Gets the name of this TopologyEdge.  # noqa: E501


        :return: The name of this TopologyEdge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TopologyEdge.


        :param name: The name of this TopologyEdge.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def source(self):
        """Gets the source of this TopologyEdge.  # noqa: E501


        :return: The source of this TopologyEdge.  # noqa: E501
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TopologyEdge.


        :param source: The source of this TopologyEdge.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def target(self):
        """Gets the target of this TopologyEdge.  # noqa: E501


        :return: The target of this TopologyEdge.  # noqa: E501
        :rtype: list[str]
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this TopologyEdge.


        :param target: The target of this TopologyEdge.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TopologyEdge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopologyEdge):
            return True

        return self.to_dict() != other.to_dict()
