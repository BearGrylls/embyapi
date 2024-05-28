# MetadataEditorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parental_rating_options** | [**List[ParentalRating]**](ParentalRating.md) |  | [optional] 
**countries** | [**List[GlobalizationCountryInfo]**](GlobalizationCountryInfo.md) |  | [optional] 
**cultures** | [**List[GlobalizationCultureDto]**](GlobalizationCultureDto.md) |  | [optional] 
**external_id_infos** | [**List[ExternalIdInfo]**](ExternalIdInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.metadata_editor_info import MetadataEditorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataEditorInfo from a JSON string
metadata_editor_info_instance = MetadataEditorInfo.from_json(json)
# print the JSON string representation of the object
print(MetadataEditorInfo.to_json())

# convert the object into a dict
metadata_editor_info_dict = metadata_editor_info_instance.to_dict()
# create an instance of MetadataEditorInfo from a dict
metadata_editor_info_from_dict = MetadataEditorInfo.from_dict(metadata_editor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


