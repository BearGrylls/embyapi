# TaskTriggerInfo

Class TaskTriggerInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type. | [optional] 
**time_of_day_ticks** | **int** | The time of day. | [optional] 
**interval_ticks** | **int** | The interval. | [optional] 
**system_event** | [**SystemEvent**](SystemEvent.md) |  | [optional] 
**day_of_week** | [**DayOfWeek**](DayOfWeek.md) |  | [optional] 
**max_runtime_ticks** | **int** | The maximum runtime ticks. | [optional] 

## Example

```python
from embyapi.models.task_trigger_info import TaskTriggerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTriggerInfo from a JSON string
task_trigger_info_instance = TaskTriggerInfo.from_json(json)
# print the JSON string representation of the object
print(TaskTriggerInfo.to_json())

# convert the object into a dict
task_trigger_info_dict = task_trigger_info_instance.to_dict()
# create an instance of TaskTriggerInfo from a dict
task_trigger_info_from_dict = TaskTriggerInfo.from_dict(task_trigger_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


