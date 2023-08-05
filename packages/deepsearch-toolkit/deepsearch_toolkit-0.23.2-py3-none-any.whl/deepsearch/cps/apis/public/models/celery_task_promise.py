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


class CeleryTaskPromise(object):
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
        'result': 'object',
        'task_id': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'task_id': 'task_id',
        'task_status': 'task_status'
    }

    def __init__(self, result=None, task_id=None, task_status=None, local_vars_configuration=None):  # noqa: E501
        """CeleryTaskPromise - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._task_id = None
        self._task_status = None
        self.discriminator = None

        self.result = result
        self.task_id = task_id
        self.task_status = task_status

    @property
    def result(self):
        """Gets the result of this CeleryTaskPromise.  # noqa: E501


        :return: The result of this CeleryTaskPromise.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CeleryTaskPromise.


        :param result: The result of this CeleryTaskPromise.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def task_id(self):
        """Gets the task_id of this CeleryTaskPromise.  # noqa: E501


        :return: The task_id of this CeleryTaskPromise.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CeleryTaskPromise.


        :param task_id: The task_id of this CeleryTaskPromise.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and task_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this CeleryTaskPromise.  # noqa: E501


        :return: The task_status of this CeleryTaskPromise.  # noqa: E501
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this CeleryTaskPromise.


        :param task_status: The task_status of this CeleryTaskPromise.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and task_status is None:  # noqa: E501
            raise ValueError("Invalid value for `task_status`, must not be `None`")  # noqa: E501

        self._task_status = task_status

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
        if not isinstance(other, CeleryTaskPromise):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CeleryTaskPromise):
            return True

        return self.to_dict() != other.to_dict()
