# InstallationInfo

Class InstallationInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id. | [optional] 
**name** | **str** | The name. | [optional] 
**assembly_guid** | **str** | The assembly guid. | [optional] 
**version** | **str** | The version. | [optional] 
**update_class** | [**PackageVersionClass**](PackageVersionClass.md) |  | [optional] 
**percent_complete** | **float** | The percent complete. | [optional] 

## Example

```python
from embyapi.models.installation_info import InstallationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationInfo from a JSON string
installation_info_instance = InstallationInfo.from_json(json)
# print the JSON string representation of the object
print(InstallationInfo.to_json())

# convert the object into a dict
installation_info_dict = installation_info_instance.to_dict()
# create an instance of InstallationInfo from a dict
installation_info_from_dict = InstallationInfo.from_dict(installation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


