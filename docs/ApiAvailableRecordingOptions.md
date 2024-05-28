# ApiAvailableRecordingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_folders** | [**List[ApiNameIdDescriptionPair]**](ApiNameIdDescriptionPair.md) |  | [optional] 
**movie_recording_folders** | [**List[ApiNameIdDescriptionPair]**](ApiNameIdDescriptionPair.md) |  | [optional] 
**series_recording_folders** | [**List[ApiNameIdDescriptionPair]**](ApiNameIdDescriptionPair.md) |  | [optional] 

## Example

```python
from embyapi.models.api_available_recording_options import ApiAvailableRecordingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAvailableRecordingOptions from a JSON string
api_available_recording_options_instance = ApiAvailableRecordingOptions.from_json(json)
# print the JSON string representation of the object
print(ApiAvailableRecordingOptions.to_json())

# convert the object into a dict
api_available_recording_options_dict = api_available_recording_options_instance.to_dict()
# create an instance of ApiAvailableRecordingOptions from a dict
api_available_recording_options_from_dict = ApiAvailableRecordingOptions.from_dict(api_available_recording_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


