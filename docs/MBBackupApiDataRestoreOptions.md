# MBBackupApiDataRestoreOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[MBBackupApiUserRestoreInfo]**](MBBackupApiUserRestoreInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.mb_backup_api_data_restore_options import MBBackupApiDataRestoreOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MBBackupApiDataRestoreOptions from a JSON string
mb_backup_api_data_restore_options_instance = MBBackupApiDataRestoreOptions.from_json(json)
# print the JSON string representation of the object
print(MBBackupApiDataRestoreOptions.to_json())

# convert the object into a dict
mb_backup_api_data_restore_options_dict = mb_backup_api_data_restore_options_instance.to_dict()
# create an instance of MBBackupApiDataRestoreOptions from a dict
mb_backup_api_data_restore_options_from_dict = MBBackupApiDataRestoreOptions.from_dict(mb_backup_api_data_restore_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


