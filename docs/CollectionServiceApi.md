# embyapi.CollectionServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_collections_by_id_items**](CollectionServiceApi.md#delete_collections_by_id_items) | **DELETE** /Collections/{Id}/Items | Removes items from a collection
[**post_collections**](CollectionServiceApi.md#post_collections) | **POST** /Collections | Creates a new collection
[**post_collections_by_id_items**](CollectionServiceApi.md#post_collections_by_id_items) | **POST** /Collections/{Id}/Items | Adds items to a collection
[**post_collections_by_id_items_delete**](CollectionServiceApi.md#post_collections_by_id_items_delete) | **POST** /Collections/{Id}/Items/Delete | Removes items from a collection


# **delete_collections_by_id_items**
> delete_collections_by_id_items(ids, id)

Removes items from a collection

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
    api_instance = embyapi.CollectionServiceApi(api_client)
    ids = 'ids_example' # str | Item id, comma delimited
    id = 'id_example' # str | 

    try:
        # Removes items from a collection
        api_instance.delete_collections_by_id_items(ids, id)
    except Exception as e:
        print("Exception when calling CollectionServiceApi->delete_collections_by_id_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id, comma delimited | 
 **id** | **str**|  | 

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

# **post_collections**
> CollectionsCollectionCreationResult post_collections(is_locked=is_locked, name=name, parent_id=parent_id, ids=ids)

Creates a new collection

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.collections_collection_creation_result import CollectionsCollectionCreationResult
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
    api_instance = embyapi.CollectionServiceApi(api_client)
    is_locked = True # bool | Whether or not to lock the new collection. (optional)
    name = 'name_example' # str | The name of the new collection. (optional)
    parent_id = 'parent_id_example' # str | Optional - create the collection within a specific folder (optional)
    ids = 'ids_example' # str | Item Ids to add to the collection (optional)

    try:
        # Creates a new collection
        api_response = api_instance.post_collections(is_locked=is_locked, name=name, parent_id=parent_id, ids=ids)
        print("The response of CollectionServiceApi->post_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionServiceApi->post_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_locked** | **bool**| Whether or not to lock the new collection. | [optional] 
 **name** | **str**| The name of the new collection. | [optional] 
 **parent_id** | **str**| Optional - create the collection within a specific folder | [optional] 
 **ids** | **str**| Item Ids to add to the collection | [optional] 

### Return type

[**CollectionsCollectionCreationResult**](CollectionsCollectionCreationResult.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a CollectionCreationResult object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_collections_by_id_items**
> post_collections_by_id_items(ids, id)

Adds items to a collection

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
    api_instance = embyapi.CollectionServiceApi(api_client)
    ids = 'ids_example' # str | Item id, comma delimited
    id = 'id_example' # str | 

    try:
        # Adds items to a collection
        api_instance.post_collections_by_id_items(ids, id)
    except Exception as e:
        print("Exception when calling CollectionServiceApi->post_collections_by_id_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id, comma delimited | 
 **id** | **str**|  | 

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

# **post_collections_by_id_items_delete**
> post_collections_by_id_items_delete(ids, id)

Removes items from a collection

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
    api_instance = embyapi.CollectionServiceApi(api_client)
    ids = 'ids_example' # str | Item id, comma delimited
    id = 'id_example' # str | 

    try:
        # Removes items from a collection
        api_instance.post_collections_by_id_items_delete(ids, id)
    except Exception as e:
        print("Exception when calling CollectionServiceApi->post_collections_by_id_items_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Item id, comma delimited | 
 **id** | **str**|  | 

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

