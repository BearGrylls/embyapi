# LogFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | The date created. | [optional] 
**date_modified** | **datetime** | The date modified. | [optional] 
**size** | **int** | The size. | [optional] 
**name** | **str** | The name. | [optional] 

## Example

```python
from embyapi.models.log_file import LogFile

# TODO update the JSON string below
json = "{}"
# create an instance of LogFile from a JSON string
log_file_instance = LogFile.from_json(json)
# print the JSON string representation of the object
print(LogFile.to_json())

# convert the object into a dict
log_file_dict = log_file_instance.to_dict()
# create an instance of LogFile from a dict
log_file_from_dict = LogFile.from_dict(log_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


