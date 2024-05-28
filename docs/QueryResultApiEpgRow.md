# QueryResultApiEpgRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ApiEpgRow]**](ApiEpgRow.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_api_epg_row import QueryResultApiEpgRow

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultApiEpgRow from a JSON string
query_result_api_epg_row_instance = QueryResultApiEpgRow.from_json(json)
# print the JSON string representation of the object
print(QueryResultApiEpgRow.to_json())

# convert the object into a dict
query_result_api_epg_row_dict = query_result_api_epg_row_instance.to_dict()
# create an instance of QueryResultApiEpgRow from a dict
query_result_api_epg_row_from_dict = QueryResultApiEpgRow.from_dict(query_result_api_epg_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


