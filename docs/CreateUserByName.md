# CreateUserByName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**copy_from_user_id** | **str** |  | [optional] 
**user_copy_options** | [**List[LibraryUserCopyOptions]**](LibraryUserCopyOptions.md) |  | [optional] 

## Example

```python
from embyapi.models.create_user_by_name import CreateUserByName

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserByName from a JSON string
create_user_by_name_instance = CreateUserByName.from_json(json)
# print the JSON string representation of the object
print(CreateUserByName.to_json())

# convert the object into a dict
create_user_by_name_dict = create_user_by_name_instance.to_dict()
# create an instance of CreateUserByName from a dict
create_user_by_name_from_dict = CreateUserByName.from_dict(create_user_by_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


