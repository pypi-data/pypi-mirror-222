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


class ProjectDefaultValuesCcsProject(object):
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
        'collection_name': 'str',
        'name': 'str',
        'proj_key': 'str'
    }

    attribute_map = {
        'collection_name': 'collection_name',
        'name': 'name',
        'proj_key': 'proj_key'
    }

    def __init__(self, collection_name=None, name=None, proj_key=None, local_vars_configuration=None):  # noqa: E501
        """ProjectDefaultValuesCcsProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._collection_name = None
        self._name = None
        self._proj_key = None
        self.discriminator = None

        if collection_name is not None:
            self.collection_name = collection_name
        self.name = name
        self.proj_key = proj_key

    @property
    def collection_name(self):
        """Gets the collection_name of this ProjectDefaultValuesCcsProject.  # noqa: E501


        :return: The collection_name of this ProjectDefaultValuesCcsProject.  # noqa: E501
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        """Sets the collection_name of this ProjectDefaultValuesCcsProject.


        :param collection_name: The collection_name of this ProjectDefaultValuesCcsProject.  # noqa: E501
        :type: str
        """

        self._collection_name = collection_name

    @property
    def name(self):
        """Gets the name of this ProjectDefaultValuesCcsProject.  # noqa: E501


        :return: The name of this ProjectDefaultValuesCcsProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectDefaultValuesCcsProject.


        :param name: The name of this ProjectDefaultValuesCcsProject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def proj_key(self):
        """Gets the proj_key of this ProjectDefaultValuesCcsProject.  # noqa: E501


        :return: The proj_key of this ProjectDefaultValuesCcsProject.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this ProjectDefaultValuesCcsProject.


        :param proj_key: The proj_key of this ProjectDefaultValuesCcsProject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proj_key is None:  # noqa: E501
            raise ValueError("Invalid value for `proj_key`, must not be `None`")  # noqa: E501

        self._proj_key = proj_key

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
        if not isinstance(other, ProjectDefaultValuesCcsProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDefaultValuesCcsProject):
            return True

        return self.to_dict() != other.to_dict()
