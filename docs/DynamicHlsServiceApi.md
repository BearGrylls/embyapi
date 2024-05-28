# embyapi.DynamicHlsServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Audio/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**get_audio_by_id_live_m3u8**](DynamicHlsServiceApi.md#get_audio_by_id_live_m3u8) | **GET** /Audio/{Id}/live.m3u8 | 
[**get_audio_by_id_main_m3u8**](DynamicHlsServiceApi.md#get_audio_by_id_main_m3u8) | **GET** /Audio/{Id}/main.m3u8 | Gets an audio stream using HTTP live streaming.
[**get_audio_by_id_master_m3u8**](DynamicHlsServiceApi.md#get_audio_by_id_master_m3u8) | **GET** /Audio/{Id}/master.m3u8 | Gets an audio stream using HTTP live streaming.
[**get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Videos/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**get_videos_by_id_live_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_live_m3u8) | **GET** /Videos/{Id}/live.m3u8 | 
[**get_videos_by_id_live_subtitles_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_live_subtitles_m3u8) | **GET** /Videos/{Id}/live_subtitles.m3u8 | Gets an HLS subtitle playlist.
[**get_videos_by_id_main_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_main_m3u8) | **GET** /Videos/{Id}/main.m3u8 | Gets a video stream using HTTP live streaming.
[**get_videos_by_id_master_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_master_m3u8) | **GET** /Videos/{Id}/master.m3u8 | Gets a video stream using HTTP live streaming.
[**get_videos_by_id_subtitles_m3u8**](DynamicHlsServiceApi.md#get_videos_by_id_subtitles_m3u8) | **GET** /Videos/{Id}/subtitles.m3u8 | Gets an HLS subtitle playlist.
[**head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **HEAD** /Audio/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**head_audio_by_id_master_m3u8**](DynamicHlsServiceApi.md#head_audio_by_id_master_m3u8) | **HEAD** /Audio/{Id}/master.m3u8 | Gets an audio stream using HTTP live streaming.
[**head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**](DynamicHlsServiceApi.md#head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer) | **HEAD** /Videos/{Id}/hls1/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**head_videos_by_id_master_m3u8**](DynamicHlsServiceApi.md#head_videos_by_id_master_m3u8) | **HEAD** /Videos/{Id}/master.m3u8 | Gets a video stream using HTTP live streaming.


# **get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    segment_container = 'segment_container_example' # str | 
    segment_id = 'segment_id_example' # str | 
    id = 'id_example' # str | 
    playlist_id = 'playlist_id_example' # str | 

    try:
        api_instance.get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_container** | **str**|  | 
 **segment_id** | **str**|  | 
 **id** | **str**|  | 
 **playlist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_by_id_live_m3u8**
> get_audio_by_id_live_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        api_instance.get_audio_by_id_live_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_live_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_by_id_main_m3u8**
> get_audio_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream using HTTP live streaming.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        # Gets an audio stream using HTTP live streaming.
        api_instance.get_audio_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_main_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_by_id_master_m3u8**
> get_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream using HTTP live streaming.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        # Gets an audio stream using HTTP live streaming.
        api_instance.get_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_audio_by_id_master_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    segment_container = 'segment_container_example' # str | 
    segment_id = 'segment_id_example' # str | 
    id = 'id_example' # str | 
    playlist_id = 'playlist_id_example' # str | 

    try:
        api_instance.get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_container** | **str**|  | 
 **segment_id** | **str**|  | 
 **id** | **str**|  | 
 **playlist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_live_m3u8**
> get_videos_by_id_live_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        api_instance.get_videos_by_id_live_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_live_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_live_subtitles_m3u8**
> get_videos_by_id_live_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles)

Gets an HLS subtitle playlist.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    subtitle_segment_length = 56 # int | The subtitle segment length
    manifest_subtitles = 'manifest_subtitles_example' # str | The subtitle segment format

    try:
        # Gets an HLS subtitle playlist.
        api_instance.get_videos_by_id_live_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_live_subtitles_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **subtitle_segment_length** | **int**| The subtitle segment length | 
 **manifest_subtitles** | **str**| The subtitle segment format | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_main_m3u8**
> get_videos_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets a video stream using HTTP live streaming.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        # Gets a video stream using HTTP live streaming.
        api_instance.get_videos_by_id_main_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_main_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_master_m3u8**
> get_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets a video stream using HTTP live streaming.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        # Gets a video stream using HTTP live streaming.
        api_instance.get_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_master_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_subtitles_m3u8**
> get_videos_by_id_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles)

Gets an HLS subtitle playlist.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    subtitle_segment_length = 56 # int | The subtitle segment length
    manifest_subtitles = 'manifest_subtitles_example' # str | The subtitle segment format

    try:
        # Gets an HLS subtitle playlist.
        api_instance.get_videos_by_id_subtitles_m3u8(id, subtitle_segment_length, manifest_subtitles)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->get_videos_by_id_subtitles_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **subtitle_segment_length** | **int**| The subtitle segment length | 
 **manifest_subtitles** | **str**| The subtitle segment format | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    segment_container = 'segment_container_example' # str | 
    segment_id = 'segment_id_example' # str | 
    id = 'id_example' # str | 
    playlist_id = 'playlist_id_example' # str | 

    try:
        api_instance.head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->head_audio_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_container** | **str**|  | 
 **segment_id** | **str**|  | 
 **id** | **str**|  | 
 **playlist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_by_id_master_m3u8**
> head_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream using HTTP live streaming.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        # Gets an audio stream using HTTP live streaming.
        api_instance.head_audio_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->head_audio_by_id_master_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer**
> head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    segment_container = 'segment_container_example' # str | 
    segment_id = 'segment_id_example' # str | 
    id = 'id_example' # str | 
    playlist_id = 'playlist_id_example' # str | 

    try:
        api_instance.head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->head_videos_by_id_hls1_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_container** | **str**|  | 
 **segment_id** | **str**|  | 
 **id** | **str**|  | 
 **playlist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_videos_by_id_master_m3u8**
> head_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets a video stream using HTTP live streaming.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitle_delivery_method import SubtitleDeliveryMethod
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyauth
configuration.api_key['apikeyauth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyauth'] = 'Bearer'

# Configure Bearer authorization (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"): embyauth
configuration = embyapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.DynamicHlsServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | Container
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100 (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2 (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2 (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = embyapi.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_video_bit_depth = 56 # int | Optional. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)

    try:
        # Gets a video stream using HTTP live streaming.
        api_instance.head_videos_by_id_master_m3u8(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling DynamicHlsServiceApi->head_videos_by_id_master_m3u8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**| Container | 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100 | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2 | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2 | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_video_bit_depth** | **int**| Optional. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h264, mpeg4, theora, vpx, wmv. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

