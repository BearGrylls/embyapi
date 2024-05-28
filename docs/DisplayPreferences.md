# DisplayPreferences

Defines the display preferences for any item that supports them (usually Folders)  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id. | [optional] 
**sort_by** | **str** | The sort by. | [optional] 
**custom_prefs** | **Dict[str, str]** | The custom prefs. | [optional] 
**sort_order** | [**SortOrder**](SortOrder.md) |  | [optional] 
**client** | **str** | The client | [optional] 

## Example

```python
from embyapi.models.display_preferences import DisplayPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayPreferences from a JSON string
display_preferences_instance = DisplayPreferences.from_json(json)
# print the JSON string representation of the object
print(DisplayPreferences.to_json())

# convert the object into a dict
display_preferences_dict = display_preferences_instance.to_dict()
# create an instance of DisplayPreferences from a dict
display_preferences_from_dict = DisplayPreferences.from_dict(display_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


