# LibraryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_archive_media_files** | **bool** |  | [optional] 
**enable_photos** | **bool** |  | [optional] 
**enable_realtime_monitor** | **bool** |  | [optional] 
**enable_marker_detection** | **bool** |  | [optional] 
**enable_marker_detection_during_library_scan** | **bool** |  | [optional] 
**intro_detection_fingerprint_length** | **int** |  | [optional] 
**enable_chapter_image_extraction** | **bool** |  | [optional] 
**extract_chapter_images_during_library_scan** | **bool** |  | [optional] 
**download_images_in_advance** | **bool** |  | [optional] 
**cache_images** | **bool** |  | [optional] 
**path_infos** | [**List[MediaPathInfo]**](MediaPathInfo.md) |  | [optional] 
**ignore_hidden_files** | **bool** |  | [optional] 
**ignore_file_extensions** | **List[str]** |  | [optional] 
**save_local_metadata** | **bool** |  | [optional] 
**save_metadata_hidden** | **bool** |  | [optional] 
**save_local_thumbnail_sets** | **bool** |  | [optional] 
**import_playlists** | **bool** |  | [optional] 
**enable_automatic_series_grouping** | **bool** |  | [optional] 
**share_embedded_music_album_images** | **bool** |  | [optional] 
**enable_embedded_titles** | **bool** |  | [optional] 
**enable_audio_resume** | **bool** |  | [optional] 
**auto_generate_chapters** | **bool** |  | [optional] 
**automatic_refresh_interval_days** | **int** |  | [optional] 
**placeholder_metadata_refresh_interval_days** | **int** |  | [optional] 
**preferred_metadata_language** | **str** | The preferred metadata language. | [optional] 
**preferred_image_language** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**metadata_country_code** | **str** | The metadata country code. | [optional] 
**metadata_savers** | **List[str]** |  | [optional] 
**disabled_local_metadata_readers** | **List[str]** |  | [optional] 
**local_metadata_reader_order** | **List[str]** |  | [optional] 
**disabled_lyrics_fetchers** | **List[str]** |  | [optional] 
**save_lyrics_with_media** | **bool** |  | [optional] 
**lyrics_download_max_age_days** | **int** |  | [optional] 
**lyrics_fetcher_order** | **List[str]** |  | [optional] 
**lyrics_download_languages** | **List[str]** |  | [optional] 
**disabled_subtitle_fetchers** | **List[str]** |  | [optional] 
**subtitle_fetcher_order** | **List[str]** |  | [optional] 
**skip_subtitles_if_embedded_subtitles_present** | **bool** |  | [optional] 
**skip_subtitles_if_audio_track_matches** | **bool** |  | [optional] 
**subtitle_download_languages** | **List[str]** |  | [optional] 
**subtitle_download_max_age_days** | **int** |  | [optional] 
**require_perfect_subtitle_match** | **bool** |  | [optional] 
**save_subtitles_with_media** | **bool** |  | [optional] 
**forced_subtitles_only** | **bool** |  | [optional] 
**hearing_impaired_subtitles_only** | **bool** |  | [optional] 
**type_options** | [**List[TypeOptions]**](TypeOptions.md) |  | [optional] 
**collapse_single_item_folders** | **bool** |  | [optional] 
**enable_adult_metadata** | **bool** |  | [optional] 
**import_collections** | **bool** |  | [optional] 
**min_collection_items** | **int** |  | [optional] 
**music_folder_structure** | **str** |  | [optional] 
**min_resume_pct** | **int** | The minimum percentage of an item that must be played in order for playstate to be updated. | [optional] 
**max_resume_pct** | **int** | The maximum percentage of an item that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. | [optional] 
**min_resume_duration_seconds** | **int** | The minimum duration that an item must have in order to be eligible for playstate updates.. | [optional] 
**thumbnail_images_interval_seconds** | **int** |  | [optional] 
**sample_ignore_size** | **int** |  | [optional] 

## Example

```python
from embyapi.models.library_options import LibraryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryOptions from a JSON string
library_options_instance = LibraryOptions.from_json(json)
# print the JSON string representation of the object
print(LibraryOptions.to_json())

# convert the object into a dict
library_options_dict = library_options_instance.to_dict()
# create an instance of LibraryOptions from a dict
library_options_from_dict = LibraryOptions.from_dict(library_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


