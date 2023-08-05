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


class ImportFromElasticToDataCatalogOptionsParametersQueryOptions(object):
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
        'source': 'list[str]',
        'query': 'dict(str, object)',
        'size': 'float'
    }

    attribute_map = {
        'source': '_source',
        'query': 'query',
        'size': 'size'
    }

    def __init__(self, source=None, query=None, size=None, local_vars_configuration=None):  # noqa: E501
        """ImportFromElasticToDataCatalogOptionsParametersQueryOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._query = None
        self._size = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if query is not None:
            self.query = query
        if size is not None:
            self.size = size

    @property
    def source(self):
        """Gets the source of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501


        :return: The source of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.


        :param source: The source of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501
        :type: list[str]
        """

        self._source = source

    @property
    def query(self):
        """Gets the query of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501


        :return: The query of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.


        :param query: The query of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501
        :type: dict(str, object)
        """

        self._query = query

    @property
    def size(self):
        """Gets the size of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501


        :return: The size of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.


        :param size: The size of this ImportFromElasticToDataCatalogOptionsParametersQueryOptions.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < 0):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

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
        if not isinstance(other, ImportFromElasticToDataCatalogOptionsParametersQueryOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportFromElasticToDataCatalogOptionsParametersQueryOptions):
            return True

        return self.to_dict() != other.to_dict()
