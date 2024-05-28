# embyapi.ItemLookupServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_by_id_externalidinfos**](ItemLookupServiceApi.md#get_items_by_id_externalidinfos) | **GET** /Items/{Id}/ExternalIdInfos | Gets external id infos for an item
[**get_items_remotesearch_image**](ItemLookupServiceApi.md#get_items_remotesearch_image) | **GET** /Items/RemoteSearch/Image | Gets a remote image
[**post_items_metadata_reset**](ItemLookupServiceApi.md#post_items_metadata_reset) | **POST** /Items/Metadata/Reset | Resets metadata for one or more items
[**post_items_remotesearch_apply_by_id**](ItemLookupServiceApi.md#post_items_remotesearch_apply_by_id) | **POST** /Items/RemoteSearch/Apply/{Id} | Applies search criteria to an item and refreshes metadata
[**post_items_remotesearch_book**](ItemLookupServiceApi.md#post_items_remotesearch_book) | **POST** /Items/RemoteSearch/Book | 
[**post_items_remotesearch_boxset**](ItemLookupServiceApi.md#post_items_remotesearch_boxset) | **POST** /Items/RemoteSearch/BoxSet | 
[**post_items_remotesearch_game**](ItemLookupServiceApi.md#post_items_remotesearch_game) | **POST** /Items/RemoteSearch/Game | 
[**post_items_remotesearch_movie**](ItemLookupServiceApi.md#post_items_remotesearch_movie) | **POST** /Items/RemoteSearch/Movie | 
[**post_items_remotesearch_musicalbum**](ItemLookupServiceApi.md#post_items_remotesearch_musicalbum) | **POST** /Items/RemoteSearch/MusicAlbum | 
[**post_items_remotesearch_musicartist**](ItemLookupServiceApi.md#post_items_remotesearch_musicartist) | **POST** /Items/RemoteSearch/MusicArtist | 
[**post_items_remotesearch_musicvideo**](ItemLookupServiceApi.md#post_items_remotesearch_musicvideo) | **POST** /Items/RemoteSearch/MusicVideo | 
[**post_items_remotesearch_person**](ItemLookupServiceApi.md#post_items_remotesearch_person) | **POST** /Items/RemoteSearch/Person | 
[**post_items_remotesearch_series**](ItemLookupServiceApi.md#post_items_remotesearch_series) | **POST** /Items/RemoteSearch/Series | 
[**post_items_remotesearch_trailer**](ItemLookupServiceApi.md#post_items_remotesearch_trailer) | **POST** /Items/RemoteSearch/Trailer | 


# **get_items_by_id_externalidinfos**
> List[ExternalIdInfo] get_items_by_id_externalidinfos(id)

Gets external id infos for an item

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.external_id_info import ExternalIdInfo
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    id = 'id_example' # str | Item Id

    try:
        # Gets external id infos for an item
        api_response = api_instance.get_items_by_id_externalidinfos(id)
        print("The response of ItemLookupServiceApi->get_items_by_id_externalidinfos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->get_items_by_id_externalidinfos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**List[ExternalIdInfo]**](ExternalIdInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;ExternalIdInfo&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_remotesearch_image**
> get_items_remotesearch_image(image_url, provider_name)

Gets a remote image

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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    image_url = 'image_url_example' # str | The image url
    provider_name = 'provider_name_example' # str | 

    try:
        # Gets a remote image
        api_instance.get_items_remotesearch_image(image_url, provider_name)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->get_items_remotesearch_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The image url | 
 **provider_name** | **str**|  | 

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

# **post_items_metadata_reset**
> post_items_metadata_reset(item_ids)

Resets metadata for one or more items

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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    item_ids = 'item_ids_example' # str | The item ids

    try:
        # Resets metadata for one or more items
        api_instance.post_items_metadata_reset(item_ids)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_metadata_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_ids** | **str**| The item ids | 

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

# **post_items_remotesearch_apply_by_id**
> post_items_remotesearch_apply_by_id(id, remote_search_result, replace_all_images=replace_all_images)

Applies search criteria to an item and refreshes metadata

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    id = 'id_example' # str | The item id
    remote_search_result = embyapi.RemoteSearchResult() # RemoteSearchResult | RemoteSearchResult: 
    replace_all_images = True # bool | Whether or not to replace all images (optional)

    try:
        # Applies search criteria to an item and refreshes metadata
        api_instance.post_items_remotesearch_apply_by_id(id, remote_search_result, replace_all_images=replace_all_images)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_apply_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The item id | 
 **remote_search_result** | [**RemoteSearchResult**](RemoteSearchResult.md)| RemoteSearchResult:  | 
 **replace_all_images** | **bool**| Whether or not to replace all images | [optional] 

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

# **post_items_remotesearch_book**
> List[RemoteSearchResult] post_items_remotesearch_book(remote_search_query_book_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_book_info import RemoteSearchQueryBookInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_book_info = embyapi.RemoteSearchQueryBookInfo() # RemoteSearchQueryBookInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_book(remote_search_query_book_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_book_info** | [**RemoteSearchQueryBookInfo**](RemoteSearchQueryBookInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_boxset**
> List[RemoteSearchResult] post_items_remotesearch_boxset(remote_search_query_item_lookup_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_item_lookup_info import RemoteSearchQueryItemLookupInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_item_lookup_info = embyapi.RemoteSearchQueryItemLookupInfo() # RemoteSearchQueryItemLookupInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_boxset(remote_search_query_item_lookup_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_boxset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_boxset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_item_lookup_info** | [**RemoteSearchQueryItemLookupInfo**](RemoteSearchQueryItemLookupInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_game**
> List[RemoteSearchResult] post_items_remotesearch_game(remote_search_query_game_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_game_info import RemoteSearchQueryGameInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_game_info = embyapi.RemoteSearchQueryGameInfo() # RemoteSearchQueryGameInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_game(remote_search_query_game_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_game: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_game_info** | [**RemoteSearchQueryGameInfo**](RemoteSearchQueryGameInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_movie**
> List[RemoteSearchResult] post_items_remotesearch_movie(remote_search_query_movie_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_movie_info import RemoteSearchQueryMovieInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_movie_info = embyapi.RemoteSearchQueryMovieInfo() # RemoteSearchQueryMovieInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_movie(remote_search_query_movie_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_movie_info** | [**RemoteSearchQueryMovieInfo**](RemoteSearchQueryMovieInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_musicalbum**
> List[RemoteSearchResult] post_items_remotesearch_musicalbum(remote_search_query_album_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_album_info import RemoteSearchQueryAlbumInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_album_info = embyapi.RemoteSearchQueryAlbumInfo() # RemoteSearchQueryAlbumInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_musicalbum(remote_search_query_album_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_musicalbum:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_musicalbum: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_album_info** | [**RemoteSearchQueryAlbumInfo**](RemoteSearchQueryAlbumInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_musicartist**
> List[RemoteSearchResult] post_items_remotesearch_musicartist(remote_search_query_artist_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_artist_info import RemoteSearchQueryArtistInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_artist_info = embyapi.RemoteSearchQueryArtistInfo() # RemoteSearchQueryArtistInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_musicartist(remote_search_query_artist_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_musicartist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_musicartist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_artist_info** | [**RemoteSearchQueryArtistInfo**](RemoteSearchQueryArtistInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_musicvideo**
> List[RemoteSearchResult] post_items_remotesearch_musicvideo(remote_search_query_music_video_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_music_video_info import RemoteSearchQueryMusicVideoInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_music_video_info = embyapi.RemoteSearchQueryMusicVideoInfo() # RemoteSearchQueryMusicVideoInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_musicvideo(remote_search_query_music_video_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_musicvideo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_musicvideo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_music_video_info** | [**RemoteSearchQueryMusicVideoInfo**](RemoteSearchQueryMusicVideoInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_person**
> List[RemoteSearchResult] post_items_remotesearch_person(remote_search_query_person_lookup_info)



Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_person_lookup_info import RemoteSearchQueryPersonLookupInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_person_lookup_info = embyapi.RemoteSearchQueryPersonLookupInfo() # RemoteSearchQueryPersonLookupInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_person(remote_search_query_person_lookup_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_person_lookup_info** | [**RemoteSearchQueryPersonLookupInfo**](RemoteSearchQueryPersonLookupInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_series**
> List[RemoteSearchResult] post_items_remotesearch_series(remote_search_query_series_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_series_info import RemoteSearchQuerySeriesInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_series_info = embyapi.RemoteSearchQuerySeriesInfo() # RemoteSearchQuerySeriesInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_series(remote_search_query_series_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_series_info** | [**RemoteSearchQuerySeriesInfo**](RemoteSearchQuerySeriesInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_remotesearch_trailer**
> List[RemoteSearchResult] post_items_remotesearch_trailer(remote_search_query_trailer_info)



Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.remote_search_query_trailer_info import RemoteSearchQueryTrailerInfo
from embyapi.models.remote_search_result import RemoteSearchResult
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
    api_instance = embyapi.ItemLookupServiceApi(api_client)
    remote_search_query_trailer_info = embyapi.RemoteSearchQueryTrailerInfo() # RemoteSearchQueryTrailerInfo | RemoteSearchQuery`1: 

    try:
        api_response = api_instance.post_items_remotesearch_trailer(remote_search_query_trailer_info)
        print("The response of ItemLookupServiceApi->post_items_remotesearch_trailer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupServiceApi->post_items_remotesearch_trailer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_search_query_trailer_info** | [**RemoteSearchQueryTrailerInfo**](RemoteSearchQueryTrailerInfo.md)| RemoteSearchQuery&#x60;1:  | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;RemoteSearchResult&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

