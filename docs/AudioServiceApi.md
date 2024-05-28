# embyapi.AudioServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_by_id_by_streamfilename**](AudioServiceApi.md#get_audio_by_id_by_streamfilename) | **GET** /Audio/{Id}/{StreamFileName} | Gets an audio stream
[**get_audio_by_id_stream**](AudioServiceApi.md#get_audio_by_id_stream) | **GET** /Audio/{Id}/stream | Gets an audio stream
[**get_audio_by_id_stream_by_container**](AudioServiceApi.md#get_audio_by_id_stream_by_container) | **GET** /Audio/{Id}/stream.{Container} | Gets an audio stream
[**head_audio_by_id_by_streamfilename**](AudioServiceApi.md#head_audio_by_id_by_streamfilename) | **HEAD** /Audio/{Id}/{StreamFileName} | Gets an audio stream
[**head_audio_by_id_stream**](AudioServiceApi.md#head_audio_by_id_stream) | **HEAD** /Audio/{Id}/stream | Gets an audio stream
[**head_audio_by_id_stream_by_container**](AudioServiceApi.md#head_audio_by_id_stream_by_container) | **HEAD** /Audio/{Id}/stream.{Container} | Gets an audio stream


# **get_audio_by_id_by_streamfilename**
> get_audio_by_id_by_streamfilename(stream_file_name, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream

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
    api_instance = embyapi.AudioServiceApi(api_client)
    stream_file_name = 'stream_file_name_example' # str | 
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
        # Gets an audio stream
        api_instance.get_audio_by_id_by_streamfilename(stream_file_name, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling AudioServiceApi->get_audio_by_id_by_streamfilename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_file_name** | **str**|  | 
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

# **get_audio_by_id_stream**
> get_audio_by_id_stream(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream

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
    api_instance = embyapi.AudioServiceApi(api_client)
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
        # Gets an audio stream
        api_instance.get_audio_by_id_stream(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling AudioServiceApi->get_audio_by_id_stream: %s\n" % e)
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

# **get_audio_by_id_stream_by_container**
> get_audio_by_id_stream_by_container(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream

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
    api_instance = embyapi.AudioServiceApi(api_client)
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
        # Gets an audio stream
        api_instance.get_audio_by_id_stream_by_container(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling AudioServiceApi->get_audio_by_id_stream_by_container: %s\n" % e)
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

# **head_audio_by_id_by_streamfilename**
> head_audio_by_id_by_streamfilename(stream_file_name, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream

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
    api_instance = embyapi.AudioServiceApi(api_client)
    stream_file_name = 'stream_file_name_example' # str | 
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
        # Gets an audio stream
        api_instance.head_audio_by_id_by_streamfilename(stream_file_name, id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling AudioServiceApi->head_audio_by_id_by_streamfilename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_file_name** | **str**|  | 
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

# **head_audio_by_id_stream**
> head_audio_by_id_stream(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream

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
    api_instance = embyapi.AudioServiceApi(api_client)
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
        # Gets an audio stream
        api_instance.head_audio_by_id_stream(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling AudioServiceApi->head_audio_by_id_stream: %s\n" % e)
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

# **head_audio_by_id_stream_by_container**
> head_audio_by_id_stream_by_container(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)

Gets an audio stream

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
    api_instance = embyapi.AudioServiceApi(api_client)
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
        # Gets an audio stream
        api_instance.head_audio_by_id_stream_by_container(id, container, device_profile_id=device_profile_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, audio_sample_rate=audio_sample_rate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, static=static, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_video_bit_depth=max_video_bit_depth, video_codec=video_codec, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index)
    except Exception as e:
        print("Exception when calling AudioServiceApi->head_audio_by_id_stream_by_container: %s\n" % e)
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

