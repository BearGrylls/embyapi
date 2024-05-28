# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.transcoding_profile import TranscodingProfile

class TestTranscodingProfile(unittest.TestCase):
    """TranscodingProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TranscodingProfile:
        """Test TranscodingProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranscodingProfile`
        """
        model = TranscodingProfile()
        if include_optional:
            return TranscodingProfile(
                container = '',
                type = 'Audio',
                video_codec = '',
                audio_codec = '',
                protocol = '',
                estimate_content_length = True,
                enable_mpegts_m2_ts_mode = True,
                transcode_seek_info = 'Auto',
                copy_timestamps = True,
                context = 'Streaming',
                max_audio_channels = '',
                min_segments = 56,
                segment_length = 56,
                break_on_non_key_frames = True,
                allow_interlaced_video_stream_copy = True,
                manifest_subtitles = '',
                max_manifest_subtitles = 56,
                max_width = 56,
                max_height = 56,
                fill_empty_subtitle_segments = True
            )
        else:
            return TranscodingProfile(
        )
        """

    def testTranscodingProfile(self):
        """Test TranscodingProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
