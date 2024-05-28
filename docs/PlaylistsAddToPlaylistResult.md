# PlaylistsAddToPlaylistResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**item_added_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.playlists_add_to_playlist_result import PlaylistsAddToPlaylistResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsAddToPlaylistResult from a JSON string
playlists_add_to_playlist_result_instance = PlaylistsAddToPlaylistResult.from_json(json)
# print the JSON string representation of the object
print(PlaylistsAddToPlaylistResult.to_json())

# convert the object into a dict
playlists_add_to_playlist_result_dict = playlists_add_to_playlist_result_instance.to_dict()
# create an instance of PlaylistsAddToPlaylistResult from a dict
playlists_add_to_playlist_result_from_dict = PlaylistsAddToPlaylistResult.from_dict(playlists_add_to_playlist_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


