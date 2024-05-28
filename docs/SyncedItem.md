# SyncedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | [optional] 
**sync_job_id** | **int** |  | [optional] 
**sync_job_name** | **str** |  | [optional] 
**sync_job_date_created** | **datetime** |  | [optional] 
**sync_job_item_id** | **int** |  | [optional] 
**original_file_name** | **str** |  | [optional] 
**item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**additional_files** | [**List[ItemFileInfo]**](ItemFileInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.synced_item import SyncedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SyncedItem from a JSON string
synced_item_instance = SyncedItem.from_json(json)
# print the JSON string representation of the object
print(SyncedItem.to_json())

# convert the object into a dict
synced_item_dict = synced_item_instance.to_dict()
# create an instance of SyncedItem from a dict
synced_item_from_dict = SyncedItem.from_dict(synced_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


