# UpdateUserPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**new_pw** | **str** |  | [optional] 
**reset_password** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.update_user_password import UpdateUserPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPassword from a JSON string
update_user_password_instance = UpdateUserPassword.from_json(json)
# print the JSON string representation of the object
print(UpdateUserPassword.to_json())

# convert the object into a dict
update_user_password_dict = update_user_password_instance.to_dict()
# create an instance of UpdateUserPassword from a dict
update_user_password_from_dict = UpdateUserPassword.from_dict(update_user_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


