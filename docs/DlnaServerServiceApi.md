# embyapi.DlnaServerServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dlna_by_uuid_connectionmanager_connectionmanager**](DlnaServerServiceApi.md#get_dlna_by_uuid_connectionmanager_connectionmanager) | **GET** /Dlna/{UuId}/connectionmanager/connectionmanager | Gets dlna connection manager xml
[**get_dlna_by_uuid_connectionmanager_connectionmanager_xml**](DlnaServerServiceApi.md#get_dlna_by_uuid_connectionmanager_connectionmanager_xml) | **GET** /Dlna/{UuId}/connectionmanager/connectionmanager.xml | Gets dlna connection manager xml
[**get_dlna_by_uuid_contentdirectory_contentdirectory**](DlnaServerServiceApi.md#get_dlna_by_uuid_contentdirectory_contentdirectory) | **GET** /Dlna/{UuId}/contentdirectory/contentdirectory | Gets dlna content directory xml
[**get_dlna_by_uuid_contentdirectory_contentdirectory_xml**](DlnaServerServiceApi.md#get_dlna_by_uuid_contentdirectory_contentdirectory_xml) | **GET** /Dlna/{UuId}/contentdirectory/contentdirectory.xml | Gets dlna content directory xml
[**get_dlna_by_uuid_description**](DlnaServerServiceApi.md#get_dlna_by_uuid_description) | **GET** /Dlna/{UuId}/description | Gets dlna server info
[**get_dlna_by_uuid_description_xml**](DlnaServerServiceApi.md#get_dlna_by_uuid_description_xml) | **GET** /Dlna/{UuId}/description.xml | Gets dlna server info
[**get_dlna_by_uuid_icons_by_filename**](DlnaServerServiceApi.md#get_dlna_by_uuid_icons_by_filename) | **GET** /Dlna/{UuId}/icons/{Filename} | Gets a server icon
[**get_dlna_icons_by_filename**](DlnaServerServiceApi.md#get_dlna_icons_by_filename) | **GET** /Dlna/icons/{Filename} | Gets a server icon
[**head_dlna_by_uuid_connectionmanager_connectionmanager**](DlnaServerServiceApi.md#head_dlna_by_uuid_connectionmanager_connectionmanager) | **HEAD** /Dlna/{UuId}/connectionmanager/connectionmanager | Gets dlna connection manager xml
[**head_dlna_by_uuid_connectionmanager_connectionmanager_xml**](DlnaServerServiceApi.md#head_dlna_by_uuid_connectionmanager_connectionmanager_xml) | **HEAD** /Dlna/{UuId}/connectionmanager/connectionmanager.xml | Gets dlna connection manager xml
[**head_dlna_by_uuid_contentdirectory_contentdirectory**](DlnaServerServiceApi.md#head_dlna_by_uuid_contentdirectory_contentdirectory) | **HEAD** /Dlna/{UuId}/contentdirectory/contentdirectory | Gets dlna content directory xml
[**head_dlna_by_uuid_contentdirectory_contentdirectory_xml**](DlnaServerServiceApi.md#head_dlna_by_uuid_contentdirectory_contentdirectory_xml) | **HEAD** /Dlna/{UuId}/contentdirectory/contentdirectory.xml | Gets dlna content directory xml
[**head_dlna_by_uuid_description**](DlnaServerServiceApi.md#head_dlna_by_uuid_description) | **HEAD** /Dlna/{UuId}/description | Gets dlna server info
[**head_dlna_by_uuid_description_xml**](DlnaServerServiceApi.md#head_dlna_by_uuid_description_xml) | **HEAD** /Dlna/{UuId}/description.xml | Gets dlna server info
[**post_dlna_by_uuid_connectionmanager_control**](DlnaServerServiceApi.md#post_dlna_by_uuid_connectionmanager_control) | **POST** /Dlna/{UuId}/connectionmanager/control | Processes a control request
[**post_dlna_by_uuid_contentdirectory_control**](DlnaServerServiceApi.md#post_dlna_by_uuid_contentdirectory_control) | **POST** /Dlna/{UuId}/contentdirectory/control | Processes a control request


# **get_dlna_by_uuid_connectionmanager_connectionmanager**
> get_dlna_by_uuid_connectionmanager_connectionmanager(uu_id)

Gets dlna connection manager xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna connection manager xml
        api_instance.get_dlna_by_uuid_connectionmanager_connectionmanager(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_connectionmanager_connectionmanager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_by_uuid_connectionmanager_connectionmanager_xml**
> get_dlna_by_uuid_connectionmanager_connectionmanager_xml(uu_id)

Gets dlna connection manager xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna connection manager xml
        api_instance.get_dlna_by_uuid_connectionmanager_connectionmanager_xml(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_connectionmanager_connectionmanager_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_by_uuid_contentdirectory_contentdirectory**
> get_dlna_by_uuid_contentdirectory_contentdirectory(uu_id)

Gets dlna content directory xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna content directory xml
        api_instance.get_dlna_by_uuid_contentdirectory_contentdirectory(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_contentdirectory_contentdirectory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_by_uuid_contentdirectory_contentdirectory_xml**
> get_dlna_by_uuid_contentdirectory_contentdirectory_xml(uu_id)

Gets dlna content directory xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna content directory xml
        api_instance.get_dlna_by_uuid_contentdirectory_contentdirectory_xml(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_contentdirectory_contentdirectory_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_by_uuid_description**
> get_dlna_by_uuid_description(uu_id)

Gets dlna server info

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna server info
        api_instance.get_dlna_by_uuid_description(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_by_uuid_description_xml**
> get_dlna_by_uuid_description_xml(uu_id)

Gets dlna server info

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna server info
        api_instance.get_dlna_by_uuid_description_xml(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_description_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_by_uuid_icons_by_filename**
> get_dlna_by_uuid_icons_by_filename(uu_id, filename)

Gets a server icon

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId
    filename = 'filename_example' # str | The icon filename

    try:
        # Gets a server icon
        api_instance.get_dlna_by_uuid_icons_by_filename(uu_id, filename)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_by_uuid_icons_by_filename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 
 **filename** | **str**| The icon filename | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlna_icons_by_filename**
> get_dlna_icons_by_filename(filename, uu_id=uu_id)

Gets a server icon

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    filename = 'filename_example' # str | The icon filename
    uu_id = 'uu_id_example' # str | Server UuId (optional)

    try:
        # Gets a server icon
        api_instance.get_dlna_icons_by_filename(filename, uu_id=uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->get_dlna_icons_by_filename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The icon filename | 
 **uu_id** | **str**| Server UuId | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dlna_by_uuid_connectionmanager_connectionmanager**
> head_dlna_by_uuid_connectionmanager_connectionmanager(uu_id)

Gets dlna connection manager xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna connection manager xml
        api_instance.head_dlna_by_uuid_connectionmanager_connectionmanager(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->head_dlna_by_uuid_connectionmanager_connectionmanager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dlna_by_uuid_connectionmanager_connectionmanager_xml**
> head_dlna_by_uuid_connectionmanager_connectionmanager_xml(uu_id)

Gets dlna connection manager xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna connection manager xml
        api_instance.head_dlna_by_uuid_connectionmanager_connectionmanager_xml(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->head_dlna_by_uuid_connectionmanager_connectionmanager_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dlna_by_uuid_contentdirectory_contentdirectory**
> head_dlna_by_uuid_contentdirectory_contentdirectory(uu_id)

Gets dlna content directory xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna content directory xml
        api_instance.head_dlna_by_uuid_contentdirectory_contentdirectory(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->head_dlna_by_uuid_contentdirectory_contentdirectory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dlna_by_uuid_contentdirectory_contentdirectory_xml**
> head_dlna_by_uuid_contentdirectory_contentdirectory_xml(uu_id)

Gets dlna content directory xml

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna content directory xml
        api_instance.head_dlna_by_uuid_contentdirectory_contentdirectory_xml(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->head_dlna_by_uuid_contentdirectory_contentdirectory_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dlna_by_uuid_description**
> head_dlna_by_uuid_description(uu_id)

Gets dlna server info

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna server info
        api_instance.head_dlna_by_uuid_description(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->head_dlna_by_uuid_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dlna_by_uuid_description_xml**
> head_dlna_by_uuid_description_xml(uu_id)

Gets dlna server info

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId

    try:
        # Gets dlna server info
        api_instance.head_dlna_by_uuid_description_xml(uu_id)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->head_dlna_by_uuid_description_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dlna_by_uuid_connectionmanager_control**
> post_dlna_by_uuid_connectionmanager_control(uu_id, body)

Processes a control request

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId
    body = None # bytearray | Binary stream

    try:
        # Processes a control request
        api_instance.post_dlna_by_uuid_connectionmanager_control(uu_id, body)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->post_dlna_by_uuid_connectionmanager_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 
 **body** | **bytearray**| Binary stream | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dlna_by_uuid_contentdirectory_control**
> post_dlna_by_uuid_contentdirectory_control(uu_id, body)

Processes a control request

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
    api_instance = embyapi.DlnaServerServiceApi(api_client)
    uu_id = 'uu_id_example' # str | Server UuId
    body = None # bytearray | Binary stream

    try:
        # Processes a control request
        api_instance.post_dlna_by_uuid_contentdirectory_control(uu_id, body)
    except Exception as e:
        print("Exception when calling DlnaServerServiceApi->post_dlna_by_uuid_contentdirectory_control: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uu_id** | **str**| Server UuId | 
 **body** | **bytearray**| Binary stream | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Response content unknown. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

