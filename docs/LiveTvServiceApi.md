# embyapi.LiveTvServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_livetv_channelmappingoptions**](LiveTvServiceApi.md#delete_livetv_channelmappingoptions) | **DELETE** /LiveTv/ChannelMappingOptions | 
[**delete_livetv_channelmappings**](LiveTvServiceApi.md#delete_livetv_channelmappings) | **DELETE** /LiveTv/ChannelMappings | 
[**delete_livetv_listingproviders**](LiveTvServiceApi.md#delete_livetv_listingproviders) | **DELETE** /LiveTv/ListingProviders | Deletes a listing provider
[**delete_livetv_recordings_by_id**](LiveTvServiceApi.md#delete_livetv_recordings_by_id) | **DELETE** /LiveTv/Recordings/{Id} | Deletes a live tv recording
[**delete_livetv_seriestimers_by_id**](LiveTvServiceApi.md#delete_livetv_seriestimers_by_id) | **DELETE** /LiveTv/SeriesTimers/{Id} | Cancels a live tv series timer
[**delete_livetv_timers_by_id**](LiveTvServiceApi.md#delete_livetv_timers_by_id) | **DELETE** /LiveTv/Timers/{Id} | Cancels a live tv timer
[**delete_livetv_tunerhosts**](LiveTvServiceApi.md#delete_livetv_tunerhosts) | **DELETE** /LiveTv/TunerHosts | Deletes a tuner host
[**get_livetv_availablerecordingoptions**](LiveTvServiceApi.md#get_livetv_availablerecordingoptions) | **GET** /LiveTv/AvailableRecordingOptions | Gets available recording options
[**get_livetv_channelmappingoptions**](LiveTvServiceApi.md#get_livetv_channelmappingoptions) | **GET** /LiveTv/ChannelMappingOptions | 
[**get_livetv_channelmappings**](LiveTvServiceApi.md#get_livetv_channelmappings) | **GET** /LiveTv/ChannelMappings | 
[**get_livetv_channels**](LiveTvServiceApi.md#get_livetv_channels) | **GET** /LiveTv/Channels | Gets available live tv channels.
[**get_livetv_channels_by_id**](LiveTvServiceApi.md#get_livetv_channels_by_id) | **GET** /LiveTv/Channels/{Id} | Gets a live tv channel
[**get_livetv_channeltags**](LiveTvServiceApi.md#get_livetv_channeltags) | **GET** /LiveTv/ChannelTags | Gets live tv channel tags
[**get_livetv_channeltags_prefixes**](LiveTvServiceApi.md#get_livetv_channeltags_prefixes) | **GET** /LiveTv/ChannelTags/Prefixes | Gets live tv channel tag prefixes
[**get_livetv_epg**](LiveTvServiceApi.md#get_livetv_epg) | **GET** /LiveTv/EPG | Gets the epg.
[**get_livetv_folder**](LiveTvServiceApi.md#get_livetv_folder) | **GET** /LiveTv/Folder | Gets the top level live tv folder
[**get_livetv_guideinfo**](LiveTvServiceApi.md#get_livetv_guideinfo) | **GET** /LiveTv/GuideInfo | Gets guide info
[**get_livetv_info**](LiveTvServiceApi.md#get_livetv_info) | **GET** /LiveTv/Info | Gets available live tv services.
[**get_livetv_listingproviders**](LiveTvServiceApi.md#get_livetv_listingproviders) | **GET** /LiveTv/ListingProviders | Gets current listing providers
[**get_livetv_listingproviders_available**](LiveTvServiceApi.md#get_livetv_listingproviders_available) | **GET** /LiveTv/ListingProviders/Available | Gets listing provider
[**get_livetv_listingproviders_default**](LiveTvServiceApi.md#get_livetv_listingproviders_default) | **GET** /LiveTv/ListingProviders/Default | 
[**get_livetv_listingproviders_lineups**](LiveTvServiceApi.md#get_livetv_listingproviders_lineups) | **GET** /LiveTv/ListingProviders/Lineups | Gets available lineups
[**get_livetv_listingproviders_schedulesdirect_countries**](LiveTvServiceApi.md#get_livetv_listingproviders_schedulesdirect_countries) | **GET** /LiveTv/ListingProviders/SchedulesDirect/Countries | Gets available lineups
[**get_livetv_manage_channels**](LiveTvServiceApi.md#get_livetv_manage_channels) | **GET** /LiveTv/Manage/Channels | Gets the channel management list
[**get_livetv_programs**](LiveTvServiceApi.md#get_livetv_programs) | **GET** /LiveTv/Programs | Gets available live tv epgs..
[**get_livetv_programs_recommended**](LiveTvServiceApi.md#get_livetv_programs_recommended) | **GET** /LiveTv/Programs/Recommended | Gets available live tv epgs..
[**get_livetv_recordings**](LiveTvServiceApi.md#get_livetv_recordings) | **GET** /LiveTv/Recordings | Gets live tv recordings
[**get_livetv_recordings_by_id**](LiveTvServiceApi.md#get_livetv_recordings_by_id) | **GET** /LiveTv/Recordings/{Id} | Gets a live tv recording
[**get_livetv_recordings_folders**](LiveTvServiceApi.md#get_livetv_recordings_folders) | **GET** /LiveTv/Recordings/Folders | Gets recording folders
[**get_livetv_recordings_groups**](LiveTvServiceApi.md#get_livetv_recordings_groups) | **GET** /LiveTv/Recordings/Groups | Gets live tv recording groups
[**get_livetv_recordings_series**](LiveTvServiceApi.md#get_livetv_recordings_series) | **GET** /LiveTv/Recordings/Series | Gets live tv recordings
[**get_livetv_seriestimers**](LiveTvServiceApi.md#get_livetv_seriestimers) | **GET** /LiveTv/SeriesTimers | Gets live tv series timers
[**get_livetv_seriestimers_by_id**](LiveTvServiceApi.md#get_livetv_seriestimers_by_id) | **GET** /LiveTv/SeriesTimers/{Id} | Gets a live tv series timer
[**get_livetv_timers**](LiveTvServiceApi.md#get_livetv_timers) | **GET** /LiveTv/Timers | Gets live tv timers
[**get_livetv_timers_by_id**](LiveTvServiceApi.md#get_livetv_timers_by_id) | **GET** /LiveTv/Timers/{Id} | Gets a live tv timer
[**get_livetv_timers_defaults**](LiveTvServiceApi.md#get_livetv_timers_defaults) | **GET** /LiveTv/Timers/Defaults | Gets default values for a new timer
[**get_livetv_tunerhosts**](LiveTvServiceApi.md#get_livetv_tunerhosts) | **GET** /LiveTv/TunerHosts | Gets tuner hosts
[**get_livetv_tunerhosts_default_by_type**](LiveTvServiceApi.md#get_livetv_tunerhosts_default_by_type) | **GET** /LiveTv/TunerHosts/Default/{Type} | Gets tuner hosts
[**get_livetv_tunerhosts_types**](LiveTvServiceApi.md#get_livetv_tunerhosts_types) | **GET** /LiveTv/TunerHosts/Types | 
[**get_livetv_tuners_discvover**](LiveTvServiceApi.md#get_livetv_tuners_discvover) | **GET** /LiveTv/Tuners/Discvover | 
[**head_livetv_channelmappingoptions**](LiveTvServiceApi.md#head_livetv_channelmappingoptions) | **HEAD** /LiveTv/ChannelMappingOptions | 
[**head_livetv_channelmappings**](LiveTvServiceApi.md#head_livetv_channelmappings) | **HEAD** /LiveTv/ChannelMappings | 
[**post_livetv_channelmappingoptions**](LiveTvServiceApi.md#post_livetv_channelmappingoptions) | **POST** /LiveTv/ChannelMappingOptions | 
[**post_livetv_channelmappings**](LiveTvServiceApi.md#post_livetv_channelmappings) | **POST** /LiveTv/ChannelMappings | 
[**post_livetv_listingproviders**](LiveTvServiceApi.md#post_livetv_listingproviders) | **POST** /LiveTv/ListingProviders | Adds a listing provider
[**post_livetv_listingproviders_delete**](LiveTvServiceApi.md#post_livetv_listingproviders_delete) | **POST** /LiveTv/ListingProviders/Delete | Deletes a listing provider
[**post_livetv_manage_channels_by_id_disabled**](LiveTvServiceApi.md#post_livetv_manage_channels_by_id_disabled) | **POST** /LiveTv/Manage/Channels/{Id}/Disabled | Sets a channel disabled or not
[**post_livetv_manage_channels_by_id_sortindex**](LiveTvServiceApi.md#post_livetv_manage_channels_by_id_sortindex) | **POST** /LiveTv/Manage/Channels/{Id}/SortIndex | Sets a channel sort index
[**post_livetv_programs**](LiveTvServiceApi.md#post_livetv_programs) | **POST** /LiveTv/Programs | Gets available live tv epgs..
[**post_livetv_recordings_by_id_delete**](LiveTvServiceApi.md#post_livetv_recordings_by_id_delete) | **POST** /LiveTv/Recordings/{Id}/Delete | Deletes a live tv recording
[**post_livetv_seriestimers**](LiveTvServiceApi.md#post_livetv_seriestimers) | **POST** /LiveTv/SeriesTimers | Creates a live tv series timer
[**post_livetv_seriestimers_by_id**](LiveTvServiceApi.md#post_livetv_seriestimers_by_id) | **POST** /LiveTv/SeriesTimers/{Id} | Updates a live tv series timer
[**post_livetv_seriestimers_by_id_delete**](LiveTvServiceApi.md#post_livetv_seriestimers_by_id_delete) | **POST** /LiveTv/SeriesTimers/{Id}/Delete | Cancels a live tv series timer
[**post_livetv_timers**](LiveTvServiceApi.md#post_livetv_timers) | **POST** /LiveTv/Timers | Creates a live tv timer
[**post_livetv_timers_by_id**](LiveTvServiceApi.md#post_livetv_timers_by_id) | **POST** /LiveTv/Timers/{Id} | Updates a live tv timer
[**post_livetv_timers_by_id_delete**](LiveTvServiceApi.md#post_livetv_timers_by_id_delete) | **POST** /LiveTv/Timers/{Id}/Delete | Cancels a live tv timer
[**post_livetv_tunerhosts**](LiveTvServiceApi.md#post_livetv_tunerhosts) | **POST** /LiveTv/TunerHosts | Adds a tuner host
[**post_livetv_tunerhosts_delete**](LiveTvServiceApi.md#post_livetv_tunerhosts_delete) | **POST** /LiveTv/TunerHosts/Delete | Deletes a tuner host
[**post_livetv_tuners_by_id_reset**](LiveTvServiceApi.md#post_livetv_tuners_by_id_reset) | **POST** /LiveTv/Tuners/{Id}/Reset | Resets a tv tuner
[**put_livetv_channelmappingoptions**](LiveTvServiceApi.md#put_livetv_channelmappingoptions) | **PUT** /LiveTv/ChannelMappingOptions | 
[**put_livetv_channelmappings**](LiveTvServiceApi.md#put_livetv_channelmappings) | **PUT** /LiveTv/ChannelMappings | 


# **delete_livetv_channelmappingoptions**
> delete_livetv_channelmappingoptions(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.delete_livetv_channelmappingoptions(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_channelmappingoptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **delete_livetv_channelmappings**
> delete_livetv_channelmappings(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.delete_livetv_channelmappings(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_channelmappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **delete_livetv_listingproviders**
> delete_livetv_listingproviders(id=id)

Deletes a listing provider

Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Provider id (optional)

    try:
        # Deletes a listing provider
        api_instance.delete_livetv_listingproviders(id=id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_listingproviders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider id | [optional] 

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

# **delete_livetv_recordings_by_id**
> delete_livetv_recordings_by_id(id)

Deletes a live tv recording

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Recording Id

    try:
        # Deletes a live tv recording
        api_instance.delete_livetv_recordings_by_id(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_recordings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recording Id | 

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

# **delete_livetv_seriestimers_by_id**
> delete_livetv_seriestimers_by_id(id)

Cancels a live tv series timer

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Timer Id

    try:
        # Cancels a live tv series timer
        api_instance.delete_livetv_seriestimers_by_id(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_seriestimers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

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

# **delete_livetv_timers_by_id**
> delete_livetv_timers_by_id(id)

Cancels a live tv timer

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Timer Id

    try:
        # Cancels a live tv timer
        api_instance.delete_livetv_timers_by_id(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_timers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

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

# **delete_livetv_tunerhosts**
> delete_livetv_tunerhosts(id=id)

Deletes a tuner host

Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Tuner host id (optional)

    try:
        # Deletes a tuner host
        api_instance.delete_livetv_tunerhosts(id=id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->delete_livetv_tunerhosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tuner host id | [optional] 

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

# **get_livetv_availablerecordingoptions**
> ApiAvailableRecordingOptions get_livetv_availablerecordingoptions()

Gets available recording options

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_available_recording_options import ApiAvailableRecordingOptions
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets available recording options
        api_response = api_instance.get_livetv_availablerecordingoptions()
        print("The response of LiveTvServiceApi->get_livetv_availablerecordingoptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_availablerecordingoptions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiAvailableRecordingOptions**](ApiAvailableRecordingOptions.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a AvailableRecordingOptions object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channelmappingoptions**
> get_livetv_channelmappingoptions(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.get_livetv_channelmappingoptions(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_channelmappingoptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **get_livetv_channelmappings**
> get_livetv_channelmappings(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.get_livetv_channelmappings(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_channelmappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **get_livetv_channels**
> QueryResultBaseItemDto get_livetv_channels(type=type, is_liked=is_liked, is_disliked=is_disliked, enable_favorite_sorting=enable_favorite_sorting, add_current_program=add_current_program, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets available live tv channels.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_channel_type import LiveTvChannelType
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    type = embyapi.LiveTvChannelType() # LiveTvChannelType | Optional filter by channel type. (optional)
    is_liked = True # bool | Filter by channels that are liked, or not. (optional)
    is_disliked = True # bool | Filter by channels that are disliked, or not. (optional)
    enable_favorite_sorting = True # bool | Incorporate favorite and like status into channel sorting. (optional)
    add_current_program = True # bool | Optional. Adds current program info to each channel (optional)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets available live tv channels.
        api_response = api_instance.get_livetv_channels(type=type, is_liked=is_liked, is_disliked=is_disliked, enable_favorite_sorting=enable_favorite_sorting, add_current_program=add_current_program, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
        print("The response of LiveTvServiceApi->get_livetv_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LiveTvChannelType**](.md)| Optional filter by channel type. | [optional] 
 **is_liked** | **bool**| Filter by channels that are liked, or not. | [optional] 
 **is_disliked** | **bool**| Filter by channels that are disliked, or not. | [optional] 
 **enable_favorite_sorting** | **bool**| Incorporate favorite and like status into channel sorting. | [optional] 
 **add_current_program** | **bool**| Optional. Adds current program info to each channel | [optional] 
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channels_by_id**
> BaseItemDto get_livetv_channels_by_id(id, user_id=user_id)

Gets a live tv channel

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.base_item_dto import BaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Channel Id
    user_id = 'user_id_example' # str | Optional attach user data. (optional)

    try:
        # Gets a live tv channel
        api_response = api_instance.get_livetv_channels_by_id(id, user_id=user_id)
        print("The response of LiveTvServiceApi->get_livetv_channels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_channels_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Channel Id | 
 **user_id** | **str**| Optional attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a BaseItemDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channeltags**
> QueryResultBaseItemDto get_livetv_channeltags(artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets live tv channel tags

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets live tv channel tags
        api_response = api_instance.get_livetv_channeltags(artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
        print("The response of LiveTvServiceApi->get_livetv_channeltags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_channeltags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_channeltags_prefixes**
> List[ApiTagItem] get_livetv_channeltags_prefixes(artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets live tv channel tag prefixes

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_tag_item import ApiTagItem
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets live tv channel tag prefixes
        api_response = api_instance.get_livetv_channeltags_prefixes(artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
        print("The response of LiveTvServiceApi->get_livetv_channeltags_prefixes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_channeltags_prefixes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

### Return type

[**List[ApiTagItem]**](ApiTagItem.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a TagItem[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_epg**
> QueryResultApiEpgRow get_livetv_epg(type=type, is_liked=is_liked, is_disliked=is_disliked, enable_favorite_sorting=enable_favorite_sorting, add_current_program=add_current_program, channel_ids=channel_ids, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets the epg.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_channel_type import LiveTvChannelType
from embyapi.models.query_result_api_epg_row import QueryResultApiEpgRow
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    type = embyapi.LiveTvChannelType() # LiveTvChannelType | Optional filter by channel type. (optional)
    is_liked = True # bool | Filter by channels that are liked, or not. (optional)
    is_disliked = True # bool | Filter by channels that are disliked, or not. (optional)
    enable_favorite_sorting = True # bool | Incorporate favorite and like status into channel sorting. (optional)
    add_current_program = True # bool | Optional. Adds current program info to each channel (optional)
    channel_ids = 'channel_ids_example' # str | The channels to return guide information for. (optional)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets the epg.
        api_response = api_instance.get_livetv_epg(type=type, is_liked=is_liked, is_disliked=is_disliked, enable_favorite_sorting=enable_favorite_sorting, add_current_program=add_current_program, channel_ids=channel_ids, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
        print("The response of LiveTvServiceApi->get_livetv_epg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_epg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**LiveTvChannelType**](.md)| Optional filter by channel type. | [optional] 
 **is_liked** | **bool**| Filter by channels that are liked, or not. | [optional] 
 **is_disliked** | **bool**| Filter by channels that are disliked, or not. | [optional] 
 **enable_favorite_sorting** | **bool**| Incorporate favorite and like status into channel sorting. | [optional] 
 **add_current_program** | **bool**| Optional. Adds current program info to each channel | [optional] 
 **channel_ids** | **str**| The channels to return guide information for. | [optional] 
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

### Return type

[**QueryResultApiEpgRow**](QueryResultApiEpgRow.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;EpgRow&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_folder**
> BaseItemDto get_livetv_folder()

Gets the top level live tv folder

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.base_item_dto import BaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets the top level live tv folder
        api_response = api_instance.get_livetv_folder()
        print("The response of LiveTvServiceApi->get_livetv_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_folder: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a BaseItemDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_guideinfo**
> LiveTvGuideInfo get_livetv_guideinfo()

Gets guide info

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_guide_info import LiveTvGuideInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets guide info
        api_response = api_instance.get_livetv_guideinfo()
        print("The response of LiveTvServiceApi->get_livetv_guideinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_guideinfo: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LiveTvGuideInfo**](LiveTvGuideInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a GuideInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_info**
> LiveTvLiveTvInfo get_livetv_info()

Gets available live tv services.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_live_tv_info import LiveTvLiveTvInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets available live tv services.
        api_response = api_instance.get_livetv_info()
        print("The response of LiveTvServiceApi->get_livetv_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LiveTvLiveTvInfo**](LiveTvLiveTvInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a LiveTvInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders**
> List[LiveTvListingsProviderInfo] get_livetv_listingproviders(channel_id)

Gets current listing providers

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_listings_provider_info import LiveTvListingsProviderInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    channel_id = 'channel_id_example' # str | Channel id

    try:
        # Gets current listing providers
        api_response = api_instance.get_livetv_listingproviders(channel_id)
        print("The response of LiveTvServiceApi->get_livetv_listingproviders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel id | 

### Return type

[**List[LiveTvListingsProviderInfo]**](LiveTvListingsProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a ListingsProviderInfo[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_available**
> List[ApiListingProviderTypeInfo] get_livetv_listingproviders_available()

Gets listing provider

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_listing_provider_type_info import ApiListingProviderTypeInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets listing provider
        api_response = api_instance.get_livetv_listingproviders_available()
        print("The response of LiveTvServiceApi->get_livetv_listingproviders_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_available: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiListingProviderTypeInfo]**](ApiListingProviderTypeInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a ListingProviderTypeInfo[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_default**
> LiveTvListingsProviderInfo get_livetv_listingproviders_default()



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_listings_provider_info import LiveTvListingsProviderInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        api_response = api_instance.get_livetv_listingproviders_default()
        print("The response of LiveTvServiceApi->get_livetv_listingproviders_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_default: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LiveTvListingsProviderInfo**](LiveTvListingsProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a ListingsProviderInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_lineups**
> List[NameIdPair] get_livetv_listingproviders_lineups(id=id, type=type, location=location, country=country)

Gets available lineups

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.name_id_pair import NameIdPair
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Provider id (optional)
    type = 'type_example' # str | Provider Type (optional)
    location = 'location_example' # str | Location (optional)
    country = 'country_example' # str | Country (optional)

    try:
        # Gets available lineups
        api_response = api_instance.get_livetv_listingproviders_lineups(id=id, type=type, location=location, country=country)
        print("The response of LiveTvServiceApi->get_livetv_listingproviders_lineups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_lineups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider id | [optional] 
 **type** | **str**| Provider Type | [optional] 
 **location** | **str**| Location | [optional] 
 **country** | **str**| Country | [optional] 

### Return type

[**List[NameIdPair]**](NameIdPair.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;NameIdPair&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_listingproviders_schedulesdirect_countries**
> get_livetv_listingproviders_schedulesdirect_countries()

Gets available lineups

Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets available lineups
        api_instance.get_livetv_listingproviders_schedulesdirect_countries()
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_listingproviders_schedulesdirect_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **get_livetv_manage_channels**
> QueryResultChannelManagementInfo get_livetv_manage_channels(start_index=start_index, limit=limit, sort_by=sort_by, sort_order=sort_order)

Gets the channel management list

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_channel_management_info import QueryResultChannelManagementInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Name, StartDate (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)

    try:
        # Gets the channel management list
        api_response = api_instance.get_livetv_manage_channels(start_index=start_index, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of LiveTvServiceApi->get_livetv_manage_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_manage_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Name, StartDate | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 

### Return type

[**QueryResultChannelManagementInfo**](QueryResultChannelManagementInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;ChannelManagementInfo&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_programs**
> get_livetv_programs(channel_ids=channel_ids, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets available live tv epgs..

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    channel_ids = 'channel_ids_example' # str | The channels to return guide information for. (optional)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets available live tv epgs..
        api_instance.get_livetv_programs(channel_ids=channel_ids, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | **str**| The channels to return guide information for. | [optional] 
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

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

# **get_livetv_programs_recommended**
> QueryResultBaseItemDto get_livetv_programs_recommended(user_id=user_id, limit=limit, is_airing=is_airing, has_aired=has_aired, is_series=is_series, is_movie=is_movie, is_news=is_news, is_kids=is_kids, is_sports=is_sports, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, genre_ids=genre_ids, fields=fields, enable_user_data=enable_user_data)

Gets available live tv epgs..

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    user_id = 'user_id_example' # str | Optional filter by user id. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    is_airing = True # bool | Optional. Filter by programs that are currently airing, or not. (optional)
    has_aired = True # bool | Optional. Filter by programs that have completed airing, or not. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    genre_ids = 'genre_ids_example' # str | The genres to return guide information for. (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    enable_user_data = True # bool | Optional, include user data (optional)

    try:
        # Gets available live tv epgs..
        api_response = api_instance.get_livetv_programs_recommended(user_id=user_id, limit=limit, is_airing=is_airing, has_aired=has_aired, is_series=is_series, is_movie=is_movie, is_news=is_news, is_kids=is_kids, is_sports=is_sports, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, genre_ids=genre_ids, fields=fields, enable_user_data=enable_user_data)
        print("The response of LiveTvServiceApi->get_livetv_programs_recommended:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_programs_recommended: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional filter by user id. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **is_airing** | **bool**| Optional. Filter by programs that are currently airing, or not. | [optional] 
 **has_aired** | **bool**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **genre_ids** | **str**| The genres to return guide information for. | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings**
> get_livetv_recordings(channel_id=channel_id, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets live tv recordings

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_recording_status import LiveTvRecordingStatus
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    channel_id = 'channel_id_example' # str | Optional filter by channel id. (optional)
    status = embyapi.LiveTvRecordingStatus() # LiveTvRecordingStatus | Optional filter by recording status. (optional)
    is_in_progress = True # bool | Optional filter by recordings that are in progress, or not. (optional)
    series_timer_id = 'series_timer_id_example' # str | Optional filter by recordings belonging to a series timer (optional)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets live tv recordings
        api_instance.get_livetv_recordings(channel_id=channel_id, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional filter by channel id. | [optional] 
 **status** | [**LiveTvRecordingStatus**](.md)| Optional filter by recording status. | [optional] 
 **is_in_progress** | **bool**| Optional filter by recordings that are in progress, or not. | [optional] 
 **series_timer_id** | **str**| Optional filter by recordings belonging to a series timer | [optional] 
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

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

# **get_livetv_recordings_by_id**
> BaseItemDto get_livetv_recordings_by_id(id, user_id=user_id)

Gets a live tv recording

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.base_item_dto import BaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Recording Id
    user_id = 'user_id_example' # str | Optional attach user data. (optional)

    try:
        # Gets a live tv recording
        api_response = api_instance.get_livetv_recordings_by_id(id, user_id=user_id)
        print("The response of LiveTvServiceApi->get_livetv_recordings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_recordings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recording Id | 
 **user_id** | **str**| Optional attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a BaseItemDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_folders**
> List[BaseItemDto] get_livetv_recordings_folders(user_id=user_id, fields=fields, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)

Gets recording folders

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.base_item_dto import BaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    user_id = 'user_id_example' # str | Optional filter by user and attach user data. (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional, include user data (optional)

    try:
        # Gets recording folders
        api_response = api_instance.get_livetv_recordings_folders(user_id=user_id, fields=fields, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)
        print("The response of LiveTvServiceApi->get_livetv_recordings_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_recordings_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional filter by user and attach user data. | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**List[BaseItemDto]**](BaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a BaseItemDto[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_groups**
> QueryResultBaseItemDto get_livetv_recordings_groups()

Gets live tv recording groups

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets live tv recording groups
        api_response = api_instance.get_livetv_recordings_groups()
        print("The response of LiveTvServiceApi->get_livetv_recordings_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_recordings_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_recordings_series**
> QueryResultBaseItemDto get_livetv_recordings_series()

Gets live tv recordings

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets live tv recordings
        api_response = api_instance.get_livetv_recordings_series()
        print("The response of LiveTvServiceApi->get_livetv_recordings_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_recordings_series: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_seriestimers**
> QueryResultLiveTvSeriesTimerInfoDto get_livetv_seriestimers(sort_by=sort_by, sort_order=sort_order, start_index=start_index, limit=limit)

Gets live tv series timers

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_live_tv_series_timer_info_dto import QueryResultLiveTvSeriesTimerInfoDto
from embyapi.models.sort_order import SortOrder
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    sort_by = 'sort_by_example' # str | Optional. Sort by SortName or Priority (optional)
    sort_order = embyapi.SortOrder() # SortOrder | Optional. Sort in Ascending or Descending order (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)

    try:
        # Gets live tv series timers
        api_response = api_instance.get_livetv_seriestimers(sort_by=sort_by, sort_order=sort_order, start_index=start_index, limit=limit)
        print("The response of LiveTvServiceApi->get_livetv_seriestimers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_seriestimers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Sort by SortName or Priority | [optional] 
 **sort_order** | [**SortOrder**](.md)| Optional. Sort in Ascending or Descending order | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 

### Return type

[**QueryResultLiveTvSeriesTimerInfoDto**](QueryResultLiveTvSeriesTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;SeriesTimerInfoDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_seriestimers_by_id**
> LiveTvTimerInfoDto get_livetv_seriestimers_by_id(id)

Gets a live tv series timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_timer_info_dto import LiveTvTimerInfoDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Timer Id

    try:
        # Gets a live tv series timer
        api_response = api_instance.get_livetv_seriestimers_by_id(id)
        print("The response of LiveTvServiceApi->get_livetv_seriestimers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_seriestimers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

### Return type

[**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a TimerInfoDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_timers**
> QueryResultLiveTvTimerInfoDto get_livetv_timers(channel_id=channel_id, series_timer_id=series_timer_id)

Gets live tv timers

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_live_tv_timer_info_dto import QueryResultLiveTvTimerInfoDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    channel_id = 'channel_id_example' # str | Optional filter by channel id. (optional)
    series_timer_id = 'series_timer_id_example' # str | Optional filter by timers belonging to a series timer (optional)

    try:
        # Gets live tv timers
        api_response = api_instance.get_livetv_timers(channel_id=channel_id, series_timer_id=series_timer_id)
        print("The response of LiveTvServiceApi->get_livetv_timers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_timers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional filter by channel id. | [optional] 
 **series_timer_id** | **str**| Optional filter by timers belonging to a series timer | [optional] 

### Return type

[**QueryResultLiveTvTimerInfoDto**](QueryResultLiveTvTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;TimerInfoDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_timers_by_id**
> LiveTvTimerInfoDto get_livetv_timers_by_id(id)

Gets a live tv timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_timer_info_dto import LiveTvTimerInfoDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Timer Id

    try:
        # Gets a live tv timer
        api_response = api_instance.get_livetv_timers_by_id(id)
        print("The response of LiveTvServiceApi->get_livetv_timers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_timers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

### Return type

[**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a TimerInfoDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_timers_defaults**
> LiveTvSeriesTimerInfoDto get_livetv_timers_defaults(program_id=program_id)

Gets default values for a new timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_series_timer_info_dto import LiveTvSeriesTimerInfoDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    program_id = 'program_id_example' # str | Optional, to attach default values based on a program. (optional)

    try:
        # Gets default values for a new timer
        api_response = api_instance.get_livetv_timers_defaults(program_id=program_id)
        print("The response of LiveTvServiceApi->get_livetv_timers_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_timers_defaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Optional, to attach default values based on a program. | [optional] 

### Return type

[**LiveTvSeriesTimerInfoDto**](LiveTvSeriesTimerInfoDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a SeriesTimerInfoDto object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tunerhosts**
> List[LiveTvTunerHostInfo] get_livetv_tunerhosts()

Gets tuner hosts

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_tuner_host_info import LiveTvTunerHostInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        # Gets tuner hosts
        api_response = api_instance.get_livetv_tunerhosts()
        print("The response of LiveTvServiceApi->get_livetv_tunerhosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_tunerhosts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LiveTvTunerHostInfo]**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a TunerHostInfo[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tunerhosts_default_by_type**
> LiveTvTunerHostInfo get_livetv_tunerhosts_default_by_type(type)

Gets tuner hosts

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_tuner_host_info import LiveTvTunerHostInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    type = 'type_example' # str | Type

    try:
        # Gets tuner hosts
        api_response = api_instance.get_livetv_tunerhosts_default_by_type(type)
        print("The response of LiveTvServiceApi->get_livetv_tunerhosts_default_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_tunerhosts_default_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type | 

### Return type

[**LiveTvTunerHostInfo**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a TunerHostInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tunerhosts_types**
> List[NameIdPair] get_livetv_tunerhosts_types()



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.name_id_pair import NameIdPair
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        api_response = api_instance.get_livetv_tunerhosts_types()
        print("The response of LiveTvServiceApi->get_livetv_tunerhosts_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_tunerhosts_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NameIdPair]**](NameIdPair.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;NameIdPair&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_livetv_tuners_discvover**
> List[LiveTvTunerHostInfo] get_livetv_tuners_discvover()



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_tuner_host_info import LiveTvTunerHostInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)

    try:
        api_response = api_instance.get_livetv_tuners_discvover()
        print("The response of LiveTvServiceApi->get_livetv_tuners_discvover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->get_livetv_tuners_discvover: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LiveTvTunerHostInfo]**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;TunerHostInfo&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_livetv_channelmappingoptions**
> head_livetv_channelmappingoptions(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.head_livetv_channelmappingoptions(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->head_livetv_channelmappingoptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **head_livetv_channelmappings**
> head_livetv_channelmappings(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.head_livetv_channelmappings(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->head_livetv_channelmappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **post_livetv_channelmappingoptions**
> post_livetv_channelmappingoptions(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.post_livetv_channelmappingoptions(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_channelmappingoptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **post_livetv_channelmappings**
> post_livetv_channelmappings(provider_id, api_set_channel_mapping)



Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_set_channel_mapping import ApiSetChannelMapping
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id
    api_set_channel_mapping = embyapi.ApiSetChannelMapping() # ApiSetChannelMapping | SetChannelMapping

    try:
        api_instance.post_livetv_channelmappings(provider_id, api_set_channel_mapping)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_channelmappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 
 **api_set_channel_mapping** | [**ApiSetChannelMapping**](ApiSetChannelMapping.md)| SetChannelMapping | 

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
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_listingproviders**
> LiveTvListingsProviderInfo post_livetv_listingproviders(live_tv_listings_provider_info)

Adds a listing provider

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_listings_provider_info import LiveTvListingsProviderInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    live_tv_listings_provider_info = embyapi.LiveTvListingsProviderInfo() # LiveTvListingsProviderInfo | ListingsProviderInfo: 

    try:
        # Adds a listing provider
        api_response = api_instance.post_livetv_listingproviders(live_tv_listings_provider_info)
        print("The response of LiveTvServiceApi->post_livetv_listingproviders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_listingproviders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_tv_listings_provider_info** | [**LiveTvListingsProviderInfo**](LiveTvListingsProviderInfo.md)| ListingsProviderInfo:  | 

### Return type

[**LiveTvListingsProviderInfo**](LiveTvListingsProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a ListingsProviderInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_listingproviders_delete**
> post_livetv_listingproviders_delete(id=id)

Deletes a listing provider

Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Provider id (optional)

    try:
        # Deletes a listing provider
        api_instance.post_livetv_listingproviders_delete(id=id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_listingproviders_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider id | [optional] 

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

# **post_livetv_manage_channels_by_id_disabled**
> QueryResultChannelManagementInfo post_livetv_manage_channels_by_id_disabled(id, api_set_channel_disabled)

Sets a channel disabled or not

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_set_channel_disabled import ApiSetChannelDisabled
from embyapi.models.query_result_channel_management_info import QueryResultChannelManagementInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | 
    api_set_channel_disabled = embyapi.ApiSetChannelDisabled() # ApiSetChannelDisabled | SetChannelDisabled

    try:
        # Sets a channel disabled or not
        api_response = api_instance.post_livetv_manage_channels_by_id_disabled(id, api_set_channel_disabled)
        print("The response of LiveTvServiceApi->post_livetv_manage_channels_by_id_disabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_manage_channels_by_id_disabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_set_channel_disabled** | [**ApiSetChannelDisabled**](ApiSetChannelDisabled.md)| SetChannelDisabled | 

### Return type

[**QueryResultChannelManagementInfo**](QueryResultChannelManagementInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;ChannelManagementInfo&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_manage_channels_by_id_sortindex**
> QueryResultChannelManagementInfo post_livetv_manage_channels_by_id_sortindex(id, api_set_channel_sort_index)

Sets a channel sort index

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_set_channel_sort_index import ApiSetChannelSortIndex
from embyapi.models.query_result_channel_management_info import QueryResultChannelManagementInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | 
    api_set_channel_sort_index = embyapi.ApiSetChannelSortIndex() # ApiSetChannelSortIndex | SetChannelSortIndex

    try:
        # Sets a channel sort index
        api_response = api_instance.post_livetv_manage_channels_by_id_sortindex(id, api_set_channel_sort_index)
        print("The response of LiveTvServiceApi->post_livetv_manage_channels_by_id_sortindex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_manage_channels_by_id_sortindex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_set_channel_sort_index** | [**ApiSetChannelSortIndex**](ApiSetChannelSortIndex.md)| SetChannelSortIndex | 

### Return type

[**QueryResultChannelManagementInfo**](QueryResultChannelManagementInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;ChannelManagementInfo&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_programs**
> post_livetv_programs(api_base_items_request, channel_ids=channel_ids, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)

Gets available live tv epgs..

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_base_items_request import ApiBaseItemsRequest
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    api_base_items_request = embyapi.ApiBaseItemsRequest() # ApiBaseItemsRequest | BaseItemsRequest: 
    channel_ids = 'channel_ids_example' # str | The channels to return guide information for. (optional)
    artist_type = 'artist_type_example' # str | Artist or AlbumArtist (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    min_index_number = 56 # int | Optional filter by minimum index number. (optional)
    min_start_date = 'min_start_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_start_date = 'max_start_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_end_date = 'min_end_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_end_date = 'max_end_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    min_players = 56 # int | Optional filter by minimum number of game players. (optional)
    max_players = 56 # int | Optional filter by maximum number of game players. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    aired_during_season = 56 # int | Gets all episodes that aired during a season, including specials. (optional)
    min_premiere_date = 'min_premiere_date_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved = 'min_date_last_saved_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    min_date_last_saved_for_user = 'min_date_last_saved_for_user_example' # str | Optional. The minimum premiere date. Format = ISO (optional)
    max_premiere_date = 'max_premiere_date_example' # str | Optional. The maximum premiere date. Format = ISO (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an imdb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a tmdb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a tvdb id or not. (optional)
    exclude_item_ids = 'exclude_item_ids_example' # str | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false (optional)
    search_term = 'search_term_example' # str | Enter a search term to perform a search request (optional)
    sort_order = 'sort_order_example' # str | Sort Order - Ascending,Descending (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines (optional)
    exclude_item_types = 'exclude_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    any_provider_id_equals = 'any_provider_id_equals_example' # str | Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs. (optional)
    filters = 'filters_example' # str | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_folder = True # bool | Optional filter for folders. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    is_new = True # bool | Optional filter for IsNew. (optional)
    is_premiere = True # bool | Optional filter for IsPremiere. (optional)
    is_new_or_premiere = True # bool | Optional filter for IsNewOrPremiere. (optional)
    is_repeat = True # bool | Optional filter for IsRepeat. (optional)
    project_to_media = True # bool | ProjectToMedia (optional)
    media_types = 'media_types_example' # str | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = 'image_types_example' # str | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = 'genres_example' # str | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. (optional)
    official_ratings = 'official_ratings_example' # str | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. (optional)
    tags = 'tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    exclude_tags = 'exclude_tags_example' # str | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. (optional)
    years = 'years_example' # str | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = 'person_ids_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_types = 'person_types_example' # str | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited (optional)
    studios = 'studios_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    studio_ids = 'studio_ids_example' # str | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. (optional)
    artists = 'artists_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    artist_ids = 'artist_ids_example' # str | Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. (optional)
    albums = 'albums_example' # str | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. (optional)
    ids = 'ids_example' # str | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = 'video_types_example' # str | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. (optional)
    containers = 'containers_example' # str | Optional filter by Container. Allows multiple, comma delimeted. (optional)
    audio_codecs = 'audio_codecs_example' # str | Optional filter by AudioCodec. Allows multiple, comma delimeted. (optional)
    audio_layouts = 'audio_layouts_example' # str | Optional filter by AudioLayout. Allows multiple, comma delimeted. (optional)
    video_codecs = 'video_codecs_example' # str | Optional filter by VideoCodec. Allows multiple, comma delimeted. (optional)
    extended_video_types = 'extended_video_types_example' # str | Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. (optional)
    subtitle_codecs = 'subtitle_codecs_example' # str | Optional filter by SubtitleCodec. Allows multiple, comma delimeted. (optional)
    path = 'path_example' # str | Optional filter by Path. (optional)
    user_id = 'user_id_example' # str | User Id (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings (optional)
    group_items_into_collections = True # bool | Whether or not to hide items behind their boxsets. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = 'series_status_example' # str | Optional filter by Series Status. Allows multiple, comma delimeted. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    artist_starts_with_or_greater = 'artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    album_artist_starts_with_or_greater = 'album_artist_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)

    try:
        # Gets available live tv epgs..
        api_instance.post_livetv_programs(api_base_items_request, channel_ids=channel_ids, artist_type=artist_type, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, min_index_number=min_index_number, min_start_date=min_start_date, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, min_players=min_players, max_players=max_players, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, aired_during_season=aired_during_season, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, any_provider_id_equals=any_provider_id_equals, filters=filters, is_favorite=is_favorite, is_movie=is_movie, is_series=is_series, is_folder=is_folder, is_news=is_news, is_kids=is_kids, is_sports=is_sports, is_new=is_new, is_premiere=is_premiere, is_new_or_premiere=is_new_or_premiere, is_repeat=is_repeat, project_to_media=project_to_media, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, exclude_tags=exclude_tags, years=years, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, artists=artists, artist_ids=artist_ids, albums=albums, ids=ids, video_types=video_types, containers=containers, audio_codecs=audio_codecs, audio_layouts=audio_layouts, video_codecs=video_codecs, extended_video_types=extended_video_types, subtitle_codecs=subtitle_codecs, path=path, user_id=user_id, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, group_items_into_collections=group_items_into_collections, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, artist_starts_with_or_greater=artist_starts_with_or_greater, album_artist_starts_with_or_greater=album_artist_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_base_items_request** | [**ApiBaseItemsRequest**](ApiBaseItemsRequest.md)| BaseItemsRequest:  | 
 **channel_ids** | **str**| The channels to return guide information for. | [optional] 
 **artist_type** | **str**| Artist or AlbumArtist | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **min_index_number** | **int**| Optional filter by minimum index number. | [optional] 
 **min_start_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_start_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_end_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_end_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **min_players** | **int**| Optional filter by minimum number of game players. | [optional] 
 **max_players** | **int**| Optional filter by maximum number of game players. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **aired_during_season** | **int**| Gets all episodes that aired during a season, including specials. | [optional] 
 **min_premiere_date** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **min_date_last_saved_for_user** | **str**| Optional. The minimum premiere date. Format &#x3D; ISO | [optional] 
 **max_premiere_date** | **str**| Optional. The maximum premiere date. Format &#x3D; ISO | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an imdb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a tmdb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a tvdb id or not. | [optional] 
 **exclude_item_ids** | **str**| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false | [optional] 
 **search_term** | **str**| Enter a search term to perform a search request | [optional] 
 **sort_order** | **str**| Sort Order - Ascending,Descending | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines | [optional] 
 **exclude_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **any_provider_id_equals** | **str**| Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form &#39;prov.id&#39;, e.g. &#39;imdb.tt123456&#39;. This allows multiple, comma delimeted value pairs. | [optional] 
 **filters** | **str**| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_folder** | **bool**| Optional filter for folders. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **is_new** | **bool**| Optional filter for IsNew. | [optional] 
 **is_premiere** | **bool**| Optional filter for IsPremiere. | [optional] 
 **is_new_or_premiere** | **bool**| Optional filter for IsNewOrPremiere. | [optional] 
 **is_repeat** | **bool**| Optional filter for IsRepeat. | [optional] 
 **project_to_media** | **bool**| ProjectToMedia | [optional] 
 **media_types** | **str**| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | **str**| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | **str**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | **str**| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **official_ratings** | **str**| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **exclude_tags** | **str**| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | **str**| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_types** | **str**| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited | [optional] 
 **studios** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **studio_ids** | **str**| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **artist_ids** | **str**| Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted. | [optional] 
 **albums** | **str**| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **ids** | **str**| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | **str**| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **containers** | **str**| Optional filter by Container. Allows multiple, comma delimeted. | [optional] 
 **audio_codecs** | **str**| Optional filter by AudioCodec. Allows multiple, comma delimeted. | [optional] 
 **audio_layouts** | **str**| Optional filter by AudioLayout. Allows multiple, comma delimeted. | [optional] 
 **video_codecs** | **str**| Optional filter by VideoCodec. Allows multiple, comma delimeted. | [optional] 
 **extended_video_types** | **str**| Optional filter by ExtendedVideoType. Allows multiple, comma delimeted. | [optional] 
 **subtitle_codecs** | **str**| Optional filter by SubtitleCodec. Allows multiple, comma delimeted. | [optional] 
 **path** | **str**| Optional filter by Path. | [optional] 
 **user_id** | **str**| User Id | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings | [optional] 
 **group_items_into_collections** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | **str**| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **album_artist_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 

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
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_recordings_by_id_delete**
> post_livetv_recordings_by_id_delete(id)

Deletes a live tv recording

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Recording Id

    try:
        # Deletes a live tv recording
        api_instance.post_livetv_recordings_by_id_delete(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_recordings_by_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recording Id | 

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

# **post_livetv_seriestimers**
> post_livetv_seriestimers(live_tv_series_timer_info)

Creates a live tv series timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_series_timer_info import LiveTvSeriesTimerInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    live_tv_series_timer_info = embyapi.LiveTvSeriesTimerInfo() # LiveTvSeriesTimerInfo | SeriesTimerInfo: 

    try:
        # Creates a live tv series timer
        api_instance.post_livetv_seriestimers(live_tv_series_timer_info)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_seriestimers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_tv_series_timer_info** | [**LiveTvSeriesTimerInfo**](LiveTvSeriesTimerInfo.md)| SeriesTimerInfo:  | 

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

# **post_livetv_seriestimers_by_id**
> post_livetv_seriestimers_by_id(id, live_tv_series_timer_info)

Updates a live tv series timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_series_timer_info import LiveTvSeriesTimerInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | 
    live_tv_series_timer_info = embyapi.LiveTvSeriesTimerInfo() # LiveTvSeriesTimerInfo | SeriesTimerInfo: 

    try:
        # Updates a live tv series timer
        api_instance.post_livetv_seriestimers_by_id(id, live_tv_series_timer_info)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_seriestimers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **live_tv_series_timer_info** | [**LiveTvSeriesTimerInfo**](LiveTvSeriesTimerInfo.md)| SeriesTimerInfo:  | 

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

# **post_livetv_seriestimers_by_id_delete**
> post_livetv_seriestimers_by_id_delete(id)

Cancels a live tv series timer

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Timer Id

    try:
        # Cancels a live tv series timer
        api_instance.post_livetv_seriestimers_by_id_delete(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_seriestimers_by_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

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

# **post_livetv_timers**
> post_livetv_timers(live_tv_timer_info_dto)

Creates a live tv timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_timer_info_dto import LiveTvTimerInfoDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    live_tv_timer_info_dto = embyapi.LiveTvTimerInfoDto() # LiveTvTimerInfoDto | TimerInfoDto: 

    try:
        # Creates a live tv timer
        api_instance.post_livetv_timers(live_tv_timer_info_dto)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_timers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_tv_timer_info_dto** | [**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)| TimerInfoDto:  | 

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

# **post_livetv_timers_by_id**
> post_livetv_timers_by_id(id, live_tv_timer_info_dto)

Updates a live tv timer

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_timer_info_dto import LiveTvTimerInfoDto
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | 
    live_tv_timer_info_dto = embyapi.LiveTvTimerInfoDto() # LiveTvTimerInfoDto | TimerInfoDto: 

    try:
        # Updates a live tv timer
        api_instance.post_livetv_timers_by_id(id, live_tv_timer_info_dto)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_timers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **live_tv_timer_info_dto** | [**LiveTvTimerInfoDto**](LiveTvTimerInfoDto.md)| TimerInfoDto:  | 

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

# **post_livetv_timers_by_id_delete**
> post_livetv_timers_by_id_delete(id)

Cancels a live tv timer

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Timer Id

    try:
        # Cancels a live tv timer
        api_instance.post_livetv_timers_by_id_delete(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_timers_by_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timer Id | 

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

# **post_livetv_tunerhosts**
> LiveTvTunerHostInfo post_livetv_tunerhosts(live_tv_tuner_host_info)

Adds a tuner host

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.live_tv_tuner_host_info import LiveTvTunerHostInfo
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    live_tv_tuner_host_info = embyapi.LiveTvTunerHostInfo() # LiveTvTunerHostInfo | TunerHostInfo: 

    try:
        # Adds a tuner host
        api_response = api_instance.post_livetv_tunerhosts(live_tv_tuner_host_info)
        print("The response of LiveTvServiceApi->post_livetv_tunerhosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_tunerhosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_tv_tuner_host_info** | [**LiveTvTunerHostInfo**](LiveTvTunerHostInfo.md)| TunerHostInfo:  | 

### Return type

[**LiveTvTunerHostInfo**](LiveTvTunerHostInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a TunerHostInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_livetv_tunerhosts_delete**
> post_livetv_tunerhosts_delete(id=id)

Deletes a tuner host

Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Tuner host id (optional)

    try:
        # Deletes a tuner host
        api_instance.post_livetv_tunerhosts_delete(id=id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_tunerhosts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tuner host id | [optional] 

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

# **post_livetv_tuners_by_id_reset**
> post_livetv_tuners_by_id_reset(id)

Resets a tv tuner

Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    id = 'id_example' # str | Tuner Id

    try:
        # Resets a tv tuner
        api_instance.post_livetv_tuners_by_id_reset(id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->post_livetv_tuners_by_id_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tuner Id | 

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

# **put_livetv_channelmappingoptions**
> put_livetv_channelmappingoptions(provider_id)



Requires authentication as administrator

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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id

    try:
        api_instance.put_livetv_channelmappingoptions(provider_id)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->put_livetv_channelmappingoptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

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

# **put_livetv_channelmappings**
> put_livetv_channelmappings(provider_id, api_set_channel_mapping)



Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.api_set_channel_mapping import ApiSetChannelMapping
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
    api_instance = embyapi.LiveTvServiceApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id
    api_set_channel_mapping = embyapi.ApiSetChannelMapping() # ApiSetChannelMapping | SetChannelMapping

    try:
        api_instance.put_livetv_channelmappings(provider_id, api_set_channel_mapping)
    except Exception as e:
        print("Exception when calling LiveTvServiceApi->put_livetv_channelmappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 
 **api_set_channel_mapping** | [**ApiSetChannelMapping**](ApiSetChannelMapping.md)| SetChannelMapping | 

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
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

