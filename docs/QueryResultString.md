# QueryResultString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_string import QueryResultString

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultString from a JSON string
query_result_string_instance = QueryResultString.from_json(json)
# print the JSON string representation of the object
print(QueryResultString.to_json())

# convert the object into a dict
query_result_string_dict = query_result_string_instance.to_dict()
# create an instance of QueryResultString from a dict
query_result_string_from_dict = QueryResultString.from_dict(query_result_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


