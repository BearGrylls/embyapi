# ApiSetChannelSortIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**management_id** | **str** |  | [optional] 
**new_index** | **int** |  | [optional] 

## Example

```python
from embyapi.models.api_set_channel_sort_index import ApiSetChannelSortIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSetChannelSortIndex from a JSON string
api_set_channel_sort_index_instance = ApiSetChannelSortIndex.from_json(json)
# print the JSON string representation of the object
print(ApiSetChannelSortIndex.to_json())

# convert the object into a dict
api_set_channel_sort_index_dict = api_set_channel_sort_index_instance.to_dict()
# create an instance of ApiSetChannelSortIndex from a dict
api_set_channel_sort_index_from_dict = ApiSetChannelSortIndex.from_dict(api_set_channel_sort_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


