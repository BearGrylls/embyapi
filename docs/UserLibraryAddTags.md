# UserLibraryAddTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[NameIdPair]**](NameIdPair.md) |  | [optional] 

## Example

```python
from embyapi.models.user_library_add_tags import UserLibraryAddTags

# TODO update the JSON string below
json = "{}"
# create an instance of UserLibraryAddTags from a JSON string
user_library_add_tags_instance = UserLibraryAddTags.from_json(json)
# print the JSON string representation of the object
print(UserLibraryAddTags.to_json())

# convert the object into a dict
user_library_add_tags_dict = user_library_add_tags_instance.to_dict()
# create an instance of UserLibraryAddTags from a dict
user_library_add_tags_from_dict = UserLibraryAddTags.from_dict(user_library_add_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


