# EditorsEditorButtonItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editor_type** | [**CommonEditorTypes**](CommonEditorTypes.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**allow_empty** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**is_advanced** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**feature_requires_premiere** | **bool** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.editors_editor_button_item import EditorsEditorButtonItem

# TODO update the JSON string below
json = "{}"
# create an instance of EditorsEditorButtonItem from a JSON string
editors_editor_button_item_instance = EditorsEditorButtonItem.from_json(json)
# print the JSON string representation of the object
print(EditorsEditorButtonItem.to_json())

# convert the object into a dict
editors_editor_button_item_dict = editors_editor_button_item_instance.to_dict()
# create an instance of EditorsEditorButtonItem from a dict
editors_editor_button_item_from_dict = EditorsEditorButtonItem.from_dict(editors_editor_button_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


