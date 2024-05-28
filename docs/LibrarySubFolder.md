# LibrarySubFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**is_user_access_configurable** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.library_sub_folder import LibrarySubFolder

# TODO update the JSON string below
json = "{}"
# create an instance of LibrarySubFolder from a JSON string
library_sub_folder_instance = LibrarySubFolder.from_json(json)
# print the JSON string representation of the object
print(LibrarySubFolder.to_json())

# convert the object into a dict
library_sub_folder_dict = library_sub_folder_instance.to_dict()
# create an instance of LibrarySubFolder from a dict
library_sub_folder_from_dict = LibrarySubFolder.from_dict(library_sub_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


