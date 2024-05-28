# QueryResultSyncJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SyncJob]**](SyncJob.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_sync_job import QueryResultSyncJob

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultSyncJob from a JSON string
query_result_sync_job_instance = QueryResultSyncJob.from_json(json)
# print the JSON string representation of the object
print(QueryResultSyncJob.to_json())

# convert the object into a dict
query_result_sync_job_dict = query_result_sync_job_instance.to_dict()
# create an instance of QueryResultSyncJob from a dict
query_result_sync_job_from_dict = QueryResultSyncJob.from_dict(query_result_sync_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


