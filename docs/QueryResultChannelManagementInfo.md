# QueryResultChannelManagementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ChannelManagementInfo]**](ChannelManagementInfo.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_channel_management_info import QueryResultChannelManagementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultChannelManagementInfo from a JSON string
query_result_channel_management_info_instance = QueryResultChannelManagementInfo.from_json(json)
# print the JSON string representation of the object
print(QueryResultChannelManagementInfo.to_json())

# convert the object into a dict
query_result_channel_management_info_dict = query_result_channel_management_info_instance.to_dict()
# create an instance of QueryResultChannelManagementInfo from a dict
query_result_channel_management_info_from_dict = QueryResultChannelManagementInfo.from_dict(query_result_channel_management_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


