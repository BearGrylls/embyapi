# ConfigurationToneMappingToneMapOptionsVisibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_advanced** | **bool** |  | [optional] 
**is_software_tone_mapping_available** | **bool** |  | [optional] 
**is_any_hardware_tone_mapping_available** | **bool** |  | [optional] 
**show_nvidia_options** | **bool** |  | [optional] 
**show_quick_sync_options** | **bool** |  | [optional] 
**show_vaapi_options** | **bool** |  | [optional] 
**is_open_cl_available** | **bool** |  | [optional] 
**is_open_cl_super_t_available** | **bool** |  | [optional] 
**is_vaapi_native_available** | **bool** |  | [optional] 
**is_quick_sync_native_available** | **bool** |  | [optional] 
**operating_system** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 

## Example

```python
from embyapi.models.configuration_tone_mapping_tone_map_options_visibility import ConfigurationToneMappingToneMapOptionsVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationToneMappingToneMapOptionsVisibility from a JSON string
configuration_tone_mapping_tone_map_options_visibility_instance = ConfigurationToneMappingToneMapOptionsVisibility.from_json(json)
# print the JSON string representation of the object
print(ConfigurationToneMappingToneMapOptionsVisibility.to_json())

# convert the object into a dict
configuration_tone_mapping_tone_map_options_visibility_dict = configuration_tone_mapping_tone_map_options_visibility_instance.to_dict()
# create an instance of ConfigurationToneMappingToneMapOptionsVisibility from a dict
configuration_tone_mapping_tone_map_options_visibility_from_dict = ConfigurationToneMappingToneMapOptionsVisibility.from_dict(configuration_tone_mapping_tone_map_options_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


