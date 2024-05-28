# ActivityLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The name. | [optional] 
**overview** | **str** | The overview. | [optional] 
**short_overview** | **str** | The short overview. | [optional] 
**type** | **str** | The type. | [optional] 
**item_id** | **str** | The item identifier. | [optional] 
**var_date** | **datetime** | The date. | [optional] 
**user_id** | **str** | The user identifier. | [optional] 
**user_primary_image_tag** | **str** | The user primary image tag. | [optional] 
**severity** | [**LoggingLogSeverity**](LoggingLogSeverity.md) |  | [optional] 

## Example

```python
from embyapi.models.activity_log_entry import ActivityLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogEntry from a JSON string
activity_log_entry_instance = ActivityLogEntry.from_json(json)
# print the JSON string representation of the object
print(ActivityLogEntry.to_json())

# convert the object into a dict
activity_log_entry_dict = activity_log_entry_instance.to_dict()
# create an instance of ActivityLogEntry from a dict
activity_log_entry_from_dict = ActivityLogEntry.from_dict(activity_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


