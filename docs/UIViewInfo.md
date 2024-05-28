# UIViewInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** |  | [optional] 
**page_id** | **str** |  | [optional] 
**caption** | **str** |  | [optional] 
**sub_caption** | **str** |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**view_type** | [**EnumsUIViewType**](EnumsUIViewType.md) |  | [optional] 
**show_dialog_full_screen** | **bool** |  | [optional] 
**is_in_sequence** | **bool** |  | [optional] 
**redirect_view_url** | **str** |  | [optional] 
**edit_object_container** | [**GenericEditIEditObjectContainer**](GenericEditIEditObjectContainer.md) |  | [optional] 
**commands** | [**List[UICommand]**](UICommand.md) |  | [optional] 
**tab_page_infos** | [**List[UITabPageInfo]**](UITabPageInfo.md) |  | [optional] 
**is_page_change_info** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.ui_view_info import UIViewInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UIViewInfo from a JSON string
ui_view_info_instance = UIViewInfo.from_json(json)
# print the JSON string representation of the object
print(UIViewInfo.to_json())

# convert the object into a dict
ui_view_info_dict = ui_view_info_instance.to_dict()
# create an instance of UIViewInfo from a dict
ui_view_info_from_dict = UIViewInfo.from_dict(ui_view_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


