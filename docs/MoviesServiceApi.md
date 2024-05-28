# embyapi.MoviesServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_movies_recommendations**](MoviesServiceApi.md#get_movies_recommendations) | **GET** /Movies/Recommendations | Gets movie recommendations


# **get_movies_recommendations**
> List[RecommendationDto] get_movies_recommendations(category_limit=category_limit, item_limit=item_limit, user_id=user_id, parent_id=parent_id, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)

Gets movie recommendations

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.recommendation_dto import RecommendationDto
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
    api_instance = embyapi.MoviesServiceApi(api_client)
    category_limit = 56 # int | The max number of categories to return (optional)
    item_limit = 56 # int | The max number of items to return per category (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)

    try:
        # Gets movie recommendations
        api_response = api_instance.get_movies_recommendations(category_limit=category_limit, item_limit=item_limit, user_id=user_id, parent_id=parent_id, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)
        print("The response of MoviesServiceApi->get_movies_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoviesServiceApi->get_movies_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_limit** | **int**| The max number of categories to return | [optional] 
 **item_limit** | **int**| The max number of items to return per category | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 

### Return type

[**List[RecommendationDto]**](RecommendationDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a RecommendationDto[] object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

