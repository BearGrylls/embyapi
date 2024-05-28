# UserConfiguration

Class UserConfiguration  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_language_preference** | **str** | The audio language preference. | [optional] 
**play_default_audio_track** | **bool** | A value indicating whether \\[play default audio track\\]. | [optional] 
**subtitle_language_preference** | **str** | The subtitle language preference. | [optional] 
**profile_pin** | **str** |  | [optional] 
**display_missing_episodes** | **bool** |  | [optional] 
**subtitle_mode** | [**SubtitlePlaybackMode**](SubtitlePlaybackMode.md) |  | [optional] 
**ordered_views** | **List[str]** |  | [optional] 
**latest_items_excludes** | **List[str]** |  | [optional] 
**my_media_excludes** | **List[str]** |  | [optional] 
**hide_played_in_latest** | **bool** |  | [optional] 
**hide_played_in_more_like_this** | **bool** |  | [optional] 
**hide_played_in_suggestions** | **bool** |  | [optional] 
**remember_audio_selections** | **bool** |  | [optional] 
**remember_subtitle_selections** | **bool** |  | [optional] 
**enable_next_episode_auto_play** | **bool** |  | [optional] 
**resume_rewind_seconds** | **int** |  | [optional] 
**intro_skip_mode** | [**SegmentSkipMode**](SegmentSkipMode.md) |  | [optional] 
**enable_local_password** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.user_configuration import UserConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfiguration from a JSON string
user_configuration_instance = UserConfiguration.from_json(json)
# print the JSON string representation of the object
print(UserConfiguration.to_json())

# convert the object into a dict
user_configuration_dict = user_configuration_instance.to_dict()
# create an instance of UserConfiguration from a dict
user_configuration_from_dict = UserConfiguration.from_dict(user_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


