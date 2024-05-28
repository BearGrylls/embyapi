# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.item_counts import ItemCounts

class TestItemCounts(unittest.TestCase):
    """ItemCounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemCounts:
        """Test ItemCounts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemCounts`
        """
        model = ItemCounts()
        if include_optional:
            return ItemCounts(
                movie_count = 56,
                series_count = 56,
                episode_count = 56,
                game_count = 56,
                artist_count = 56,
                program_count = 56,
                game_system_count = 56,
                trailer_count = 56,
                song_count = 56,
                album_count = 56,
                music_video_count = 56,
                box_set_count = 56,
                book_count = 56,
                item_count = 56
            )
        else:
            return ItemCounts(
        )
        """

    def testItemCounts(self):
        """Test ItemCounts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
