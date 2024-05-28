# RokuMetadataApiThumbnailInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_ticks** | **int** |  | [optional] 
**image_tag** | **str** |  | [optional] 

## Example

```python
from embyapi.models.roku_metadata_api_thumbnail_info import RokuMetadataApiThumbnailInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RokuMetadataApiThumbnailInfo from a JSON string
roku_metadata_api_thumbnail_info_instance = RokuMetadataApiThumbnailInfo.from_json(json)
# print the JSON string representation of the object
print(RokuMetadataApiThumbnailInfo.to_json())

# convert the object into a dict
roku_metadata_api_thumbnail_info_dict = roku_metadata_api_thumbnail_info_instance.to_dict()
# create an instance of RokuMetadataApiThumbnailInfo from a dict
roku_metadata_api_thumbnail_info_from_dict = RokuMetadataApiThumbnailInfo.from_dict(roku_metadata_api_thumbnail_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


