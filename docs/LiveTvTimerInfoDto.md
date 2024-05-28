# LiveTvTimerInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**LiveTvRecordingStatus**](LiveTvRecordingStatus.md) |  | [optional] 
**series_timer_id** | **str** | The series timer identifier. | [optional] 
**run_time_ticks** | **int** | The run time ticks. | [optional] 
**program_info** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**timer_type** | [**LiveTvTimerType**](LiveTvTimerType.md) |  | [optional] 
**id** | **str** | Id of the recording. | [optional] 
**type** | **str** |  | [optional] 
**server_id** | **str** | The server identifier. | [optional] 
**channel_id** | **str** | ChannelId of the recording. | [optional] 
**channel_name** | **str** | ChannelName of the recording. | [optional] 
**channel_number** | **str** |  | [optional] 
**channel_primary_image_tag** | **str** |  | [optional] 
**program_id** | **str** | The program identifier. | [optional] 
**name** | **str** | Name of the recording. | [optional] 
**overview** | **str** | Description of the recording. | [optional] 
**parent_folder_id** | **str** |  | [optional] 
**start_date** | **datetime** | The start date of the recording, in UTC. | [optional] 
**end_date** | **datetime** | The end date of the recording, in UTC. | [optional] 
**priority** | **int** | The priority. | [optional] 
**pre_padding_seconds** | **int** | The pre padding seconds. | [optional] 
**post_padding_seconds** | **int** | The post padding seconds. | [optional] 
**is_pre_padding_required** | **bool** | A value indicating whether this instance is pre padding required. | [optional] 
**parent_backdrop_item_id** | **str** | If the item does not have any backdrops, this will hold the Id of the Parent that has one. | [optional] 
**parent_backdrop_image_tags** | **List[str]** | The parent backdrop image tags. | [optional] 
**is_post_padding_required** | **bool** | A value indicating whether this instance is post padding required. | [optional] 
**keep_until** | [**LiveTvKeepUntil**](LiveTvKeepUntil.md) |  | [optional] 

## Example

```python
from embyapi.models.live_tv_timer_info_dto import LiveTvTimerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvTimerInfoDto from a JSON string
live_tv_timer_info_dto_instance = LiveTvTimerInfoDto.from_json(json)
# print the JSON string representation of the object
print(LiveTvTimerInfoDto.to_json())

# convert the object into a dict
live_tv_timer_info_dto_dict = live_tv_timer_info_dto_instance.to_dict()
# create an instance of LiveTvTimerInfoDto from a dict
live_tv_timer_info_dto_from_dict = LiveTvTimerInfoDto.from_dict(live_tv_timer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


