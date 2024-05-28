# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.ffmpeg_options_service_api import FfmpegOptionsServiceApi


class TestFfmpegOptionsServiceApi(unittest.TestCase):
    """FfmpegOptionsServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FfmpegOptionsServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_encoding_ffmpegoptions(self) -> None:
        """Test case for get_encoding_ffmpegoptions

        Gets the ffmpeg options
        """
        pass

    def test_post_encoding_ffmpegoptions(self) -> None:
        """Test case for post_encoding_ffmpegoptions

        Updates the ffmpeg options
        """
        pass


if __name__ == '__main__':
    unittest.main()
