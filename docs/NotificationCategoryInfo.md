# NotificationCategoryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**events** | [**List[NotificationTypeInfo]**](NotificationTypeInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.notification_category_info import NotificationCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCategoryInfo from a JSON string
notification_category_info_instance = NotificationCategoryInfo.from_json(json)
# print the JSON string representation of the object
print(NotificationCategoryInfo.to_json())

# convert the object into a dict
notification_category_info_dict = notification_category_info_instance.to_dict()
# create an instance of NotificationCategoryInfo from a dict
notification_category_info_from_dict = NotificationCategoryInfo.from_dict(notification_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


