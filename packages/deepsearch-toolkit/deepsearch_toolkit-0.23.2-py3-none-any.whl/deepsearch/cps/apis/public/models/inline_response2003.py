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


class InlineResponse2003(object):
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
        'avail_cpu_slots': 'int',
        'avail_mem_slots': 'int',
        'avail_slots': 'int',
        'name': 'str',
        'num_nodes': 'int',
        'number_kgs': 'int',
        'running_kgs': 'int',
        'workers_pool': 'str'
    }

    attribute_map = {
        'avail_cpu_slots': 'availCpuSlots',
        'avail_mem_slots': 'availMemSlots',
        'avail_slots': 'availSlots',
        'name': 'name',
        'num_nodes': 'numNodes',
        'number_kgs': 'numberKgs',
        'running_kgs': 'runningKgs',
        'workers_pool': 'workersPool'
    }

    def __init__(self, avail_cpu_slots=None, avail_mem_slots=None, avail_slots=None, name=None, num_nodes=None, number_kgs=None, running_kgs=None, workers_pool=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2003 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._avail_cpu_slots = None
        self._avail_mem_slots = None
        self._avail_slots = None
        self._name = None
        self._num_nodes = None
        self._number_kgs = None
        self._running_kgs = None
        self._workers_pool = None
        self.discriminator = None

        if avail_cpu_slots is not None:
            self.avail_cpu_slots = avail_cpu_slots
        if avail_mem_slots is not None:
            self.avail_mem_slots = avail_mem_slots
        if avail_slots is not None:
            self.avail_slots = avail_slots
        if name is not None:
            self.name = name
        if num_nodes is not None:
            self.num_nodes = num_nodes
        if number_kgs is not None:
            self.number_kgs = number_kgs
        if running_kgs is not None:
            self.running_kgs = running_kgs
        if workers_pool is not None:
            self.workers_pool = workers_pool

    @property
    def avail_cpu_slots(self):
        """Gets the avail_cpu_slots of this InlineResponse2003.  # noqa: E501


        :return: The avail_cpu_slots of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._avail_cpu_slots

    @avail_cpu_slots.setter
    def avail_cpu_slots(self, avail_cpu_slots):
        """Sets the avail_cpu_slots of this InlineResponse2003.


        :param avail_cpu_slots: The avail_cpu_slots of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._avail_cpu_slots = avail_cpu_slots

    @property
    def avail_mem_slots(self):
        """Gets the avail_mem_slots of this InlineResponse2003.  # noqa: E501


        :return: The avail_mem_slots of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._avail_mem_slots

    @avail_mem_slots.setter
    def avail_mem_slots(self, avail_mem_slots):
        """Sets the avail_mem_slots of this InlineResponse2003.


        :param avail_mem_slots: The avail_mem_slots of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._avail_mem_slots = avail_mem_slots

    @property
    def avail_slots(self):
        """Gets the avail_slots of this InlineResponse2003.  # noqa: E501


        :return: The avail_slots of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._avail_slots

    @avail_slots.setter
    def avail_slots(self, avail_slots):
        """Sets the avail_slots of this InlineResponse2003.


        :param avail_slots: The avail_slots of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._avail_slots = avail_slots

    @property
    def name(self):
        """Gets the name of this InlineResponse2003.  # noqa: E501


        :return: The name of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2003.


        :param name: The name of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_nodes(self):
        """Gets the num_nodes of this InlineResponse2003.  # noqa: E501


        :return: The num_nodes of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._num_nodes

    @num_nodes.setter
    def num_nodes(self, num_nodes):
        """Sets the num_nodes of this InlineResponse2003.


        :param num_nodes: The num_nodes of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._num_nodes = num_nodes

    @property
    def number_kgs(self):
        """Gets the number_kgs of this InlineResponse2003.  # noqa: E501


        :return: The number_kgs of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._number_kgs

    @number_kgs.setter
    def number_kgs(self, number_kgs):
        """Sets the number_kgs of this InlineResponse2003.


        :param number_kgs: The number_kgs of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._number_kgs = number_kgs

    @property
    def running_kgs(self):
        """Gets the running_kgs of this InlineResponse2003.  # noqa: E501


        :return: The running_kgs of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._running_kgs

    @running_kgs.setter
    def running_kgs(self, running_kgs):
        """Sets the running_kgs of this InlineResponse2003.


        :param running_kgs: The running_kgs of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._running_kgs = running_kgs

    @property
    def workers_pool(self):
        """Gets the workers_pool of this InlineResponse2003.  # noqa: E501


        :return: The workers_pool of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._workers_pool

    @workers_pool.setter
    def workers_pool(self, workers_pool):
        """Sets the workers_pool of this InlineResponse2003.


        :param workers_pool: The workers_pool of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._workers_pool = workers_pool

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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2003):
            return True

        return self.to_dict() != other.to_dict()
