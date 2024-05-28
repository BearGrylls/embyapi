# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.sync_quality_option import SyncQualityOption

class TestSyncQualityOption(unittest.TestCase):
    """SyncQualityOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncQualityOption:
        """Test SyncQualityOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncQualityOption`
        """
        model = SyncQualityOption()
        if include_optional:
            return SyncQualityOption(
                name = '',
                description = '',
                id = '',
                is_default = True,
                is_original_quality = True
            )
        else:
            return SyncQualityOption(
        )
        """

    def testSyncQualityOption(self):
        """Test SyncQualityOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
