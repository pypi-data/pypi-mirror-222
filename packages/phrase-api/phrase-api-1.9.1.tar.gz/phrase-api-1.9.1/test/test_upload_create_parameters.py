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
from phrase_api.models.upload_create_parameters import UploadCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestUploadCreateParameters(unittest.TestCase):
    """UploadCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UploadCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.upload_create_parameters.UploadCreateParameters()  # noqa: E501
        if include_optional :
            return UploadCreateParameters(
                branch = 'my-feature-branch', 
                file = bytes(b'blah'), 
                file_format = 'json', 
                locale_id = 'abcd1234cdef1234abcd1234cdef1234', 
                tags = 'awesome-feature,needs-proofreading', 
                update_translations = True, 
                update_descriptions = True, 
                convert_emoji = True, 
                skip_upload_tags = True, 
                skip_unverification = True, 
                file_encoding = '0', 
                locale_mapping = {"en": "2"}, 
                format_options = {"foo": "bar"}, 
                autotranslate = True, 
                mark_reviewed = True
            )
        else :
            return UploadCreateParameters(
        )

    def testUploadCreateParameters(self):
        """Test UploadCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
