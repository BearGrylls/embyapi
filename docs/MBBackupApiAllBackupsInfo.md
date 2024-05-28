# MBBackupApiAllBackupsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_backup_info** | [**MBBackupBackupInfo**](MBBackupBackupInfo.md) |  | [optional] 
**light_backups** | [**List[MBBackupBackupInfo]**](MBBackupBackupInfo.md) |  | [optional] 

## Example

```python
from embyapi.models.mb_backup_api_all_backups_info import MBBackupApiAllBackupsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MBBackupApiAllBackupsInfo from a JSON string
mb_backup_api_all_backups_info_instance = MBBackupApiAllBackupsInfo.from_json(json)
# print the JSON string representation of the object
print(MBBackupApiAllBackupsInfo.to_json())

# convert the object into a dict
mb_backup_api_all_backups_info_dict = mb_backup_api_all_backups_info_instance.to_dict()
# create an instance of MBBackupApiAllBackupsInfo from a dict
mb_backup_api_all_backups_info_from_dict = MBBackupApiAllBackupsInfo.from_dict(mb_backup_api_all_backups_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


