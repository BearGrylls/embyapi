# BookInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_name** | **str** |  | [optional] 
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
from embyapi.models.book_info import BookInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BookInfo from a JSON string
book_info_instance = BookInfo.from_json(json)
# print the JSON string representation of the object
print(BookInfo.to_json())

# convert the object into a dict
book_info_dict = book_info_instance.to_dict()
# create an instance of BookInfo from a dict
book_info_from_dict = BookInfo.from_dict(book_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


