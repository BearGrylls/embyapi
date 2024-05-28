# ExternalIdInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**key** | **str** | The key. | [optional] 
**website** | **str** |  | [optional] 
**url_format_string** | **str** | The URL format string. | [optional] 
**is_supported_as_identifier** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.external_id_info import ExternalIdInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIdInfo from a JSON string
external_id_info_instance = ExternalIdInfo.from_json(json)
# print the JSON string representation of the object
print(ExternalIdInfo.to_json())

# convert the object into a dict
external_id_info_dict = external_id_info_instance.to_dict()
# create an instance of ExternalIdInfo from a dict
external_id_info_from_dict = ExternalIdInfo.from_dict(external_id_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


