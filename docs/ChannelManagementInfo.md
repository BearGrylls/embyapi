# ChannelManagementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from embyapi.models.channel_management_info import ChannelManagementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelManagementInfo from a JSON string
channel_management_info_instance = ChannelManagementInfo.from_json(json)
# print the JSON string representation of the object
print(ChannelManagementInfo.to_json())

# convert the object into a dict
channel_management_info_dict = channel_management_info_instance.to_dict()
# create an instance of ChannelManagementInfo from a dict
channel_management_info_from_dict = ChannelManagementInfo.from_dict(channel_management_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


