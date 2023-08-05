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


class AnnotatorImageInput(object):
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
        'metadata': 'ImageMetadata',
        'source': 'ImageSource'
    }

    attribute_map = {
        'metadata': 'metadata',
        'source': 'source'
    }

    def __init__(self, metadata=None, source=None, local_vars_configuration=None):  # noqa: E501
        """AnnotatorImageInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self._source = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        self.source = source

    @property
    def metadata(self):
        """Gets the metadata of this AnnotatorImageInput.  # noqa: E501


        :return: The metadata of this AnnotatorImageInput.  # noqa: E501
        :rtype: ImageMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AnnotatorImageInput.


        :param metadata: The metadata of this AnnotatorImageInput.  # noqa: E501
        :type: ImageMetadata
        """

        self._metadata = metadata

    @property
    def source(self):
        """Gets the source of this AnnotatorImageInput.  # noqa: E501


        :return: The source of this AnnotatorImageInput.  # noqa: E501
        :rtype: ImageSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AnnotatorImageInput.


        :param source: The source of this AnnotatorImageInput.  # noqa: E501
        :type: ImageSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

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
        if not isinstance(other, AnnotatorImageInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnotatorImageInput):
            return True

        return self.to_dict() != other.to_dict()
