# CommonPluginsIPlugin

Interface IPlugin  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the plugin | [optional] 
**description** | **str** | The description. | [optional] 
**id** | **str** | The unique id. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**assembly_file_path** | **str** | The path to the assembly file | [optional] 
**data_folder_path** | **str** | The full path to the data folder, where the plugin can store any miscellaneous files needed | [optional] 

## Example

```python
from embyapi.models.common_plugins_i_plugin import CommonPluginsIPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPluginsIPlugin from a JSON string
common_plugins_i_plugin_instance = CommonPluginsIPlugin.from_json(json)
# print the JSON string representation of the object
print(CommonPluginsIPlugin.to_json())

# convert the object into a dict
common_plugins_i_plugin_dict = common_plugins_i_plugin_instance.to_dict()
# create an instance of CommonPluginsIPlugin from a dict
common_plugins_i_plugin_from_dict = CommonPluginsIPlugin.from_dict(common_plugins_i_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


