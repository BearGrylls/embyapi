# UserDto

Class UserDto  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**server_id** | **str** | The server identifier. | [optional] 
**server_name** | **str** | The name of the server. This is not used by the server and is for client\\-side usage only. | [optional] 
**prefix** | **str** |  | [optional] 
**connect_user_name** | **str** | The name of the connect user. | [optional] 
**date_created** | **datetime** |  | [optional] 
**connect_link_type** | [**ConnectUserLinkType**](ConnectUserLinkType.md) |  | [optional] 
**id** | **str** | The id. | [optional] 
**primary_image_tag** | **str** | The primary image tag. | [optional] 
**has_password** | **bool** | A value indicating whether this instance has password. | [optional] 
**has_configured_password** | **bool** | A value indicating whether this instance has configured password. | [optional] 
**enable_auto_login** | **bool** |  | [optional] 
**last_login_date** | **datetime** | The last login date. | [optional] 
**last_activity_date** | **datetime** | The last activity date. | [optional] 
**configuration** | [**UserConfiguration**](UserConfiguration.md) |  | [optional] 
**policy** | [**UserPolicy**](UserPolicy.md) |  | [optional] 
**primary_image_aspect_ratio** | **float** | The primary image aspect ratio. | [optional] 
**has_configured_easy_password** | **bool** |  | [optional] 
**user_item_share_level** | [**UserItemShareLevel**](UserItemShareLevel.md) |  | [optional] 

## Example

```python
from embyapi.models.user_dto import UserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserDto from a JSON string
user_dto_instance = UserDto.from_json(json)
# print the JSON string representation of the object
print(UserDto.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDto from a dict
user_dto_from_dict = UserDto.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


