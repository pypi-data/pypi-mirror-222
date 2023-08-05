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


class TranslationDetails(object):
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
        'content': 'str',
        'unverified': 'bool',
        'excluded': 'bool',
        'plural_suffix': 'str',
        'key': 'KeyPreview',
        'locale': 'LocalePreview',
        'placeholders': 'list[str]',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user': 'UserPreview',
        'word_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'content': 'content',
        'unverified': 'unverified',
        'excluded': 'excluded',
        'plural_suffix': 'plural_suffix',
        'key': 'key',
        'locale': 'locale',
        'placeholders': 'placeholders',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user',
        'word_count': 'word_count'
    }

    def __init__(self, id=None, content=None, unverified=None, excluded=None, plural_suffix=None, key=None, locale=None, placeholders=None, state=None, created_at=None, updated_at=None, user=None, word_count=None, local_vars_configuration=None):  # noqa: E501
        """TranslationDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._content = None
        self._unverified = None
        self._excluded = None
        self._plural_suffix = None
        self._key = None
        self._locale = None
        self._placeholders = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self._word_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content is not None:
            self.content = content
        if unverified is not None:
            self.unverified = unverified
        if excluded is not None:
            self.excluded = excluded
        if plural_suffix is not None:
            self.plural_suffix = plural_suffix
        if key is not None:
            self.key = key
        if locale is not None:
            self.locale = locale
        if placeholders is not None:
            self.placeholders = placeholders
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user
        if word_count is not None:
            self.word_count = word_count

    @property
    def id(self):
        """Gets the id of this TranslationDetails.  # noqa: E501


        :return: The id of this TranslationDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationDetails.


        :param id: The id of this TranslationDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def content(self):
        """Gets the content of this TranslationDetails.  # noqa: E501


        :return: The content of this TranslationDetails.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TranslationDetails.


        :param content: The content of this TranslationDetails.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def unverified(self):
        """Gets the unverified of this TranslationDetails.  # noqa: E501


        :return: The unverified of this TranslationDetails.  # noqa: E501
        :rtype: bool
        """
        return self._unverified

    @unverified.setter
    def unverified(self, unverified):
        """Sets the unverified of this TranslationDetails.


        :param unverified: The unverified of this TranslationDetails.  # noqa: E501
        :type: bool
        """

        self._unverified = unverified

    @property
    def excluded(self):
        """Gets the excluded of this TranslationDetails.  # noqa: E501


        :return: The excluded of this TranslationDetails.  # noqa: E501
        :rtype: bool
        """
        return self._excluded

    @excluded.setter
    def excluded(self, excluded):
        """Sets the excluded of this TranslationDetails.


        :param excluded: The excluded of this TranslationDetails.  # noqa: E501
        :type: bool
        """

        self._excluded = excluded

    @property
    def plural_suffix(self):
        """Gets the plural_suffix of this TranslationDetails.  # noqa: E501


        :return: The plural_suffix of this TranslationDetails.  # noqa: E501
        :rtype: str
        """
        return self._plural_suffix

    @plural_suffix.setter
    def plural_suffix(self, plural_suffix):
        """Sets the plural_suffix of this TranslationDetails.


        :param plural_suffix: The plural_suffix of this TranslationDetails.  # noqa: E501
        :type: str
        """

        self._plural_suffix = plural_suffix

    @property
    def key(self):
        """Gets the key of this TranslationDetails.  # noqa: E501


        :return: The key of this TranslationDetails.  # noqa: E501
        :rtype: KeyPreview
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TranslationDetails.


        :param key: The key of this TranslationDetails.  # noqa: E501
        :type: KeyPreview
        """

        self._key = key

    @property
    def locale(self):
        """Gets the locale of this TranslationDetails.  # noqa: E501


        :return: The locale of this TranslationDetails.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this TranslationDetails.


        :param locale: The locale of this TranslationDetails.  # noqa: E501
        :type: LocalePreview
        """

        self._locale = locale

    @property
    def placeholders(self):
        """Gets the placeholders of this TranslationDetails.  # noqa: E501


        :return: The placeholders of this TranslationDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._placeholders

    @placeholders.setter
    def placeholders(self, placeholders):
        """Sets the placeholders of this TranslationDetails.


        :param placeholders: The placeholders of this TranslationDetails.  # noqa: E501
        :type: list[str]
        """

        self._placeholders = placeholders

    @property
    def state(self):
        """Gets the state of this TranslationDetails.  # noqa: E501


        :return: The state of this TranslationDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TranslationDetails.


        :param state: The state of this TranslationDetails.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this TranslationDetails.  # noqa: E501


        :return: The created_at of this TranslationDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TranslationDetails.


        :param created_at: The created_at of this TranslationDetails.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TranslationDetails.  # noqa: E501


        :return: The updated_at of this TranslationDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TranslationDetails.


        :param updated_at: The updated_at of this TranslationDetails.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this TranslationDetails.  # noqa: E501


        :return: The user of this TranslationDetails.  # noqa: E501
        :rtype: UserPreview
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TranslationDetails.


        :param user: The user of this TranslationDetails.  # noqa: E501
        :type: UserPreview
        """

        self._user = user

    @property
    def word_count(self):
        """Gets the word_count of this TranslationDetails.  # noqa: E501


        :return: The word_count of this TranslationDetails.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this TranslationDetails.


        :param word_count: The word_count of this TranslationDetails.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

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
        if not isinstance(other, TranslationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationDetails):
            return True

        return self.to_dict() != other.to_dict()
