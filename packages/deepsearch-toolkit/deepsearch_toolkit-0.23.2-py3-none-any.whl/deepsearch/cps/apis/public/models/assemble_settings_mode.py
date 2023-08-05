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


class AssembleSettingsMode(object):
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
        'page_elements': 'list[str]',
        'tables': 'list[str]'
    }

    attribute_map = {
        'page_elements': 'page_elements',
        'tables': 'tables'
    }

    def __init__(self, page_elements=None, tables=None, local_vars_configuration=None):  # noqa: E501
        """AssembleSettingsMode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page_elements = None
        self._tables = None
        self.discriminator = None

        self.page_elements = page_elements
        self.tables = tables

    @property
    def page_elements(self):
        """Gets the page_elements of this AssembleSettingsMode.  # noqa: E501


        :return: The page_elements of this AssembleSettingsMode.  # noqa: E501
        :rtype: list[str]
        """
        return self._page_elements

    @page_elements.setter
    def page_elements(self, page_elements):
        """Sets the page_elements of this AssembleSettingsMode.


        :param page_elements: The page_elements of this AssembleSettingsMode.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and page_elements is None:  # noqa: E501
            raise ValueError("Invalid value for `page_elements`, must not be `None`")  # noqa: E501
        allowed_values = ["H", "M", "None"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(page_elements).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `page_elements` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(page_elements) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._page_elements = page_elements

    @property
    def tables(self):
        """Gets the tables of this AssembleSettingsMode.  # noqa: E501


        :return: The tables of this AssembleSettingsMode.  # noqa: E501
        :rtype: list[str]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this AssembleSettingsMode.


        :param tables: The tables of this AssembleSettingsMode.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tables is None:  # noqa: E501
            raise ValueError("Invalid value for `tables`, must not be `None`")  # noqa: E501
        allowed_values = ["H", "M", "None"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(tables).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `tables` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(tables) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._tables = tables

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
        if not isinstance(other, AssembleSettingsMode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssembleSettingsMode):
            return True

        return self.to_dict() != other.to_dict()
