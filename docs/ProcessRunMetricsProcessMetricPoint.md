# ProcessRunMetricsProcessMetricPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** | The time. | [optional] 
**cpu_percent** | **float** | The cpu percent. | [optional] 
**virtual_memory** | **float** | The virtual memory. | [optional] 
**working_set** | **float** | The working set. | [optional] 

## Example

```python
from embyapi.models.process_run_metrics_process_metric_point import ProcessRunMetricsProcessMetricPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessRunMetricsProcessMetricPoint from a JSON string
process_run_metrics_process_metric_point_instance = ProcessRunMetricsProcessMetricPoint.from_json(json)
# print the JSON string representation of the object
print(ProcessRunMetricsProcessMetricPoint.to_json())

# convert the object into a dict
process_run_metrics_process_metric_point_dict = process_run_metrics_process_metric_point_instance.to_dict()
# create an instance of ProcessRunMetricsProcessMetricPoint from a dict
process_run_metrics_process_metric_point_from_dict = ProcessRunMetricsProcessMetricPoint.from_dict(process_run_metrics_process_metric_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


