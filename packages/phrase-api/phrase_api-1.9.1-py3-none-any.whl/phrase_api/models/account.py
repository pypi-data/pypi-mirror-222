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


class Account(object):
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
        'name': 'str',
        'slug': 'str',
        'company': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'company_logo_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'company': 'company',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'company_logo_url': 'company_logo_url'
    }

    def __init__(self, id=None, name=None, slug=None, company=None, created_at=None, updated_at=None, company_logo_url=None, local_vars_configuration=None):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._slug = None
        self._company = None
        self._created_at = None
        self._updated_at = None
        self._company_logo_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if company is not None:
            self.company = company
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if company_logo_url is not None:
            self.company_logo_url = company_logo_url

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501


        :return: The id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.


        :param id: The id of this Account.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501


        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.


        :param name: The name of this Account.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Account.  # noqa: E501


        :return: The slug of this Account.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Account.


        :param slug: The slug of this Account.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def company(self):
        """Gets the company of this Account.  # noqa: E501


        :return: The company of this Account.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Account.


        :param company: The company of this Account.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def created_at(self):
        """Gets the created_at of this Account.  # noqa: E501


        :return: The created_at of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Account.


        :param created_at: The created_at of this Account.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Account.  # noqa: E501


        :return: The updated_at of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Account.


        :param updated_at: The updated_at of this Account.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def company_logo_url(self):
        """Gets the company_logo_url of this Account.  # noqa: E501


        :return: The company_logo_url of this Account.  # noqa: E501
        :rtype: str
        """
        return self._company_logo_url

    @company_logo_url.setter
    def company_logo_url(self, company_logo_url):
        """Sets the company_logo_url of this Account.


        :param company_logo_url: The company_logo_url of this Account.  # noqa: E501
        :type: str
        """

        self._company_logo_url = company_logo_url

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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
