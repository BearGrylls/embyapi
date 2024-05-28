# RunUICommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** |  | [optional] 
**command_id** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**client_locale** | **str** |  | [optional] 

## Example

```python
from embyapi.models.run_ui_command import RunUICommand

# TODO update the JSON string below
json = "{}"
# create an instance of RunUICommand from a JSON string
run_ui_command_instance = RunUICommand.from_json(json)
# print the JSON string representation of the object
print(RunUICommand.to_json())

# convert the object into a dict
run_ui_command_dict = run_ui_command_instance.to_dict()
# create an instance of RunUICommand from a dict
run_ui_command_from_dict = RunUICommand.from_dict(run_ui_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


