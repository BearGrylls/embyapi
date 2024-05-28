# TranscodingVpStepInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_type** | [**TranscodingVpStepTypes**](TranscodingVpStepTypes.md) |  | [optional] 
**step_type_name** | **str** |  | [optional] 
**hardware_context_name** | **str** |  | [optional] 
**is_hardware_context** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**short** | **str** |  | [optional] 
**ffmpeg_name** | **str** |  | [optional] 
**ffmpeg_description** | **str** |  | [optional] 
**ffmpeg_options** | **str** |  | [optional] 
**param** | **str** |  | [optional] 
**param_short** | **str** |  | [optional] 

## Example

```python
from embyapi.models.transcoding_vp_step_info import TranscodingVpStepInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodingVpStepInfo from a JSON string
transcoding_vp_step_info_instance = TranscodingVpStepInfo.from_json(json)
# print the JSON string representation of the object
print(TranscodingVpStepInfo.to_json())

# convert the object into a dict
transcoding_vp_step_info_dict = transcoding_vp_step_info_instance.to_dict()
# create an instance of TranscodingVpStepInfo from a dict
transcoding_vp_step_info_from_dict = TranscodingVpStepInfo.from_dict(transcoding_vp_step_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


