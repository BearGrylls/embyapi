# LibraryAddMediaPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**path_info** | [**MediaPathInfo**](MediaPathInfo.md) |  | [optional] 
**refresh_library** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.library_add_media_path import LibraryAddMediaPath

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryAddMediaPath from a JSON string
library_add_media_path_instance = LibraryAddMediaPath.from_json(json)
# print the JSON string representation of the object
print(LibraryAddMediaPath.to_json())

# convert the object into a dict
library_add_media_path_dict = library_add_media_path_instance.to_dict()
# create an instance of LibraryAddMediaPath from a dict
library_add_media_path_from_dict = LibraryAddMediaPath.from_dict(library_add_media_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


