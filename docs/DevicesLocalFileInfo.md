# DevicesLocalFileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**album** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 

## Example

```python
from embyapi.models.devices_local_file_info import DevicesLocalFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesLocalFileInfo from a JSON string
devices_local_file_info_instance = DevicesLocalFileInfo.from_json(json)
# print the JSON string representation of the object
print(DevicesLocalFileInfo.to_json())

# convert the object into a dict
devices_local_file_info_dict = devices_local_file_info_instance.to_dict()
# create an instance of DevicesLocalFileInfo from a dict
devices_local_file_info_from_dict = DevicesLocalFileInfo.from_dict(devices_local_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


