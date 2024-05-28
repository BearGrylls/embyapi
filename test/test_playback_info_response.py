# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.playback_info_response import PlaybackInfoResponse

class TestPlaybackInfoResponse(unittest.TestCase):
    """PlaybackInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaybackInfoResponse:
        """Test PlaybackInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaybackInfoResponse`
        """
        model = PlaybackInfoResponse()
        if include_optional:
            return PlaybackInfoResponse(
                media_sources = [
                    embyapi.models.media_source_info.MediaSourceInfo(
                        protocol = 'File', 
                        id = '', 
                        path = '', 
                        encoder_path = '', 
                        encoder_protocol = 'File', 
                        type = 'Default', 
                        probe_path = '', 
                        probe_protocol = 'File', 
                        container = '', 
                        size = 56, 
                        name = '', 
                        sort_name = '', 
                        is_remote = True, 
                        has_mixed_protocols = True, 
                        run_time_ticks = 56, 
                        container_start_time_ticks = 56, 
                        supports_transcoding = True, 
                        trancode_live_start_index = 56, 
                        wall_clock_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        supports_direct_stream = True, 
                        supports_direct_play = True, 
                        is_infinite_stream = True, 
                        requires_opening = True, 
                        open_token = '', 
                        requires_closing = True, 
                        live_stream_id = '', 
                        buffer_ms = 56, 
                        requires_looping = True, 
                        supports_probing = True, 
                        video3_d_format = 'HalfSideBySide', 
                        media_streams = [
                            embyapi.models.media_stream.MediaStream(
                                codec = '', 
                                codec_tag = '', 
                                language = '', 
                                color_transfer = '', 
                                color_primaries = '', 
                                color_space = '', 
                                comment = '', 
                                stream_start_time_ticks = 56, 
                                time_base = '', 
                                title = '', 
                                extradata = '', 
                                video_range = '', 
                                display_title = '', 
                                display_language = '', 
                                nal_length_size = '', 
                                is_interlaced = True, 
                                is_avc = True, 
                                channel_layout = '', 
                                bit_rate = 56, 
                                bit_depth = 56, 
                                ref_frames = 56, 
                                rotation = 56, 
                                channels = 56, 
                                sample_rate = 56, 
                                is_default = True, 
                                is_forced = True, 
                                is_hearing_impaired = True, 
                                height = 56, 
                                width = 56, 
                                average_frame_rate = 1.337, 
                                real_frame_rate = 1.337, 
                                profile = '', 
                                aspect_ratio = '', 
                                index = 56, 
                                is_external = True, 
                                delivery_method = 'Encode', 
                                delivery_url = '', 
                                is_external_url = True, 
                                is_text_subtitle_stream = True, 
                                supports_external_stream = True, 
                                path = '', 
                                pixel_format = '', 
                                level = 1.337, 
                                is_anamorphic = True, 
                                extended_video_type = 'None', 
                                extended_video_sub_type = 'None', 
                                extended_video_sub_type_description = '', 
                                item_id = '', 
                                server_id = '', 
                                attachment_size = 56, 
                                mime_type = '', 
                                subtitle_location_type = 'InternalStream', )
                            ], 
                        formats = [
                            ''
                            ], 
                        bitrate = 56, 
                        timestamp = 'None', 
                        required_http_headers = {
                            'key' : ''
                            }, 
                        direct_stream_url = '', 
                        add_api_key_to_direct_stream_url = True, 
                        transcoding_url = '', 
                        transcoding_sub_protocol = '', 
                        transcoding_container = '', 
                        analyze_duration_ms = 56, 
                        read_at_native_framerate = True, 
                        default_audio_stream_index = 56, 
                        default_subtitle_stream_index = 56, 
                        item_id = '', 
                        server_id = '', )
                    ],
                play_session_id = '',
                error_code = 'NotAllowed'
            )
        else:
            return PlaybackInfoResponse(
        )
        """

    def testPlaybackInfoResponse(self):
        """Test PlaybackInfoResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
