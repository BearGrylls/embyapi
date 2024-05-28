# VideoCodecBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec_device_info** | [**CommonInterfacesICodecDeviceInfo**](CommonInterfacesICodecDeviceInfo.md) |  | [optional] 
**codec_kind** | [**CodecKinds**](CodecKinds.md) |  | [optional] 
**media_type_name** | **str** |  | [optional] 
**video_media_type** | [**VideoMediaTypes**](VideoMediaTypes.md) |  | [optional] 
**min_width** | **int** |  | [optional] 
**max_width** | **int** |  | [optional] 
**min_height** | **int** |  | [optional] 
**max_height** | **int** |  | [optional] 
**width_alignment** | **int** |  | [optional] 
**height_alignment** | **int** |  | [optional] 
**max_bit_rate** | [**BitRate**](BitRate.md) |  | [optional] 
**supported_color_formats** | [**List[ColorFormats]**](ColorFormats.md) |  | [optional] 
**supported_color_format_strings** | **List[str]** |  | [optional] 
**profile_and_level_information** | [**List[ProfileLevelInformation]**](ProfileLevelInformation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**direction** | [**CodecDirections**](CodecDirections.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**framework_codec** | **str** |  | [optional] 
**is_hardware_codec** | **bool** |  | [optional] 
**secondary_framework** | [**SecondaryFrameworks**](SecondaryFrameworks.md) |  | [optional] 
**secondary_framework_codec** | **str** |  | [optional] 
**max_instance_count** | **int** |  | [optional] 
**is_enabled_by_default** | **bool** |  | [optional] 
**default_priority** | **int** |  | [optional] 

## Example

```python
from embyapi.models.video_codec_base import VideoCodecBase

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCodecBase from a JSON string
video_codec_base_instance = VideoCodecBase.from_json(json)
# print the JSON string representation of the object
print(VideoCodecBase.to_json())

# convert the object into a dict
video_codec_base_dict = video_codec_base_instance.to_dict()
# create an instance of VideoCodecBase from a dict
video_codec_base_from_dict = VideoCodecBase.from_dict(video_codec_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


