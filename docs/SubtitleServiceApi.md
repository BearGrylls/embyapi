# embyapi.SubtitleServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_items_by_id_subtitles_by_index**](SubtitleServiceApi.md#delete_items_by_id_subtitles_by_index) | **DELETE** /Items/{Id}/Subtitles/{Index} | Deletes an external subtitle file
[**delete_videos_by_id_subtitles_by_index**](SubtitleServiceApi.md#delete_videos_by_id_subtitles_by_index) | **DELETE** /Videos/{Id}/Subtitles/{Index} | Deletes an external subtitle file
[**get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**](SubtitleServiceApi.md#get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format) | **GET** /Items/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format} | Gets subtitles in a specified format.
[**get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**](SubtitleServiceApi.md#get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format) | **GET** /Items/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format} | Gets subtitles in a specified format.
[**get_items_by_id_remotesearch_subtitles_by_language**](SubtitleServiceApi.md#get_items_by_id_remotesearch_subtitles_by_language) | **GET** /Items/{Id}/RemoteSearch/Subtitles/{Language} | 
[**get_providers_subtitles_subtitles_by_id**](SubtitleServiceApi.md#get_providers_subtitles_subtitles_by_id) | **GET** /Providers/Subtitles/Subtitles/{Id} | 
[**get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**](SubtitleServiceApi.md#get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format) | **GET** /Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format} | Gets subtitles in a specified format.
[**get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**](SubtitleServiceApi.md#get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format) | **GET** /Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format} | Gets subtitles in a specified format.
[**post_items_by_id_remotesearch_subtitles_by_subtitleid**](SubtitleServiceApi.md#post_items_by_id_remotesearch_subtitles_by_subtitleid) | **POST** /Items/{Id}/RemoteSearch/Subtitles/{SubtitleId} | 
[**post_items_by_id_subtitles_by_index_delete**](SubtitleServiceApi.md#post_items_by_id_subtitles_by_index_delete) | **POST** /Items/{Id}/Subtitles/{Index}/Delete | Deletes an external subtitle file
[**post_videos_by_id_subtitles_by_index_delete**](SubtitleServiceApi.md#post_videos_by_id_subtitles_by_index_delete) | **POST** /Videos/{Id}/Subtitles/{Index}/Delete | Deletes an external subtitle file


# **delete_items_by_id_subtitles_by_index**
> delete_items_by_id_subtitles_by_index(id, media_source_id, index)

Deletes an external subtitle file

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index

    try:
        # Deletes an external subtitle file
        api_instance.delete_items_by_id_subtitles_by_index(id, media_source_id, index)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->delete_items_by_id_subtitles_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

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

# **delete_videos_by_id_subtitles_by_index**
> delete_videos_by_id_subtitles_by_index(id, media_source_id, index)

Deletes an external subtitle file

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index

    try:
        # Deletes an external subtitle file
        api_instance.delete_videos_by_id_subtitles_by_index(id, media_source_id, index)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->delete_videos_by_id_subtitles_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

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

# **get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**
> get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index
    format = 'format_example' # str | Format
    start_position_ticks = 56 # int | StartPositionTicks
    end_position_ticks = 56 # int | EndPositionTicks (optional)
    copy_timestamps = True # bool | CopyTimestamps (optional)

    try:
        # Gets subtitles in a specified format.
        api_instance.get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->get_items_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

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

# **get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**
> get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index
    format = 'format_example' # str | Format
    start_position_ticks = 56 # int | StartPositionTicks (optional)
    end_position_ticks = 56 # int | EndPositionTicks (optional)
    copy_timestamps = True # bool | CopyTimestamps (optional)

    try:
        # Gets subtitles in a specified format.
        api_instance.get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->get_items_by_id_by_mediasourceid_subtitles_by_index_stream_by_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | [optional] 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

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

# **get_items_by_id_remotesearch_subtitles_by_language**
> List[RemoteSubtitleInfo] get_items_by_id_remotesearch_subtitles_by_language(id, media_source_id, language, is_perfect_match=is_perfect_match, is_forced=is_forced, is_hearing_impaired=is_hearing_impaired)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_subtitle_info import RemoteSubtitleInfo
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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    language = 'language_example' # str | Language
    is_perfect_match = True # bool | IsPerfectMatch (optional)
    is_forced = True # bool | IsForced (optional)
    is_hearing_impaired = True # bool | IsHearingImpaired (optional)

    try:
        api_response = api_instance.get_items_by_id_remotesearch_subtitles_by_language(id, media_source_id, language, is_perfect_match=is_perfect_match, is_forced=is_forced, is_hearing_impaired=is_hearing_impaired)
        print("The response of SubtitleServiceApi->get_items_by_id_remotesearch_subtitles_by_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->get_items_by_id_remotesearch_subtitles_by_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **language** | **str**| Language | 
 **is_perfect_match** | **bool**| IsPerfectMatch | [optional] 
 **is_forced** | **bool**| IsForced | [optional] 
 **is_hearing_impaired** | **bool**| IsHearingImpaired | [optional] 

### Return type

[**List[RemoteSubtitleInfo]**](RemoteSubtitleInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a RemoteSubtitleInfo[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_subtitles_subtitles_by_id**
> get_providers_subtitles_subtitles_by_id(id)



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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id

    try:
        api_instance.get_providers_subtitles_subtitles_by_id(id)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->get_providers_subtitles_subtitles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

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
**200** | Operation successful. Empty response. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format**
> get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index
    format = 'format_example' # str | Format
    start_position_ticks = 56 # int | StartPositionTicks
    end_position_ticks = 56 # int | EndPositionTicks (optional)
    copy_timestamps = True # bool | CopyTimestamps (optional)

    try:
        # Gets subtitles in a specified format.
        api_instance.get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format(id, media_source_id, index, format, start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->get_videos_by_id_by_mediasourceid_subtitles_by_index_by_startpositionticks_stream_by_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

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

# **get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format**
> get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)

Gets subtitles in a specified format.

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index
    format = 'format_example' # str | Format
    start_position_ticks = 56 # int | StartPositionTicks (optional)
    end_position_ticks = 56 # int | EndPositionTicks (optional)
    copy_timestamps = True # bool | CopyTimestamps (optional)

    try:
        # Gets subtitles in a specified format.
        api_instance.get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format(id, media_source_id, index, format, start_position_ticks=start_position_ticks, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->get_videos_by_id_by_mediasourceid_subtitles_by_index_stream_by_format: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 
 **format** | **str**| Format | 
 **start_position_ticks** | **int**| StartPositionTicks | [optional] 
 **end_position_ticks** | **int**| EndPositionTicks | [optional] 
 **copy_timestamps** | **bool**| CopyTimestamps | [optional] 

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

# **post_items_by_id_remotesearch_subtitles_by_subtitleid**
> SubtitlesSubtitleDownloadResult post_items_by_id_remotesearch_subtitles_by_subtitleid(id, media_source_id, subtitle_id)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.subtitles_subtitle_download_result import SubtitlesSubtitleDownloadResult
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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    subtitle_id = 'subtitle_id_example' # str | SubtitleId

    try:
        api_response = api_instance.post_items_by_id_remotesearch_subtitles_by_subtitleid(id, media_source_id, subtitle_id)
        print("The response of SubtitleServiceApi->post_items_by_id_remotesearch_subtitles_by_subtitleid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->post_items_by_id_remotesearch_subtitles_by_subtitleid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **subtitle_id** | **str**| SubtitleId | 

### Return type

[**SubtitlesSubtitleDownloadResult**](SubtitlesSubtitleDownloadResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a SubtitleDownloadResult object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_subtitles_by_index_delete**
> post_items_by_id_subtitles_by_index_delete(id, media_source_id, index)

Deletes an external subtitle file

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index

    try:
        # Deletes an external subtitle file
        api_instance.post_items_by_id_subtitles_by_index_delete(id, media_source_id, index)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->post_items_by_id_subtitles_by_index_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

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

# **post_videos_by_id_subtitles_by_index_delete**
> post_videos_by_id_subtitles_by_index_delete(id, media_source_id, index)

Deletes an external subtitle file

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
    api_instance = embyapi.SubtitleServiceApi(api_client)
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | MediaSourceId
    index = 56 # int | The subtitle stream index

    try:
        # Deletes an external subtitle file
        api_instance.post_videos_by_id_subtitles_by_index_delete(id, media_source_id, index)
    except Exception as e:
        print("Exception when calling SubtitleServiceApi->post_videos_by_id_subtitles_by_index_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| MediaSourceId | 
 **index** | **int**| The subtitle stream index | 

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

