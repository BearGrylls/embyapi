# LibraryUpdateLibraryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**library_options** | [**LibraryOptions**](LibraryOptions.md) |  | [optional] 

## Example

```python
from embyapi.models.library_update_library_options import LibraryUpdateLibraryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryUpdateLibraryOptions from a JSON string
library_update_library_options_instance = LibraryUpdateLibraryOptions.from_json(json)
# print the JSON string representation of the object
print(LibraryUpdateLibraryOptions.to_json())

# convert the object into a dict
library_update_library_options_dict = library_update_library_options_instance.to_dict()
# create an instance of LibraryUpdateLibraryOptions from a dict
library_update_library_options_from_dict = LibraryUpdateLibraryOptions.from_dict(library_update_library_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


