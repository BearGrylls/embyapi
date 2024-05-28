# ForgotPasswordPin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** |  | [optional] 

## Example

```python
from embyapi.models.forgot_password_pin import ForgotPasswordPin

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordPin from a JSON string
forgot_password_pin_instance = ForgotPasswordPin.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordPin.to_json())

# convert the object into a dict
forgot_password_pin_dict = forgot_password_pin_instance.to_dict()
# create an instance of ForgotPasswordPin from a dict
forgot_password_pin_from_dict = ForgotPasswordPin.from_dict(forgot_password_pin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


