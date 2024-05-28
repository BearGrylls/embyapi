# ValidatePath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validate_writeable** | **bool** |  | [optional] 
**is_file** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from embyapi.models.validate_path import ValidatePath

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePath from a JSON string
validate_path_instance = ValidatePath.from_json(json)
# print the JSON string representation of the object
print(ValidatePath.to_json())

# convert the object into a dict
validate_path_dict = validate_path_instance.to_dict()
# create an instance of ValidatePath from a dict
validate_path_from_dict = ValidatePath.from_dict(validate_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


