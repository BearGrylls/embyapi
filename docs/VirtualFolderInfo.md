# VirtualFolderInfo

Used to hold information about a user's list of configured virtual folders  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**locations** | **List[str]** | The locations. | [optional] 
**collection_type** | **str** | The type of the collection. | [optional] 
**library_options** | [**LibraryOptions**](LibraryOptions.md) |  | [optional] 
**item_id** | **str** | The item identifier. | [optional] 
**id** | **str** | ItemId came first, so that is left for compatability purposes | [optional] 
**guid** | **str** |  | [optional] 
**primary_image_item_id** | **str** | The primary image item identifier. | [optional] 
**refresh_progress** | **float** |  | [optional] 
**refresh_status** | **str** |  | [optional] 

## Example

```python
from embyapi.models.virtual_folder_info import VirtualFolderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFolderInfo from a JSON string
virtual_folder_info_instance = VirtualFolderInfo.from_json(json)
# print the JSON string representation of the object
print(VirtualFolderInfo.to_json())

# convert the object into a dict
virtual_folder_info_dict = virtual_folder_info_instance.to_dict()
# create an instance of VirtualFolderInfo from a dict
virtual_folder_info_from_dict = VirtualFolderInfo.from_dict(virtual_folder_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


