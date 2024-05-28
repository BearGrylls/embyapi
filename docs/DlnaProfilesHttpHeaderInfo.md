# DlnaProfilesHttpHeaderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**match** | [**DlnaProfilesHeaderMatchType**](DlnaProfilesHeaderMatchType.md) |  | [optional] 

## Example

```python
from embyapi.models.dlna_profiles_http_header_info import DlnaProfilesHttpHeaderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DlnaProfilesHttpHeaderInfo from a JSON string
dlna_profiles_http_header_info_instance = DlnaProfilesHttpHeaderInfo.from_json(json)
# print the JSON string representation of the object
print(DlnaProfilesHttpHeaderInfo.to_json())

# convert the object into a dict
dlna_profiles_http_header_info_dict = dlna_profiles_http_header_info_instance.to_dict()
# create an instance of DlnaProfilesHttpHeaderInfo from a dict
dlna_profiles_http_header_info_from_dict = DlnaProfilesHttpHeaderInfo.from_dict(dlna_profiles_http_header_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


