# UICommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_type** | [**EnumsUICommandType**](EnumsUICommandType.md) |  | [optional] 
**command_id** | **str** |  | [optional] 
**is_visible** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**caption** | **str** |  | [optional] 
**set_focus** | **bool** |  | [optional] 
**confirmation_prompt** | **str** |  | [optional] 

## Example

```python
from embyapi.models.ui_command import UICommand

# TODO update the JSON string below
json = "{}"
# create an instance of UICommand from a JSON string
ui_command_instance = UICommand.from_json(json)
# print the JSON string representation of the object
print(UICommand.to_json())

# convert the object into a dict
ui_command_dict = ui_command_instance.to_dict()
# create an instance of UICommand from a dict
ui_command_from_dict = UICommand.from_dict(ui_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


