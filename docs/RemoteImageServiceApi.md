# embyapi.RemoteImageServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_images_remote**](RemoteImageServiceApi.md#get_images_remote) | **GET** /Images/Remote | Gets a remote image
[**get_items_by_id_remoteimages**](RemoteImageServiceApi.md#get_items_by_id_remoteimages) | **GET** /Items/{Id}/RemoteImages | Gets available remote images for an item
[**get_items_by_id_remoteimages_providers**](RemoteImageServiceApi.md#get_items_by_id_remoteimages_providers) | **GET** /Items/{Id}/RemoteImages/Providers | Gets available remote image providers for an item
[**post_items_by_id_remoteimages_download**](RemoteImageServiceApi.md#post_items_by_id_remoteimages_download) | **POST** /Items/{Id}/RemoteImages/Download | Downloads a remote image for an item


# **get_images_remote**
> get_images_remote(image_url)

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
    api_instance = embyapi.RemoteImageServiceApi(api_client)
    image_url = 'image_url_example' # str | The image url

    try:
        # Gets a remote image
        api_instance.get_images_remote(image_url)
    except Exception as e:
        print("Exception when calling RemoteImageServiceApi->get_images_remote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The image url | 

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

# **get_items_by_id_remoteimages**
> RemoteImageResult get_items_by_id_remoteimages(id, type=type, start_index=start_index, limit=limit, provider_name=provider_name, include_all_languages=include_all_languages)

Gets available remote images for an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.image_type import ImageType
from embyapi.models.remote_image_result import RemoteImageResult
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
    api_instance = embyapi.RemoteImageServiceApi(api_client)
    id = 'id_example' # str | Item Id
    type = embyapi.ImageType() # ImageType | The image type (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    provider_name = 'provider_name_example' # str | Optional. The image provider to use (optional)
    include_all_languages = True # bool | Optional. (optional)

    try:
        # Gets available remote images for an item
        api_response = api_instance.get_items_by_id_remoteimages(id, type=type, start_index=start_index, limit=limit, provider_name=provider_name, include_all_languages=include_all_languages)
        print("The response of RemoteImageServiceApi->get_items_by_id_remoteimages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteImageServiceApi->get_items_by_id_remoteimages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | [**ImageType**](.md)| The image type | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **provider_name** | **str**| Optional. The image provider to use | [optional] 
 **include_all_languages** | **bool**| Optional. | [optional] 

### Return type

[**RemoteImageResult**](RemoteImageResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a RemoteImageResult object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_remoteimages_providers**
> List[ImageProviderInfo] get_items_by_id_remoteimages_providers(id)

Gets available remote image providers for an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.image_provider_info import ImageProviderInfo
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
    api_instance = embyapi.RemoteImageServiceApi(api_client)
    id = 'id_example' # str | Item Id

    try:
        # Gets available remote image providers for an item
        api_response = api_instance.get_items_by_id_remoteimages_providers(id)
        print("The response of RemoteImageServiceApi->get_items_by_id_remoteimages_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteImageServiceApi->get_items_by_id_remoteimages_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 

### Return type

[**List[ImageProviderInfo]**](ImageProviderInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a List&lt;ImageProviderInfo&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_items_by_id_remoteimages_download**
> post_items_by_id_remoteimages_download(id, type, provider_name=provider_name, image_url=image_url)

Downloads a remote image for an item

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.image_type import ImageType
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
    api_instance = embyapi.RemoteImageServiceApi(api_client)
    id = 'id_example' # str | Item Id
    type = embyapi.ImageType() # ImageType | The image type
    provider_name = 'provider_name_example' # str | The image provider (optional)
    image_url = 'image_url_example' # str | The image url (optional)

    try:
        # Downloads a remote image for an item
        api_instance.post_items_by_id_remoteimages_download(id, type, provider_name=provider_name, image_url=image_url)
    except Exception as e:
        print("Exception when calling RemoteImageServiceApi->post_items_by_id_remoteimages_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **type** | [**ImageType**](.md)| The image type | 
 **provider_name** | **str**| The image provider | [optional] 
 **image_url** | **str**| The image url | [optional] 

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

