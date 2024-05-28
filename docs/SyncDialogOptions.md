# SyncDialogOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**List[SyncTarget]**](SyncTarget.md) |  | [optional] 
**options** | [**List[SyncJobOption]**](SyncJobOption.md) |  | [optional] 
**quality_options** | [**List[SyncQualityOption]**](SyncQualityOption.md) |  | [optional] 
**profile_options** | [**List[SyncProfileOption]**](SyncProfileOption.md) |  | [optional] 

## Example

```python
from embyapi.models.sync_dialog_options import SyncDialogOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SyncDialogOptions from a JSON string
sync_dialog_options_instance = SyncDialogOptions.from_json(json)
# print the JSON string representation of the object
print(SyncDialogOptions.to_json())

# convert the object into a dict
sync_dialog_options_dict = sync_dialog_options_instance.to_dict()
# create an instance of SyncDialogOptions from a dict
sync_dialog_options_from_dict = SyncDialogOptions.from_dict(sync_dialog_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


