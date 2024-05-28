# BitRate

A type for handling bit rates.      The purpose of this type is to avoid manual calculations and conversions in code,             unified handling and conversion as well as presentation through its various To\\*\\*\\*String methods.      `System.IComparable`      `System.IEquatable`1`  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bps** | **int** |  | [optional] 
**kbps** | **float** |  | [optional] 
**mbps** | **float** |  | [optional] 

## Example

```python
from embyapi.models.bit_rate import BitRate

# TODO update the JSON string below
json = "{}"
# create an instance of BitRate from a JSON string
bit_rate_instance = BitRate.from_json(json)
# print the JSON string representation of the object
print(BitRate.to_json())

# convert the object into a dict
bit_rate_dict = bit_rate_instance.to_dict()
# create an instance of BitRate from a dict
bit_rate_from_dict = BitRate.from_dict(bit_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


