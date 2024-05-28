# GenericEditIEditObjectContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** |  | [optional] 
**default_object** | **object** |  | [optional] 
**type_name** | **str** |  | [optional] 

## Example

```python
from embyapi.models.generic_edit_i_edit_object_container import GenericEditIEditObjectContainer

# TODO update the JSON string below
json = "{}"
# create an instance of GenericEditIEditObjectContainer from a JSON string
generic_edit_i_edit_object_container_instance = GenericEditIEditObjectContainer.from_json(json)
# print the JSON string representation of the object
print(GenericEditIEditObjectContainer.to_json())

# convert the object into a dict
generic_edit_i_edit_object_container_dict = generic_edit_i_edit_object_container_instance.to_dict()
# create an instance of GenericEditIEditObjectContainer from a dict
generic_edit_i_edit_object_container_from_dict = GenericEditIEditObjectContainer.from_dict(generic_edit_i_edit_object_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


