# ProfileLevelInformation

A class combining both `Emby.Media.Model.Types.ProfileInformation` and `Emby.Media.Model.Types.LevelInformation`.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileInformation**](ProfileInformation.md) |  | [optional] 
**level** | [**LevelInformation**](LevelInformation.md) |  | [optional] 

## Example

```python
from embyapi.models.profile_level_information import ProfileLevelInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileLevelInformation from a JSON string
profile_level_information_instance = ProfileLevelInformation.from_json(json)
# print the JSON string representation of the object
print(ProfileLevelInformation.to_json())

# convert the object into a dict
profile_level_information_dict = profile_level_information_instance.to_dict()
# create an instance of ProfileLevelInformation from a dict
profile_level_information_from_dict = ProfileLevelInformation.from_dict(profile_level_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


