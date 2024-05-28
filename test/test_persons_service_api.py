# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.persons_service_api import PersonsServiceApi


class TestPersonsServiceApi(unittest.TestCase):
    """PersonsServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PersonsServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_persons(self) -> None:
        """Test case for get_persons

        Gets all persons from a given item, folder, or the entire library
        """
        pass

    def test_get_persons_by_name(self) -> None:
        """Test case for get_persons_by_name

        Gets a person, by name
        """
        pass


if __name__ == '__main__':
    unittest.main()
