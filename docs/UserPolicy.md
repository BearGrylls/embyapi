# UserPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_administrator** | **bool** | A value indicating whether this instance is administrator. | [optional] 
**is_hidden** | **bool** | A value indicating whether this instance is hidden. | [optional] 
**is_hidden_remotely** | **bool** |  | [optional] 
**is_hidden_from_unused_devices** | **bool** |  | [optional] 
**is_disabled** | **bool** | A value indicating whether this instance is disabled. | [optional] 
**locked_out_date** | **int** |  | [optional] 
**max_parental_rating** | **int** | The max parental rating. | [optional] 
**allow_tag_or_rating** | **bool** |  | [optional] 
**blocked_tags** | **List[str]** |  | [optional] 
**is_tag_blocking_mode_inclusive** | **bool** |  | [optional] 
**include_tags** | **List[str]** |  | [optional] 
**enable_user_preference_access** | **bool** |  | [optional] 
**access_schedules** | [**List[AccessSchedule]**](AccessSchedule.md) |  | [optional] 
**block_unrated_items** | [**List[UnratedItem]**](UnratedItem.md) |  | [optional] 
**enable_remote_control_of_other_users** | **bool** |  | [optional] 
**enable_shared_device_control** | **bool** |  | [optional] 
**enable_remote_access** | **bool** |  | [optional] 
**enable_live_tv_management** | **bool** |  | [optional] 
**enable_live_tv_access** | **bool** |  | [optional] 
**enable_media_playback** | **bool** |  | [optional] 
**enable_audio_playback_transcoding** | **bool** |  | [optional] 
**enable_video_playback_transcoding** | **bool** |  | [optional] 
**enable_playback_remuxing** | **bool** |  | [optional] 
**enable_content_deletion** | **bool** |  | [optional] 
**restricted_features** | **List[str]** |  | [optional] 
**enable_content_deletion_from_folders** | **List[str]** |  | [optional] 
**enable_content_downloading** | **bool** |  | [optional] 
**enable_subtitle_downloading** | **bool** |  | [optional] 
**enable_subtitle_management** | **bool** |  | [optional] 
**enable_sync_transcoding** | **bool** | A value indicating whether \\[enable synchronize\\]. | [optional] 
**enable_media_conversion** | **bool** |  | [optional] 
**enabled_channels** | **List[str]** |  | [optional] 
**enable_all_channels** | **bool** |  | [optional] 
**enabled_folders** | **List[str]** |  | [optional] 
**enable_all_folders** | **bool** |  | [optional] 
**invalid_login_attempt_count** | **int** |  | [optional] 
**enable_public_sharing** | **bool** |  | [optional] 
**blocked_media_folders** | **List[str]** |  | [optional] 
**remote_client_bitrate_limit** | **int** |  | [optional] 
**authentication_provider_id** | **str** |  | [optional] 
**excluded_sub_folders** | **List[str]** |  | [optional] 
**simultaneous_stream_limit** | **int** |  | [optional] 
**enabled_devices** | **List[str]** |  | [optional] 
**enable_all_devices** | **bool** |  | [optional] 
**allow_camera_upload** | **bool** |  | [optional] 
**allow_sharing_personal_items** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.user_policy import UserPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UserPolicy from a JSON string
user_policy_instance = UserPolicy.from_json(json)
# print the JSON string representation of the object
print(UserPolicy.to_json())

# convert the object into a dict
user_policy_dict = user_policy_instance.to_dict()
# create an instance of UserPolicy from a dict
user_policy_from_dict = UserPolicy.from_dict(user_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


