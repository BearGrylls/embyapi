# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.remote_search_query_album_info import RemoteSearchQueryAlbumInfo

class TestRemoteSearchQueryAlbumInfo(unittest.TestCase):
    """RemoteSearchQueryAlbumInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteSearchQueryAlbumInfo:
        """Test RemoteSearchQueryAlbumInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteSearchQueryAlbumInfo`
        """
        model = RemoteSearchQueryAlbumInfo()
        if include_optional:
            return RemoteSearchQueryAlbumInfo(
                search_info = embyapi.models.album_info.AlbumInfo(
                    album_artists = [
                        ''
                        ], 
                    song_infos = [
                        embyapi.models.song_info.SongInfo(
                            album = '', 
                            artists = [
                                ''
                                ], 
                            composers = [
                                ''
                                ], 
                            name = '', 
                            metadata_language = '', 
                            metadata_country_code = '', 
                            metadata_languages = [
                                embyapi.models.globalization/culture_dto.Globalization.CultureDto(
                                    name = '', 
                                    display_name = '', 
                                    two_letter_iso_language_name = '', 
                                    three_letter_iso_language_name = '', 
                                    three_letter_iso_language_names = [
                                        ''
                                        ], 
                                    two_letter_iso_language_names = [
                                        ''
                                        ], )
                                ], 
                            provider_ids = {
                                'key' : ''
                                }, 
                            year = 56, 
                            index_number = 56, 
                            parent_index_number = 56, 
                            premiere_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            is_automated = True, 
                            enable_adult_metadata = True, )
                        ], 
                    name = '', 
                    metadata_language = '', 
                    metadata_country_code = '', 
                    metadata_languages = [
                        embyapi.models.globalization/culture_dto.Globalization.CultureDto(
                            name = '', 
                            display_name = '', 
                            two_letter_iso_language_name = '', 
                            three_letter_iso_language_name = '', )
                        ], 
                    provider_ids = {
                        'key' : ''
                        }, 
                    year = 56, 
                    index_number = 56, 
                    parent_index_number = 56, 
                    premiere_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_automated = True, 
                    enable_adult_metadata = True, ),
                item_id = 56,
                search_provider_name = '',
                providers = [
                    ''
                    ],
                include_disabled_providers = True
            )
        else:
            return RemoteSearchQueryAlbumInfo(
        )
        """

    def testRemoteSearchQueryAlbumInfo(self):
        """Test RemoteSearchQueryAlbumInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
