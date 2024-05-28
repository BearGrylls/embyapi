# ResolutionWithRate

Struct representing a combination of video resolution and frame rate.      `System.IEquatable`1`  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | The resolution width. | [optional] 
**height** | **int** | The resolution height. | [optional] 
**frame_rate** | **float** | The frame rate in frames/second (fps). | [optional] 
**resolution** | [**Resolution**](Resolution.md) |  | [optional] 

## Example

```python
from embyapi.models.resolution_with_rate import ResolutionWithRate

# TODO update the JSON string below
json = "{}"
# create an instance of ResolutionWithRate from a JSON string
resolution_with_rate_instance = ResolutionWithRate.from_json(json)
# print the JSON string representation of the object
print(ResolutionWithRate.to_json())

# convert the object into a dict
resolution_with_rate_dict = resolution_with_rate_instance.to_dict()
# create an instance of ResolutionWithRate from a dict
resolution_with_rate_from_dict = ResolutionWithRate.from_dict(resolution_with_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


