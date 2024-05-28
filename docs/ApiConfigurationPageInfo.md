# ApiConfigurationPageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enable_in_main_menu** | **bool** |  | [optional] 
**enable_in_user_menu** | **bool** |  | [optional] 
**feature_id** | **str** |  | [optional] 
**menu_section** | **str** |  | [optional] 
**menu_icon** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**configuration_page_type** | [**PluginsConfigurationPageType**](PluginsConfigurationPageType.md) |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**nav_menu_id** | **str** |  | [optional] 
**plugin** | [**CommonPluginsIPlugin**](CommonPluginsIPlugin.md) |  | [optional] 
**translations** | **List[str]** |  | [optional] 

## Example

```python
from embyapi.models.api_configuration_page_info import ApiConfigurationPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigurationPageInfo from a JSON string
api_configuration_page_info_instance = ApiConfigurationPageInfo.from_json(json)
# print the JSON string representation of the object
print(ApiConfigurationPageInfo.to_json())

# convert the object into a dict
api_configuration_page_info_dict = api_configuration_page_info_instance.to_dict()
# create an instance of ApiConfigurationPageInfo from a dict
api_configuration_page_info_from_dict = ApiConfigurationPageInfo.from_dict(api_configuration_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


