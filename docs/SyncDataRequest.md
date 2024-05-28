# SyncDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_item_ids** | **List[str]** |  | [optional] 
**internal_target_ids** | **List[int]** |  | [optional] 

## Example

```python
from embyapi.models.sync_data_request import SyncDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDataRequest from a JSON string
sync_data_request_instance = SyncDataRequest.from_json(json)
# print the JSON string representation of the object
print(SyncDataRequest.to_json())

# convert the object into a dict
sync_data_request_dict = sync_data_request_instance.to_dict()
# create an instance of SyncDataRequest from a dict
sync_data_request_from_dict = SyncDataRequest.from_dict(sync_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


