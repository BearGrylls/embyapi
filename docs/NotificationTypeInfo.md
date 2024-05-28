# NotificationTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.notification_type_info import NotificationTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTypeInfo from a JSON string
notification_type_info_instance = NotificationTypeInfo.from_json(json)
# print the JSON string representation of the object
print(NotificationTypeInfo.to_json())

# convert the object into a dict
notification_type_info_dict = notification_type_info_instance.to_dict()
# create an instance of NotificationTypeInfo from a dict
notification_type_info_from_dict = NotificationTypeInfo.from_dict(notification_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


