# PublicSystemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_address** | **str** | The local address. | [optional] 
**local_addresses** | **List[str]** |  | [optional] 
**wan_address** | **str** | The wan address. | [optional] 
**remote_addresses** | **List[str]** |  | [optional] 
**server_name** | **str** | The name of the server. | [optional] 
**version** | **str** | The version. | [optional] 
**id** | **str** | The id. | [optional] 

## Example

```python
from embyapi.models.public_system_info import PublicSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSystemInfo from a JSON string
public_system_info_instance = PublicSystemInfo.from_json(json)
# print the JSON string representation of the object
print(PublicSystemInfo.to_json())

# convert the object into a dict
public_system_info_dict = public_system_info_instance.to_dict()
# create an instance of PublicSystemInfo from a dict
public_system_info_from_dict = PublicSystemInfo.from_dict(public_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


