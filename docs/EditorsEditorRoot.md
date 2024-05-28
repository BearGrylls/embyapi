# EditorsEditorRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_conditions** | [**List[ConditionsPropertyCondition]**](ConditionsPropertyCondition.md) |  | [optional] 
**postback_actions** | [**List[ActionsPostbackAction]**](ActionsPostbackAction.md) |  | [optional] 
**title_button** | [**EditorsEditorButtonItem**](EditorsEditorButtonItem.md) |  | [optional] 
**editor_items** | [**List[EditorsEditorBase]**](EditorsEditorBase.md) |  | [optional] 
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
from embyapi.models.editors_editor_root import EditorsEditorRoot

# TODO update the JSON string below
json = "{}"
# create an instance of EditorsEditorRoot from a JSON string
editors_editor_root_instance = EditorsEditorRoot.from_json(json)
# print the JSON string representation of the object
print(EditorsEditorRoot.to_json())

# convert the object into a dict
editors_editor_root_dict = editors_editor_root_instance.to_dict()
# create an instance of EditorsEditorRoot from a dict
editors_editor_root_from_dict = EditorsEditorRoot.from_dict(editors_editor_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


