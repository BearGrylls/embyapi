# RemoteImageInfo

Class RemoteImageInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | The name of the provider. | [optional] 
**url** | **str** | The URL. | [optional] 
**thumbnail_url** | **str** | A url used for previewing a smaller version | [optional] 
**height** | **int** | The height. | [optional] 
**width** | **int** | The width. | [optional] 
**community_rating** | **float** | The community rating. | [optional] 
**vote_count** | **int** | The vote count. | [optional] 
**language** | **str** | The language. | [optional] 
**display_language** | **str** |  | [optional] 
**type** | [**ImageType**](ImageType.md) |  | [optional] 
**rating_type** | [**RatingType**](RatingType.md) |  | [optional] 

## Example

```python
from embyapi.models.remote_image_info import RemoteImageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteImageInfo from a JSON string
remote_image_info_instance = RemoteImageInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteImageInfo.to_json())

# convert the object into a dict
remote_image_info_dict = remote_image_info_instance.to_dict()
# create an instance of RemoteImageInfo from a dict
remote_image_info_from_dict = RemoteImageInfo.from_dict(remote_image_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


