# CodecConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | A value indicating whether the codec is enabled. | [optional] 
**priority** | **int** | The selection priority for the codec.    Higher values mean higher priority. | [optional] 
**codec_id** | **str** | The codec identifier. | [optional] 

## Example

```python
from embyapi.models.codec_configuration import CodecConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CodecConfiguration from a JSON string
codec_configuration_instance = CodecConfiguration.from_json(json)
# print the JSON string representation of the object
print(CodecConfiguration.to_json())

# convert the object into a dict
codec_configuration_dict = codec_configuration_instance.to_dict()
# create an instance of CodecConfiguration from a dict
codec_configuration_from_dict = CodecConfiguration.from_dict(codec_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


