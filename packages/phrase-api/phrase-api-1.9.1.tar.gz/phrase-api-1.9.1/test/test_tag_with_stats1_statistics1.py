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
from phrase_api.models.tag_with_stats1_statistics1 import TagWithStats1Statistics1  # noqa: E501
from phrase_api.rest import ApiException

class TestTagWithStats1Statistics1(unittest.TestCase):
    """TagWithStats1Statistics1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TagWithStats1Statistics1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.tag_with_stats1_statistics1.TagWithStats1Statistics1()  # noqa: E501
        if include_optional :
            return TagWithStats1Statistics1(
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}, 
                statistics = phrase_api.models.tag_with_stats_1_statistics.tag_with_stats_1_statistics(
                    keys_total_count = 56, 
                    translations_completed_count = 56, 
                    translations_unverified_count = 56, 
                    keys_untranslated_count = 56, )
            )
        else :
            return TagWithStats1Statistics1(
        )

    def testTagWithStats1Statistics1(self):
        """Test TagWithStats1Statistics1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
