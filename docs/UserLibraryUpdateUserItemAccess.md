# UserLibraryUpdateUserItemAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**item_access** | [**UserItemShareLevel**](UserItemShareLevel.md) |  | [optional] 

## Example

```python
from embyapi.models.user_library_update_user_item_access import UserLibraryUpdateUserItemAccess

# TODO update the JSON string below
json = "{}"
# create an instance of UserLibraryUpdateUserItemAccess from a JSON string
user_library_update_user_item_access_instance = UserLibraryUpdateUserItemAccess.from_json(json)
# print the JSON string representation of the object
print(UserLibraryUpdateUserItemAccess.to_json())

# convert the object into a dict
user_library_update_user_item_access_dict = user_library_update_user_item_access_instance.to_dict()
# create an instance of UserLibraryUpdateUserItemAccess from a dict
user_library_update_user_item_access_from_dict = UserLibraryUpdateUserItemAccess.from_dict(user_library_update_user_item_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


