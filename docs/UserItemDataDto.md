# UserItemDataDto

Class UserItemDataDto  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **float** | The rating. | [optional] 
**played_percentage** | **float** | The played percentage. | [optional] 
**unplayed_item_count** | **int** | The unplayed item count. | [optional] 
**playback_position_ticks** | **int** | The playback position ticks. | [optional] 
**play_count** | **int** | The play count. | [optional] 
**is_favorite** | **bool** | A value indicating whether this instance is favorite. | [optional] 
**last_played_date** | **datetime** | The last played date. | [optional] 
**played** | **bool** | A value indicating whether this &#x60;MediaBrowser.Model.Dto.UserItemDataDto&#x60; is played. | [optional] 
**key** | **str** | The key. | [optional] 
**item_id** | **str** | The item identifier. | [optional] 
**server_id** | **str** | Used only by our Windows app. Not used by Emby Server. | [optional] 

## Example

```python
from embyapi.models.user_item_data_dto import UserItemDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserItemDataDto from a JSON string
user_item_data_dto_instance = UserItemDataDto.from_json(json)
# print the JSON string representation of the object
print(UserItemDataDto.to_json())

# convert the object into a dict
user_item_data_dto_dict = user_item_data_dto_instance.to_dict()
# create an instance of UserItemDataDto from a dict
user_item_data_dto_from_dict = UserItemDataDto.from_dict(user_item_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


