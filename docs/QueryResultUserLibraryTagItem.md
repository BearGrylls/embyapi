# QueryResultUserLibraryTagItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserLibraryTagItem]**](UserLibraryTagItem.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_user_library_tag_item import QueryResultUserLibraryTagItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultUserLibraryTagItem from a JSON string
query_result_user_library_tag_item_instance = QueryResultUserLibraryTagItem.from_json(json)
# print the JSON string representation of the object
print(QueryResultUserLibraryTagItem.to_json())

# convert the object into a dict
query_result_user_library_tag_item_dict = query_result_user_library_tag_item_instance.to_dict()
# create an instance of QueryResultUserLibraryTagItem from a dict
query_result_user_library_tag_item_from_dict = QueryResultUserLibraryTagItem.from_dict(query_result_user_library_tag_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


