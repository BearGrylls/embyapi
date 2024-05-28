# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.play_request import PlayRequest

class TestPlayRequest(unittest.TestCase):
    """PlayRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayRequest:
        """Test PlayRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayRequest`
        """
        model = PlayRequest()
        if include_optional:
            return PlayRequest(
                controlling_user_id = '',
                subtitle_stream_index = 56,
                audio_stream_index = 56,
                media_source_id = '',
                start_index = 56
            )
        else:
            return PlayRequest(
        )
        """

    def testPlayRequest(self):
        """Test PlayRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
