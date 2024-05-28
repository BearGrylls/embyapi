# TaskResult

Class TaskExecutionInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time_utc** | **datetime** | The start time UTC. | [optional] 
**end_time_utc** | **datetime** | The end time UTC. | [optional] 
**status** | [**TaskCompletionStatus**](TaskCompletionStatus.md) |  | [optional] 
**name** | **str** | The name. | [optional] 
**key** | **str** | The key. | [optional] 
**id** | **str** | The id. | [optional] 
**error_message** | **str** | The error message. | [optional] 
**long_error_message** | **str** | The long error message. | [optional] 

## Example

```python
from embyapi.models.task_result import TaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResult from a JSON string
task_result_instance = TaskResult.from_json(json)
# print the JSON string representation of the object
print(TaskResult.to_json())

# convert the object into a dict
task_result_dict = task_result_instance.to_dict()
# create an instance of TaskResult from a dict
task_result_from_dict = TaskResult.from_dict(task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


