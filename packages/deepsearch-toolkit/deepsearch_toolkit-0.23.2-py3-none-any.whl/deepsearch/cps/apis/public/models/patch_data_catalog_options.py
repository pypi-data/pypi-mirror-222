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


class PatchDataCatalogOptions(object):
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
        'category_schemas': 'list[DataCatalogCategorySchema]',
        'collections_data_flows': 'list[DataCatalogDataFlow]',
        'description': 'str',
        'name': 'str',
        'public': 'bool',
        'topology': 'DataCatalogTopology'
    }

    attribute_map = {
        'category_schemas': 'category_schemas',
        'collections_data_flows': 'collections_data_flows',
        'description': 'description',
        'name': 'name',
        'public': 'public',
        'topology': 'topology'
    }

    def __init__(self, category_schemas=None, collections_data_flows=None, description=None, name=None, public=None, topology=None, local_vars_configuration=None):  # noqa: E501
        """PatchDataCatalogOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category_schemas = None
        self._collections_data_flows = None
        self._description = None
        self._name = None
        self._public = None
        self._topology = None
        self.discriminator = None

        if category_schemas is not None:
            self.category_schemas = category_schemas
        if collections_data_flows is not None:
            self.collections_data_flows = collections_data_flows
        self.description = description
        if name is not None:
            self.name = name
        if public is not None:
            self.public = public
        if topology is not None:
            self.topology = topology

    @property
    def category_schemas(self):
        """Gets the category_schemas of this PatchDataCatalogOptions.  # noqa: E501


        :return: The category_schemas of this PatchDataCatalogOptions.  # noqa: E501
        :rtype: list[DataCatalogCategorySchema]
        """
        return self._category_schemas

    @category_schemas.setter
    def category_schemas(self, category_schemas):
        """Sets the category_schemas of this PatchDataCatalogOptions.


        :param category_schemas: The category_schemas of this PatchDataCatalogOptions.  # noqa: E501
        :type: list[DataCatalogCategorySchema]
        """

        self._category_schemas = category_schemas

    @property
    def collections_data_flows(self):
        """Gets the collections_data_flows of this PatchDataCatalogOptions.  # noqa: E501


        :return: The collections_data_flows of this PatchDataCatalogOptions.  # noqa: E501
        :rtype: list[DataCatalogDataFlow]
        """
        return self._collections_data_flows

    @collections_data_flows.setter
    def collections_data_flows(self, collections_data_flows):
        """Sets the collections_data_flows of this PatchDataCatalogOptions.


        :param collections_data_flows: The collections_data_flows of this PatchDataCatalogOptions.  # noqa: E501
        :type: list[DataCatalogDataFlow]
        """

        self._collections_data_flows = collections_data_flows

    @property
    def description(self):
        """Gets the description of this PatchDataCatalogOptions.  # noqa: E501


        :return: The description of this PatchDataCatalogOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchDataCatalogOptions.


        :param description: The description of this PatchDataCatalogOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this PatchDataCatalogOptions.  # noqa: E501


        :return: The name of this PatchDataCatalogOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchDataCatalogOptions.


        :param name: The name of this PatchDataCatalogOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def public(self):
        """Gets the public of this PatchDataCatalogOptions.  # noqa: E501


        :return: The public of this PatchDataCatalogOptions.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this PatchDataCatalogOptions.


        :param public: The public of this PatchDataCatalogOptions.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def topology(self):
        """Gets the topology of this PatchDataCatalogOptions.  # noqa: E501


        :return: The topology of this PatchDataCatalogOptions.  # noqa: E501
        :rtype: DataCatalogTopology
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """Sets the topology of this PatchDataCatalogOptions.


        :param topology: The topology of this PatchDataCatalogOptions.  # noqa: E501
        :type: DataCatalogTopology
        """

        self._topology = topology

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
        if not isinstance(other, PatchDataCatalogOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchDataCatalogOptions):
            return True

        return self.to_dict() != other.to_dict()
