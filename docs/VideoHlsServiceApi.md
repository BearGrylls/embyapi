# embyapi.VideoHlsServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer**](VideoHlsServiceApi.md#get_audio_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Audio/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer} | 
[**get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer**](VideoHlsServiceApi.md#get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer) | **GET** /Videos/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer} | 


# **get_audio_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer**
> get_audio_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



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
    api_instance = embyapi.VideoHlsServiceApi(api_client)
    segment_container = 'segment_container_example' # str | 
    segment_id = 'segment_id_example' # str | 
    id = 'id_example' # str | 
    playlist_id = 'playlist_id_example' # str | 

    try:
        api_instance.get_audio_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
    except Exception as e:
        print("Exception when calling VideoHlsServiceApi->get_audio_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
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

# **get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer**
> get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)



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
    api_instance = embyapi.VideoHlsServiceApi(api_client)
    segment_container = 'segment_container_example' # str | 
    segment_id = 'segment_id_example' # str | 
    id = 'id_example' # str | 
    playlist_id = 'playlist_id_example' # str | 

    try:
        api_instance.get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer(segment_container, segment_id, id, playlist_id)
    except Exception as e:
        print("Exception when calling VideoHlsServiceApi->get_videos_by_id_hls_by_playlistid_by_segmentid_by_segmentcontainer: %s\n" % e)
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

