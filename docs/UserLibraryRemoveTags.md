# UserLibraryRemoveTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[NameIdPair]**](NameIdPair.md) |  | [optional] 

## Example

```python
from embyapi.models.user_library_remove_tags import UserLibraryRemoveTags

# TODO update the JSON string below
json = "{}"
# create an instance of UserLibraryRemoveTags from a JSON string
user_library_remove_tags_instance = UserLibraryRemoveTags.from_json(json)
# print the JSON string representation of the object
print(UserLibraryRemoveTags.to_json())

# convert the object into a dict
user_library_remove_tags_dict = user_library_remove_tags_instance.to_dict()
# create an instance of UserLibraryRemoveTags from a dict
user_library_remove_tags_from_dict = UserLibraryRemoveTags.from_dict(user_library_remove_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


