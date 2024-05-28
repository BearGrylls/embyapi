# ClientCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playable_media_types** | **List[str]** |  | [optional] 
**supported_commands** | **List[str]** |  | [optional] 
**supports_media_control** | **bool** |  | [optional] 
**push_token** | **str** |  | [optional] 
**push_token_type** | **str** |  | [optional] 
**supports_sync** | **bool** |  | [optional] 
**device_profile** | [**DeviceProfile**](DeviceProfile.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.client_capabilities import ClientCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCapabilities from a JSON string
client_capabilities_instance = ClientCapabilities.from_json(json)
# print the JSON string representation of the object
print(ClientCapabilities.to_json())

# convert the object into a dict
client_capabilities_dict = client_capabilities_instance.to_dict()
# create an instance of ClientCapabilities from a dict
client_capabilities_from_dict = ClientCapabilities.from_dict(client_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


