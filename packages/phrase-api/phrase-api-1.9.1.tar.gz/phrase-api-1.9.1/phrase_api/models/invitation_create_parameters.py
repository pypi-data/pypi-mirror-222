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


class InvitationCreateParameters(object):
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
        'email': 'str',
        'role': 'str',
        'project_ids': 'str',
        'locale_ids': 'str',
        'space_ids': 'list[str]',
        'team_ids': 'list[str]',
        'default_locale_codes': 'list[str]',
        'permissions': 'dict(str, str)'
    }

    attribute_map = {
        'email': 'email',
        'role': 'role',
        'project_ids': 'project_ids',
        'locale_ids': 'locale_ids',
        'space_ids': 'space_ids',
        'team_ids': 'team_ids',
        'default_locale_codes': 'default_locale_codes',
        'permissions': 'permissions'
    }

    def __init__(self, email=None, role=None, project_ids=None, locale_ids=None, space_ids=None, team_ids=None, default_locale_codes=None, permissions=None, local_vars_configuration=None):  # noqa: E501
        """InvitationCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._role = None
        self._project_ids = None
        self._locale_ids = None
        self._space_ids = None
        self._team_ids = None
        self._default_locale_codes = None
        self._permissions = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if role is not None:
            self.role = role
        if project_ids is not None:
            self.project_ids = project_ids
        if locale_ids is not None:
            self.locale_ids = locale_ids
        if space_ids is not None:
            self.space_ids = space_ids
        if team_ids is not None:
            self.team_ids = team_ids
        if default_locale_codes is not None:
            self.default_locale_codes = default_locale_codes
        if permissions is not None:
            self.permissions = permissions

    @property
    def email(self):
        """Gets the email of this InvitationCreateParameters.  # noqa: E501

        The email of the invited user. The <code>email</code> can not be updated once created. Create a new invitation for each unique email.  # noqa: E501

        :return: The email of this InvitationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvitationCreateParameters.

        The email of the invited user. The <code>email</code> can not be updated once created. Create a new invitation for each unique email.  # noqa: E501

        :param email: The email of this InvitationCreateParameters.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this InvitationCreateParameters.  # noqa: E501

        Invitiation role, can be any of Manager, Developer, Translator.  # noqa: E501

        :return: The role of this InvitationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InvitationCreateParameters.

        Invitiation role, can be any of Manager, Developer, Translator.  # noqa: E501

        :param role: The role of this InvitationCreateParameters.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def project_ids(self):
        """Gets the project_ids of this InvitationCreateParameters.  # noqa: E501

        List of project ids the invited user has access to.  # noqa: E501

        :return: The project_ids of this InvitationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this InvitationCreateParameters.

        List of project ids the invited user has access to.  # noqa: E501

        :param project_ids: The project_ids of this InvitationCreateParameters.  # noqa: E501
        :type: str
        """

        self._project_ids = project_ids

    @property
    def locale_ids(self):
        """Gets the locale_ids of this InvitationCreateParameters.  # noqa: E501

        List of locale ids the invited user has access to.  # noqa: E501

        :return: The locale_ids of this InvitationCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._locale_ids

    @locale_ids.setter
    def locale_ids(self, locale_ids):
        """Sets the locale_ids of this InvitationCreateParameters.

        List of locale ids the invited user has access to.  # noqa: E501

        :param locale_ids: The locale_ids of this InvitationCreateParameters.  # noqa: E501
        :type: str
        """

        self._locale_ids = locale_ids

    @property
    def space_ids(self):
        """Gets the space_ids of this InvitationCreateParameters.  # noqa: E501

        List of spaces the user is assigned to.  # noqa: E501

        :return: The space_ids of this InvitationCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._space_ids

    @space_ids.setter
    def space_ids(self, space_ids):
        """Sets the space_ids of this InvitationCreateParameters.

        List of spaces the user is assigned to.  # noqa: E501

        :param space_ids: The space_ids of this InvitationCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._space_ids = space_ids

    @property
    def team_ids(self):
        """Gets the team_ids of this InvitationCreateParameters.  # noqa: E501

        List of teams the user is assigned to.  # noqa: E501

        :return: The team_ids of this InvitationCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """Sets the team_ids of this InvitationCreateParameters.

        List of teams the user is assigned to.  # noqa: E501

        :param team_ids: The team_ids of this InvitationCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._team_ids = team_ids

    @property
    def default_locale_codes(self):
        """Gets the default_locale_codes of this InvitationCreateParameters.  # noqa: E501

        List of default locales for the user.  # noqa: E501

        :return: The default_locale_codes of this InvitationCreateParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_locale_codes

    @default_locale_codes.setter
    def default_locale_codes(self, default_locale_codes):
        """Sets the default_locale_codes of this InvitationCreateParameters.

        List of default locales for the user.  # noqa: E501

        :param default_locale_codes: The default_locale_codes of this InvitationCreateParameters.  # noqa: E501
        :type: list[str]
        """

        self._default_locale_codes = default_locale_codes

    @property
    def permissions(self):
        """Gets the permissions of this InvitationCreateParameters.  # noqa: E501

        Additional permissions depending on invitation role. Available permissions are <code>create_upload</code> and <code>review_translations</code>  # noqa: E501

        :return: The permissions of this InvitationCreateParameters.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this InvitationCreateParameters.

        Additional permissions depending on invitation role. Available permissions are <code>create_upload</code> and <code>review_translations</code>  # noqa: E501

        :param permissions: The permissions of this InvitationCreateParameters.  # noqa: E501
        :type: dict(str, str)
        """

        self._permissions = permissions

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
        if not isinstance(other, InvitationCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvitationCreateParameters):
            return True

        return self.to_dict() != other.to_dict()
