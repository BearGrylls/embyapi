# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.official_rating_service_api import OfficialRatingServiceApi


class TestOfficialRatingServiceApi(unittest.TestCase):
    """OfficialRatingServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OfficialRatingServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_officialratings(self) -> None:
        """Test case for get_officialratings

        Gets items based on a query.
        """
        pass


if __name__ == '__main__':
    unittest.main()
