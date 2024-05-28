# ApiBaseItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is4_k** | **bool** |  | [optional] 
**enable_total_record_count** | **bool** |  | [optional] 
**recording_keyword** | **str** |  | [optional] 
**recording_keyword_type** | [**LiveTvKeywordType**](LiveTvKeywordType.md) |  | [optional] 
**random_seed** | **int** |  | [optional] 
**genre_ids** | **str** |  | [optional] 
**collection_ids** | **str** |  | [optional] 
**tag_ids** | **str** |  | [optional] 
**exclude_tag_ids** | **str** |  | [optional] 
**exclude_artist_ids** | **str** |  | [optional] 
**album_artist_ids** | **str** |  | [optional] 
**contributing_artist_ids** | **str** |  | [optional] 
**album_ids** | **str** |  | [optional] 
**outer_ids** | **str** |  | [optional] 
**list_item_ids** | **str** |  | [optional] 
**audio_languages** | **str** |  | [optional] 
**subtitle_languages** | **str** |  | [optional] 
**can_edit_items** | **bool** |  | [optional] 
**group_items_into** | [**LibraryItemLinkType**](LibraryItemLinkType.md) |  | [optional] 
**min_width** | **int** |  | [optional] 
**min_height** | **int** |  | [optional] 
**max_width** | **int** |  | [optional] 
**max_height** | **int** |  | [optional] 
**group_programs_by_series** | **bool** |  | [optional] 
**air_days** | [**List[DayOfWeek]**](DayOfWeek.md) |  | [optional] 
**is_airing** | **bool** |  | [optional] 
**has_aired** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.api_base_items_request import ApiBaseItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBaseItemsRequest from a JSON string
api_base_items_request_instance = ApiBaseItemsRequest.from_json(json)
# print the JSON string representation of the object
print(ApiBaseItemsRequest.to_json())

# convert the object into a dict
api_base_items_request_dict = api_base_items_request_instance.to_dict()
# create an instance of ApiBaseItemsRequest from a dict
api_base_items_request_from_dict = ApiBaseItemsRequest.from_dict(api_base_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


