# Resolution

Struct representing a video resolution specified in X and Y dimension.      `System.IComparable`      `System.IEquatable`1`  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | The resolution width. | [optional] 
**height** | **int** | The resolution height. | [optional] 

## Example

```python
from embyapi.models.resolution import Resolution

# TODO update the JSON string below
json = "{}"
# create an instance of Resolution from a JSON string
resolution_instance = Resolution.from_json(json)
# print the JSON string representation of the object
print(Resolution.to_json())

# convert the object into a dict
resolution_dict = resolution_instance.to_dict()
# create an instance of Resolution from a dict
resolution_from_dict = Resolution.from_dict(resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


