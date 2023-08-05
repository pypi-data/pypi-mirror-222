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
from phrase_api.models.affected_resources import AffectedResources  # noqa: E501
from phrase_api.rest import ApiException

class TestAffectedResources(unittest.TestCase):
    """AffectedResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AffectedResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.affected_resources.AffectedResources()  # noqa: E501
        if include_optional :
            return AffectedResources(
                records_affected = 56
            )
        else :
            return AffectedResources(
        )

    def testAffectedResources(self):
        """Test AffectedResources"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
