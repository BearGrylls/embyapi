# RokuMetadataApiThumbnailSetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] 
**thumbnails** | [**List[RokuMetadataApiThumbnailInfo]**](RokuMetadataApiThumbnailInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.roku_metadata_api_thumbnail_set_info import RokuMetadataApiThumbnailSetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RokuMetadataApiThumbnailSetInfo from a JSON string
roku_metadata_api_thumbnail_set_info_instance = RokuMetadataApiThumbnailSetInfo.from_json(json)
# print the JSON string representation of the object
print(RokuMetadataApiThumbnailSetInfo.to_json())

# convert the object into a dict
roku_metadata_api_thumbnail_set_info_dict = roku_metadata_api_thumbnail_set_info_instance.to_dict()
# create an instance of RokuMetadataApiThumbnailSetInfo from a dict
roku_metadata_api_thumbnail_set_info_from_dict = RokuMetadataApiThumbnailSetInfo.from_dict(roku_metadata_api_thumbnail_set_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


