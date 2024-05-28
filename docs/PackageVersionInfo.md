# PackageVersionInfo

Class PackageVersionInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**guid** | **str** | The guid. | [optional] 
**version_str** | **str** | The version STR. | [optional] 
**classification** | [**PackageVersionClass**](PackageVersionClass.md) |  | [optional] 
**description** | **str** | The description. | [optional] 
**required_version_str** | **str** | The required version STR. | [optional] 
**source_url** | **str** | The source URL. | [optional] 
**checksum** | **str** | The source URL. | [optional] 
**target_filename** | **str** | The target filename. | [optional] 
**info_url** | **str** |  | [optional] 
**runtimes** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from embyapi.models.package_version_info import PackageVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PackageVersionInfo from a JSON string
package_version_info_instance = PackageVersionInfo.from_json(json)
# print the JSON string representation of the object
print(PackageVersionInfo.to_json())

# convert the object into a dict
package_version_info_dict = package_version_info_instance.to_dict()
# create an instance of PackageVersionInfo from a dict
package_version_info_from_dict = PackageVersionInfo.from_dict(package_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


