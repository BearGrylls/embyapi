# AuthenticationAuthenticationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserDto**](UserDto.md) |  | [optional] 
**session_info** | [**SessionSessionInfo**](SessionSessionInfo.md) |  | [optional] 
**access_token** | **str** | The authentication token. | [optional] 
**server_id** | **str** | The server identifier. | [optional] 

## Example

```python
from embyapi.models.authentication_authentication_result import AuthenticationAuthenticationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationAuthenticationResult from a JSON string
authentication_authentication_result_instance = AuthenticationAuthenticationResult.from_json(json)
# print the JSON string representation of the object
print(AuthenticationAuthenticationResult.to_json())

# convert the object into a dict
authentication_authentication_result_dict = authentication_authentication_result_instance.to_dict()
# create an instance of AuthenticationAuthenticationResult from a dict
authentication_authentication_result_from_dict = AuthenticationAuthenticationResult.from_dict(authentication_authentication_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


