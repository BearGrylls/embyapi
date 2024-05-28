# BaseItemPerson

This is used by the api to get information about a Person within a BaseItem  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name. | [optional] 
**id** | **str** | The identifier. | [optional] 
**role** | **str** | The role. | [optional] 
**type** | [**PersonType**](PersonType.md) |  | [optional] 
**primary_image_tag** | **str** | The primary image tag. | [optional] 

## Example

```python
from embyapi.models.base_item_person import BaseItemPerson

# TODO update the JSON string below
json = "{}"
# create an instance of BaseItemPerson from a JSON string
base_item_person_instance = BaseItemPerson.from_json(json)
# print the JSON string representation of the object
print(BaseItemPerson.to_json())

# convert the object into a dict
base_item_person_dict = base_item_person_instance.to_dict()
# create an instance of BaseItemPerson from a dict
base_item_person_from_dict = BaseItemPerson.from_dict(base_item_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


