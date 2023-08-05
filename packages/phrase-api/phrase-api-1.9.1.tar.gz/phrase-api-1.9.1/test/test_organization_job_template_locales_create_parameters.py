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
from phrase_api.models.organization_job_template_locales_create_parameters import OrganizationJobTemplateLocalesCreateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestOrganizationJobTemplateLocalesCreateParameters(unittest.TestCase):
    """OrganizationJobTemplateLocalesCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganizationJobTemplateLocalesCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.organization_job_template_locales_create_parameters.OrganizationJobTemplateLocalesCreateParameters()  # noqa: E501
        if include_optional :
            return OrganizationJobTemplateLocalesCreateParameters(
                locale_name = 'de-1', 
                locale_code = 'de-DE', 
                user_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                reviewer_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                translator_team_ids = ["abcd1234cdef1234abcd1234cdef1234"], 
                reviewer_team_ids = ["abcd1234cdef1234abcd1234cdef1234"]
            )
        else :
            return OrganizationJobTemplateLocalesCreateParameters(
                locale_name = 'de-1',
                locale_code = 'de-DE',
        )

    def testOrganizationJobTemplateLocalesCreateParameters(self):
        """Test OrganizationJobTemplateLocalesCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
