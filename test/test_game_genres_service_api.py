# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.game_genres_service_api import GameGenresServiceApi


class TestGameGenresServiceApi(unittest.TestCase):
    """GameGenresServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GameGenresServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_gamegenres(self) -> None:
        """Test case for get_gamegenres

        Gets all Game genres from a given item, folder, or the entire library
        """
        pass

    def test_get_gamegenres_by_name(self) -> None:
        """Test case for get_gamegenres_by_name

        Gets a Game genre, by name
        """
        pass


if __name__ == '__main__':
    unittest.main()
