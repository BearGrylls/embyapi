# LibraryRenameVirtualFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 

## Example

```python
from embyapi.models.library_rename_virtual_folder import LibraryRenameVirtualFolder

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryRenameVirtualFolder from a JSON string
library_rename_virtual_folder_instance = LibraryRenameVirtualFolder.from_json(json)
# print the JSON string representation of the object
print(LibraryRenameVirtualFolder.to_json())

# convert the object into a dict
library_rename_virtual_folder_dict = library_rename_virtual_folder_instance.to_dict()
# create an instance of LibraryRenameVirtualFolder from a dict
library_rename_virtual_folder_from_dict = LibraryRenameVirtualFolder.from_dict(library_rename_virtual_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


