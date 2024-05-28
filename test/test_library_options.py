# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.library_options import LibraryOptions

class TestLibraryOptions(unittest.TestCase):
    """LibraryOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LibraryOptions:
        """Test LibraryOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LibraryOptions`
        """
        model = LibraryOptions()
        if include_optional:
            return LibraryOptions(
                enable_archive_media_files = True,
                enable_photos = True,
                enable_realtime_monitor = True,
                enable_marker_detection = True,
                enable_marker_detection_during_library_scan = True,
                intro_detection_fingerprint_length = 56,
                enable_chapter_image_extraction = True,
                extract_chapter_images_during_library_scan = True,
                download_images_in_advance = True,
                cache_images = True,
                path_infos = [
                    embyapi.models.media_path_info.MediaPathInfo(
                        path = '', 
                        network_path = '', 
                        username = '', 
                        password = '', )
                    ],
                ignore_hidden_files = True,
                ignore_file_extensions = [
                    ''
                    ],
                save_local_metadata = True,
                save_metadata_hidden = True,
                save_local_thumbnail_sets = True,
                import_playlists = True,
                enable_automatic_series_grouping = True,
                share_embedded_music_album_images = True,
                enable_embedded_titles = True,
                enable_audio_resume = True,
                auto_generate_chapters = True,
                automatic_refresh_interval_days = 56,
                placeholder_metadata_refresh_interval_days = 56,
                preferred_metadata_language = '',
                preferred_image_language = '',
                content_type = '',
                metadata_country_code = '',
                metadata_savers = [
                    ''
                    ],
                disabled_local_metadata_readers = [
                    ''
                    ],
                local_metadata_reader_order = [
                    ''
                    ],
                disabled_lyrics_fetchers = [
                    ''
                    ],
                save_lyrics_with_media = True,
                lyrics_download_max_age_days = 56,
                lyrics_fetcher_order = [
                    ''
                    ],
                lyrics_download_languages = [
                    ''
                    ],
                disabled_subtitle_fetchers = [
                    ''
                    ],
                subtitle_fetcher_order = [
                    ''
                    ],
                skip_subtitles_if_embedded_subtitles_present = True,
                skip_subtitles_if_audio_track_matches = True,
                subtitle_download_languages = [
                    ''
                    ],
                subtitle_download_max_age_days = 56,
                require_perfect_subtitle_match = True,
                save_subtitles_with_media = True,
                forced_subtitles_only = True,
                hearing_impaired_subtitles_only = True,
                type_options = [
                    embyapi.models.type_options.TypeOptions(
                        type = '', 
                        metadata_fetchers = [
                            ''
                            ], 
                        metadata_fetcher_order = [
                            ''
                            ], 
                        image_fetchers = [
                            ''
                            ], 
                        image_fetcher_order = [
                            ''
                            ], 
                        image_options = [
                            embyapi.models.image_option.ImageOption(
                                type = 'Primary', 
                                limit = 56, 
                                min_width = 56, )
                            ], )
                    ],
                collapse_single_item_folders = True,
                enable_adult_metadata = True,
                import_collections = True,
                min_collection_items = 56,
                music_folder_structure = '',
                min_resume_pct = 56,
                max_resume_pct = 56,
                min_resume_duration_seconds = 56,
                thumbnail_images_interval_seconds = 56,
                sample_ignore_size = 56
            )
        else:
            return LibraryOptions(
        )
        """

    def testLibraryOptions(self):
        """Test LibraryOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
