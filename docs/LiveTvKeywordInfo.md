# LiveTvKeywordInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_type** | [**LiveTvKeywordType**](LiveTvKeywordType.md) |  | [optional] 
**keyword** | **str** |  | [optional] 

## Example

```python
from embyapi.models.live_tv_keyword_info import LiveTvKeywordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvKeywordInfo from a JSON string
live_tv_keyword_info_instance = LiveTvKeywordInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvKeywordInfo.to_json())

# convert the object into a dict
live_tv_keyword_info_dict = live_tv_keyword_info_instance.to_dict()
# create an instance of LiveTvKeywordInfo from a dict
live_tv_keyword_info_from_dict = LiveTvKeywordInfo.from_dict(live_tv_keyword_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


