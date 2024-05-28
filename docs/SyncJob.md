# SyncJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**target_id** | **str** | The device identifier. | [optional] 
**internal_target_id** | **int** |  | [optional] 
**target_name** | **str** | The name of the target. | [optional] 
**quality** | **str** | The quality. | [optional] 
**bitrate** | **int** | The bitrate. | [optional] 
**container** | **str** |  | [optional] 
**video_codec** | **str** |  | [optional] 
**audio_codec** | **str** |  | [optional] 
**profile** | **str** | The profile. | [optional] 
**category** | [**SyncCategory**](SyncCategory.md) |  | [optional] 
**parent_id** | **int** | The parent identifier. | [optional] 
**progress** | **float** | The current progress. | [optional] 
**name** | **str** | The name. | [optional] 
**status** | [**SyncJobStatus**](SyncJobStatus.md) |  | [optional] 
**user_id** | **int** | The user identifier. | [optional] 
**unwatched_only** | **bool** | A value indicating whether \\[unwatched only\\]. | [optional] 
**sync_new_content** | **bool** | A value indicating whether \\[synchronize new content\\]. | [optional] 
**item_limit** | **int** | The item limit. | [optional] 
**requested_item_ids** | **List[int]** | The requested item ids. | [optional] 
**item_id** | **int** |  | [optional] 
**date_created** | **datetime** | The date created. | [optional] 
**date_last_modified** | **datetime** | The date last modified. | [optional] 
**item_count** | **int** | The item count. | [optional] 
**parent_name** | **str** |  | [optional] 
**primary_image_item_id** | **str** |  | [optional] 
**primary_image_tag** | **str** |  | [optional] 

## Example

```python
from embyapi.models.sync_job import SyncJob

# TODO update the JSON string below
json = "{}"
# create an instance of SyncJob from a JSON string
sync_job_instance = SyncJob.from_json(json)
# print the JSON string representation of the object
print(SyncJob.to_json())

# convert the object into a dict
sync_job_dict = sync_job_instance.to_dict()
# create an instance of SyncJob from a dict
sync_job_from_dict = SyncJob.from_dict(sync_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


