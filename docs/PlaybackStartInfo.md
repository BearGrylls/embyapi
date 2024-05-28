# PlaybackStartInfo

Class PlaybackStartInfo.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_seek** | **bool** | A value indicating whether this instance can seek. | [optional] 
**item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**now_playing_queue** | [**List[QueueItem]**](QueueItem.md) |  | [optional] 
**playlist_item_id** | **str** |  | [optional] 
**item_id** | **str** | The item identifier. | [optional] 
**session_id** | **str** | The session id. | [optional] 
**media_source_id** | **str** | The media version identifier. | [optional] 
**audio_stream_index** | **int** | The index of the audio stream. | [optional] 
**subtitle_stream_index** | **int** | The index of the subtitle stream. | [optional] 
**is_paused** | **bool** | A value indicating whether this instance is paused. | [optional] 
**playlist_index** | **int** |  | [optional] 
**playlist_length** | **int** |  | [optional] 
**is_muted** | **bool** | A value indicating whether this instance is muted. | [optional] 
**position_ticks** | **int** | The position ticks. | [optional] 
**run_time_ticks** | **int** |  | [optional] 
**playback_start_time_ticks** | **int** |  | [optional] 
**volume_level** | **int** | The volume level. | [optional] 
**brightness** | **int** |  | [optional] 
**aspect_ratio** | **str** |  | [optional] 
**event_name** | [**ProgressEvent**](ProgressEvent.md) |  | [optional] 
**play_method** | [**PlayMethod**](PlayMethod.md) |  | [optional] 
**live_stream_id** | **str** | The live stream identifier. | [optional] 
**play_session_id** | **str** | The play session identifier. | [optional] 
**repeat_mode** | [**RepeatMode**](RepeatMode.md) |  | [optional] 
**subtitle_offset** | **int** |  | [optional] 
**playback_rate** | **float** |  | [optional] 
**playlist_item_ids** | **List[str]** |  | [optional] 

## Example

```python
from embyapi.models.playback_start_info import PlaybackStartInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackStartInfo from a JSON string
playback_start_info_instance = PlaybackStartInfo.from_json(json)
# print the JSON string representation of the object
print(PlaybackStartInfo.to_json())

# convert the object into a dict
playback_start_info_dict = playback_start_info_instance.to_dict()
# create an instance of PlaybackStartInfo from a dict
playback_start_info_from_dict = PlaybackStartInfo.from_dict(playback_start_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


