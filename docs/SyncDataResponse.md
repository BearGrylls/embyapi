# SyncDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids_to_remove** | **List[str]** |  | [optional] 

## Example

```python
from embyapi.models.sync_data_response import SyncDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDataResponse from a JSON string
sync_data_response_instance = SyncDataResponse.from_json(json)
# print the JSON string representation of the object
print(SyncDataResponse.to_json())

# convert the object into a dict
sync_data_response_dict = sync_data_response_instance.to_dict()
# create an instance of SyncDataResponse from a dict
sync_data_response_from_dict = SyncDataResponse.from_dict(sync_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


