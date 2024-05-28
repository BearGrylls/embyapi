# LiveStreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_token** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**play_session_id** | **str** |  | [optional] 
**max_streaming_bitrate** | **int** |  | [optional] 
**start_time_ticks** | **int** |  | [optional] 
**audio_stream_index** | **int** |  | [optional] 
**subtitle_stream_index** | **int** |  | [optional] 
**max_audio_channels** | **int** |  | [optional] 
**item_id** | **int** |  | [optional] 
**device_profile** | [**DeviceProfile**](DeviceProfile.md) |  | [optional] 
**enable_direct_play** | **bool** |  | [optional] 
**enable_direct_stream** | **bool** |  | [optional] 
**enable_transcoding** | **bool** |  | [optional] 
**allow_video_stream_copy** | **bool** |  | [optional] 
**allow_interlaced_video_stream_copy** | **bool** |  | [optional] 
**allow_audio_stream_copy** | **bool** |  | [optional] 
**direct_play_protocols** | [**List[MediaProtocol]**](MediaProtocol.md) |  | [optional] 

## Example

```python
from embyapi.models.live_stream_request import LiveStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveStreamRequest from a JSON string
live_stream_request_instance = LiveStreamRequest.from_json(json)
# print the JSON string representation of the object
print(LiveStreamRequest.to_json())

# convert the object into a dict
live_stream_request_dict = live_stream_request_instance.to_dict()
# create an instance of LiveStreamRequest from a dict
live_stream_request_from_dict = LiveStreamRequest.from_dict(live_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


