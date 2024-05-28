# SyncQualityOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_original_quality** | **bool** |  | [optional] 

## Example

```python
from embyapi.models.sync_quality_option import SyncQualityOption

# TODO update the JSON string below
json = "{}"
# create an instance of SyncQualityOption from a JSON string
sync_quality_option_instance = SyncQualityOption.from_json(json)
# print the JSON string representation of the object
print(SyncQualityOption.to_json())

# convert the object into a dict
sync_quality_option_dict = sync_quality_option_instance.to_dict()
# create an instance of SyncQualityOption from a dict
sync_quality_option_from_dict = SyncQualityOption.from_dict(sync_quality_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


