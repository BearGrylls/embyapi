# QueryResultLogFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LogFile]**](LogFile.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_log_file import QueryResultLogFile

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultLogFile from a JSON string
query_result_log_file_instance = QueryResultLogFile.from_json(json)
# print the JSON string representation of the object
print(QueryResultLogFile.to_json())

# convert the object into a dict
query_result_log_file_dict = query_result_log_file_instance.to_dict()
# create an instance of QueryResultLogFile from a dict
query_result_log_file_from_dict = QueryResultLogFile.from_dict(query_result_log_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


