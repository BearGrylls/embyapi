# ApiListingProviderTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**setup_url** | **str** |  | [optional] 

## Example

```python
from embyapi.models.api_listing_provider_type_info import ApiListingProviderTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiListingProviderTypeInfo from a JSON string
api_listing_provider_type_info_instance = ApiListingProviderTypeInfo.from_json(json)
# print the JSON string representation of the object
print(ApiListingProviderTypeInfo.to_json())

# convert the object into a dict
api_listing_provider_type_info_dict = api_listing_provider_type_info_instance.to_dict()
# create an instance of ApiListingProviderTypeInfo from a dict
api_listing_provider_type_info_from_dict = ApiListingProviderTypeInfo.from_dict(api_listing_provider_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


