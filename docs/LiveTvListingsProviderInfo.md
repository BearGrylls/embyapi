# LiveTvListingsProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**setup_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**listings_id** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**enabled_tuners** | **List[str]** |  | [optional] 
**enable_all_tuners** | **bool** |  | [optional] 
**news_categories** | **List[str]** |  | [optional] 
**sports_categories** | **List[str]** |  | [optional] 
**kids_categories** | **List[str]** |  | [optional] 
**movie_categories** | **List[str]** |  | [optional] 
**channel_mappings** | [**List[NameValuePair]**](NameValuePair.md) |  | [optional] 
**movie_prefix** | **str** |  | [optional] 
**preferred_language** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 

## Example

```python
from embyapi.models.live_tv_listings_provider_info import LiveTvListingsProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvListingsProviderInfo from a JSON string
live_tv_listings_provider_info_instance = LiveTvListingsProviderInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvListingsProviderInfo.to_json())

# convert the object into a dict
live_tv_listings_provider_info_dict = live_tv_listings_provider_info_instance.to_dict()
# create an instance of LiveTvListingsProviderInfo from a dict
live_tv_listings_provider_info_from_dict = LiveTvListingsProviderInfo.from_dict(live_tv_listings_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


