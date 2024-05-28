# RemoteSearchQueryAlbumInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**AlbumInfo**](AlbumInfo.md) |  | [optional] 
**item_id** | **int** |  | [optional] 
**search_provider_name** | **str** |  | [optional] 
**providers** | **List[str]** |  | [optional] 
**include_disabled_providers** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.remote_search_query_album_info import RemoteSearchQueryAlbumInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSearchQueryAlbumInfo from a JSON string
remote_search_query_album_info_instance = RemoteSearchQueryAlbumInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteSearchQueryAlbumInfo.to_json())

# convert the object into a dict
remote_search_query_album_info_dict = remote_search_query_album_info_instance.to_dict()
# create an instance of RemoteSearchQueryAlbumInfo from a dict
remote_search_query_album_info_from_dict = RemoteSearchQueryAlbumInfo.from_dict(remote_search_query_album_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


