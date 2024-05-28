# RemoteSubtitleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**three_letter_iso_language_name** | **str** | Use language instead to return the language specified by the subtitle provider | [optional] 
**id** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**community_rating** | **float** |  | [optional] 
**download_count** | **int** |  | [optional] 
**is_hash_match** | **bool** |  | [optional] 
**is_forced** | **bool** |  | [optional] 
**is_hearing_impaired** | **bool** |  | [optional] 
**language** | **str** |  | [optional] 

## Example

```python
from embyapi.models.remote_subtitle_info import RemoteSubtitleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSubtitleInfo from a JSON string
remote_subtitle_info_instance = RemoteSubtitleInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteSubtitleInfo.to_json())

# convert the object into a dict
remote_subtitle_info_dict = remote_subtitle_info_instance.to_dict()
# create an instance of RemoteSubtitleInfo from a dict
remote_subtitle_info_from_dict = RemoteSubtitleInfo.from_dict(remote_subtitle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


