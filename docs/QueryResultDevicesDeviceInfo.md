# QueryResultDevicesDeviceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DevicesDeviceInfo]**](DevicesDeviceInfo.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.query_result_devices_device_info import QueryResultDevicesDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultDevicesDeviceInfo from a JSON string
query_result_devices_device_info_instance = QueryResultDevicesDeviceInfo.from_json(json)
# print the JSON string representation of the object
print(QueryResultDevicesDeviceInfo.to_json())

# convert the object into a dict
query_result_devices_device_info_dict = query_result_devices_device_info_instance.to_dict()
# create an instance of QueryResultDevicesDeviceInfo from a dict
query_result_devices_device_info_from_dict = QueryResultDevicesDeviceInfo.from_dict(query_result_devices_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


