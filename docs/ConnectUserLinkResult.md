# ConnectUserLinkResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_pending** | **bool** |  | [optional] 
**is_new_user_invitation** | **bool** |  | [optional] 
**guest_display_name** | **str** |  | [optional] 

## Example

```python
from embyapi.models.connect_user_link_result import ConnectUserLinkResult

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectUserLinkResult from a JSON string
connect_user_link_result_instance = ConnectUserLinkResult.from_json(json)
# print the JSON string representation of the object
print(ConnectUserLinkResult.to_json())

# convert the object into a dict
connect_user_link_result_dict = connect_user_link_result_instance.to_dict()
# create an instance of ConnectUserLinkResult from a dict
connect_user_link_result_from_dict = ConnectUserLinkResult.from_dict(connect_user_link_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


