# ApiTagItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.api_tag_item import ApiTagItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTagItem from a JSON string
api_tag_item_instance = ApiTagItem.from_json(json)
# print the JSON string representation of the object
print(ApiTagItem.to_json())

# convert the object into a dict
api_tag_item_dict = api_tag_item_instance.to_dict()
# create an instance of ApiTagItem from a dict
api_tag_item_from_dict = ApiTagItem.from_dict(api_tag_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


