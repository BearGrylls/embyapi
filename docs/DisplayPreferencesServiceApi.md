# embyapi.DisplayPreferencesServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_displaypreferences_by_id**](DisplayPreferencesServiceApi.md#get_displaypreferences_by_id) | **GET** /DisplayPreferences/{Id} | Gets a user&#39;s display preferences for an item
[**post_displaypreferences_by_displaypreferencesid**](DisplayPreferencesServiceApi.md#post_displaypreferences_by_displaypreferencesid) | **POST** /DisplayPreferences/{DisplayPreferencesId} | Updates a user&#39;s display preferences for an item


# **get_displaypreferences_by_id**
> DisplayPreferences get_displaypreferences_by_id(id, user_id, client)

Gets a user's display preferences for an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.display_preferences import DisplayPreferences
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
    api_instance = embyapi.DisplayPreferencesServiceApi(api_client)
    id = 'id_example' # str | Item Id
    user_id = 'user_id_example' # str | User Id
    client = 'client_example' # str | Client

    try:
        # Gets a user's display preferences for an item
        api_response = api_instance.get_displaypreferences_by_id(id, user_id, client)
        print("The response of DisplayPreferencesServiceApi->get_displaypreferences_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisplayPreferencesServiceApi->get_displaypreferences_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **user_id** | **str**| User Id | 
 **client** | **str**| Client | 

### Return type

[**DisplayPreferences**](DisplayPreferences.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a DisplayPreferences object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_displaypreferences_by_displaypreferencesid**
> post_displaypreferences_by_displaypreferencesid(display_preferences_id, user_id, display_preferences)

Updates a user's display preferences for an item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.display_preferences import DisplayPreferences
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
    api_instance = embyapi.DisplayPreferencesServiceApi(api_client)
    display_preferences_id = 'display_preferences_id_example' # str | DisplayPreferences Id
    user_id = 'user_id_example' # str | User Id
    display_preferences = embyapi.DisplayPreferences() # DisplayPreferences | DisplayPreferences: 

    try:
        # Updates a user's display preferences for an item
        api_instance.post_displaypreferences_by_displaypreferencesid(display_preferences_id, user_id, display_preferences)
    except Exception as e:
        print("Exception when calling DisplayPreferencesServiceApi->post_displaypreferences_by_displaypreferencesid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_preferences_id** | **str**| DisplayPreferences Id | 
 **user_id** | **str**| User Id | 
 **display_preferences** | [**DisplayPreferences**](DisplayPreferences.md)| DisplayPreferences:  | 

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

