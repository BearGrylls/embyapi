# PersistenceIntroDebugInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 

## Example

```python
from embyapi.models.persistence_intro_debug_info import PersistenceIntroDebugInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PersistenceIntroDebugInfo from a JSON string
persistence_intro_debug_info_instance = PersistenceIntroDebugInfo.from_json(json)
# print the JSON string representation of the object
print(PersistenceIntroDebugInfo.to_json())

# convert the object into a dict
persistence_intro_debug_info_dict = persistence_intro_debug_info_instance.to_dict()
# create an instance of PersistenceIntroDebugInfo from a dict
persistence_intro_debug_info_from_dict = PersistenceIntroDebugInfo.from_dict(persistence_intro_debug_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


