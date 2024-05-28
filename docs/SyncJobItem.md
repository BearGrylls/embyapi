# SyncJobItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**job_id** | **int** |  | [optional] 
**item_id** | **int** |  | [optional] 
**item_name** | **str** |  | [optional] 
**media_source_id** | **str** |  | [optional] 
**media_source** | [**MediaSourceInfo**](MediaSourceInfo.md) |  | [optional] 
**target_id** | **str** |  | [optional] 
**internal_target_id** | **int** |  | [optional] 
**output_path** | **str** |  | [optional] 
**status** | [**SyncJobItemStatus**](SyncJobItemStatus.md) |  | [optional] 
**progress** | **float** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**primary_image_item_id** | **str** |  | [optional] 
**primary_image_tag** | **str** |  | [optional] 
**temporary_path** | **str** |  | [optional] 
**additional_files** | [**List[ItemFileInfo]**](ItemFileInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.sync_job_item import SyncJobItem

# TODO update the JSON string below
json = "{}"
# create an instance of SyncJobItem from a JSON string
sync_job_item_instance = SyncJobItem.from_json(json)
# print the JSON string representation of the object
print(SyncJobItem.to_json())

# convert the object into a dict
sync_job_item_dict = sync_job_item_instance.to_dict()
# create an instance of SyncJobItem from a dict
sync_job_item_from_dict = SyncJobItem.from_dict(sync_job_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


