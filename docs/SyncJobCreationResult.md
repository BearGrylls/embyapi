# SyncJobCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**SyncJob**](SyncJob.md) |  | [optional] 
**job_items** | [**List[SyncJobItem]**](SyncJobItem.md) |  | [optional] 

## Example

```python
from embyapi.models.sync_job_creation_result import SyncJobCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of SyncJobCreationResult from a JSON string
sync_job_creation_result_instance = SyncJobCreationResult.from_json(json)
# print the JSON string representation of the object
print(SyncJobCreationResult.to_json())

# convert the object into a dict
sync_job_creation_result_dict = sync_job_creation_result_instance.to_dict()
# create an instance of SyncJobCreationResult from a dict
sync_job_creation_result_from_dict = SyncJobCreationResult.from_dict(sync_job_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


