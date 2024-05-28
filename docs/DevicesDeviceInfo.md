# DevicesDeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** | The identifier. | [optional] 
**internal_id** | **int** |  | [optional] 
**reported_device_id** | **str** |  | [optional] 
**last_user_name** | **str** | The last name of the user. | [optional] 
**app_name** | **str** | The name of the application. | [optional] 
**app_version** | **str** | The application version. | [optional] 
**last_user_id** | **str** | The last user identifier. | [optional] 
**date_last_activity** | **datetime** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 

## Example

```python
from embyapi.models.devices_device_info import DevicesDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesDeviceInfo from a JSON string
devices_device_info_instance = DevicesDeviceInfo.from_json(json)
# print the JSON string representation of the object
print(DevicesDeviceInfo.to_json())

# convert the object into a dict
devices_device_info_dict = devices_device_info_instance.to_dict()
# create an instance of DevicesDeviceInfo from a dict
devices_device_info_from_dict = DevicesDeviceInfo.from_dict(devices_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


