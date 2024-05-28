# LiveTvLiveTvInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | A value indicating whether this instance is enabled. | [optional] 
**enabled_users** | **List[str]** | The enabled users. | [optional] 

## Example

```python
from embyapi.models.live_tv_live_tv_info import LiveTvLiveTvInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvLiveTvInfo from a JSON string
live_tv_live_tv_info_instance = LiveTvLiveTvInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvLiveTvInfo.to_json())

# convert the object into a dict
live_tv_live_tv_info_dict = live_tv_live_tv_info_instance.to_dict()
# create an instance of LiveTvLiveTvInfo from a dict
live_tv_live_tv_info_from_dict = LiveTvLiveTvInfo.from_dict(live_tv_live_tv_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


