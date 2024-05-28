# ApiNameIdDescriptionPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_overview** | **str** |  | [optional] 
**name** | **str** | The name. | [optional] 
**id** | **str** | The identifier. | [optional] 

## Example

```python
from embyapi.models.api_name_id_description_pair import ApiNameIdDescriptionPair

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNameIdDescriptionPair from a JSON string
api_name_id_description_pair_instance = ApiNameIdDescriptionPair.from_json(json)
# print the JSON string representation of the object
print(ApiNameIdDescriptionPair.to_json())

# convert the object into a dict
api_name_id_description_pair_dict = api_name_id_description_pair_instance.to_dict()
# create an instance of ApiNameIdDescriptionPair from a dict
api_name_id_description_pair_from_dict = ApiNameIdDescriptionPair.from_dict(api_name_id_description_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


