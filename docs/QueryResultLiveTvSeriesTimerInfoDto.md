# QueryResultLiveTvSeriesTimerInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LiveTvSeriesTimerInfoDto]**](LiveTvSeriesTimerInfoDto.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_live_tv_series_timer_info_dto import QueryResultLiveTvSeriesTimerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultLiveTvSeriesTimerInfoDto from a JSON string
query_result_live_tv_series_timer_info_dto_instance = QueryResultLiveTvSeriesTimerInfoDto.from_json(json)
# print the JSON string representation of the object
print(QueryResultLiveTvSeriesTimerInfoDto.to_json())

# convert the object into a dict
query_result_live_tv_series_timer_info_dto_dict = query_result_live_tv_series_timer_info_dto_instance.to_dict()
# create an instance of QueryResultLiveTvSeriesTimerInfoDto from a dict
query_result_live_tv_series_timer_info_dto_from_dict = QueryResultLiveTvSeriesTimerInfoDto.from_dict(query_result_live_tv_series_timer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


