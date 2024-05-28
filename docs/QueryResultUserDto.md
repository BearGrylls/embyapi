# QueryResultUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserDto]**](UserDto.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_user_dto import QueryResultUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultUserDto from a JSON string
query_result_user_dto_instance = QueryResultUserDto.from_json(json)
# print the JSON string representation of the object
print(QueryResultUserDto.to_json())

# convert the object into a dict
query_result_user_dto_dict = query_result_user_dto_instance.to_dict()
# create an instance of QueryResultUserDto from a dict
query_result_user_dto_from_dict = QueryResultUserDto.from_dict(query_result_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


