# embyapi.PlaystateServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_by_userid_playeditems_by_id**](PlaystateServiceApi.md#delete_users_by_userid_playeditems_by_id) | **DELETE** /Users/{UserId}/PlayedItems/{Id} | Marks an item as unplayed
[**delete_users_by_userid_playingitems_by_id**](PlaystateServiceApi.md#delete_users_by_userid_playingitems_by_id) | **DELETE** /Users/{UserId}/PlayingItems/{Id} | Reports that a user has stopped playing an item
[**post_sessions_playing**](PlaystateServiceApi.md#post_sessions_playing) | **POST** /Sessions/Playing | Reports playback has started within a session
[**post_sessions_playing_ping**](PlaystateServiceApi.md#post_sessions_playing_ping) | **POST** /Sessions/Playing/Ping | Pings a playback session
[**post_sessions_playing_progress**](PlaystateServiceApi.md#post_sessions_playing_progress) | **POST** /Sessions/Playing/Progress | Reports playback progress within a session
[**post_sessions_playing_stopped**](PlaystateServiceApi.md#post_sessions_playing_stopped) | **POST** /Sessions/Playing/Stopped | Reports playback has stopped within a session
[**post_users_by_userid_items_by_itemid_userdata**](PlaystateServiceApi.md#post_users_by_userid_items_by_itemid_userdata) | **POST** /Users/{UserId}/Items/{ItemId}/UserData | Updates userdata for an item
[**post_users_by_userid_playeditems_by_id**](PlaystateServiceApi.md#post_users_by_userid_playeditems_by_id) | **POST** /Users/{UserId}/PlayedItems/{Id} | Marks an item as played
[**post_users_by_userid_playeditems_by_id_delete**](PlaystateServiceApi.md#post_users_by_userid_playeditems_by_id_delete) | **POST** /Users/{UserId}/PlayedItems/{Id}/Delete | Marks an item as unplayed
[**post_users_by_userid_playingitems_by_id**](PlaystateServiceApi.md#post_users_by_userid_playingitems_by_id) | **POST** /Users/{UserId}/PlayingItems/{Id} | Reports that a user has begun playing an item
[**post_users_by_userid_playingitems_by_id_delete**](PlaystateServiceApi.md#post_users_by_userid_playingitems_by_id_delete) | **POST** /Users/{UserId}/PlayingItems/{Id}/Delete | Reports that a user has stopped playing an item
[**post_users_by_userid_playingitems_by_id_progress**](PlaystateServiceApi.md#post_users_by_userid_playingitems_by_id_progress) | **POST** /Users/{UserId}/PlayingItems/{Id}/Progress | Reports a user&#39;s playback progress


# **delete_users_by_userid_playeditems_by_id**
> UserItemDataDto delete_users_by_userid_playeditems_by_id(user_id, id)

Marks an item as unplayed

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.user_item_data_dto import UserItemDataDto
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id

    try:
        # Marks an item as unplayed
        api_response = api_instance.delete_users_by_userid_playeditems_by_id(user_id, id)
        print("The response of PlaystateServiceApi->delete_users_by_userid_playeditems_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->delete_users_by_userid_playeditems_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a UserItemDataDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users_by_userid_playingitems_by_id**
> delete_users_by_userid_playingitems_by_id(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a user has stopped playing an item

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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource
    next_media_type = 'next_media_type_example' # str | The next media type that will play
    position_ticks = 56 # int | Optional. The position, in ticks, where playback stopped. 1ms = 10000 ticks. (optional)
    live_stream_id = 'live_stream_id_example' # str |  (optional)
    play_session_id = 'play_session_id_example' # str |  (optional)

    try:
        # Reports that a user has stopped playing an item
        api_instance.delete_users_by_userid_playingitems_by_id(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->delete_users_by_userid_playingitems_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **next_media_type** | **str**| The next media type that will play | 
 **position_ticks** | **int**| Optional. The position, in ticks, where playback stopped. 1ms &#x3D; 10000 ticks. | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 

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

# **post_sessions_playing**
> post_sessions_playing(playback_start_info)

Reports playback has started within a session

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.playback_start_info import PlaybackStartInfo
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    playback_start_info = embyapi.PlaybackStartInfo() # PlaybackStartInfo | PlaybackStartInfo: 

    try:
        # Reports playback has started within a session
        api_instance.post_sessions_playing(playback_start_info)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_sessions_playing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_start_info** | [**PlaybackStartInfo**](PlaybackStartInfo.md)| PlaybackStartInfo:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
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

# **post_sessions_playing_ping**
> post_sessions_playing_ping(play_session_id=play_session_id)

Pings a playback session

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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    play_session_id = 'play_session_id_example' # str |  (optional)

    try:
        # Pings a playback session
        api_instance.post_sessions_playing_ping(play_session_id=play_session_id)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_sessions_playing_ping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **play_session_id** | **str**|  | [optional] 

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

# **post_sessions_playing_progress**
> post_sessions_playing_progress(playback_progress_info)

Reports playback progress within a session

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.playback_progress_info import PlaybackProgressInfo
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    playback_progress_info = embyapi.PlaybackProgressInfo() # PlaybackProgressInfo | PlaybackProgressInfo: 

    try:
        # Reports playback progress within a session
        api_instance.post_sessions_playing_progress(playback_progress_info)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_sessions_playing_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_progress_info** | [**PlaybackProgressInfo**](PlaybackProgressInfo.md)| PlaybackProgressInfo:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
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

# **post_sessions_playing_stopped**
> post_sessions_playing_stopped(playback_stop_info)

Reports playback has stopped within a session

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.playback_stop_info import PlaybackStopInfo
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    playback_stop_info = embyapi.PlaybackStopInfo() # PlaybackStopInfo | PlaybackStopInfo: 

    try:
        # Reports playback has stopped within a session
        api_instance.post_sessions_playing_stopped(playback_stop_info)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_sessions_playing_stopped: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_stop_info** | [**PlaybackStopInfo**](PlaybackStopInfo.md)| PlaybackStopInfo:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
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

# **post_users_by_userid_items_by_itemid_userdata**
> post_users_by_userid_items_by_itemid_userdata(user_id, item_id, user_item_data_dto)

Updates userdata for an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.user_item_data_dto import UserItemDataDto
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    item_id = 'item_id_example' # str | 
    user_item_data_dto = embyapi.UserItemDataDto() # UserItemDataDto | UserItemDataDto: 

    try:
        # Updates userdata for an item
        api_instance.post_users_by_userid_items_by_itemid_userdata(user_id, item_id, user_item_data_dto)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_users_by_userid_items_by_itemid_userdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **item_id** | **str**|  | 
 **user_item_data_dto** | [**UserItemDataDto**](UserItemDataDto.md)| UserItemDataDto:  | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
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

# **post_users_by_userid_playeditems_by_id**
> UserItemDataDto post_users_by_userid_playeditems_by_id(user_id, id, date_played=date_played)

Marks an item as played

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.user_item_data_dto import UserItemDataDto
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id
    date_played = 'date_played_example' # str | The date the item was played (if any). Format = yyyyMMddHHmmss (optional)

    try:
        # Marks an item as played
        api_response = api_instance.post_users_by_userid_playeditems_by_id(user_id, id, date_played=date_played)
        print("The response of PlaystateServiceApi->post_users_by_userid_playeditems_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_users_by_userid_playeditems_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **date_played** | **str**| The date the item was played (if any). Format &#x3D; yyyyMMddHHmmss | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a UserItemDataDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playeditems_by_id_delete**
> UserItemDataDto post_users_by_userid_playeditems_by_id_delete(user_id, id)

Marks an item as unplayed

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.user_item_data_dto import UserItemDataDto
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id

    try:
        # Marks an item as unplayed
        api_response = api_instance.post_users_by_userid_playeditems_by_id_delete(user_id, id)
        print("The response of PlaystateServiceApi->post_users_by_userid_playeditems_by_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_users_by_userid_playeditems_by_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a UserItemDataDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_by_userid_playingitems_by_id**
> post_users_by_userid_playingitems_by_id(user_id, id, media_source_id, can_seek=can_seek, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a user has begun playing an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.play_method import PlayMethod
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource
    can_seek = True # bool | Indicates if the client can seek (optional)
    audio_stream_index = 56 # int |  (optional)
    subtitle_stream_index = 56 # int |  (optional)
    play_method = embyapi.PlayMethod() # PlayMethod |  (optional)
    live_stream_id = 'live_stream_id_example' # str |  (optional)
    play_session_id = 'play_session_id_example' # str |  (optional)

    try:
        # Reports that a user has begun playing an item
        api_instance.post_users_by_userid_playingitems_by_id(user_id, id, media_source_id, can_seek=can_seek, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_users_by_userid_playingitems_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **can_seek** | **bool**| Indicates if the client can seek | [optional] 
 **audio_stream_index** | **int**|  | [optional] 
 **subtitle_stream_index** | **int**|  | [optional] 
 **play_method** | [**PlayMethod**](.md)|  | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 

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

# **post_users_by_userid_playingitems_by_id_delete**
> post_users_by_userid_playingitems_by_id_delete(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a user has stopped playing an item

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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource
    next_media_type = 'next_media_type_example' # str | The next media type that will play
    position_ticks = 56 # int | Optional. The position, in ticks, where playback stopped. 1ms = 10000 ticks. (optional)
    live_stream_id = 'live_stream_id_example' # str |  (optional)
    play_session_id = 'play_session_id_example' # str |  (optional)

    try:
        # Reports that a user has stopped playing an item
        api_instance.post_users_by_userid_playingitems_by_id_delete(user_id, id, media_source_id, next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_users_by_userid_playingitems_by_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **next_media_type** | **str**| The next media type that will play | 
 **position_ticks** | **int**| Optional. The position, in ticks, where playback stopped. 1ms &#x3D; 10000 ticks. | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 

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

# **post_users_by_userid_playingitems_by_id_progress**
> post_users_by_userid_playingitems_by_id_progress(user_id, id, media_source_id, api_on_playback_progress, position_ticks=position_ticks, is_paused=is_paused, is_muted=is_muted, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, volume_level=volume_level, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, repeat_mode=repeat_mode, subtitle_offset=subtitle_offset, playback_rate=playback_rate)

Reports a user's playback progress

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_on_playback_progress import ApiOnPlaybackProgress
from embyapi.models.play_method import PlayMethod
from embyapi.models.repeat_mode import RepeatMode
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
    api_instance = embyapi.PlaystateServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    id = 'id_example' # str | Item Id
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource
    api_on_playback_progress = embyapi.ApiOnPlaybackProgress() # ApiOnPlaybackProgress | OnPlaybackProgress
    position_ticks = 56 # int | Optional. The current position, in ticks. 1ms = 10000 ticks. (optional)
    is_paused = True # bool | Indicates if the player is paused. (optional)
    is_muted = True # bool | Indicates if the player is muted. (optional)
    audio_stream_index = 56 # int |  (optional)
    subtitle_stream_index = 56 # int |  (optional)
    volume_level = 56 # int | Scale of 0-100 (optional)
    play_method = embyapi.PlayMethod() # PlayMethod |  (optional)
    live_stream_id = 'live_stream_id_example' # str |  (optional)
    play_session_id = 'play_session_id_example' # str |  (optional)
    repeat_mode = embyapi.RepeatMode() # RepeatMode |  (optional)
    subtitle_offset = 56 # int |  (optional)
    playback_rate = 3.4 # float |  (optional)

    try:
        # Reports a user's playback progress
        api_instance.post_users_by_userid_playingitems_by_id_progress(user_id, id, media_source_id, api_on_playback_progress, position_ticks=position_ticks, is_paused=is_paused, is_muted=is_muted, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, volume_level=volume_level, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, repeat_mode=repeat_mode, subtitle_offset=subtitle_offset, playback_rate=playback_rate)
    except Exception as e:
        print("Exception when calling PlaystateServiceApi->post_users_by_userid_playingitems_by_id_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **id** | **str**| Item Id | 
 **media_source_id** | **str**| The id of the MediaSource | 
 **api_on_playback_progress** | [**ApiOnPlaybackProgress**](ApiOnPlaybackProgress.md)| OnPlaybackProgress | 
 **position_ticks** | **int**| Optional. The current position, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 
 **is_paused** | **bool**| Indicates if the player is paused. | [optional] 
 **is_muted** | **bool**| Indicates if the player is muted. | [optional] 
 **audio_stream_index** | **int**|  | [optional] 
 **subtitle_stream_index** | **int**|  | [optional] 
 **volume_level** | **int**| Scale of 0-100 | [optional] 
 **play_method** | [**PlayMethod**](.md)|  | [optional] 
 **live_stream_id** | **str**|  | [optional] 
 **play_session_id** | **str**|  | [optional] 
 **repeat_mode** | [**RepeatMode**](.md)|  | [optional] 
 **subtitle_offset** | **int**|  | [optional] 
 **playback_rate** | **float**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
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

