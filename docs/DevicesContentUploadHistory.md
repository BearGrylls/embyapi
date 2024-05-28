# DevicesContentUploadHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**files_uploaded** | [**List[DevicesLocalFileInfo]**](DevicesLocalFileInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.devices_content_upload_history import DevicesContentUploadHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesContentUploadHistory from a JSON string
devices_content_upload_history_instance = DevicesContentUploadHistory.from_json(json)
# print the JSON string representation of the object
print(DevicesContentUploadHistory.to_json())

# convert the object into a dict
devices_content_upload_history_dict = devices_content_upload_history_instance.to_dict()
# create an instance of DevicesContentUploadHistory from a dict
devices_content_upload_history_from_dict = DevicesContentUploadHistory.from_dict(devices_content_upload_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


