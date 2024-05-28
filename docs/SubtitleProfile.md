# SubtitleProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**method** | [**SubtitleDeliveryMethod**](SubtitleDeliveryMethod.md) |  | [optional] 
**didl_mode** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 

## Example

```python
from embyapi.models.subtitle_profile import SubtitleProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleProfile from a JSON string
subtitle_profile_instance = SubtitleProfile.from_json(json)
# print the JSON string representation of the object
print(SubtitleProfile.to_json())

# convert the object into a dict
subtitle_profile_dict = subtitle_profile_instance.to_dict()
# create an instance of SubtitleProfile from a dict
subtitle_profile_from_dict = SubtitleProfile.from_dict(subtitle_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


