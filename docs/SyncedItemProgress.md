# SyncedItemProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **float** |  | [optional] 
**status** | [**SyncJobItemStatus**](SyncJobItemStatus.md) |  | [optional] 

## Example

```python
from embyapi.models.synced_item_progress import SyncedItemProgress

# TODO update the JSON string below
json = "{}"
# create an instance of SyncedItemProgress from a JSON string
synced_item_progress_instance = SyncedItemProgress.from_json(json)
# print the JSON string representation of the object
print(SyncedItemProgress.to_json())

# convert the object into a dict
synced_item_progress_dict = synced_item_progress_instance.to_dict()
# create an instance of SyncedItemProgress from a dict
synced_item_progress_from_dict = SyncedItemProgress.from_dict(synced_item_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


