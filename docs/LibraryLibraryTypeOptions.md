# LibraryLibraryTypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**metadata_fetchers** | [**List[LibraryLibraryOptionInfo]**](LibraryLibraryOptionInfo.md) |  | [optional] 
**image_fetchers** | [**List[LibraryLibraryOptionInfo]**](LibraryLibraryOptionInfo.md) |  | [optional] 
**supported_image_types** | [**List[ImageType]**](ImageType.md) |  | [optional] 
**default_image_options** | [**List[ImageOption]**](ImageOption.md) |  | [optional] 

## Example

```python
from embyapi.models.library_library_type_options import LibraryLibraryTypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryLibraryTypeOptions from a JSON string
library_library_type_options_instance = LibraryLibraryTypeOptions.from_json(json)
# print the JSON string representation of the object
print(LibraryLibraryTypeOptions.to_json())

# convert the object into a dict
library_library_type_options_dict = library_library_type_options_instance.to_dict()
# create an instance of LibraryLibraryTypeOptions from a dict
library_library_type_options_from_dict = LibraryLibraryTypeOptions.from_dict(library_library_type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


