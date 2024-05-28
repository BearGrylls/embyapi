# DlnaProfilesProtocolInfoDetection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_for_video** | **bool** |  | [optional] 
**enabled_for_audio** | **bool** |  | [optional] 
**enabled_for_photos** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.dlna_profiles_protocol_info_detection import DlnaProfilesProtocolInfoDetection

# TODO update the JSON string below
json = "{}"
# create an instance of DlnaProfilesProtocolInfoDetection from a JSON string
dlna_profiles_protocol_info_detection_instance = DlnaProfilesProtocolInfoDetection.from_json(json)
# print the JSON string representation of the object
print(DlnaProfilesProtocolInfoDetection.to_json())

# convert the object into a dict
dlna_profiles_protocol_info_detection_dict = dlna_profiles_protocol_info_detection_instance.to_dict()
# create an instance of DlnaProfilesProtocolInfoDetection from a dict
dlna_profiles_protocol_info_detection_from_dict = DlnaProfilesProtocolInfoDetection.from_dict(dlna_profiles_protocol_info_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


