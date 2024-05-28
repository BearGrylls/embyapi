# LiveTvGuideInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date. | [optional] 
**end_date** | **datetime** | The end date. | [optional] 

## Example

```python
from embyapi.models.live_tv_guide_info import LiveTvGuideInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvGuideInfo from a JSON string
live_tv_guide_info_instance = LiveTvGuideInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvGuideInfo.to_json())

# convert the object into a dict
live_tv_guide_info_dict = live_tv_guide_info_instance.to_dict()
# create an instance of LiveTvGuideInfo from a dict
live_tv_guide_info_from_dict = LiveTvGuideInfo.from_dict(live_tv_guide_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


