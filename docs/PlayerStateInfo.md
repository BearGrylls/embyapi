# PlayerStateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_ticks** | **int** | The now playing position ticks. | [optional] 
**can_seek** | **bool** | A value indicating whether this instance can seek. | [optional] 
**is_paused** | **bool** | A value indicating whether this instance is paused. | [optional] 
**is_muted** | **bool** | A value indicating whether this instance is muted. | [optional] 
**volume_level** | **int** | The volume level. | [optional] 
**audio_stream_index** | **int** | The index of the now playing audio stream. | [optional] 
**subtitle_stream_index** | **int** | The index of the now playing subtitle stream. | [optional] 
**media_source_id** | **str** | The now playing media version identifier. | [optional] 
**play_method** | [**PlayMethod**](PlayMethod.md) |  | [optional] 
**repeat_mode** | [**RepeatMode**](RepeatMode.md) |  | [optional] 
**subtitle_offset** | **int** |  | [optional] 
**playback_rate** | **float** |  | [optional] 

## Example

```python
from embyapi.models.player_state_info import PlayerStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStateInfo from a JSON string
player_state_info_instance = PlayerStateInfo.from_json(json)
# print the JSON string representation of the object
print(PlayerStateInfo.to_json())

# convert the object into a dict
player_state_info_dict = player_state_info_instance.to_dict()
# create an instance of PlayerStateInfo from a dict
player_state_info_from_dict = PlayerStateInfo.from_dict(player_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


