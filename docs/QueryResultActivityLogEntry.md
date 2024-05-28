# QueryResultActivityLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ActivityLogEntry]**](ActivityLogEntry.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_activity_log_entry import QueryResultActivityLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultActivityLogEntry from a JSON string
query_result_activity_log_entry_instance = QueryResultActivityLogEntry.from_json(json)
# print the JSON string representation of the object
print(QueryResultActivityLogEntry.to_json())

# convert the object into a dict
query_result_activity_log_entry_dict = query_result_activity_log_entry_instance.to_dict()
# create an instance of QueryResultActivityLogEntry from a dict
query_result_activity_log_entry_from_dict = QueryResultActivityLogEntry.from_dict(query_result_activity_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


