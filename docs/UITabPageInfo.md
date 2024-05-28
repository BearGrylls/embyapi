# UITabPageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**nav_key** | **str** |  | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from embyapi.models.ui_tab_page_info import UITabPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UITabPageInfo from a JSON string
ui_tab_page_info_instance = UITabPageInfo.from_json(json)
# print the JSON string representation of the object
print(UITabPageInfo.to_json())

# convert the object into a dict
ui_tab_page_info_dict = ui_tab_page_info_instance.to_dict()
# create an instance of UITabPageInfo from a dict
ui_tab_page_info_from_dict = UITabPageInfo.from_dict(ui_tab_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


