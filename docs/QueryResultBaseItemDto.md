# QueryResultBaseItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BaseItemDto]**](BaseItemDto.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_base_item_dto import QueryResultBaseItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultBaseItemDto from a JSON string
query_result_base_item_dto_instance = QueryResultBaseItemDto.from_json(json)
# print the JSON string representation of the object
print(QueryResultBaseItemDto.to_json())

# convert the object into a dict
query_result_base_item_dto_dict = query_result_base_item_dto_instance.to_dict()
# create an instance of QueryResultBaseItemDto from a dict
query_result_base_item_dto_from_dict = QueryResultBaseItemDto.from_dict(query_result_base_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


