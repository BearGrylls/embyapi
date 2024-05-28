# LibraryPostUpdatedMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[LibraryMediaUpdateInfo]**](LibraryMediaUpdateInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.library_post_updated_media import LibraryPostUpdatedMedia

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryPostUpdatedMedia from a JSON string
library_post_updated_media_instance = LibraryPostUpdatedMedia.from_json(json)
# print the JSON string representation of the object
print(LibraryPostUpdatedMedia.to_json())

# convert the object into a dict
library_post_updated_media_dict = library_post_updated_media_instance.to_dict()
# create an instance of LibraryPostUpdatedMedia from a dict
library_post_updated_media_from_dict = LibraryPostUpdatedMedia.from_dict(library_post_updated_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


