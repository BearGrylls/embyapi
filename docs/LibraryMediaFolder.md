# LibraryMediaFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**sub_folders** | [**List[LibrarySubFolder]**](LibrarySubFolder.md) |  | [optional] 
**is_user_access_configurable** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.library_media_folder import LibraryMediaFolder

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryMediaFolder from a JSON string
library_media_folder_instance = LibraryMediaFolder.from_json(json)
# print the JSON string representation of the object
print(LibraryMediaFolder.to_json())

# convert the object into a dict
library_media_folder_dict = library_media_folder_instance.to_dict()
# create an instance of LibraryMediaFolder from a dict
library_media_folder_from_dict = LibraryMediaFolder.from_dict(library_media_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


