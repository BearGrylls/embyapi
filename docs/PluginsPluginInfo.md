# PluginsPluginInfo

This is a serializable stub class that is used by the api to provide information about installed plugins.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**version** | **str** | The version. | [optional] 
**configuration_file_name** | **str** | The name of the configuration file. | [optional] 
**description** | **str** | The description. | [optional] 
**id** | **str** | The unique id. | [optional] 
**image_tag** | **str** | The image URL. | [optional] 

## Example

```python
from embyapi.models.plugins_plugin_info import PluginsPluginInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PluginsPluginInfo from a JSON string
plugins_plugin_info_instance = PluginsPluginInfo.from_json(json)
# print the JSON string representation of the object
print(PluginsPluginInfo.to_json())

# convert the object into a dict
plugins_plugin_info_dict = plugins_plugin_info_instance.to_dict()
# create an instance of PluginsPluginInfo from a dict
plugins_plugin_info_from_dict = PluginsPluginInfo.from_dict(plugins_plugin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


