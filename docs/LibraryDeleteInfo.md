# LibraryDeleteInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | **List[str]** |  | [optional] 

## Example

```python
from embyapi.models.library_delete_info import LibraryDeleteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryDeleteInfo from a JSON string
library_delete_info_instance = LibraryDeleteInfo.from_json(json)
# print the JSON string representation of the object
print(LibraryDeleteInfo.to_json())

# convert the object into a dict
library_delete_info_dict = library_delete_info_instance.to_dict()
# create an instance of LibraryDeleteInfo from a dict
library_delete_info_from_dict = LibraryDeleteInfo.from_dict(library_delete_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


