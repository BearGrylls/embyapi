# UserLibraryLeaveSharedItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from embyapi.models.user_library_leave_shared_items import UserLibraryLeaveSharedItems

# TODO update the JSON string below
json = "{}"
# create an instance of UserLibraryLeaveSharedItems from a JSON string
user_library_leave_shared_items_instance = UserLibraryLeaveSharedItems.from_json(json)
# print the JSON string representation of the object
print(UserLibraryLeaveSharedItems.to_json())

# convert the object into a dict
user_library_leave_shared_items_dict = user_library_leave_shared_items_instance.to_dict()
# create an instance of UserLibraryLeaveSharedItems from a dict
user_library_leave_shared_items_from_dict = UserLibraryLeaveSharedItems.from_dict(user_library_leave_shared_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


