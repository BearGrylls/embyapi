# ConnectConnectAuthenticationExchangeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_user_id** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 

## Example

```python
from embyapi.models.connect_connect_authentication_exchange_result import ConnectConnectAuthenticationExchangeResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectConnectAuthenticationExchangeResult from a JSON string
connect_connect_authentication_exchange_result_instance = ConnectConnectAuthenticationExchangeResult.from_json(json)
# print the JSON string representation of the object
print(ConnectConnectAuthenticationExchangeResult.to_json())

# convert the object into a dict
connect_connect_authentication_exchange_result_dict = connect_connect_authentication_exchange_result_instance.to_dict()
# create an instance of ConnectConnectAuthenticationExchangeResult from a dict
connect_connect_authentication_exchange_result_from_dict = ConnectConnectAuthenticationExchangeResult.from_dict(connect_connect_authentication_exchange_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


