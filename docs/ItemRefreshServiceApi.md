# embyapi.ItemRefreshServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_items_by_id_refresh**](ItemRefreshServiceApi.md#post_items_by_id_refresh) | **POST** /Items/{Id}/Refresh | Refreshes metadata for an item


# **post_items_by_id_refresh**
> post_items_by_id_refresh(id, recursive=recursive, metadata_refresh_mode=metadata_refresh_mode, image_refresh_mode=image_refresh_mode, replace_all_metadata=replace_all_metadata, replace_all_images=replace_all_images)

Refreshes metadata for an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.metadata_refresh_mode import MetadataRefreshMode
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
    api_instance = embyapi.ItemRefreshServiceApi(api_client)
    id = 'id_example' # str | Item Id
    recursive = True # bool | Indicates if the refresh should occur recursively. (optional)
    metadata_refresh_mode = embyapi.MetadataRefreshMode() # MetadataRefreshMode | Specifies the metadata refresh mode (optional)
    image_refresh_mode = embyapi.MetadataRefreshMode() # MetadataRefreshMode | Specifies the image refresh mode (optional)
    replace_all_metadata = True # bool | Determines if metadata should be replaced. Only applicable if mode is FullRefresh (optional)
    replace_all_images = True # bool | Determines if images should be replaced. Only applicable if mode is FullRefresh (optional)

    try:
        # Refreshes metadata for an item
        api_instance.post_items_by_id_refresh(id, recursive=recursive, metadata_refresh_mode=metadata_refresh_mode, image_refresh_mode=image_refresh_mode, replace_all_metadata=replace_all_metadata, replace_all_images=replace_all_images)
    except Exception as e:
        print("Exception when calling ItemRefreshServiceApi->post_items_by_id_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **recursive** | **bool**| Indicates if the refresh should occur recursively. | [optional] 
 **metadata_refresh_mode** | [**MetadataRefreshMode**](.md)| Specifies the metadata refresh mode | [optional] 
 **image_refresh_mode** | [**MetadataRefreshMode**](.md)| Specifies the image refresh mode | [optional] 
 **replace_all_metadata** | **bool**| Determines if metadata should be replaced. Only applicable if mode is FullRefresh | [optional] 
 **replace_all_images** | **bool**| Determines if images should be replaced. Only applicable if mode is FullRefresh | [optional] 

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

