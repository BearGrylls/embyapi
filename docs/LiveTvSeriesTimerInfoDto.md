# LiveTvSeriesTimerInfoDto

Class SeriesTimerInfoDto.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_any_time** | **bool** | A value indicating whether \\[record any time\\]. | [optional] 
**skip_episodes_in_library** | **bool** |  | [optional] 
**match_existing_items_with_any_library** | **bool** |  | [optional] 
**record_any_channel** | **bool** | A value indicating whether \\[record any channel\\]. | [optional] 
**keep_up_to** | **int** |  | [optional] 
**max_recording_seconds** | **int** |  | [optional] 
**record_new_only** | **bool** | A value indicating whether \\[record new only\\]. | [optional] 
**channel_ids** | **List[str]** |  | [optional] 
**days** | [**List[DayOfWeek]**](DayOfWeek.md) | The days. | [optional] 
**image_tags** | **Dict[str, str]** | The image tags. | [optional] 
**parent_thumb_item_id** | **str** | The parent thumb item id. | [optional] 
**parent_thumb_image_tag** | **str** | The parent thumb image tag. | [optional] 
**parent_primary_image_item_id** | **str** | The parent primary image item identifier. | [optional] 
**parent_primary_image_tag** | **str** | The parent primary image tag. | [optional] 
**series_id** | **str** |  | [optional] 
**keywords** | [**List[LiveTvKeywordInfo]**](LiveTvKeywordInfo.md) |  | [optional] 
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
from embyapi.models.live_tv_series_timer_info_dto import LiveTvSeriesTimerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvSeriesTimerInfoDto from a JSON string
live_tv_series_timer_info_dto_instance = LiveTvSeriesTimerInfoDto.from_json(json)
# print the JSON string representation of the object
print(LiveTvSeriesTimerInfoDto.to_json())

# convert the object into a dict
live_tv_series_timer_info_dto_dict = live_tv_series_timer_info_dto_instance.to_dict()
# create an instance of LiveTvSeriesTimerInfoDto from a dict
live_tv_series_timer_info_dto_from_dict = LiveTvSeriesTimerInfoDto.from_dict(live_tv_series_timer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


