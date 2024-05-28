# SystemInfo

Class SystemInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_update_level** | [**PackageVersionClass**](PackageVersionClass.md) |  | [optional] 
**operating_system_display_name** | **str** | The display name of the operating system. | [optional] 
**package_name** | **str** |  | [optional] 
**has_pending_restart** | **bool** | A value indicating whether this instance has pending restart. | [optional] 
**is_shutting_down** | **bool** |  | [optional] 
**has_image_enhancers** | **bool** |  | [optional] 
**operating_system** | **str** | The operating sytem. | [optional] 
**supports_library_monitor** | **bool** | A value indicating whether \\[supports library monitor\\]. | [optional] 
**supports_local_port_configuration** | **bool** |  | [optional] 
**supports_wake_server** | **bool** |  | [optional] 
**web_socket_port_number** | **int** | The web socket port number. | [optional] 
**completed_installations** | [**List[InstallationInfo]**](InstallationInfo.md) | The completed installations. | [optional] 
**can_self_restart** | **bool** | A value indicating whether this instance can self restart. | [optional] 
**can_self_update** | **bool** | A value indicating whether this instance can self update. | [optional] 
**can_launch_web_browser** | **bool** |  | [optional] 
**program_data_path** | **str** | The program data path. | [optional] 
**items_by_name_path** | **str** | The items by name path. | [optional] 
**cache_path** | **str** | The cache path. | [optional] 
**log_path** | **str** | The log path. | [optional] 
**internal_metadata_path** | **str** | The internal metadata path. | [optional] 
**transcoding_temp_path** | **str** | The transcoding temporary path. | [optional] 
**http_server_port_number** | **int** | The HTTP server port number. | [optional] 
**supports_https** | **bool** | A value indicating whether \\[enable HTTPS\\]. | [optional] 
**https_port_number** | **int** | The HTTPS server port number. | [optional] 
**has_update_available** | **bool** | A value indicating whether this instance has update available. | [optional] 
**supports_auto_run_at_startup** | **bool** | A value indicating whether \\[supports automatic run at startup\\]. | [optional] 
**hardware_acceleration_requires_premiere** | **bool** |  | [optional] 
**wake_on_lan_info** | [**List[WakeOnLanInfo]**](WakeOnLanInfo.md) |  | [optional] 
**local_address** | **str** | The local address. | [optional] 
**local_addresses** | **List[str]** |  | [optional] 
**wan_address** | **str** | The wan address. | [optional] 
**remote_addresses** | **List[str]** |  | [optional] 
**server_name** | **str** | The name of the server. | [optional] 
**version** | **str** | The version. | [optional] 
**id** | **str** | The id. | [optional] 

## Example

```python
from embyapi.models.system_info import SystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfo from a JSON string
system_info_instance = SystemInfo.from_json(json)
# print the JSON string representation of the object
print(SystemInfo.to_json())

# convert the object into a dict
system_info_dict = system_info_instance.to_dict()
# create an instance of SystemInfo from a dict
system_info_from_dict = SystemInfo.from_dict(system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


