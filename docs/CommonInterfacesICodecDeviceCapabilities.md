# CommonInterfacesICodecDeviceCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_hw_upload** | **bool** |  | [optional] 
**supports_hw_download** | **bool** |  | [optional] 
**supports_standalone_device_init** | **bool** |  | [optional] 
**supports10_bit_processing** | **bool** |  | [optional] 
**supports_native_tone_mapping** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.common_interfaces_i_codec_device_capabilities import CommonInterfacesICodecDeviceCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of CommonInterfacesICodecDeviceCapabilities from a JSON string
common_interfaces_i_codec_device_capabilities_instance = CommonInterfacesICodecDeviceCapabilities.from_json(json)
# print the JSON string representation of the object
print(CommonInterfacesICodecDeviceCapabilities.to_json())

# convert the object into a dict
common_interfaces_i_codec_device_capabilities_dict = common_interfaces_i_codec_device_capabilities_instance.to_dict()
# create an instance of CommonInterfacesICodecDeviceCapabilities from a dict
common_interfaces_i_codec_device_capabilities_from_dict = CommonInterfacesICodecDeviceCapabilities.from_dict(common_interfaces_i_codec_device_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


