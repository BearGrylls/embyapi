# WakeOnLanInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** |  | [optional] 
**broadcast_address** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from embyapi.models.wake_on_lan_info import WakeOnLanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WakeOnLanInfo from a JSON string
wake_on_lan_info_instance = WakeOnLanInfo.from_json(json)
# print the JSON string representation of the object
print(WakeOnLanInfo.to_json())

# convert the object into a dict
wake_on_lan_info_dict = wake_on_lan_info_instance.to_dict()
# create an instance of WakeOnLanInfo from a dict
wake_on_lan_info_from_dict = WakeOnLanInfo.from_dict(wake_on_lan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


