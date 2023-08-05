# coding: utf-8

"""
    User Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.user.configuration import Configuration


class CreateTokensRequestBody(object):
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
        'code': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'code': 'code',
        'refresh_token': 'refresh_token'
    }

    def __init__(self, code=None, refresh_token=None, local_vars_configuration=None):  # noqa: E501
        """CreateTokensRequestBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._refresh_token = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def code(self):
        """Gets the code of this CreateTokensRequestBody.  # noqa: E501

        The oidc code response  # noqa: E501

        :return: The code of this CreateTokensRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateTokensRequestBody.

        The oidc code response  # noqa: E501

        :param code: The code of this CreateTokensRequestBody.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def refresh_token(self):
        """Gets the refresh_token of this CreateTokensRequestBody.  # noqa: E501

        The refresh token  # noqa: E501

        :return: The refresh_token of this CreateTokensRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this CreateTokensRequestBody.

        The refresh token  # noqa: E501

        :param refresh_token: The refresh_token of this CreateTokensRequestBody.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

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
        if not isinstance(other, CreateTokensRequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTokensRequestBody):
            return True

        return self.to_dict() != other.to_dict()
