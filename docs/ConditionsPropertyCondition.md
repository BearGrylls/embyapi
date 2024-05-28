# ConditionsPropertyCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_property_id** | **str** |  | [optional] 
**condition_type** | [**ConditionsPropertyConditionType**](ConditionsPropertyConditionType.md) |  | [optional] 
**target_property_id** | **str** | The target property name or path. | [optional] 
**simple_condition** | [**AttributesSimpleCondition**](AttributesSimpleCondition.md) |  | [optional] 
**value_condition** | [**AttributesValueCondition**](AttributesValueCondition.md) |  | [optional] 
**value** | **object** | The value. | [optional] 

## Example

```python
from embyapi.models.conditions_property_condition import ConditionsPropertyCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsPropertyCondition from a JSON string
conditions_property_condition_instance = ConditionsPropertyCondition.from_json(json)
# print the JSON string representation of the object
print(ConditionsPropertyCondition.to_json())

# convert the object into a dict
conditions_property_condition_dict = conditions_property_condition_instance.to_dict()
# create an instance of ConditionsPropertyCondition from a dict
conditions_property_condition_from_dict = ConditionsPropertyCondition.from_dict(conditions_property_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


