# BrandingBrandingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_disclaimer** | **str** | The login disclaimer. | [optional] 
**custom_css** | **str** | The custom CSS. | [optional] 

## Example

```python
from embyapi.models.branding_branding_options import BrandingBrandingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingBrandingOptions from a JSON string
branding_branding_options_instance = BrandingBrandingOptions.from_json(json)
# print the JSON string representation of the object
print(BrandingBrandingOptions.to_json())

# convert the object into a dict
branding_branding_options_dict = branding_branding_options_instance.to_dict()
# create an instance of BrandingBrandingOptions from a dict
branding_branding_options_from_dict = BrandingBrandingOptions.from_dict(branding_branding_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


