# GlobalizationCultureDto

Class CultureDto  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**display_name** | **str** | The display name. | [optional] 
**two_letter_iso_language_name** | **str** | The name of the two letter ISO language. | [optional] 
**three_letter_iso_language_name** | **str** | The name of the three letter ISO language. | [optional] 
**three_letter_iso_language_names** | **List[str]** |  | [optional] 
**two_letter_iso_language_names** | **List[str]** |  | [optional] 

## Example

```python
from embyapi.models.globalization_culture_dto import GlobalizationCultureDto

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalizationCultureDto from a JSON string
globalization_culture_dto_instance = GlobalizationCultureDto.from_json(json)
# print the JSON string representation of the object
print(GlobalizationCultureDto.to_json())

# convert the object into a dict
globalization_culture_dto_dict = globalization_culture_dto_instance.to_dict()
# create an instance of GlobalizationCultureDto from a dict
globalization_culture_dto_from_dict = GlobalizationCultureDto.from_dict(globalization_culture_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


