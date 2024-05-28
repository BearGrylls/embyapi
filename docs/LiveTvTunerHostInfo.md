# LiveTvTunerHostInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**setup_url** | **str** |  | [optional] 
**import_favorites_only** | **bool** |  | [optional] 
**prefer_epg_channel_images** | **bool** |  | [optional] 
**prefer_epg_channel_numbers** | **bool** |  | [optional] 
**allow_hw_transcoding** | **bool** |  | [optional] 
**allow_mapping_by_number** | **bool** |  | [optional] 
**import_guide_data** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**tuner_count** | **int** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**referrer** | **str** |  | [optional] 
**provider_options** | **str** |  | [optional] 
**data_version** | **int** |  | [optional] 

## Example

```python
from embyapi.models.live_tv_tuner_host_info import LiveTvTunerHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvTunerHostInfo from a JSON string
live_tv_tuner_host_info_instance = LiveTvTunerHostInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvTunerHostInfo.to_json())

# convert the object into a dict
live_tv_tuner_host_info_dict = live_tv_tuner_host_info_instance.to_dict()
# create an instance of LiveTvTunerHostInfo from a dict
live_tv_tuner_host_info_from_dict = LiveTvTunerHostInfo.from_dict(live_tv_tuner_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


