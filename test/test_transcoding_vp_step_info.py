# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.transcoding_vp_step_info import TranscodingVpStepInfo

class TestTranscodingVpStepInfo(unittest.TestCase):
    """TranscodingVpStepInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TranscodingVpStepInfo:
        """Test TranscodingVpStepInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranscodingVpStepInfo`
        """
        model = TranscodingVpStepInfo()
        if include_optional:
            return TranscodingVpStepInfo(
                step_type = 'Decoder',
                step_type_name = '',
                hardware_context_name = '',
                is_hardware_context = True,
                name = '',
                short = '',
                ffmpeg_name = '',
                ffmpeg_description = '',
                ffmpeg_options = '',
                param = '',
                param_short = ''
            )
        else:
            return TranscodingVpStepInfo(
        )
        """

    def testTranscodingVpStepInfo(self):
        """Test TranscodingVpStepInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
