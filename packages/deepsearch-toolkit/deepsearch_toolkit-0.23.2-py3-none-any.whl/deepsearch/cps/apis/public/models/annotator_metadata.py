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


class AnnotatorMetadata(object):
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
        'author': 'str',
        'description': 'str',
        'name': 'str',
        'url': 'str',
        'version': 'str'
    }

    attribute_map = {
        'author': 'author',
        'description': 'description',
        'name': 'name',
        'url': 'url',
        'version': 'version'
    }

    def __init__(self, author=None, description=None, name=None, url=None, version=None, local_vars_configuration=None):  # noqa: E501
        """AnnotatorMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._description = None
        self._name = None
        self._url = None
        self._version = None
        self.discriminator = None

        self.author = author
        self.description = description
        self.name = name
        self.url = url
        self.version = version

    @property
    def author(self):
        """Gets the author of this AnnotatorMetadata.  # noqa: E501


        :return: The author of this AnnotatorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this AnnotatorMetadata.


        :param author: The author of this AnnotatorMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def description(self):
        """Gets the description of this AnnotatorMetadata.  # noqa: E501


        :return: The description of this AnnotatorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnnotatorMetadata.


        :param description: The description of this AnnotatorMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this AnnotatorMetadata.  # noqa: E501


        :return: The name of this AnnotatorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnnotatorMetadata.


        :param name: The name of this AnnotatorMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this AnnotatorMetadata.  # noqa: E501


        :return: The url of this AnnotatorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AnnotatorMetadata.


        :param url: The url of this AnnotatorMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def version(self):
        """Gets the version of this AnnotatorMetadata.  # noqa: E501


        :return: The version of this AnnotatorMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnnotatorMetadata.


        :param version: The version of this AnnotatorMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, AnnotatorMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnotatorMetadata):
            return True

        return self.to_dict() != other.to_dict()
