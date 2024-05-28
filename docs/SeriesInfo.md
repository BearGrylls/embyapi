# SeriesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episode_air_date** | **datetime** |  | [optional] 
**display_order** | [**SeriesDisplayOrder**](SeriesDisplayOrder.md) |  | [optional] 
**name** | **str** | The name. | [optional] 
**metadata_language** | **str** | The metadata language. | [optional] 
**metadata_country_code** | **str** | The metadata country code. | [optional] 
**metadata_languages** | [**List[GlobalizationCultureDto]**](GlobalizationCultureDto.md) |  | [optional] 
**provider_ids** | **Dict[str, str]** |  | [optional] 
**year** | **int** | The year. | [optional] 
**index_number** | **int** |  | [optional] 
**parent_index_number** | **int** |  | [optional] 
**premiere_date** | **datetime** |  | [optional] 
**is_automated** | **bool** |  | [optional] 
**enable_adult_metadata** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.series_info import SeriesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesInfo from a JSON string
series_info_instance = SeriesInfo.from_json(json)
# print the JSON string representation of the object
print(SeriesInfo.to_json())

# convert the object into a dict
series_info_dict = series_info_instance.to_dict()
# create an instance of SeriesInfo from a dict
series_info_from_dict = SeriesInfo.from_dict(series_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


