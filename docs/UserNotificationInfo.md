# UserNotificationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifier_key** | **str** |  | [optional] 
**setup_module_url** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**user_ids** | **List[str]** | Limit events based on user ids, for admin notifications | [optional] 
**device_ids** | **List[str]** |  | [optional] 
**library_ids** | **List[str]** |  | [optional] 
**event_ids** | **List[str]** |  | [optional] 
**user_id** | **str** | Notification intended for a specific user | [optional] 
**is_self_notification** | **bool** |  | [optional] 
**group_items** | **bool** |  | [optional] 
**options** | **Dict[str, str]** | This is for webhooks since this will cause xml serialization to fail | [optional] 

## Example

```python
from embyapi.models.user_notification_info import UserNotificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotificationInfo from a JSON string
user_notification_info_instance = UserNotificationInfo.from_json(json)
# print the JSON string representation of the object
print(UserNotificationInfo.to_json())

# convert the object into a dict
user_notification_info_dict = user_notification_info_instance.to_dict()
# create an instance of UserNotificationInfo from a dict
user_notification_info_from_dict = UserNotificationInfo.from_dict(user_notification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


