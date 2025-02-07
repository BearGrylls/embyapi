# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.dynamic_hls_service_api import DynamicHlsServiceApi


class TestDynamicHlsServiceApi(unittest.TestCase):
    """DynamicHlsServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DynamicHlsServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self) -> None:
        """Test case for get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer

        """
        pass

    def test_get_audio_by_id_live_m3u8(self) -> None:
        """Test case for get_audio_by_id_live_m3u8

        """
        pass

    def test_get_audio_by_id_main_m3u8(self) -> None:
        """Test case for get_audio_by_id_main_m3u8

        Gets an audio stream using HTTP live streaming.
        """
        pass

    def test_get_audio_by_id_master_m3u8(self) -> None:
        """Test case for get_audio_by_id_master_m3u8

        Gets an audio stream using HTTP live streaming.
        """
        pass

    def test_get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self) -> None:
        """Test case for get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer

        """
        pass

    def test_get_videos_by_id_live_m3u8(self) -> None:
        """Test case for get_videos_by_id_live_m3u8

        """
        pass

    def test_get_videos_by_id_live_subtitles_m3u8(self) -> None:
        """Test case for get_videos_by_id_live_subtitles_m3u8

        Gets an HLS subtitle playlist.
        """
        pass

    def test_get_videos_by_id_main_m3u8(self) -> None:
        """Test case for get_videos_by_id_main_m3u8

        Gets a video stream using HTTP live streaming.
        """
        pass

    def test_get_videos_by_id_master_m3u8(self) -> None:
        """Test case for get_videos_by_id_master_m3u8

        Gets a video stream using HTTP live streaming.
        """
        pass

    def test_get_videos_by_id_subtitles_m3u8(self) -> None:
        """Test case for get_videos_by_id_subtitles_m3u8

        Gets an HLS subtitle playlist.
        """
        pass

    def test_head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self) -> None:
        """Test case for head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer

        """
        pass

    def test_head_audio_by_id_master_m3u8(self) -> None:
        """Test case for head_audio_by_id_master_m3u8

        Gets an audio stream using HTTP live streaming.
        """
        pass

    def test_head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(self) -> None:
        """Test case for head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer

        """
        pass

    def test_head_videos_by_id_master_m3u8(self) -> None:
        """Test case for head_videos_by_id_master_m3u8

        Gets a video stream using HTTP live streaming.
        """
        pass


if __name__ == '__main__':
    unittest.main()
