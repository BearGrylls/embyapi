# ProcessRunMetricsProcessStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_cpu** | **float** | The current cpu. | [optional] 
**average_cpu** | **float** | The average cpu. | [optional] 
**current_virtual_memory** | **float** | The currently allocated virtual memory. | [optional] 
**current_working_set** | **float** | The currently allocated working set. | [optional] 
**metrics** | [**List[ProcessRunMetricsProcessMetricPoint]**](ProcessRunMetricsProcessMetricPoint.md) | The metrics. | [optional] 

## Example

```python
from embyapi.models.process_run_metrics_process_statistics import ProcessRunMetricsProcessStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessRunMetricsProcessStatistics from a JSON string
process_run_metrics_process_statistics_instance = ProcessRunMetricsProcessStatistics.from_json(json)
# print the JSON string representation of the object
print(ProcessRunMetricsProcessStatistics.to_json())

# convert the object into a dict
process_run_metrics_process_statistics_dict = process_run_metrics_process_statistics_instance.to_dict()
# create an instance of ProcessRunMetricsProcessStatistics from a dict
process_run_metrics_process_statistics_from_dict = ProcessRunMetricsProcessStatistics.from_dict(process_run_metrics_process_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


