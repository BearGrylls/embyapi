# NameLongIdPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**id** | **int** | The identifier. | [optional] 

## Example

```python
from embyapi.models.name_long_id_pair import NameLongIdPair

# TODO update the JSON string below
json = "{}"
# create an instance of NameLongIdPair from a JSON string
name_long_id_pair_instance = NameLongIdPair.from_json(json)
# print the JSON string representation of the object
print(NameLongIdPair.to_json())

# convert the object into a dict
name_long_id_pair_dict = name_long_id_pair_instance.to_dict()
# create an instance of NameLongIdPair from a dict
name_long_id_pair_from_dict = NameLongIdPair.from_dict(name_long_id_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


