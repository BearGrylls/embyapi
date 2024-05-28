# CollectionsCollectionCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from embyapi.models.collections_collection_creation_result import CollectionsCollectionCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsCollectionCreationResult from a JSON string
collections_collection_creation_result_instance = CollectionsCollectionCreationResult.from_json(json)
# print the JSON string representation of the object
print(CollectionsCollectionCreationResult.to_json())

# convert the object into a dict
collections_collection_creation_result_dict = collections_collection_creation_result_instance.to_dict()
# create an instance of CollectionsCollectionCreationResult from a dict
collections_collection_creation_result_from_dict = CollectionsCollectionCreationResult.from_dict(collections_collection_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


