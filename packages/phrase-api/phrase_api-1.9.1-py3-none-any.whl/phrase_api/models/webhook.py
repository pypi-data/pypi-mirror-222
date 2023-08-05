# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from phrase_api.configuration import Configuration


class Webhook(object):
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
        'id': 'str',
        'callback_url': 'str',
        'description': 'str',
        'events': 'list[str]',
        'active': 'bool',
        'include_branches': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'callback_url': 'callback_url',
        'description': 'description',
        'events': 'events',
        'active': 'active',
        'include_branches': 'include_branches',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, callback_url=None, description=None, events=None, active=None, include_branches=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Webhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._callback_url = None
        self._description = None
        self._events = None
        self._active = None
        self._include_branches = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if callback_url is not None:
            self.callback_url = callback_url
        if description is not None:
            self.description = description
        if events is not None:
            self.events = events
        if active is not None:
            self.active = active
        if include_branches is not None:
            self.include_branches = include_branches
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501


        :return: The id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.


        :param id: The id of this Webhook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def callback_url(self):
        """Gets the callback_url of this Webhook.  # noqa: E501


        :return: The callback_url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this Webhook.


        :param callback_url: The callback_url of this Webhook.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def description(self):
        """Gets the description of this Webhook.  # noqa: E501


        :return: The description of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Webhook.


        :param description: The description of this Webhook.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def events(self):
        """Gets the events of this Webhook.  # noqa: E501


        :return: The events of this Webhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Webhook.


        :param events: The events of this Webhook.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def active(self):
        """Gets the active of this Webhook.  # noqa: E501


        :return: The active of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Webhook.


        :param active: The active of this Webhook.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def include_branches(self):
        """Gets the include_branches of this Webhook.  # noqa: E501


        :return: The include_branches of this Webhook.  # noqa: E501
        :rtype: bool
        """
        return self._include_branches

    @include_branches.setter
    def include_branches(self, include_branches):
        """Sets the include_branches of this Webhook.


        :param include_branches: The include_branches of this Webhook.  # noqa: E501
        :type: bool
        """

        self._include_branches = include_branches

    @property
    def created_at(self):
        """Gets the created_at of this Webhook.  # noqa: E501


        :return: The created_at of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Webhook.


        :param created_at: The created_at of this Webhook.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Webhook.  # noqa: E501


        :return: The updated_at of this Webhook.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Webhook.


        :param updated_at: The updated_at of this Webhook.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Webhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Webhook):
            return True

        return self.to_dict() != other.to_dict()
