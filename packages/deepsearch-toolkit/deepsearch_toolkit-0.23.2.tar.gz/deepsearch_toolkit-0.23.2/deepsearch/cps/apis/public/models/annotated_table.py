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


class AnnotatedTable(object):
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
        'entities': 'dict(str, list[EntityAnnotation])',
        'properties': 'object',
        'relationships': 'dict(str, list[object])',
        'text': 'str'
    }

    attribute_map = {
        'entities': 'entities',
        'properties': 'properties',
        'relationships': 'relationships',
        'text': 'text'
    }

    def __init__(self, entities=None, properties=None, relationships=None, text=None, local_vars_configuration=None):  # noqa: E501
        """AnnotatedTable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entities = None
        self._properties = None
        self._relationships = None
        self._text = None
        self.discriminator = None

        self.entities = entities
        self.properties = properties
        self.relationships = relationships
        if text is not None:
            self.text = text

    @property
    def entities(self):
        """Gets the entities of this AnnotatedTable.  # noqa: E501


        :return: The entities of this AnnotatedTable.  # noqa: E501
        :rtype: dict(str, list[EntityAnnotation])
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this AnnotatedTable.


        :param entities: The entities of this AnnotatedTable.  # noqa: E501
        :type: dict(str, list[EntityAnnotation])
        """
        if self.local_vars_configuration.client_side_validation and entities is None:  # noqa: E501
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501

        self._entities = entities

    @property
    def properties(self):
        """Gets the properties of this AnnotatedTable.  # noqa: E501


        :return: The properties of this AnnotatedTable.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AnnotatedTable.


        :param properties: The properties of this AnnotatedTable.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def relationships(self):
        """Gets the relationships of this AnnotatedTable.  # noqa: E501


        :return: The relationships of this AnnotatedTable.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this AnnotatedTable.


        :param relationships: The relationships of this AnnotatedTable.  # noqa: E501
        :type: dict(str, list[object])
        """
        if self.local_vars_configuration.client_side_validation and relationships is None:  # noqa: E501
            raise ValueError("Invalid value for `relationships`, must not be `None`")  # noqa: E501

        self._relationships = relationships

    @property
    def text(self):
        """Gets the text of this AnnotatedTable.  # noqa: E501


        :return: The text of this AnnotatedTable.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AnnotatedTable.


        :param text: The text of this AnnotatedTable.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if not isinstance(other, AnnotatedTable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnotatedTable):
            return True

        return self.to_dict() != other.to_dict()
