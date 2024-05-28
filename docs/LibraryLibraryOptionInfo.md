# LibraryLibraryOptionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**setup_url** | **str** |  | [optional] 
**default_enabled** | **bool** |  | [optional] 
**features** | [**List[MetadataFeatures]**](MetadataFeatures.md) |  | [optional] 

## Example

```python
from embyapi.models.library_library_option_info import LibraryLibraryOptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryLibraryOptionInfo from a JSON string
library_library_option_info_instance = LibraryLibraryOptionInfo.from_json(json)
# print the JSON string representation of the object
print(LibraryLibraryOptionInfo.to_json())

# convert the object into a dict
library_library_option_info_dict = library_library_option_info_instance.to_dict()
# create an instance of LibraryLibraryOptionInfo from a dict
library_library_option_info_from_dict = LibraryLibraryOptionInfo.from_dict(library_library_option_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


