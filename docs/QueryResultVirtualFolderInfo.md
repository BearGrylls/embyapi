# QueryResultVirtualFolderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VirtualFolderInfo]**](VirtualFolderInfo.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_virtual_folder_info import QueryResultVirtualFolderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultVirtualFolderInfo from a JSON string
query_result_virtual_folder_info_instance = QueryResultVirtualFolderInfo.from_json(json)
# print the JSON string representation of the object
print(QueryResultVirtualFolderInfo.to_json())

# convert the object into a dict
query_result_virtual_folder_info_dict = query_result_virtual_folder_info_instance.to_dict()
# create an instance of QueryResultVirtualFolderInfo from a dict
query_result_virtual_folder_info_from_dict = QueryResultVirtualFolderInfo.from_dict(query_result_virtual_folder_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


