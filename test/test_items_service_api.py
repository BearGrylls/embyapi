# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.items_service_api import ItemsServiceApi


class TestItemsServiceApi(unittest.TestCase):
    """ItemsServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ItemsServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_items(self) -> None:
        """Test case for get_items

        Gets items based on a query.
        """
        pass

    def test_get_users_by_userid_items(self) -> None:
        """Test case for get_users_by_userid_items

        Gets items based on a query.
        """
        pass

    def test_get_users_by_userid_items_resume(self) -> None:
        """Test case for get_users_by_userid_items_resume

        Gets items based on a query.
        """
        pass


if __name__ == '__main__':
    unittest.main()
