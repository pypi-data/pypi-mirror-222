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


class AttachmentUploadDataUploadData(object):
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
        'fields': 'object',
        'url': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'url': 'url'
    }

    def __init__(self, fields=None, url=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentUploadDataUploadData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fields = None
        self._url = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if url is not None:
            self.url = url

    @property
    def fields(self):
        """Gets the fields of this AttachmentUploadDataUploadData.  # noqa: E501

        fields to use in request body.  # noqa: E501

        :return: The fields of this AttachmentUploadDataUploadData.  # noqa: E501
        :rtype: object
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this AttachmentUploadDataUploadData.

        fields to use in request body.  # noqa: E501

        :param fields: The fields of this AttachmentUploadDataUploadData.  # noqa: E501
        :type: object
        """

        self._fields = fields

    @property
    def url(self):
        """Gets the url of this AttachmentUploadDataUploadData.  # noqa: E501

        url of the host.  # noqa: E501

        :return: The url of this AttachmentUploadDataUploadData.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AttachmentUploadDataUploadData.

        url of the host.  # noqa: E501

        :param url: The url of this AttachmentUploadDataUploadData.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, AttachmentUploadDataUploadData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentUploadDataUploadData):
            return True

        return self.to_dict() != other.to_dict()
