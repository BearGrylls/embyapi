# DeviceProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from embyapi.models.device_profile import DeviceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceProfile from a JSON string
device_profile_instance = DeviceProfile.from_json(json)
# print the JSON string representation of the object
print(DeviceProfile.to_json())

# convert the object into a dict
device_profile_dict = device_profile_instance.to_dict()
# create an instance of DeviceProfile from a dict
device_profile_from_dict = DeviceProfile.from_dict(device_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


