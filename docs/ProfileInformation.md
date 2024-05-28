# ProfileInformation

Class for unified presentation of all information associated with a specific codec profile.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** | The enum member name of the profile. | [optional] 
**description** | **str** | The common name of the profile. | [optional] 
**details** | **str** | Detail information about the profile. | [optional] 
**id** | **str** | A unique identifier. | [optional] 
**bit_depths** | **List[int]** | The bit depths. | [optional] 

## Example

```python
from embyapi.models.profile_information import ProfileInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileInformation from a JSON string
profile_information_instance = ProfileInformation.from_json(json)
# print the JSON string representation of the object
print(ProfileInformation.to_json())

# convert the object into a dict
profile_information_dict = profile_information_instance.to_dict()
# create an instance of ProfileInformation from a dict
profile_information_from_dict = ProfileInformation.from_dict(profile_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


