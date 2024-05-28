# embyapi.InstantMixServiceApi

All URIs are relative to *http://emby.media/emby*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_albums_by_id_instantmix**](InstantMixServiceApi.md#get_albums_by_id_instantmix) | **GET** /Albums/{Id}/InstantMix | Creates an instant playlist based on a given album
[**get_artists_instantmix**](InstantMixServiceApi.md#get_artists_instantmix) | **GET** /Artists/InstantMix | Creates an instant playlist based on a given artist
[**get_audiobooks_nextup**](InstantMixServiceApi.md#get_audiobooks_nextup) | **GET** /AudioBooks/NextUp | Gets a list of next up episodes
[**get_items_by_id_instantmix**](InstantMixServiceApi.md#get_items_by_id_instantmix) | **GET** /Items/{Id}/InstantMix | Creates an instant playlist based on a given item
[**get_musicgenres_by_name_instantmix**](InstantMixServiceApi.md#get_musicgenres_by_name_instantmix) | **GET** /MusicGenres/{Name}/InstantMix | Creates an instant playlist based on a music genre
[**get_musicgenres_instantmix**](InstantMixServiceApi.md#get_musicgenres_instantmix) | **GET** /MusicGenres/InstantMix | Creates an instant playlist based on a music genre
[**get_playlists_by_id_instantmix**](InstantMixServiceApi.md#get_playlists_by_id_instantmix) | **GET** /Playlists/{Id}/InstantMix | Creates an instant playlist based on a given playlist
[**get_songs_by_id_instantmix**](InstantMixServiceApi.md#get_songs_by_id_instantmix) | **GET** /Songs/{Id}/InstantMix | Creates an instant playlist based on a given song


# **get_albums_by_id_instantmix**
> QueryResultBaseItemDto get_albums_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given album

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    id = 'id_example' # str | Item Id
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a given album
        api_response = api_instance.get_albums_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_albums_by_id_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_albums_by_id_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artists_instantmix**
> QueryResultBaseItemDto get_artists_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given artist

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a given artist
        api_response = api_instance.get_artists_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_artists_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_artists_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiobooks_nextup**
> QueryResultBaseItemDto get_audiobooks_nextup(user_id, start_index=start_index, limit=limit, fields=fields, album_id=album_id, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)

Gets a list of next up episodes

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    user_id = 'user_id_example' # str | User Id
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)
    album_id = 'album_id_example' # str | Optional. Filter by series id (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional, include user data (optional)

    try:
        # Gets a list of next up episodes
        api_response = api_instance.get_audiobooks_nextup(user_id, start_index=start_index, limit=limit, fields=fields, album_id=album_id, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)
        print("The response of InstantMixServiceApi->get_audiobooks_nextup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_audiobooks_nextup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 
 **album_id** | **str**| Optional. Filter by series id | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_id_instantmix**
> QueryResultBaseItemDto get_items_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given item

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    id = 'id_example' # str | Item Id
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a given item
        api_response = api_instance.get_items_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_items_by_id_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_items_by_id_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_musicgenres_by_name_instantmix**
> QueryResultBaseItemDto get_musicgenres_by_name_instantmix(name, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a music genre

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    name = 'name_example' # str | The genre name
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a music genre
        api_response = api_instance.get_musicgenres_by_name_instantmix(name, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_musicgenres_by_name_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_musicgenres_by_name_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The genre name | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_musicgenres_instantmix**
> QueryResultBaseItemDto get_musicgenres_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a music genre

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a music genre
        api_response = api_instance.get_musicgenres_instantmix(include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_musicgenres_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_musicgenres_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlists_by_id_instantmix**
> QueryResultBaseItemDto get_playlists_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given playlist

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    id = 'id_example' # str | Item Id
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a given playlist
        api_response = api_instance.get_playlists_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_playlists_by_id_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_playlists_by_id_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_songs_by_id_instantmix**
> QueryResultBaseItemDto get_songs_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)

Creates an instant playlist based on a given song

Requires authentication as user

### Example

* Api Key Authentication (apikeyauth):
* Bearer (Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)") Authentication (embyauth):

```python
import embyapi
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto
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
    api_instance = embyapi.InstantMixServiceApi(api_client)
    id = 'id_example' # str | Item Id
    include_item_types = 'include_item_types_example' # str | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. (optional)
    enable_images = True # bool | Optional, include image information in output (optional)
    enable_user_data = True # bool | Optional, include user data (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type (optional)
    enable_image_types = 'enable_image_types_example' # str | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data (optional)
    limit = 56 # int | Optional. The maximum number of records to return (optional)
    fields = 'fields_example' # str | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls (optional)

    try:
        # Creates an instant playlist based on a given song
        api_response = api_instance.get_songs_by_id_instantmix(id, include_item_types=include_item_types, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, limit=limit, fields=fields)
        print("The response of InstantMixServiceApi->get_songs_by_id_instantmix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstantMixServiceApi->get_songs_by_id_instantmix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item Id | 
 **include_item_types** | **str**| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output | [optional] 
 **enable_user_data** | **bool**| Optional, include user data | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type | [optional] 
 **enable_image_types** | **str**| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| Optional. Filter by user id, and attach user data | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return | [optional] 
 **fields** | **str**| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls | [optional] 

### Return type

[**QueryResultBaseItemDto**](QueryResultBaseItemDto.md)

### Authorization

[apikeyauth](../README.md#apikeyauth), [embyauth](../README.md#embyauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful. Returning a QueryResult&lt;BaseItemDto&gt; object. |  -  |
**400** | Bad Request. Server cannot process request. |  -  |
**401** | Unauthorized. Client needs to authenticate. |  -  |
**403** | Forbidden. No permission for the reqested operation. |  -  |
**404** | Resource not found or unavailable. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

