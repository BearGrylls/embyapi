# DlnaProfilesDeviceIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendly_name** | **str** |  | [optional] 
**model_number** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**model_description** | **str** |  | [optional] 
**device_description** | **str** |  | [optional] 
**model_url** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**manufacturer_url** | **str** |  | [optional] 
**headers** | [**List[DlnaProfilesHttpHeaderInfo]**](DlnaProfilesHttpHeaderInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.dlna_profiles_device_identification import DlnaProfilesDeviceIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of DlnaProfilesDeviceIdentification from a JSON string
dlna_profiles_device_identification_instance = DlnaProfilesDeviceIdentification.from_json(json)
# print the JSON string representation of the object
print(DlnaProfilesDeviceIdentification.to_json())

# convert the object into a dict
dlna_profiles_device_identification_dict = dlna_profiles_device_identification_instance.to_dict()
# create an instance of DlnaProfilesDeviceIdentification from a dict
dlna_profiles_device_identification_from_dict = DlnaProfilesDeviceIdentification.from_dict(dlna_profiles_device_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


