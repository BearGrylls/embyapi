# ApiSetChannelMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tuner_channel_id** | **str** |  | [optional] 
**provider_channel_id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.api_set_channel_mapping import ApiSetChannelMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSetChannelMapping from a JSON string
api_set_channel_mapping_instance = ApiSetChannelMapping.from_json(json)
# print the JSON string representation of the object
print(ApiSetChannelMapping.to_json())

# convert the object into a dict
api_set_channel_mapping_dict = api_set_channel_mapping_instance.to_dict()
# create an instance of ApiSetChannelMapping from a dict
api_set_channel_mapping_from_dict = ApiSetChannelMapping.from_dict(api_set_channel_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


