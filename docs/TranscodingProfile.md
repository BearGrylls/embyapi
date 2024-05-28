# TranscodingProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** |  | [optional] 
**type** | [**DlnaProfileType**](DlnaProfileType.md) |  | [optional] 
**video_codec** | **str** |  | [optional] 
**audio_codec** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**estimate_content_length** | **bool** |  | [optional] 
**enable_mpegts_m2_ts_mode** | **bool** |  | [optional] 
**transcode_seek_info** | [**TranscodeSeekInfo**](TranscodeSeekInfo.md) |  | [optional] 
**copy_timestamps** | **bool** |  | [optional] 
**context** | [**EncodingContext**](EncodingContext.md) |  | [optional] 
**max_audio_channels** | **str** |  | [optional] 
**min_segments** | **int** |  | [optional] 
**segment_length** | **int** |  | [optional] 
**break_on_non_key_frames** | **bool** |  | [optional] 
**allow_interlaced_video_stream_copy** | **bool** |  | [optional] 
**manifest_subtitles** | **str** |  | [optional] 
**max_manifest_subtitles** | **int** |  | [optional] 
**max_width** | **int** |  | [optional] 
**max_height** | **int** |  | [optional] 
**fill_empty_subtitle_segments** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.transcoding_profile import TranscodingProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodingProfile from a JSON string
transcoding_profile_instance = TranscodingProfile.from_json(json)
# print the JSON string representation of the object
print(TranscodingProfile.to_json())

# convert the object into a dict
transcoding_profile_dict = transcoding_profile_instance.to_dict()
# create an instance of TranscodingProfile from a dict
transcoding_profile_from_dict = TranscodingProfile.from_dict(transcoding_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


