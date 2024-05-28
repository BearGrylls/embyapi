# NetEndPointInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_local** | **bool** |  | [optional] 
**is_in_network** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.net_end_point_info import NetEndPointInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetEndPointInfo from a JSON string
net_end_point_info_instance = NetEndPointInfo.from_json(json)
# print the JSON string representation of the object
print(NetEndPointInfo.to_json())

# convert the object into a dict
net_end_point_info_dict = net_end_point_info_instance.to_dict()
# create an instance of NetEndPointInfo from a dict
net_end_point_info_from_dict = NetEndPointInfo.from_dict(net_end_point_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


