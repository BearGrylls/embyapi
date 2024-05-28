# IOFileSystemEntryInfo

Class FileSystemEntryInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**path** | **str** | The path. | [optional] 
**type** | [**IOFileSystemEntryType**](IOFileSystemEntryType.md) |  | [optional] 

## Example

```python
from embyapi.models.io_file_system_entry_info import IOFileSystemEntryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IOFileSystemEntryInfo from a JSON string
io_file_system_entry_info_instance = IOFileSystemEntryInfo.from_json(json)
# print the JSON string representation of the object
print(IOFileSystemEntryInfo.to_json())

# convert the object into a dict
io_file_system_entry_info_dict = io_file_system_entry_info_instance.to_dict()
# create an instance of IOFileSystemEntryInfo from a dict
io_file_system_entry_info_from_dict = IOFileSystemEntryInfo.from_dict(io_file_system_entry_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


