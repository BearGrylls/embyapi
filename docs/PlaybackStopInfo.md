# PlaybackStopInfo

Class PlaybackStopInfo.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**now_playing_queue** | [**List[QueueItem]**](QueueItem.md) |  | [optional] 
**playlist_item_id** | **str** |  | [optional] 
**playlist_index** | **int** |  | [optional] 
**playlist_length** | **int** |  | [optional] 
**item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**item_id** | **str** | The item identifier. | [optional] 
**session_id** | **str** | The session id. | [optional] 
**media_source_id** | **str** | The media version identifier. | [optional] 
**position_ticks** | **int** | The position ticks. | [optional] 
**live_stream_id** | **str** | The live stream identifier. | [optional] 
**play_session_id** | **str** | The play session identifier. | [optional] 
**failed** | **bool** | A value indicating whether this &#x60;MediaBrowser.Model.Session.PlaybackStopInfo&#x60; is failed. | [optional] 
**is_automated** | **bool** |  | [optional] 
**next_media_type** | **str** |  | [optional] 

## Example

```python
from embyapi.models.playback_stop_info import PlaybackStopInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackStopInfo from a JSON string
playback_stop_info_instance = PlaybackStopInfo.from_json(json)
# print the JSON string representation of the object
print(PlaybackStopInfo.to_json())

# convert the object into a dict
playback_stop_info_dict = playback_stop_info_instance.to_dict()
# create an instance of PlaybackStopInfo from a dict
playback_stop_info_from_dict = PlaybackStopInfo.from_dict(playback_stop_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


