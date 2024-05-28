# QueryResultSyncJobItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SyncJobItem]**](SyncJobItem.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_sync_job_item import QueryResultSyncJobItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultSyncJobItem from a JSON string
query_result_sync_job_item_instance = QueryResultSyncJobItem.from_json(json)
# print the JSON string representation of the object
print(QueryResultSyncJobItem.to_json())

# convert the object into a dict
query_result_sync_job_item_dict = query_result_sync_job_item_instance.to_dict()
# create an instance of QueryResultSyncJobItem from a dict
query_result_sync_job_item_from_dict = QueryResultSyncJobItem.from_dict(query_result_sync_job_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


