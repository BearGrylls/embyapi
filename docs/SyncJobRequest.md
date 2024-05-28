# SyncJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **str** |  | [optional] 
**item_ids** | **List[str]** |  | [optional] 
**category** | [**SyncCategory**](SyncCategory.md) |  | [optional] 
**parent_id** | **str** |  | [optional] 
**quality** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**video_codec** | **str** |  | [optional] 
**audio_codec** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**unwatched_only** | **bool** |  | [optional] 
**sync_new_content** | **bool** |  | [optional] 
**item_limit** | **int** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**downloaded** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.sync_job_request import SyncJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncJobRequest from a JSON string
sync_job_request_instance = SyncJobRequest.from_json(json)
# print the JSON string representation of the object
print(SyncJobRequest.to_json())

# convert the object into a dict
sync_job_request_dict = sync_job_request_instance.to_dict()
# create an instance of SyncJobRequest from a dict
sync_job_request_from_dict = SyncJobRequest.from_dict(sync_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


