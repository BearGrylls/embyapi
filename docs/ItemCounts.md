# ItemCounts

Class LibrarySummary  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_count** | **int** | The movie count. | [optional] 
**series_count** | **int** | The series count. | [optional] 
**episode_count** | **int** | The episode count. | [optional] 
**game_count** | **int** | The game count. | [optional] 
**artist_count** | **int** |  | [optional] 
**program_count** | **int** |  | [optional] 
**game_system_count** | **int** | The game system count. | [optional] 
**trailer_count** | **int** | The trailer count. | [optional] 
**song_count** | **int** | The song count. | [optional] 
**album_count** | **int** | The album count. | [optional] 
**music_video_count** | **int** | The music video count. | [optional] 
**box_set_count** | **int** | The box set count. | [optional] 
**book_count** | **int** | The book count. | [optional] 
**item_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.item_counts import ItemCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCounts from a JSON string
item_counts_instance = ItemCounts.from_json(json)
# print the JSON string representation of the object
print(ItemCounts.to_json())

# convert the object into a dict
item_counts_dict = item_counts_instance.to_dict()
# create an instance of ItemCounts from a dict
item_counts_from_dict = ItemCounts.from_dict(item_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


