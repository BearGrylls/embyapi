# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.bit_rate import BitRate

class TestBitRate(unittest.TestCase):
    """BitRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BitRate:
        """Test BitRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BitRate`
        """
        model = BitRate()
        if include_optional:
            return BitRate(
                bps = 56,
                kbps = 1.337,
                mbps = 1.337
            )
        else:
            return BitRate(
        )
        """

    def testBitRate(self):
        """Test BitRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
