# TranscodingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_codec** | **str** |  | [optional] 
**video_codec** | **str** |  | [optional] 
**sub_protocol** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**is_video_direct** | **bool** |  | [optional] 
**is_audio_direct** | **bool** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**audio_bitrate** | **int** |  | [optional] 
**video_bitrate** | **int** |  | [optional] 
**framerate** | **float** |  | [optional] 
**completion_percentage** | **float** |  | [optional] 
**transcoding_position_ticks** | **float** |  | [optional] 
**transcoding_start_position_ticks** | **float** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**audio_channels** | **int** |  | [optional] 
**transcode_reasons** | [**List[TranscodeReason]**](TranscodeReason.md) |  | [optional] 
**current_cpu_usage** | **float** | Deprecated, please use ProcessStatistics instead | [optional] 
**average_cpu_usage** | **float** | Deprecated, please use ProcessStatistics instead | [optional] 
**cpu_history** | [**List[TupleDoubleDouble]**](TupleDoubleDouble.md) | Deprecated, please use ProcessStatistics instead | [optional] 
**process_statistics** | [**ProcessRunMetricsProcessStatistics**](ProcessRunMetricsProcessStatistics.md) |  | [optional] 
**current_throttle** | **int** |  | [optional] 
**video_decoder** | **str** |  | [optional] 
**video_decoder_is_hardware** | **bool** |  | [optional] 
**video_decoder_media_type** | **str** |  | [optional] 
**video_decoder_hw_accel** | **str** |  | [optional] 
**video_encoder** | **str** |  | [optional] 
**video_encoder_is_hardware** | **bool** |  | [optional] 
**video_encoder_media_type** | **str** |  | [optional] 
**video_encoder_hw_accel** | **str** |  | [optional] 
**video_pipeline_info** | [**List[TranscodingVpStepInfo]**](TranscodingVpStepInfo.md) |  | [optional] 
**subtitle_pipeline_infos** | **List[List[TranscodingVpStepInfo]]** |  | [optional] 

## Example

```python
from embyapi.models.transcoding_info import TranscodingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodingInfo from a JSON string
transcoding_info_instance = TranscodingInfo.from_json(json)
# print the JSON string representation of the object
print(TranscodingInfo.to_json())

# convert the object into a dict
transcoding_info_dict = transcoding_info_instance.to_dict()
# create an instance of TranscodingInfo from a dict
transcoding_info_from_dict = TranscodingInfo.from_dict(transcoding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


