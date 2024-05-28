# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.chapter_info import ChapterInfo

class TestChapterInfo(unittest.TestCase):
    """ChapterInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChapterInfo:
        """Test ChapterInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChapterInfo`
        """
        model = ChapterInfo()
        if include_optional:
            return ChapterInfo(
                start_position_ticks = 56,
                name = '',
                image_tag = '',
                marker_type = 'Chapter',
                chapter_index = 56
            )
        else:
            return ChapterInfo(
        )
        """

    def testChapterInfo(self):
        """Test ChapterInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
