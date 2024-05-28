# ApiOnPlaybackProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_index** | **int** |  | [optional] 
**playlist_length** | **int** |  | [optional] 
**event_name** | [**ProgressEvent**](ProgressEvent.md) |  | [optional] 

## Example

```python
from embyapi.models.api_on_playback_progress import ApiOnPlaybackProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOnPlaybackProgress from a JSON string
api_on_playback_progress_instance = ApiOnPlaybackProgress.from_json(json)
# print the JSON string representation of the object
print(ApiOnPlaybackProgress.to_json())

# convert the object into a dict
api_on_playback_progress_dict = api_on_playback_progress_instance.to_dict()
# create an instance of ApiOnPlaybackProgress from a dict
api_on_playback_progress_from_dict = ApiOnPlaybackProgress.from_dict(api_on_playback_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


