# MBBackupBackupInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_version** | **str** |  | [optional] 
**plugin_version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**can_restore** | **bool** |  | [optional] 
**is_full_backup** | **bool** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**users** | [**List[NameIdPair]**](NameIdPair.md) |  | [optional] 

## Example

```python
from embyapi.models.mb_backup_backup_info import MBBackupBackupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MBBackupBackupInfo from a JSON string
mb_backup_backup_info_instance = MBBackupBackupInfo.from_json(json)
# print the JSON string representation of the object
print(MBBackupBackupInfo.to_json())

# convert the object into a dict
mb_backup_backup_info_dict = mb_backup_backup_info_instance.to_dict()
# create an instance of MBBackupBackupInfo from a dict
mb_backup_backup_info_from_dict = MBBackupBackupInfo.from_dict(mb_backup_backup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


