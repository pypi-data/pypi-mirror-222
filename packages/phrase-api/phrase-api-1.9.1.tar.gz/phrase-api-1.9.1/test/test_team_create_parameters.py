# coding: utf-8

"""
    Phrase Strings API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import phrase_api
from phrase_api.models.team_create_parameters import TeamCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestTeamCreateParameters(unittest.TestCase):
    """TeamCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TeamCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.team_create_parameters.TeamCreateParameters()  # noqa: E501
        if include_optional :
            return TeamCreateParameters(
                name = 'German Translators'
            )
        else :
            return TeamCreateParameters(
        )

    def testTeamCreateParameters(self):
        """Test TeamCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
