# embyapi.OpenApiServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_openapi**](OpenApiServiceApi.md#get_openapi) | **GET** /openapi | Gets the OpenAPI 3 specifications
[**get_openapi_json**](OpenApiServiceApi.md#get_openapi_json) | **GET** /openapi.json | Gets OpenAPI 3 specifications
[**get_swagger**](OpenApiServiceApi.md#get_swagger) | **GET** /swagger | Gets the swagger specifications
[**get_swagger_json**](OpenApiServiceApi.md#get_swagger_json) | **GET** /swagger.json | Gets the swagger specifications


# **get_openapi**
> str get_openapi()

Gets the OpenAPI 3 specifications

No authentication required

### Example


```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)


# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.OpenApiServiceApi(api_client)

    try:
        # Gets the OpenAPI 3 specifications
        api_response = api_instance.get_openapi()
        print("The response of OpenApiServiceApi->get_openapi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApiServiceApi->get_openapi: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a String object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_openapi_json**
> str get_openapi_json()

Gets OpenAPI 3 specifications

No authentication required

### Example


```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)


# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.OpenApiServiceApi(api_client)

    try:
        # Gets OpenAPI 3 specifications
        api_response = api_instance.get_openapi_json()
        print("The response of OpenApiServiceApi->get_openapi_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApiServiceApi->get_openapi_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a String object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger**
> str get_swagger()

Gets the swagger specifications

No authentication required

### Example


```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)


# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.OpenApiServiceApi(api_client)

    try:
        # Gets the swagger specifications
        api_response = api_instance.get_swagger()
        print("The response of OpenApiServiceApi->get_swagger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApiServiceApi->get_swagger: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a String object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_json**
> str get_swagger_json()

Gets the swagger specifications

No authentication required

### Example


```python
import embyapi
from embyapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://emby.media/emby
# See configuration.py for a list of all supported configuration parameters.
configuration = embyapi.Configuration(
    host = "http://emby.media/emby"
)


# Enter a context with an instance of the API client
with embyapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = embyapi.OpenApiServiceApi(api_client)

    try:
        # Gets the swagger specifications
        api_response = api_instance.get_swagger_json()
        print("The response of OpenApiServiceApi->get_swagger_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApiServiceApi->get_swagger_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a String object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

