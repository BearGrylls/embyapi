# CommonInterfacesICodecDeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**CommonInterfacesICodecDeviceCapabilities**](CommonInterfacesICodecDeviceCapabilities.md) |  | [optional] 
**adapter** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**desription** | **str** |  | [optional] 
**driver** | **str** |  | [optional] 
**driver_version** | [**Version**](Version.md) |  | [optional] 
**api_version** | [**Version**](Version.md) |  | [optional] 
**vendor_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_identifier** | **str** |  | [optional] 
**hardware_context_framework** | [**SecondaryFrameworks**](SecondaryFrameworks.md) |  | [optional] 
**dev_path** | **str** |  | [optional] 
**drm_node** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 

## Example

```python
from embyapi.models.common_interfaces_i_codec_device_info import CommonInterfacesICodecDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommonInterfacesICodecDeviceInfo from a JSON string
common_interfaces_i_codec_device_info_instance = CommonInterfacesICodecDeviceInfo.from_json(json)
# print the JSON string representation of the object
print(CommonInterfacesICodecDeviceInfo.to_json())

# convert the object into a dict
common_interfaces_i_codec_device_info_dict = common_interfaces_i_codec_device_info_instance.to_dict()
# create an instance of CommonInterfacesICodecDeviceInfo from a dict
common_interfaces_i_codec_device_info_from_dict = CommonInterfacesICodecDeviceInfo.from_dict(common_interfaces_i_codec_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


