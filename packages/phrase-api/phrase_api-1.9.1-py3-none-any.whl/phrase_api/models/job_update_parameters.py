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


class JobUpdateParameters(object):
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
        'branch': 'str',
        'name': 'str',
        'briefing': 'str',
        'due_date': 'datetime',
        'ticket_url': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'name': 'name',
        'briefing': 'briefing',
        'due_date': 'due_date',
        'ticket_url': 'ticket_url'
    }

    def __init__(self, branch=None, name=None, briefing=None, due_date=None, ticket_url=None, local_vars_configuration=None):  # noqa: E501
        """JobUpdateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._name = None
        self._briefing = None
        self._due_date = None
        self._ticket_url = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if name is not None:
            self.name = name
        if briefing is not None:
            self.briefing = briefing
        if due_date is not None:
            self.due_date = due_date
        if ticket_url is not None:
            self.ticket_url = ticket_url

    @property
    def branch(self):
        """Gets the branch of this JobUpdateParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this JobUpdateParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this JobUpdateParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def name(self):
        """Gets the name of this JobUpdateParameters.  # noqa: E501

        Job name  # noqa: E501

        :return: The name of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobUpdateParameters.

        Job name  # noqa: E501

        :param name: The name of this JobUpdateParameters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def briefing(self):
        """Gets the briefing of this JobUpdateParameters.  # noqa: E501

        Briefing for the translators  # noqa: E501

        :return: The briefing of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._briefing

    @briefing.setter
    def briefing(self, briefing):
        """Sets the briefing of this JobUpdateParameters.

        Briefing for the translators  # noqa: E501

        :param briefing: The briefing of this JobUpdateParameters.  # noqa: E501
        :type: str
        """

        self._briefing = briefing

    @property
    def due_date(self):
        """Gets the due_date of this JobUpdateParameters.  # noqa: E501

        Date the job should be finished  # noqa: E501

        :return: The due_date of this JobUpdateParameters.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this JobUpdateParameters.

        Date the job should be finished  # noqa: E501

        :param due_date: The due_date of this JobUpdateParameters.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def ticket_url(self):
        """Gets the ticket_url of this JobUpdateParameters.  # noqa: E501

        URL to a ticket for this job (e.g. Jira, Trello)  # noqa: E501

        :return: The ticket_url of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._ticket_url

    @ticket_url.setter
    def ticket_url(self, ticket_url):
        """Sets the ticket_url of this JobUpdateParameters.

        URL to a ticket for this job (e.g. Jira, Trello)  # noqa: E501

        :param ticket_url: The ticket_url of this JobUpdateParameters.  # noqa: E501
        :type: str
        """

        self._ticket_url = ticket_url

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
        if not isinstance(other, JobUpdateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobUpdateParameters):
            return True

        return self.to_dict() != other.to_dict()
