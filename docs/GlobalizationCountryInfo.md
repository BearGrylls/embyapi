# GlobalizationCountryInfo

Class CountryInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**display_name** | **str** | The display name. | [optional] 
**english_name** | **str** | The English name. | [optional] 
**two_letter_iso_region_name** | **str** | The name of the two letter ISO region. | [optional] 
**three_letter_iso_region_name** | **str** | The name of the three letter ISO region. | [optional] 

## Example

```python
from embyapi.models.globalization_country_info import GlobalizationCountryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalizationCountryInfo from a JSON string
globalization_country_info_instance = GlobalizationCountryInfo.from_json(json)
# print the JSON string representation of the object
print(GlobalizationCountryInfo.to_json())

# convert the object into a dict
globalization_country_info_dict = globalization_country_info_instance.to_dict()
# create an instance of GlobalizationCountryInfo from a dict
globalization_country_info_from_dict = GlobalizationCountryInfo.from_dict(globalization_country_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


