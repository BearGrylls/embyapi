# MBBackupApiRestoreOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restore_server_id** | **bool** |  | [optional] 
**use_files** | **str** |  | [optional] 

## Example

```python
from embyapi.models.mb_backup_api_restore_options import MBBackupApiRestoreOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MBBackupApiRestoreOptions from a JSON string
mb_backup_api_restore_options_instance = MBBackupApiRestoreOptions.from_json(json)
# print the JSON string representation of the object
print(MBBackupApiRestoreOptions.to_json())

# convert the object into a dict
mb_backup_api_restore_options_dict = mb_backup_api_restore_options_instance.to_dict()
# create an instance of MBBackupApiRestoreOptions from a dict
mb_backup_api_restore_options_from_dict = MBBackupApiRestoreOptions.from_dict(mb_backup_api_restore_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


