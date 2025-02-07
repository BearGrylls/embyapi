# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.video_codec_base import VideoCodecBase

class TestVideoCodecBase(unittest.TestCase):
    """VideoCodecBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoCodecBase:
        """Test VideoCodecBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoCodecBase`
        """
        model = VideoCodecBase()
        if include_optional:
            return VideoCodecBase(
                codec_device_info = embyapi.models.common/interfaces/i_codec_device_info.Common.Interfaces.ICodecDeviceInfo(
                    capabilities = embyapi.models.common/interfaces/i_codec_device_capabilities.Common.Interfaces.ICodecDeviceCapabilities(
                        supports_hw_upload = True, 
                        supports_hw_download = True, 
                        supports_standalone_device_init = True, 
                        supports10_bit_processing = True, 
                        supports_native_tone_mapping = True, ), 
                    adapter = 56, 
                    name = '', 
                    desription = '', 
                    driver = '', 
                    driver_version = embyapi.models.version.Version(
                        major = 56, 
                        minor = 56, 
                        build = 56, 
                        revision = 56, 
                        major_revision = 56, 
                        minor_revision = 56, ), 
                    api_version = embyapi.models.version.Version(
                        major = 56, 
                        minor = 56, 
                        build = 56, 
                        revision = 56, 
                        major_revision = 56, 
                        minor_revision = 56, ), 
                    vendor_id = 56, 
                    device_id = 56, 
                    device_identifier = '', 
                    hardware_context_framework = 'Unknown', 
                    dev_path = '', 
                    drm_node = '', 
                    vendor_name = '', 
                    device_name = '', ),
                codec_kind = 'Audio',
                media_type_name = '',
                video_media_type = 'Unknown',
                min_width = 56,
                max_width = 56,
                min_height = 56,
                max_height = 56,
                width_alignment = 56,
                height_alignment = 56,
                max_bit_rate = embyapi.models.bit_rate.BitRate(
                    bps = 56, 
                    kbps = 1.337, 
                    mbps = 1.337, ),
                supported_color_formats = [
                    'Unknown'
                    ],
                supported_color_format_strings = [
                    ''
                    ],
                profile_and_level_information = [
                    embyapi.models.profile_level_information.ProfileLevelInformation(
                        profile = embyapi.models.profile_information.ProfileInformation(
                            short_name = '', 
                            description = '', 
                            details = '', 
                            id = '', 
                            bit_depths = [
                                56
                                ], ), 
                        level = embyapi.models.level_information.LevelInformation(
                            short_name = '', 
                            description = '', 
                            ordinal = 56, 
                            max_bit_rate = embyapi.models.bit_rate.BitRate(
                                bps = 56, 
                                kbps = 1.337, 
                                mbps = 1.337, ), 
                            max_bit_rate_display = '', 
                            id = '', 
                            resolution_rates = [
                                embyapi.models.resolution_with_rate.ResolutionWithRate(
                                    width = 56, 
                                    height = 56, 
                                    frame_rate = 1.337, 
                                    resolution = embyapi.models.resolution.Resolution(
                                        width = 56, 
                                        height = 56, ), )
                                ], 
                            resolution_rate_strings = [
                                ''
                                ], 
                            resolution_rates_display = '', ), )
                    ],
                id = '',
                direction = 'Encoder',
                name = '',
                description = '',
                framework_codec = '',
                is_hardware_codec = True,
                secondary_framework = 'Unknown',
                secondary_framework_codec = '',
                max_instance_count = 56,
                is_enabled_by_default = True,
                default_priority = 56
            )
        else:
            return VideoCodecBase(
        )
        """

    def testVideoCodecBase(self):
        """Test VideoCodecBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
