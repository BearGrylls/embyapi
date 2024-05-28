# GetDirectoryContents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from embyapi.models.get_directory_contents import GetDirectoryContents

# TODO update the JSON string below
json = "{}"
# create an instance of GetDirectoryContents from a JSON string
get_directory_contents_instance = GetDirectoryContents.from_json(json)
# print the JSON string representation of the object
print(GetDirectoryContents.to_json())

# convert the object into a dict
get_directory_contents_dict = get_directory_contents_instance.to_dict()
# create an instance of GetDirectoryContents from a dict
get_directory_contents_from_dict = GetDirectoryContents.from_dict(get_directory_contents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


