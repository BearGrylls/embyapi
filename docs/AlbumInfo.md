# AlbumInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_artists** | **List[str]** | The album artist. | [optional] 
**song_infos** | [**List[SongInfo]**](SongInfo.md) |  | [optional] 
**name** | **str** | The name. | [optional] 
**metadata_language** | **str** | The metadata language. | [optional] 
**metadata_country_code** | **str** | The metadata country code. | [optional] 
**metadata_languages** | [**List[GlobalizationCultureDto]**](GlobalizationCultureDto.md) |  | [optional] 
**provider_ids** | **Dict[str, str]** |  | [optional] 
**year** | **int** | The year. | [optional] 
**index_number** | **int** |  | [optional] 
**parent_index_number** | **int** |  | [optional] 
**premiere_date** | **datetime** |  | [optional] 
**is_automated** | **bool** |  | [optional] 
**enable_adult_metadata** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.album_info import AlbumInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumInfo from a JSON string
album_info_instance = AlbumInfo.from_json(json)
# print the JSON string representation of the object
print(AlbumInfo.to_json())

# convert the object into a dict
album_info_dict = album_info_instance.to_dict()
# create an instance of AlbumInfo from a dict
album_info_from_dict = AlbumInfo.from_dict(album_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


