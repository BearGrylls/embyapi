# TrailerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from embyapi.models.trailer_info import TrailerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrailerInfo from a JSON string
trailer_info_instance = TrailerInfo.from_json(json)
# print the JSON string representation of the object
print(TrailerInfo.to_json())

# convert the object into a dict
trailer_info_dict = trailer_info_instance.to_dict()
# create an instance of TrailerInfo from a dict
trailer_info_from_dict = TrailerInfo.from_dict(trailer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


