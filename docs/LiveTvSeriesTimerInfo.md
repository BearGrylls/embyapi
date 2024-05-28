# LiveTvSeriesTimerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the recording. | [optional] 
**channel_id** | **str** | ChannelId of the recording. | [optional] 
**channel_ids** | **List[str]** |  | [optional] 
**parent_folder_id** | **int** |  | [optional] 
**program_id** | **str** | The program identifier. | [optional] 
**name** | **str** | Name of the recording. | [optional] 
**service_name** | **str** |  | [optional] 
**overview** | **str** | Description of the recording. | [optional] 
**start_date** | **datetime** | The start date of the recording, in UTC. | [optional] 
**end_date** | **datetime** | The end date of the recording, in UTC. | [optional] 
**record_any_time** | **bool** | A value indicating whether \\[record any time\\]. | [optional] 
**keep_up_to** | **int** |  | [optional] 
**keep_until** | [**LiveTvKeepUntil**](LiveTvKeepUntil.md) |  | [optional] 
**skip_episodes_in_library** | **bool** |  | [optional] 
**match_existing_items_with_any_library** | **bool** |  | [optional] 
**record_new_only** | **bool** | A value indicating whether \\[record new only\\]. | [optional] 
**days** | [**List[DayOfWeek]**](DayOfWeek.md) | The days. | [optional] 
**priority** | **int** | The priority. | [optional] 
**pre_padding_seconds** | **int** | The pre padding seconds. | [optional] 
**post_padding_seconds** | **int** | The post padding seconds. | [optional] 
**is_pre_padding_required** | **bool** | A value indicating whether this instance is pre padding required. | [optional] 
**is_post_padding_required** | **bool** | A value indicating whether this instance is post padding required. | [optional] 
**series_id** | **str** | The series identifier. | [optional] 
**provider_ids** | **Dict[str, str]** |  | [optional] 
**max_recording_seconds** | **int** |  | [optional] 
**keywords** | [**List[LiveTvKeywordInfo]**](LiveTvKeywordInfo.md) |  | [optional] 
**timer_type** | [**LiveTvTimerType**](LiveTvTimerType.md) |  | [optional] 

## Example

```python
from embyapi.models.live_tv_series_timer_info import LiveTvSeriesTimerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvSeriesTimerInfo from a JSON string
live_tv_series_timer_info_instance = LiveTvSeriesTimerInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvSeriesTimerInfo.to_json())

# convert the object into a dict
live_tv_series_timer_info_dict = live_tv_series_timer_info_instance.to_dict()
# create an instance of LiveTvSeriesTimerInfo from a dict
live_tv_series_timer_info_from_dict = LiveTvSeriesTimerInfo.from_dict(live_tv_series_timer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


