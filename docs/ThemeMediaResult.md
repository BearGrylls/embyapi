# ThemeMediaResult

Class ThemeMediaResult  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **int** | The owner id. | [optional] 
**items** | [**List[BaseItemDto]**](BaseItemDto.md) |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from embyapi.models.theme_media_result import ThemeMediaResult

# TODO update the JSON string below
json = "{}"
# create an instance of ThemeMediaResult from a JSON string
theme_media_result_instance = ThemeMediaResult.from_json(json)
# print the JSON string representation of the object
print(ThemeMediaResult.to_json())

# convert the object into a dict
theme_media_result_dict = theme_media_result_instance.to_dict()
# create an instance of ThemeMediaResult from a dict
theme_media_result_from_dict = ThemeMediaResult.from_dict(theme_media_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


