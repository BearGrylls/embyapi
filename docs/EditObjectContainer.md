# EditObjectContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** |  | [optional] 
**default_object** | **object** |  | [optional] 
**type_name** | **str** |  | [optional] 
**editor_root** | [**EditorsEditorRoot**](EditorsEditorRoot.md) |  | [optional] 

## Example

```python
from embyapi.models.edit_object_container import EditObjectContainer

# TODO update the JSON string below
json = "{}"
# create an instance of EditObjectContainer from a JSON string
edit_object_container_instance = EditObjectContainer.from_json(json)
# print the JSON string representation of the object
print(EditObjectContainer.to_json())

# convert the object into a dict
edit_object_container_dict = edit_object_container_instance.to_dict()
# create an instance of EditObjectContainer from a dict
edit_object_container_from_dict = EditObjectContainer.from_dict(edit_object_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


