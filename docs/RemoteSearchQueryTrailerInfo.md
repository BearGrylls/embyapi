# RemoteSearchQueryTrailerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**TrailerInfo**](TrailerInfo.md) |  | [optional] 
**item_id** | **int** |  | [optional] 
**search_provider_name** | **str** |  | [optional] 
**providers** | **List[str]** |  | [optional] 
**include_disabled_providers** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.remote_search_query_trailer_info import RemoteSearchQueryTrailerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSearchQueryTrailerInfo from a JSON string
remote_search_query_trailer_info_instance = RemoteSearchQueryTrailerInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteSearchQueryTrailerInfo.to_json())

# convert the object into a dict
remote_search_query_trailer_info_dict = remote_search_query_trailer_info_instance.to_dict()
# create an instance of RemoteSearchQueryTrailerInfo from a dict
remote_search_query_trailer_info_from_dict = RemoteSearchQueryTrailerInfo.from_dict(remote_search_query_trailer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


