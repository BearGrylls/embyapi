# ApiSetChannelDisabled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**management_id** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.api_set_channel_disabled import ApiSetChannelDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSetChannelDisabled from a JSON string
api_set_channel_disabled_instance = ApiSetChannelDisabled.from_json(json)
# print the JSON string representation of the object
print(ApiSetChannelDisabled.to_json())

# convert the object into a dict
api_set_channel_disabled_dict = api_set_channel_disabled_instance.to_dict()
# create an instance of ApiSetChannelDisabled from a dict
api_set_channel_disabled_from_dict = ApiSetChannelDisabled.from_dict(api_set_channel_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


