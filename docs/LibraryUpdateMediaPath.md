# LibraryUpdateMediaPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path_info** | [**MediaPathInfo**](MediaPathInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.library_update_media_path import LibraryUpdateMediaPath

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryUpdateMediaPath from a JSON string
library_update_media_path_instance = LibraryUpdateMediaPath.from_json(json)
# print the JSON string representation of the object
print(LibraryUpdateMediaPath.to_json())

# convert the object into a dict
library_update_media_path_dict = library_update_media_path_instance.to_dict()
# create an instance of LibraryUpdateMediaPath from a dict
library_update_media_path_from_dict = LibraryUpdateMediaPath.from_dict(library_update_media_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


