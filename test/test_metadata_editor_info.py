# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.metadata_editor_info import MetadataEditorInfo

class TestMetadataEditorInfo(unittest.TestCase):
    """MetadataEditorInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataEditorInfo:
        """Test MetadataEditorInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataEditorInfo`
        """
        model = MetadataEditorInfo()
        if include_optional:
            return MetadataEditorInfo(
                parental_rating_options = [
                    embyapi.models.parental_rating.ParentalRating(
                        name = '', 
                        value = 56, )
                    ],
                countries = [
                    embyapi.models.globalization/country_info.Globalization.CountryInfo(
                        name = '', 
                        display_name = '', 
                        english_name = '', 
                        two_letter_iso_region_name = '', 
                        three_letter_iso_region_name = '', )
                    ],
                cultures = [
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
                external_id_infos = [
                    embyapi.models.external_id_info.ExternalIdInfo(
                        name = '', 
                        key = '', 
                        website = '', 
                        url_format_string = '', 
                        is_supported_as_identifier = True, )
                    ]
            )
        else:
            return MetadataEditorInfo(
        )
        """

    def testMetadataEditorInfo(self):
        """Test MetadataEditorInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
