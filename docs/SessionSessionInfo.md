# SessionSessionInfo

Class SessionInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_state** | [**PlayerStateInfo**](PlayerStateInfo.md) |  | [optional] 
**additional_users** | [**List[SessionUserInfo]**](SessionUserInfo.md) |  | [optional] 
**remote_end_point** | **str** | The remote end point. | [optional] 
**protocol** | **str** |  | [optional] 
**playable_media_types** | **List[str]** | The playable media types. | [optional] 
**playlist_item_id** | **str** |  | [optional] 
**playlist_index** | **int** |  | [optional] 
**playlist_length** | **int** |  | [optional] 
**id** | **str** | The id. | [optional] 
**server_id** | **str** |  | [optional] 
**user_id** | **str** | The user id. | [optional] 
**user_name** | **str** | The username. | [optional] 
**user_primary_image_tag** | **str** |  | [optional] 
**client** | **str** | The type of the client. | [optional] 
**last_activity_date** | **datetime** | The last activity date. | [optional] 
**device_name** | **str** | The name of the device. | [optional] 
**device_type** | **str** |  | [optional] 
**now_playing_item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**internal_device_id** | **int** |  | [optional] 
**device_id** | **str** | The device id. | [optional] 
**application_version** | **str** | The application version. | [optional] 
**app_icon_url** | **str** | The application icon URL. | [optional] 
**supported_commands** | **List[str]** | The supported commands. | [optional] 
**transcoding_info** | [**TranscodingInfo**](TranscodingInfo.md) |  | [optional] 
**supports_remote_control** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.session_session_info import SessionSessionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSessionInfo from a JSON string
session_session_info_instance = SessionSessionInfo.from_json(json)
# print the JSON string representation of the object
print(SessionSessionInfo.to_json())

# convert the object into a dict
session_session_info_dict = session_session_info_instance.to_dict()
# create an instance of SessionSessionInfo from a dict
session_session_info_from_dict = SessionSessionInfo.from_dict(session_session_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


