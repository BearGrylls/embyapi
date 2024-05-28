# embyapi.PackageServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_packages_installing_by_id**](PackageServiceApi.md#delete_packages_installing_by_id) | **DELETE** /Packages/Installing/{Id} | Cancels a package installation
[**get_packages**](PackageServiceApi.md#get_packages) | **GET** /Packages | Gets available packages
[**get_packages_by_name**](PackageServiceApi.md#get_packages_by_name) | **GET** /Packages/{Name} | Gets a package, by name or assembly guid
[**get_packages_updates**](PackageServiceApi.md#get_packages_updates) | **GET** /Packages/Updates | Gets available package updates for currently installed packages
[**post_packages_installed_by_name**](PackageServiceApi.md#post_packages_installed_by_name) | **POST** /Packages/Installed/{Name} | Installs a package
[**post_packages_installing_by_id_delete**](PackageServiceApi.md#post_packages_installing_by_id_delete) | **POST** /Packages/Installing/{Id}/Delete | Cancels a package installation


# **delete_packages_installing_by_id**
> delete_packages_installing_by_id(id)

Cancels a package installation

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
    api_instance = embyapi.PackageServiceApi(api_client)
    id = 'id_example' # str | Installation Id

    try:
        # Cancels a package installation
        api_instance.delete_packages_installing_by_id(id)
    except Exception as e:
        print("Exception when calling PackageServiceApi->delete_packages_installing_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation Id | 

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

# **get_packages**
> List[PackageInfo] get_packages(package_type=package_type, target_systems=target_systems, is_premium=is_premium, is_adult=is_adult)

Gets available packages

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.package_info import PackageInfo
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
    api_instance = embyapi.PackageServiceApi(api_client)
    package_type = 'package_type_example' # str | Optional package type filter (System/UserInstalled) (optional)
    target_systems = 'target_systems_example' # str | Optional. Filter by target system type. Allows multiple, comma delimited. (optional)
    is_premium = True # bool | Optional. Filter by premium status (optional)
    is_adult = True # bool | Optional. Filter by package that contain adult content. (optional)

    try:
        # Gets available packages
        api_response = api_instance.get_packages(package_type=package_type, target_systems=target_systems, is_premium=is_premium, is_adult=is_adult)
        print("The response of PackageServiceApi->get_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageServiceApi->get_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type** | **str**| Optional package type filter (System/UserInstalled) | [optional] 
 **target_systems** | **str**| Optional. Filter by target system type. Allows multiple, comma delimited. | [optional] 
 **is_premium** | **bool**| Optional. Filter by premium status | [optional] 
 **is_adult** | **bool**| Optional. Filter by package that contain adult content. | [optional] 

### Return type

[**List[PackageInfo]**](PackageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a PackageInfo[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packages_by_name**
> PackageInfo get_packages_by_name(name, assembly_guid=assembly_guid)

Gets a package, by name or assembly guid

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.package_info import PackageInfo
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
    api_instance = embyapi.PackageServiceApi(api_client)
    name = 'name_example' # str | The name of the package
    assembly_guid = 'assembly_guid_example' # str | The guid of the associated assembly (optional)

    try:
        # Gets a package, by name or assembly guid
        api_response = api_instance.get_packages_by_name(name, assembly_guid=assembly_guid)
        print("The response of PackageServiceApi->get_packages_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageServiceApi->get_packages_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the package | 
 **assembly_guid** | **str**| The guid of the associated assembly | [optional] 

### Return type

[**PackageInfo**](PackageInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a PackageInfo object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packages_updates**
> List[PackageVersionInfo] get_packages_updates(package_type)

Gets available package updates for currently installed packages

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.package_version_info import PackageVersionInfo
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
    api_instance = embyapi.PackageServiceApi(api_client)
    package_type = 'package_type_example' # str | Package type filter (System/UserInstalled)

    try:
        # Gets available package updates for currently installed packages
        api_response = api_instance.get_packages_updates(package_type)
        print("The response of PackageServiceApi->get_packages_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageServiceApi->get_packages_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type** | **str**| Package type filter (System/UserInstalled) | 

### Return type

[**List[PackageVersionInfo]**](PackageVersionInfo.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a PackageVersionInfo[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_packages_installed_by_name**
> post_packages_installed_by_name(name, assembly_guid=assembly_guid, version=version, update_class=update_class)

Installs a package

Requires authentication as administrator

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.package_version_class import PackageVersionClass
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
    api_instance = embyapi.PackageServiceApi(api_client)
    name = 'name_example' # str | Package name
    assembly_guid = 'assembly_guid_example' # str | Guid of the associated assembly (optional)
    version = 'version_example' # str | Optional version. Defaults to latest version. (optional)
    update_class = embyapi.PackageVersionClass() # PackageVersionClass | Optional update class (Dev, Beta, Release). Defaults to Release. (optional)

    try:
        # Installs a package
        api_instance.post_packages_installed_by_name(name, assembly_guid=assembly_guid, version=version, update_class=update_class)
    except Exception as e:
        print("Exception when calling PackageServiceApi->post_packages_installed_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Package name | 
 **assembly_guid** | **str**| Guid of the associated assembly | [optional] 
 **version** | **str**| Optional version. Defaults to latest version. | [optional] 
 **update_class** | [**PackageVersionClass**](.md)| Optional update class (Dev, Beta, Release). Defaults to Release. | [optional] 

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

# **post_packages_installing_by_id_delete**
> post_packages_installing_by_id_delete(id)

Cancels a package installation

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
    api_instance = embyapi.PackageServiceApi(api_client)
    id = 'id_example' # str | Installation Id

    try:
        # Cancels a package installation
        api_instance.post_packages_installing_by_id_delete(id)
    except Exception as e:
        print("Exception when calling PackageServiceApi->post_packages_installing_by_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Installation Id | 

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

