# ContainerProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DlnaProfileType**](DlnaProfileType.md) |  | [optional] 
**conditions** | [**List[ProfileCondition]**](ProfileCondition.md) |  | [optional] 
**container** | **str** |  | [optional] 

## Example

```python
from embyapi.models.container_profile import ContainerProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerProfile from a JSON string
container_profile_instance = ContainerProfile.from_json(json)
# print the JSON string representation of the object
print(ContainerProfile.to_json())

# convert the object into a dict
container_profile_dict = container_profile_instance.to_dict()
# create an instance of ContainerProfile from a dict
container_profile_from_dict = ContainerProfile.from_dict(container_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


