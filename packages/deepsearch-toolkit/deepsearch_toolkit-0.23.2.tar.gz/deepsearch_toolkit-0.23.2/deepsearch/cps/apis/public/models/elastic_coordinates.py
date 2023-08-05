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


class ElasticCoordinates(object):
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
        'ca_certificate_base64': 'str',
        'dangerously_disable_ssl_validation': 'bool',
        'hosts': 'list[str]'
    }

    attribute_map = {
        'ca_certificate_base64': 'ca_certificate_base64',
        'dangerously_disable_ssl_validation': 'dangerously_disable_ssl_validation',
        'hosts': 'hosts'
    }

    def __init__(self, ca_certificate_base64=None, dangerously_disable_ssl_validation=None, hosts=None, local_vars_configuration=None):  # noqa: E501
        """ElasticCoordinates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ca_certificate_base64 = None
        self._dangerously_disable_ssl_validation = None
        self._hosts = None
        self.discriminator = None

        if ca_certificate_base64 is not None:
            self.ca_certificate_base64 = ca_certificate_base64
        if dangerously_disable_ssl_validation is not None:
            self.dangerously_disable_ssl_validation = dangerously_disable_ssl_validation
        self.hosts = hosts

    @property
    def ca_certificate_base64(self):
        """Gets the ca_certificate_base64 of this ElasticCoordinates.  # noqa: E501


        :return: The ca_certificate_base64 of this ElasticCoordinates.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate_base64

    @ca_certificate_base64.setter
    def ca_certificate_base64(self, ca_certificate_base64):
        """Sets the ca_certificate_base64 of this ElasticCoordinates.


        :param ca_certificate_base64: The ca_certificate_base64 of this ElasticCoordinates.  # noqa: E501
        :type: str
        """

        self._ca_certificate_base64 = ca_certificate_base64

    @property
    def dangerously_disable_ssl_validation(self):
        """Gets the dangerously_disable_ssl_validation of this ElasticCoordinates.  # noqa: E501


        :return: The dangerously_disable_ssl_validation of this ElasticCoordinates.  # noqa: E501
        :rtype: bool
        """
        return self._dangerously_disable_ssl_validation

    @dangerously_disable_ssl_validation.setter
    def dangerously_disable_ssl_validation(self, dangerously_disable_ssl_validation):
        """Sets the dangerously_disable_ssl_validation of this ElasticCoordinates.


        :param dangerously_disable_ssl_validation: The dangerously_disable_ssl_validation of this ElasticCoordinates.  # noqa: E501
        :type: bool
        """

        self._dangerously_disable_ssl_validation = dangerously_disable_ssl_validation

    @property
    def hosts(self):
        """Gets the hosts of this ElasticCoordinates.  # noqa: E501


        :return: The hosts of this ElasticCoordinates.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ElasticCoordinates.


        :param hosts: The hosts of this ElasticCoordinates.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and hosts is None:  # noqa: E501
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

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
        if not isinstance(other, ElasticCoordinates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElasticCoordinates):
            return True

        return self.to_dict() != other.to_dict()
