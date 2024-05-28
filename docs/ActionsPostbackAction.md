# ActionsPostbackAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_editor_id** | **str** |  | [optional] 
**postback_command_id** | **str** |  | [optional] 
**command_parameter_property_id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.actions_postback_action import ActionsPostbackAction

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsPostbackAction from a JSON string
actions_postback_action_instance = ActionsPostbackAction.from_json(json)
# print the JSON string representation of the object
print(ActionsPostbackAction.to_json())

# convert the object into a dict
actions_postback_action_dict = actions_postback_action_instance.to_dict()
# create an instance of ActionsPostbackAction from a dict
actions_postback_action_from_dict = ActionsPostbackAction.from_dict(actions_postback_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


