# PlaylistsPlaylistCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**item_added_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.playlists_playlist_creation_result import PlaylistsPlaylistCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistsPlaylistCreationResult from a JSON string
playlists_playlist_creation_result_instance = PlaylistsPlaylistCreationResult.from_json(json)
# print the JSON string representation of the object
print(PlaylistsPlaylistCreationResult.to_json())

# convert the object into a dict
playlists_playlist_creation_result_dict = playlists_playlist_creation_result_instance.to_dict()
# create an instance of PlaylistsPlaylistCreationResult from a dict
playlists_playlist_creation_result_from_dict = PlaylistsPlaylistCreationResult.from_dict(playlists_playlist_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


