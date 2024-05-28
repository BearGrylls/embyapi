# ResponseProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** |  | [optional] 
**audio_codec** | **str** |  | [optional] 
**video_codec** | **str** |  | [optional] 
**type** | [**DlnaProfileType**](DlnaProfileType.md) |  | [optional] 
**org_pn** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**conditions** | [**List[ProfileCondition]**](ProfileCondition.md) |  | [optional] 

## Example

```python
from embyapi.models.response_profile import ResponseProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseProfile from a JSON string
response_profile_instance = ResponseProfile.from_json(json)
# print the JSON string representation of the object
print(ResponseProfile.to_json())

# convert the object into a dict
response_profile_dict = response_profile_instance.to_dict()
# create an instance of ResponseProfile from a dict
response_profile_from_dict = ResponseProfile.from_dict(response_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


