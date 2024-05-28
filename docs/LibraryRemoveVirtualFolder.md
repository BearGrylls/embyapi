# LibraryRemoveVirtualFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**refresh_library** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.library_remove_virtual_folder import LibraryRemoveVirtualFolder

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryRemoveVirtualFolder from a JSON string
library_remove_virtual_folder_instance = LibraryRemoveVirtualFolder.from_json(json)
# print the JSON string representation of the object
print(LibraryRemoveVirtualFolder.to_json())

# convert the object into a dict
library_remove_virtual_folder_dict = library_remove_virtual_folder_instance.to_dict()
# create an instance of LibraryRemoveVirtualFolder from a dict
library_remove_virtual_folder_from_dict = LibraryRemoveVirtualFolder.from_dict(library_remove_virtual_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


