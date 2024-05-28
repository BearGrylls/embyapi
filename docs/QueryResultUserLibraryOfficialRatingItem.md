# QueryResultUserLibraryOfficialRatingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserLibraryOfficialRatingItem]**](UserLibraryOfficialRatingItem.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_user_library_official_rating_item import QueryResultUserLibraryOfficialRatingItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultUserLibraryOfficialRatingItem from a JSON string
query_result_user_library_official_rating_item_instance = QueryResultUserLibraryOfficialRatingItem.from_json(json)
# print the JSON string representation of the object
print(QueryResultUserLibraryOfficialRatingItem.to_json())

# convert the object into a dict
query_result_user_library_official_rating_item_dict = query_result_user_library_official_rating_item_instance.to_dict()
# create an instance of QueryResultUserLibraryOfficialRatingItem from a dict
query_result_user_library_official_rating_item_from_dict = QueryResultUserLibraryOfficialRatingItem.from_dict(query_result_user_library_official_rating_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


