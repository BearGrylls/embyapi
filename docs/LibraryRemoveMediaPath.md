# LibraryRemoveMediaPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**refresh_library** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.library_remove_media_path import LibraryRemoveMediaPath

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryRemoveMediaPath from a JSON string
library_remove_media_path_instance = LibraryRemoveMediaPath.from_json(json)
# print the JSON string representation of the object
print(LibraryRemoveMediaPath.to_json())

# convert the object into a dict
library_remove_media_path_dict = library_remove_media_path_instance.to_dict()
# create an instance of LibraryRemoveMediaPath from a dict
library_remove_media_path_from_dict = LibraryRemoveMediaPath.from_dict(library_remove_media_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


