# UserLibraryTagItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.user_library_tag_item import UserLibraryTagItem

# TODO update the JSON string below
json = "{}"
# create an instance of UserLibraryTagItem from a JSON string
user_library_tag_item_instance = UserLibraryTagItem.from_json(json)
# print the JSON string representation of the object
print(UserLibraryTagItem.to_json())

# convert the object into a dict
user_library_tag_item_dict = user_library_tag_item_instance.to_dict()
# create an instance of UserLibraryTagItem from a dict
user_library_tag_item_from_dict = UserLibraryTagItem.from_dict(user_library_tag_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


