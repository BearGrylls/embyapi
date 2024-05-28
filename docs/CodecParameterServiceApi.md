# embyapi.CodecParameterServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_encoding_codecparameters**](CodecParameterServiceApi.md#get_encoding_codecparameters) | **GET** /Encoding/CodecParameters | Gets the parameters for a specified codec.
[**post_encoding_codecparameters**](CodecParameterServiceApi.md#post_encoding_codecparameters) | **POST** /Encoding/CodecParameters | Updates the parameters for a specified codec.


# **get_encoding_codecparameters**
> EditObjectContainer get_encoding_codecparameters(codec_id, parameter_context)

Gets the parameters for a specified codec.

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.edit_object_container import EditObjectContainer
from embyapi.models.media_encoding_codec_parameter_context import MediaEncodingCodecParameterContext
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
    api_instance = embyapi.CodecParameterServiceApi(api_client)
    codec_id = 'codec_id_example' # str | Codec Id
    parameter_context = embyapi.MediaEncodingCodecParameterContext() # MediaEncodingCodecParameterContext | Parameter Context

    try:
        # Gets the parameters for a specified codec.
        api_response = api_instance.get_encoding_codecparameters(codec_id, parameter_context)
        print("The response of CodecParameterServiceApi->get_encoding_codecparameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodecParameterServiceApi->get_encoding_codecparameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codec_id** | **str**| Codec Id | 
 **parameter_context** | [**MediaEncodingCodecParameterContext**](.md)| Parameter Context | 

### Return type

[**EditObjectContainer**](EditObjectContainer.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a EditObjectContainer object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_encoding_codecparameters**
> post_encoding_codecparameters(codec_id, parameter_context, body)

Updates the parameters for a specified codec.

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.media_encoding_codec_parameter_context import MediaEncodingCodecParameterContext
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
    api_instance = embyapi.CodecParameterServiceApi(api_client)
    codec_id = 'codec_id_example' # str | Codec Id
    parameter_context = embyapi.MediaEncodingCodecParameterContext() # MediaEncodingCodecParameterContext | Parameter Context
    body = None # bytearray | Binary stream

    try:
        # Updates the parameters for a specified codec.
        api_instance.post_encoding_codecparameters(codec_id, parameter_context, body)
    except Exception as e:
        print("Exception when calling CodecParameterServiceApi->post_encoding_codecparameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codec_id** | **str**| Codec Id | 
 **parameter_context** | [**MediaEncodingCodecParameterContext**](.md)| Parameter Context | 
 **body** | **bytearray**| Binary stream | 

### Return type

void (empty response body)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

