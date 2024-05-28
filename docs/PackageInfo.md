# PackageInfo

Class PackageInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The internal id of this package. | [optional] 
**name** | **str** | The name. | [optional] 
**short_description** | **str** | The short description. | [optional] 
**overview** | **str** | The overview. | [optional] 
**is_premium** | **bool** | A value indicating whether this instance is premium. | [optional] 
**adult** | **bool** | A value indicating whether this instance is adult only content. | [optional] 
**rich_desc_url** | **str** | The rich desc URL. | [optional] 
**thumb_image** | **str** | The thumb image. | [optional] 
**preview_image** | **str** | The preview image. | [optional] 
**type** | **str** | The type. | [optional] 
**target_filename** | **str** | The target filename. | [optional] 
**owner** | **str** | The owner. | [optional] 
**category** | **str** | The category. | [optional] 
**tile_color** | **str** | The catalog tile color. | [optional] 
**feature_id** | **str** | The feature id of this package (if premium). | [optional] 
**price** | **float** | The price for this package (if premium). | [optional] 
**target_system** | [**PackageTargetSystem**](PackageTargetSystem.md) |  | [optional] 
**guid** | **str** | The guid of the assembly associated with this package (if a plug\\-in). This is used to identify the proper item for automatic updates. | [optional] 
**is_registered** | **bool** | Whether or not this package is registered. | [optional] 
**exp_date** | **datetime** | The expiration date for this package. | [optional] 
**versions** | [**List[PackageVersionInfo]**](PackageVersionInfo.md) | The versions. | [optional] 
**enable_in_app_store** | **bool** | A value indicating whether \\[enable in application store\\]. | [optional] 
**installs** | **int** | The installs. | [optional] 

## Example

```python
from embyapi.models.package_info import PackageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PackageInfo from a JSON string
package_info_instance = PackageInfo.from_json(json)
# print the JSON string representation of the object
print(PackageInfo.to_json())

# convert the object into a dict
package_info_dict = package_info_instance.to_dict()
# create an instance of PackageInfo from a dict
package_info_from_dict = PackageInfo.from_dict(package_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


