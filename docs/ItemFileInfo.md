# ItemFileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ItemFileType**](ItemFileType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**image_type** | [**ImageType**](ImageType.md) |  | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from embyapi.models.item_file_info import ItemFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFileInfo from a JSON string
item_file_info_instance = ItemFileInfo.from_json(json)
# print the JSON string representation of the object
print(ItemFileInfo.to_json())

# convert the object into a dict
item_file_info_dict = item_file_info_instance.to_dict()
# create an instance of ItemFileInfo from a dict
item_file_info_from_dict = ItemFileInfo.from_dict(item_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


