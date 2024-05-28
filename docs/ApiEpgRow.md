# ApiEpgRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**programs** | [**List[BaseItemDto]**](BaseItemDto.md) |  | [optional] 

## Example

```python
from embyapi.models.api_epg_row import ApiEpgRow

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEpgRow from a JSON string
api_epg_row_instance = ApiEpgRow.from_json(json)
# print the JSON string representation of the object
print(ApiEpgRow.to_json())

# convert the object into a dict
api_epg_row_dict = api_epg_row_instance.to_dict()
# create an instance of ApiEpgRow from a dict
api_epg_row_from_dict = ApiEpgRow.from_dict(api_epg_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


