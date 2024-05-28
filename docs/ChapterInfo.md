# ChapterInfo

Class ChapterInfo  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_position_ticks** | **int** | The start position ticks. | [optional] 
**name** | **str** | The name. | [optional] 
**image_tag** | **str** |  | [optional] 
**marker_type** | [**MarkerType**](MarkerType.md) |  | [optional] 
**chapter_index** | **int** |  | [optional] 

## Example

```python
from embyapi.models.chapter_info import ChapterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterInfo from a JSON string
chapter_info_instance = ChapterInfo.from_json(json)
# print the JSON string representation of the object
print(ChapterInfo.to_json())

# convert the object into a dict
chapter_info_dict = chapter_info_instance.to_dict()
# create an instance of ChapterInfo from a dict
chapter_info_from_dict = ChapterInfo.from_dict(chapter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


