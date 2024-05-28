# QueryResultLiveTvTimerInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LiveTvTimerInfoDto]**](LiveTvTimerInfoDto.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_live_tv_timer_info_dto import QueryResultLiveTvTimerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultLiveTvTimerInfoDto from a JSON string
query_result_live_tv_timer_info_dto_instance = QueryResultLiveTvTimerInfoDto.from_json(json)
# print the JSON string representation of the object
print(QueryResultLiveTvTimerInfoDto.to_json())

# convert the object into a dict
query_result_live_tv_timer_info_dto_dict = query_result_live_tv_timer_info_dto_instance.to_dict()
# create an instance of QueryResultLiveTvTimerInfoDto from a dict
query_result_live_tv_timer_info_dto_from_dict = QueryResultLiveTvTimerInfoDto.from_dict(query_result_live_tv_timer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


