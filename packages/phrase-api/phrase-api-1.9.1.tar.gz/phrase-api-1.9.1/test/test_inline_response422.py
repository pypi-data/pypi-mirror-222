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
from phrase_api.models.inline_response422 import InlineResponse422  # noqa: E501
from phrase_api.rest import ApiException

class TestInlineResponse422(unittest.TestCase):
    """InlineResponse422 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse422
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.inline_response422.InlineResponse422()  # noqa: E501
        if include_optional :
            return InlineResponse422(
                message = '0', 
                errors = [
                    phrase_api.models.inline_response_422_errors.inline_response_422_errors(
                        resource = '0', 
                        field = '0', 
                        message = '0', )
                    ]
            )
        else :
            return InlineResponse422(
        )

    def testInlineResponse422(self):
        """Test InlineResponse422"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
