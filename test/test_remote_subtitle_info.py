# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.remote_subtitle_info import RemoteSubtitleInfo

class TestRemoteSubtitleInfo(unittest.TestCase):
    """RemoteSubtitleInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteSubtitleInfo:
        """Test RemoteSubtitleInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteSubtitleInfo`
        """
        model = RemoteSubtitleInfo()
        if include_optional:
            return RemoteSubtitleInfo(
                three_letter_iso_language_name = '',
                id = '',
                provider_name = '',
                name = '',
                format = '',
                author = '',
                comment = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                community_rating = 1.337,
                download_count = 56,
                is_hash_match = True,
                is_forced = True,
                is_hearing_impaired = True,
                language = ''
            )
        else:
            return RemoteSubtitleInfo(
        )
        """

    def testRemoteSubtitleInfo(self):
        """Test RemoteSubtitleInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
