# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.remote_search_query_book_info import RemoteSearchQueryBookInfo

class TestRemoteSearchQueryBookInfo(unittest.TestCase):
    """RemoteSearchQueryBookInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoteSearchQueryBookInfo:
        """Test RemoteSearchQueryBookInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoteSearchQueryBookInfo`
        """
        model = RemoteSearchQueryBookInfo()
        if include_optional:
            return RemoteSearchQueryBookInfo(
                search_info = embyapi.models.book_info.BookInfo(
                    series_name = '', 
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
                    enable_adult_metadata = True, ),
                item_id = 56,
                search_provider_name = '',
                providers = [
                    ''
                    ],
                include_disabled_providers = True
            )
        else:
            return RemoteSearchQueryBookInfo(
        )
        """

    def testRemoteSearchQueryBookInfo(self):
        """Test RemoteSearchQueryBookInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
