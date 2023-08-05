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


class StorageSummaryTask(object):
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
        'dc_key': 'str',
        'kg_key': 'str',
        'kind': 'str',
        'proj_key': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'dc_key': 'dc_key',
        'kg_key': 'kg_key',
        'kind': 'kind',
        'proj_key': 'proj_key',
        'task_id': 'task_id'
    }

    def __init__(self, dc_key=None, kg_key=None, kind=None, proj_key=None, task_id=None, local_vars_configuration=None):  # noqa: E501
        """StorageSummaryTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dc_key = None
        self._kg_key = None
        self._kind = None
        self._proj_key = None
        self._task_id = None
        self.discriminator = None

        if dc_key is not None:
            self.dc_key = dc_key
        if kg_key is not None:
            self.kg_key = kg_key
        self.kind = kind
        self.proj_key = proj_key
        self.task_id = task_id

    @property
    def dc_key(self):
        """Gets the dc_key of this StorageSummaryTask.  # noqa: E501


        :return: The dc_key of this StorageSummaryTask.  # noqa: E501
        :rtype: str
        """
        return self._dc_key

    @dc_key.setter
    def dc_key(self, dc_key):
        """Sets the dc_key of this StorageSummaryTask.


        :param dc_key: The dc_key of this StorageSummaryTask.  # noqa: E501
        :type: str
        """

        self._dc_key = dc_key

    @property
    def kg_key(self):
        """Gets the kg_key of this StorageSummaryTask.  # noqa: E501


        :return: The kg_key of this StorageSummaryTask.  # noqa: E501
        :rtype: str
        """
        return self._kg_key

    @kg_key.setter
    def kg_key(self, kg_key):
        """Sets the kg_key of this StorageSummaryTask.


        :param kg_key: The kg_key of this StorageSummaryTask.  # noqa: E501
        :type: str
        """

        self._kg_key = kg_key

    @property
    def kind(self):
        """Gets the kind of this StorageSummaryTask.  # noqa: E501


        :return: The kind of this StorageSummaryTask.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this StorageSummaryTask.


        :param kind: The kind of this StorageSummaryTask.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["project_task", "celery_task"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and kind not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def proj_key(self):
        """Gets the proj_key of this StorageSummaryTask.  # noqa: E501


        :return: The proj_key of this StorageSummaryTask.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this StorageSummaryTask.


        :param proj_key: The proj_key of this StorageSummaryTask.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proj_key is None:  # noqa: E501
            raise ValueError("Invalid value for `proj_key`, must not be `None`")  # noqa: E501

        self._proj_key = proj_key

    @property
    def task_id(self):
        """Gets the task_id of this StorageSummaryTask.  # noqa: E501


        :return: The task_id of this StorageSummaryTask.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this StorageSummaryTask.


        :param task_id: The task_id of this StorageSummaryTask.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and task_id is None:  # noqa: E501
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

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
        if not isinstance(other, StorageSummaryTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageSummaryTask):
            return True

        return self.to_dict() != other.to_dict()
