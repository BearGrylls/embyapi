# LibraryLibraryOptionsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_savers** | [**List[LibraryLibraryOptionInfo]**](LibraryLibraryOptionInfo.md) |  | [optional] 
**metadata_readers** | [**List[LibraryLibraryOptionInfo]**](LibraryLibraryOptionInfo.md) |  | [optional] 
**subtitle_fetchers** | [**List[LibraryLibraryOptionInfo]**](LibraryLibraryOptionInfo.md) |  | [optional] 
**lyrics_fetchers** | [**List[LibraryLibraryOptionInfo]**](LibraryLibraryOptionInfo.md) |  | [optional] 
**type_options** | [**List[LibraryLibraryTypeOptions]**](LibraryLibraryTypeOptions.md) |  | [optional] 

## Example

```python
from embyapi.models.library_library_options_result import LibraryLibraryOptionsResult

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryLibraryOptionsResult from a JSON string
library_library_options_result_instance = LibraryLibraryOptionsResult.from_json(json)
# print the JSON string representation of the object
print(LibraryLibraryOptionsResult.to_json())

# convert the object into a dict
library_library_options_result_dict = library_library_options_result_instance.to_dict()
# create an instance of LibraryLibraryOptionsResult from a dict
library_library_options_result_from_dict = LibraryLibraryOptionsResult.from_dict(library_library_options_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


