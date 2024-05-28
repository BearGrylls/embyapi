# RemoteImageResult

Class RemoteImageResult.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[RemoteImageInfo]**](RemoteImageInfo.md) | The images. | [optional] 
**total_record_count** | **int** | The total record count. | [optional] 
**providers** | **List[str]** | The providers. | [optional] 

## Example

```python
from embyapi.models.remote_image_result import RemoteImageResult

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteImageResult from a JSON string
remote_image_result_instance = RemoteImageResult.from_json(json)
# print the JSON string representation of the object
print(RemoteImageResult.to_json())

# convert the object into a dict
remote_image_result_dict = remote_image_result_instance.to_dict()
# create an instance of RemoteImageResult from a dict
remote_image_result_from_dict = RemoteImageResult.from_dict(remote_image_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


