# RemoteSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**provider_ids** | **Dict[str, str]** |  | [optional] 
**production_year** | **int** | The year. | [optional] 
**index_number** | **int** |  | [optional] 
**index_number_end** | **int** |  | [optional] 
**parent_index_number** | **int** |  | [optional] 
**sort_index_number** | **int** |  | [optional] 
**sort_parent_index_number** | **int** |  | [optional] 
**premiere_date** | **datetime** |  | [optional] 
**image_url** | **str** |  | [optional] 
**search_provider_name** | **str** |  | [optional] 
**game_system** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**disambiguation_comment** | **str** |  | [optional] 
**album_artist** | [**RemoteSearchResult**](RemoteSearchResult.md) |  | [optional] 
**artists** | [**List[RemoteSearchResult]**](RemoteSearchResult.md) |  | [optional] 

## Example

```python
from embyapi.models.remote_search_result import RemoteSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSearchResult from a JSON string
remote_search_result_instance = RemoteSearchResult.from_json(json)
# print the JSON string representation of the object
print(RemoteSearchResult.to_json())

# convert the object into a dict
remote_search_result_dict = remote_search_result_instance.to_dict()
# create an instance of RemoteSearchResult from a dict
remote_search_result_from_dict = RemoteSearchResult.from_dict(remote_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


