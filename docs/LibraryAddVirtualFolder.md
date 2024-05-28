# LibraryAddVirtualFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**collection_type** | **str** |  | [optional] 
**refresh_library** | **bool** |  | [optional] 
**paths** | **List[str]** |  | [optional] 
**library_options** | [**LibraryOptions**](LibraryOptions.md) |  | [optional] 

## Example

```python
from embyapi.models.library_add_virtual_folder import LibraryAddVirtualFolder

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryAddVirtualFolder from a JSON string
library_add_virtual_folder_instance = LibraryAddVirtualFolder.from_json(json)
# print the JSON string representation of the object
print(LibraryAddVirtualFolder.to_json())

# convert the object into a dict
library_add_virtual_folder_dict = library_add_virtual_folder_instance.to_dict()
# create an instance of LibraryAddVirtualFolder from a dict
library_add_virtual_folder_from_dict = LibraryAddVirtualFolder.from_dict(library_add_virtual_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


