# LibraryMediaUpdateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**update_type** | **str** |  | [optional] 

## Example

```python
from embyapi.models.library_media_update_info import LibraryMediaUpdateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryMediaUpdateInfo from a JSON string
library_media_update_info_instance = LibraryMediaUpdateInfo.from_json(json)
# print the JSON string representation of the object
print(LibraryMediaUpdateInfo.to_json())

# convert the object into a dict
library_media_update_info_dict = library_media_update_info_instance.to_dict()
# create an instance of LibraryMediaUpdateInfo from a dict
library_media_update_info_from_dict = LibraryMediaUpdateInfo.from_dict(library_media_update_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


