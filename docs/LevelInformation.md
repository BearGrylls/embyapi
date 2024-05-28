# LevelInformation

Class for unified presentation of all information associated with a specific codec level.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** | The enum member name of the level. | [optional] 
**description** | **str** | The common name of the level. | [optional] 
**ordinal** | **int** | A value indicating the level&#39;s ranking relative to other levels. | [optional] 
**max_bit_rate** | [**BitRate**](BitRate.md) |  | [optional] 
**max_bit_rate_display** | **str** | A display value of the &#x60;Emby.Media.Model.Types.LevelInformation.MaxBitRate&#x60; property. | [optional] 
**id** | **str** | A unique identifier. | [optional] 
**resolution_rates** | [**List[ResolutionWithRate]**](ResolutionWithRate.md) | Examples for the maximum supported combinations of resolution and rate for this level. | [optional] 
**resolution_rate_strings** | **List[str]** | Examples for the maximum supported combinations of resolution and rate for this level as string values. | [optional] 
**resolution_rates_display** | **str** | A single string from the &#x60;Emby.Media.Model.Types.LevelInformation.ResolutionRateStrings&#x60; list. | [optional] 

## Example

```python
from embyapi.models.level_information import LevelInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LevelInformation from a JSON string
level_information_instance = LevelInformation.from_json(json)
# print the JSON string representation of the object
print(LevelInformation.to_json())

# convert the object into a dict
level_information_dict = level_information_instance.to_dict()
# create an instance of LevelInformation from a dict
level_information_from_dict = LevelInformation.from_dict(level_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


