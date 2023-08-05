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


class ModelPipelineSettings(object):
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
        'clusters': 'object',
        'normalization': 'object',
        'page': 'object',
        'tables': 'object'
    }

    attribute_map = {
        'clusters': 'clusters',
        'normalization': 'normalization',
        'page': 'page',
        'tables': 'tables'
    }

    def __init__(self, clusters=None, normalization=None, page=None, tables=None, local_vars_configuration=None):  # noqa: E501
        """ModelPipelineSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._clusters = None
        self._normalization = None
        self._page = None
        self._tables = None
        self.discriminator = None

        self.clusters = clusters
        self.normalization = normalization
        self.page = page
        self.tables = tables

    @property
    def clusters(self):
        """Gets the clusters of this ModelPipelineSettings.  # noqa: E501


        :return: The clusters of this ModelPipelineSettings.  # noqa: E501
        :rtype: object
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ModelPipelineSettings.


        :param clusters: The clusters of this ModelPipelineSettings.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and clusters is None:  # noqa: E501
            raise ValueError("Invalid value for `clusters`, must not be `None`")  # noqa: E501

        self._clusters = clusters

    @property
    def normalization(self):
        """Gets the normalization of this ModelPipelineSettings.  # noqa: E501


        :return: The normalization of this ModelPipelineSettings.  # noqa: E501
        :rtype: object
        """
        return self._normalization

    @normalization.setter
    def normalization(self, normalization):
        """Sets the normalization of this ModelPipelineSettings.


        :param normalization: The normalization of this ModelPipelineSettings.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and normalization is None:  # noqa: E501
            raise ValueError("Invalid value for `normalization`, must not be `None`")  # noqa: E501

        self._normalization = normalization

    @property
    def page(self):
        """Gets the page of this ModelPipelineSettings.  # noqa: E501


        :return: The page of this ModelPipelineSettings.  # noqa: E501
        :rtype: object
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ModelPipelineSettings.


        :param page: The page of this ModelPipelineSettings.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and page is None:  # noqa: E501
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def tables(self):
        """Gets the tables of this ModelPipelineSettings.  # noqa: E501


        :return: The tables of this ModelPipelineSettings.  # noqa: E501
        :rtype: object
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this ModelPipelineSettings.


        :param tables: The tables of this ModelPipelineSettings.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and tables is None:  # noqa: E501
            raise ValueError("Invalid value for `tables`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ModelPipelineSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelPipelineSettings):
            return True

        return self.to_dict() != other.to_dict()
