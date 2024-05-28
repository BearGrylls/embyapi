# DlnaProfilesDlnaProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DlnaProfilesDeviceProfileType**](DlnaProfilesDeviceProfileType.md) |  | [optional] 
**path** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**album_art_pn** | **str** |  | [optional] 
**max_album_art_width** | **int** |  | [optional] 
**max_album_art_height** | **int** |  | [optional] 
**max_icon_width** | **int** |  | [optional] 
**max_icon_height** | **int** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**manufacturer_url** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**model_description** | **str** |  | [optional] 
**model_number** | **str** |  | [optional] 
**model_url** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**enable_album_art_in_didl** | **bool** |  | [optional] 
**enable_single_album_art_limit** | **bool** |  | [optional] 
**enable_single_subtitle_limit** | **bool** |  | [optional] 
**protocol_info** | **str** |  | [optional] 
**timeline_offset_seconds** | **int** |  | [optional] 
**requires_plain_video_items** | **bool** |  | [optional] 
**requires_plain_folders** | **bool** |  | [optional] 
**ignore_transcode_byte_range_requests** | **bool** |  | [optional] 
**supports_samsung_bookmark** | **bool** |  | [optional] 
**identification** | [**DlnaProfilesDeviceIdentification**](DlnaProfilesDeviceIdentification.md) |  | [optional] 
**protocol_info_detection** | [**DlnaProfilesProtocolInfoDetection**](DlnaProfilesProtocolInfoDetection.md) |  | [optional] 
**name** | **str** | The name. | [optional] 
**id** | **str** |  | [optional] 
**supported_media_types** | **str** |  | [optional] 
**max_streaming_bitrate** | **int** |  | [optional] 
**music_streaming_transcoding_bitrate** | **int** |  | [optional] 
**max_static_music_bitrate** | **int** |  | [optional] 
**direct_play_profiles** | [**List[DirectPlayProfile]**](DirectPlayProfile.md) | The direct play profiles. | [optional] 
**transcoding_profiles** | [**List[TranscodingProfile]**](TranscodingProfile.md) | The transcoding profiles. | [optional] 
**container_profiles** | [**List[ContainerProfile]**](ContainerProfile.md) |  | [optional] 
**codec_profiles** | [**List[CodecProfile]**](CodecProfile.md) |  | [optional] 
**response_profiles** | [**List[ResponseProfile]**](ResponseProfile.md) |  | [optional] 
**subtitle_profiles** | [**List[SubtitleProfile]**](SubtitleProfile.md) |  | [optional] 

## Example

```python
from embyapi.models.dlna_profiles_dlna_profile import DlnaProfilesDlnaProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DlnaProfilesDlnaProfile from a JSON string
dlna_profiles_dlna_profile_instance = DlnaProfilesDlnaProfile.from_json(json)
# print the JSON string representation of the object
print(DlnaProfilesDlnaProfile.to_json())

# convert the object into a dict
dlna_profiles_dlna_profile_dict = dlna_profiles_dlna_profile_instance.to_dict()
# create an instance of DlnaProfilesDlnaProfile from a dict
dlna_profiles_dlna_profile_from_dict = DlnaProfilesDlnaProfile.from_dict(dlna_profiles_dlna_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


