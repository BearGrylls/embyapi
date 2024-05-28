# embyapi.UniversalAudioServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_by_id_universal**](UniversalAudioServiceApi.md#get_audio_by_id_universal) | **GET** /Audio/{Id}/universal | Gets an audio stream
[**get_audio_by_id_universal_by_container**](UniversalAudioServiceApi.md#get_audio_by_id_universal_by_container) | **GET** /Audio/{Id}/universal.{Container} | Gets an audio stream
[**head_audio_by_id_universal**](UniversalAudioServiceApi.md#head_audio_by_id_universal) | **HEAD** /Audio/{Id}/universal | Gets an audio stream
[**head_audio_by_id_universal_by_container**](UniversalAudioServiceApi.md#head_audio_by_id_universal_by_container) | **HEAD** /Audio/{Id}/universal.{Container} | Gets an audio stream


# **get_audio_by_id_universal**
> get_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
    api_instance = embyapi.UniversalAudioServiceApi(api_client)
    id = 'id_example' # str | Item Id
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)

    try:
        # Gets an audio stream
        api_instance.get_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)
    except Exception as e:
        print("Exception when calling UniversalAudioServiceApi->get_audio_by_id_universal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 

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

# **get_audio_by_id_universal_by_container**
> get_audio_by_id_universal_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
    api_instance = embyapi.UniversalAudioServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | 
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)

    try:
        # Gets an audio stream
        api_instance.get_audio_by_id_universal_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)
    except Exception as e:
        print("Exception when calling UniversalAudioServiceApi->get_audio_by_id_universal_by_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**|  | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 

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

# **head_audio_by_id_universal**
> head_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
    api_instance = embyapi.UniversalAudioServiceApi(api_client)
    id = 'id_example' # str | Item Id
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)

    try:
        # Gets an audio stream
        api_instance.head_audio_by_id_universal(id, device_id=device_id, start_time_ticks=start_time_ticks)
    except Exception as e:
        print("Exception when calling UniversalAudioServiceApi->head_audio_by_id_universal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 

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

# **head_audio_by_id_universal_by_container**
> head_audio_by_id_universal_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)

Gets an audio stream

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
    api_instance = embyapi.UniversalAudioServiceApi(api_client)
    id = 'id_example' # str | Item Id
    container = 'container_example' # str | 
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks. (optional)

    try:
        # Gets an audio stream
        api_instance.head_audio_by_id_universal_by_container(id, container, device_id=device_id, start_time_ticks=start_time_ticks)
    except Exception as e:
        print("Exception when calling UniversalAudioServiceApi->head_audio_by_id_universal_by_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **container** | **str**|  | 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1ms &#x3D; 10000 ticks. | [optional] 

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

