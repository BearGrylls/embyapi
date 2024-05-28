# FeatureInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**feature_type** | [**FeatureType**](FeatureType.md) |  | [optional] 

## Example

```python
from embyapi.models.feature_info import FeatureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureInfo from a JSON string
feature_info_instance = FeatureInfo.from_json(json)
# print the JSON string representation of the object
print(FeatureInfo.to_json())

# convert the object into a dict
feature_info_dict = feature_info_instance.to_dict()
# create an instance of FeatureInfo from a dict
feature_info_from_dict = FeatureInfo.from_dict(feature_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


