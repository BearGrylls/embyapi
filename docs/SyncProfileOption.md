# SyncProfileOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**enable_quality_options** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.sync_profile_option import SyncProfileOption

# TODO update the JSON string below
json = "{}"
# create an instance of SyncProfileOption from a JSON string
sync_profile_option_instance = SyncProfileOption.from_json(json)
# print the JSON string representation of the object
print(SyncProfileOption.to_json())

# convert the object into a dict
sync_profile_option_dict = sync_profile_option_instance.to_dict()
# create an instance of SyncProfileOption from a dict
sync_profile_option_from_dict = SyncProfileOption.from_dict(sync_profile_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


