# MediaSourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**MediaProtocol**](MediaProtocol.md) |  | [optional] 
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**encoder_path** | **str** |  | [optional] 
**encoder_protocol** | [**MediaProtocol**](MediaProtocol.md) |  | [optional] 
**type** | [**MediaSourceType**](MediaSourceType.md) |  | [optional] 
**probe_path** | **str** |  | [optional] 
**probe_protocol** | [**MediaProtocol**](MediaProtocol.md) |  | [optional] 
**container** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_name** | **str** |  | [optional] 
**is_remote** | **bool** | Differentiate internet url vs local network | [optional] 
**has_mixed_protocols** | **bool** |  | [optional] 
**run_time_ticks** | **int** |  | [optional] 
**container_start_time_ticks** | **int** |  | [optional] 
**supports_transcoding** | **bool** |  | [optional] 
**trancode_live_start_index** | **int** |  | [optional] 
**wall_clock_start** | **datetime** |  | [optional] 
**supports_direct_stream** | **bool** |  | [optional] 
**supports_direct_play** | **bool** |  | [optional] 
**is_infinite_stream** | **bool** |  | [optional] 
**requires_opening** | **bool** |  | [optional] 
**open_token** | **str** |  | [optional] 
**requires_closing** | **bool** |  | [optional] 
**live_stream_id** | **str** |  | [optional] 
**buffer_ms** | **int** |  | [optional] 
**requires_looping** | **bool** |  | [optional] 
**supports_probing** | **bool** |  | [optional] 
**video3_d_format** | [**Video3DFormat**](Video3DFormat.md) |  | [optional] 
**media_streams** | [**List[MediaStream]**](MediaStream.md) |  | [optional] 
**formats** | **List[str]** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**timestamp** | [**TransportStreamTimestamp**](TransportStreamTimestamp.md) |  | [optional] 
**required_http_headers** | **Dict[str, str]** |  | [optional] 
**direct_stream_url** | **str** |  | [optional] 
**add_api_key_to_direct_stream_url** | **bool** |  | [optional] 
**transcoding_url** | **str** |  | [optional] 
**transcoding_sub_protocol** | **str** |  | [optional] 
**transcoding_container** | **str** |  | [optional] 
**analyze_duration_ms** | **int** |  | [optional] 
**read_at_native_framerate** | **bool** |  | [optional] 
**default_audio_stream_index** | **int** |  | [optional] 
**default_subtitle_stream_index** | **int** |  | [optional] 
**item_id** | **str** | Used only by our Windows app. Not used by Emby Server. The id of the item that this mediasource belongs to, if there is one Also used by Emby for Kodi | [optional] 
**server_id** | **str** | Used only by our Windows app. Not used by Emby Server. | [optional] 

## Example

```python
from embyapi.models.media_source_info import MediaSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSourceInfo from a JSON string
media_source_info_instance = MediaSourceInfo.from_json(json)
# print the JSON string representation of the object
print(MediaSourceInfo.to_json())

# convert the object into a dict
media_source_info_dict = media_source_info_instance.to_dict()
# create an instance of MediaSourceInfo from a dict
media_source_info_from_dict = MediaSourceInfo.from_dict(media_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


