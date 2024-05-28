# ServerConfiguration

Represents the server configuration.  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_upn_p** | **bool** | A value indicating whether \\[enable u pn p\\]. | [optional] 
**public_port** | **int** | The public mapped port. | [optional] 
**public_https_port** | **int** | The public HTTPS port. | [optional] 
**http_server_port_number** | **int** | The HTTP server port number. | [optional] 
**https_port_number** | **int** | The HTTPS server port number. | [optional] 
**enable_https** | **bool** | A value indicating whether \\[use HTTPS\\]. | [optional] 
**certificate_path** | **str** | The value pointing to the file system where the ssl certiifcate is located.. | [optional] 
**certificate_password** | **str** |  | [optional] 
**is_port_authorized** | **bool** | A value indicating whether this instance is port authorized. | [optional] 
**auto_run_web_app** | **bool** |  | [optional] 
**enable_remote_access** | **bool** |  | [optional] 
**log_all_query_times** | **bool** |  | [optional] 
**enable_case_sensitive_item_ids** | **bool** | A value indicating whether \\[enable case sensitive item ids\\]. | [optional] 
**metadata_path** | **str** | The metadata path. | [optional] 
**metadata_network_path** | **str** |  | [optional] 
**preferred_metadata_language** | **str** | The preferred metadata language. | [optional] 
**metadata_country_code** | **str** | The metadata country code. | [optional] 
**sort_remove_words** | **List[str]** | Words to be removed from strings to create a sort name | [optional] 
**library_monitor_delay_seconds** | **int** | The delay in seconds that we will wait after a file system change to try and discover what has been added/removed Some delay is necessary with some items because their creation is not atomic.  It involves the creation of several different directories and files. | [optional] 
**enable_dashboard_response_caching** | **bool** | A value indicating whether \\[enable dashboard response caching\\]. Allows potential contributors without visual studio to modify production dashboard code and test changes. | [optional] 
**dashboard_source_path** | **str** | Allows the dashboard to be served from a custom path. | [optional] 
**image_saving_convention** | [**ImageSavingConvention**](ImageSavingConvention.md) |  | [optional] 
**enable_automatic_restart** | **bool** |  | [optional] 
**server_name** | **str** |  | [optional] 
**preferred_detected_remote_address_family** | [**NetSocketsAddressFamily**](NetSocketsAddressFamily.md) |  | [optional] 
**wan_ddns** | **str** |  | [optional] 
**ui_culture** | **str** |  | [optional] 
**remote_client_bitrate_limit** | **int** |  | [optional] 
**local_network_subnets** | **List[str]** |  | [optional] 
**local_network_addresses** | **List[str]** |  | [optional] 
**enable_external_content_in_suggestions** | **bool** |  | [optional] 
**require_https** | **bool** |  | [optional] 
**is_behind_proxy** | **bool** |  | [optional] 
**remote_ip_filter** | **List[str]** |  | [optional] 
**is_remote_ip_filter_blacklist** | **bool** |  | [optional] 
**image_extraction_timeout_ms** | **int** |  | [optional] 
**path_substitutions** | [**List[PathSubstitution]**](PathSubstitution.md) |  | [optional] 
**uninstalled_plugins** | **List[str]** |  | [optional] 
**collapse_video_folders** | **bool** |  | [optional] 
**enable_original_track_titles** | **bool** |  | [optional] 
**vacuum_database_on_startup** | **bool** |  | [optional] 
**simultaneous_stream_limit** | **int** |  | [optional] 
**database_cache_size_mb** | **int** |  | [optional] 
**enable_sq_lite_mmio** | **bool** |  | [optional] 
**playlists_upgraded_to_m3_u** | **bool** |  | [optional] 
**image_extractor_upgraded1** | **bool** |  | [optional] 
**enable_people_letter_sub_folders** | **bool** |  | [optional] 
**optimize_database_on_shutdown** | **bool** |  | [optional] 
**database_analysis_limit** | **int** |  | [optional] 
**disable_async_io** | **bool** |  | [optional] 
**migrated_to_user_item_shares7** | **bool** |  | [optional] 
**migrated_library_options_to_db** | **bool** |  | [optional] 
**allow_legacy_local_network_password** | **bool** |  | [optional] 
**enable_saved_metadata_for_people** | **bool** |  | [optional] 
**tv_channels_refreshed** | **bool** |  | [optional] 
**proxy_header_mode** | [**ProxyHeaderMode**](ProxyHeaderMode.md) |  | [optional] 
**enable_debug_level_logging** | **bool** | A value indicating whether \\[enable debug level logging\\]. | [optional] 
**revert_debug_logging** | **str** |  | [optional] 
**enable_auto_update** | **bool** | Enable automatically and silently updating of the application | [optional] 
**log_file_retention_days** | **int** | The number of days we should retain log files | [optional] 
**run_at_startup** | **bool** | A value indicating whether \\[run at startup\\]. | [optional] 
**is_startup_wizard_completed** | **bool** | A value indicating whether this instance is first run. | [optional] 
**cache_path** | **str** | The cache path. | [optional] 

## Example

```python
from embyapi.models.server_configuration import ServerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfiguration from a JSON string
server_configuration_instance = ServerConfiguration.from_json(json)
# print the JSON string representation of the object
print(ServerConfiguration.to_json())

# convert the object into a dict
server_configuration_dict = server_configuration_instance.to_dict()
# create an instance of ServerConfiguration from a dict
server_configuration_from_dict = ServerConfiguration.from_dict(server_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


