# SyncTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**id** | **str** | The identifier. | [optional] 

## Example

```python
from embyapi.models.sync_target import SyncTarget

# TODO update the JSON string below
json = "{}"
# create an instance of SyncTarget from a JSON string
sync_target_instance = SyncTarget.from_json(json)
# print the JSON string representation of the object
print(SyncTarget.to_json())

# convert the object into a dict
sync_target_dict = sync_target_instance.to_dict()
# create an instance of SyncTarget from a dict
sync_target_from_dict = SyncTarget.from_dict(sync_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


