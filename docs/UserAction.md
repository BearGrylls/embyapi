# UserAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**server_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**type** | [**UserActionType**](UserActionType.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**position_ticks** | **int** |  | [optional] 
**played** | **bool** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.user_action import UserAction

# TODO update the JSON string below
json = "{}"
# create an instance of UserAction from a JSON string
user_action_instance = UserAction.from_json(json)
# print the JSON string representation of the object
print(UserAction.to_json())

# convert the object into a dict
user_action_dict = user_action_instance.to_dict()
# create an instance of UserAction from a dict
user_action_from_dict = UserAction.from_dict(user_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


