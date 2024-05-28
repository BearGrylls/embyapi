# CodecProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CodecType**](CodecType.md) |  | [optional] 
**conditions** | [**List[ProfileCondition]**](ProfileCondition.md) |  | [optional] 
**apply_conditions** | [**List[ProfileCondition]**](ProfileCondition.md) |  | [optional] 
**codec** | **str** |  | [optional] 
**container** | **str** |  | [optional] 

## Example

```python
from embyapi.models.codec_profile import CodecProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CodecProfile from a JSON string
codec_profile_instance = CodecProfile.from_json(json)
# print the JSON string representation of the object
print(CodecProfile.to_json())

# convert the object into a dict
codec_profile_dict = codec_profile_instance.to_dict()
# create an instance of CodecProfile from a dict
codec_profile_from_dict = CodecProfile.from_dict(codec_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


