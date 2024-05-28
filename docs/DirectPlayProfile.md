# DirectPlayProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** |  | [optional] 
**audio_codec** | **str** |  | [optional] 
**video_codec** | **str** |  | [optional] 
**type** | [**DlnaProfileType**](DlnaProfileType.md) |  | [optional] 

## Example

```python
from embyapi.models.direct_play_profile import DirectPlayProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DirectPlayProfile from a JSON string
direct_play_profile_instance = DirectPlayProfile.from_json(json)
# print the JSON string representation of the object
print(DirectPlayProfile.to_json())

# convert the object into a dict
direct_play_profile_dict = direct_play_profile_instance.to_dict()
# create an instance of DirectPlayProfile from a dict
direct_play_profile_from_dict = DirectPlayProfile.from_dict(direct_play_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


