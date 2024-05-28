# AuthenticateUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pw** | **str** |  | [optional] 

## Example

```python
from embyapi.models.authenticate_user import AuthenticateUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateUser from a JSON string
authenticate_user_instance = AuthenticateUser.from_json(json)
# print the JSON string representation of the object
print(AuthenticateUser.to_json())

# convert the object into a dict
authenticate_user_dict = authenticate_user_instance.to_dict()
# create an instance of AuthenticateUser from a dict
authenticate_user_from_dict = AuthenticateUser.from_dict(authenticate_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


