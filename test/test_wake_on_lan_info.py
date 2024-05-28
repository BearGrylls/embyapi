# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.wake_on_lan_info import WakeOnLanInfo

class TestWakeOnLanInfo(unittest.TestCase):
    """WakeOnLanInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WakeOnLanInfo:
        """Test WakeOnLanInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WakeOnLanInfo`
        """
        model = WakeOnLanInfo()
        if include_optional:
            return WakeOnLanInfo(
                mac_address = '',
                broadcast_address = '',
                port = 56
            )
        else:
            return WakeOnLanInfo(
        )
        """

    def testWakeOnLanInfo(self):
        """Test WakeOnLanInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
