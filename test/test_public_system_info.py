# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.public_system_info import PublicSystemInfo

class TestPublicSystemInfo(unittest.TestCase):
    """PublicSystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicSystemInfo:
        """Test PublicSystemInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicSystemInfo`
        """
        model = PublicSystemInfo()
        if include_optional:
            return PublicSystemInfo(
                local_address = '',
                local_addresses = [
                    ''
                    ],
                wan_address = '',
                remote_addresses = [
                    ''
                    ],
                server_name = '',
                version = '',
                id = ''
            )
        else:
            return PublicSystemInfo(
        )
        """

    def testPublicSystemInfo(self):
        """Test PublicSystemInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
