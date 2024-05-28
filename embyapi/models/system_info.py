# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from embyapi.models.installation_info import InstallationInfo
from embyapi.models.package_version_class import PackageVersionClass
from embyapi.models.wake_on_lan_info import WakeOnLanInfo
from typing import Optional, Set
from typing_extensions import Self

class SystemInfo(BaseModel):
    """
    Class SystemInfo  
    """ # noqa: E501
    system_update_level: Optional[PackageVersionClass] = Field(default=None, alias="SystemUpdateLevel")
    operating_system_display_name: Optional[StrictStr] = Field(default=None, description="The display name of the operating system.", alias="OperatingSystemDisplayName")
    package_name: Optional[StrictStr] = Field(default=None, alias="PackageName")
    has_pending_restart: Optional[StrictBool] = Field(default=None, description="A value indicating whether this instance has pending restart.", alias="HasPendingRestart")
    is_shutting_down: Optional[StrictBool] = Field(default=None, alias="IsShuttingDown")
    has_image_enhancers: Optional[StrictBool] = Field(default=None, alias="HasImageEnhancers")
    operating_system: Optional[StrictStr] = Field(default=None, description="The operating sytem.", alias="OperatingSystem")
    supports_library_monitor: Optional[StrictBool] = Field(default=None, description="A value indicating whether \\[supports library monitor\\].", alias="SupportsLibraryMonitor")
    supports_local_port_configuration: Optional[StrictBool] = Field(default=None, alias="SupportsLocalPortConfiguration")
    supports_wake_server: Optional[StrictBool] = Field(default=None, alias="SupportsWakeServer")
    web_socket_port_number: Optional[StrictInt] = Field(default=None, description="The web socket port number.", alias="WebSocketPortNumber")
    completed_installations: Optional[List[InstallationInfo]] = Field(default=None, description="The completed installations.", alias="CompletedInstallations")
    can_self_restart: Optional[StrictBool] = Field(default=None, description="A value indicating whether this instance can self restart.", alias="CanSelfRestart")
    can_self_update: Optional[StrictBool] = Field(default=None, description="A value indicating whether this instance can self update.", alias="CanSelfUpdate")
    can_launch_web_browser: Optional[StrictBool] = Field(default=None, alias="CanLaunchWebBrowser")
    program_data_path: Optional[StrictStr] = Field(default=None, description="The program data path.", alias="ProgramDataPath")
    items_by_name_path: Optional[StrictStr] = Field(default=None, description="The items by name path.", alias="ItemsByNamePath")
    cache_path: Optional[StrictStr] = Field(default=None, description="The cache path.", alias="CachePath")
    log_path: Optional[StrictStr] = Field(default=None, description="The log path.", alias="LogPath")
    internal_metadata_path: Optional[StrictStr] = Field(default=None, description="The internal metadata path.", alias="InternalMetadataPath")
    transcoding_temp_path: Optional[StrictStr] = Field(default=None, description="The transcoding temporary path.", alias="TranscodingTempPath")
    http_server_port_number: Optional[StrictInt] = Field(default=None, description="The HTTP server port number.", alias="HttpServerPortNumber")
    supports_https: Optional[StrictBool] = Field(default=None, description="A value indicating whether \\[enable HTTPS\\].", alias="SupportsHttps")
    https_port_number: Optional[StrictInt] = Field(default=None, description="The HTTPS server port number.", alias="HttpsPortNumber")
    has_update_available: Optional[StrictBool] = Field(default=None, description="A value indicating whether this instance has update available.", alias="HasUpdateAvailable")
    supports_auto_run_at_startup: Optional[StrictBool] = Field(default=None, description="A value indicating whether \\[supports automatic run at startup\\].", alias="SupportsAutoRunAtStartup")
    hardware_acceleration_requires_premiere: Optional[StrictBool] = Field(default=None, alias="HardwareAccelerationRequiresPremiere")
    wake_on_lan_info: Optional[List[WakeOnLanInfo]] = Field(default=None, alias="WakeOnLanInfo")
    local_address: Optional[StrictStr] = Field(default=None, description="The local address.", alias="LocalAddress")
    local_addresses: Optional[List[StrictStr]] = Field(default=None, alias="LocalAddresses")
    wan_address: Optional[StrictStr] = Field(default=None, description="The wan address.", alias="WanAddress")
    remote_addresses: Optional[List[StrictStr]] = Field(default=None, alias="RemoteAddresses")
    server_name: Optional[StrictStr] = Field(default=None, description="The name of the server.", alias="ServerName")
    version: Optional[StrictStr] = Field(default=None, description="The version.", alias="Version")
    id: Optional[StrictStr] = Field(default=None, description="The id.", alias="Id")
    __properties: ClassVar[List[str]] = ["SystemUpdateLevel", "OperatingSystemDisplayName", "PackageName", "HasPendingRestart", "IsShuttingDown", "HasImageEnhancers", "OperatingSystem", "SupportsLibraryMonitor", "SupportsLocalPortConfiguration", "SupportsWakeServer", "WebSocketPortNumber", "CompletedInstallations", "CanSelfRestart", "CanSelfUpdate", "CanLaunchWebBrowser", "ProgramDataPath", "ItemsByNamePath", "CachePath", "LogPath", "InternalMetadataPath", "TranscodingTempPath", "HttpServerPortNumber", "SupportsHttps", "HttpsPortNumber", "HasUpdateAvailable", "SupportsAutoRunAtStartup", "HardwareAccelerationRequiresPremiere", "WakeOnLanInfo", "LocalAddress", "LocalAddresses", "WanAddress", "RemoteAddresses", "ServerName", "Version", "Id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SystemInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in completed_installations (list)
        _items = []
        if self.completed_installations:
            for _item in self.completed_installations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CompletedInstallations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in wake_on_lan_info (list)
        _items = []
        if self.wake_on_lan_info:
            for _item in self.wake_on_lan_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['WakeOnLanInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "SystemUpdateLevel": obj.get("SystemUpdateLevel"),
            "OperatingSystemDisplayName": obj.get("OperatingSystemDisplayName"),
            "PackageName": obj.get("PackageName"),
            "HasPendingRestart": obj.get("HasPendingRestart"),
            "IsShuttingDown": obj.get("IsShuttingDown"),
            "HasImageEnhancers": obj.get("HasImageEnhancers"),
            "OperatingSystem": obj.get("OperatingSystem"),
            "SupportsLibraryMonitor": obj.get("SupportsLibraryMonitor"),
            "SupportsLocalPortConfiguration": obj.get("SupportsLocalPortConfiguration"),
            "SupportsWakeServer": obj.get("SupportsWakeServer"),
            "WebSocketPortNumber": obj.get("WebSocketPortNumber"),
            "CompletedInstallations": [InstallationInfo.from_dict(_item) for _item in obj["CompletedInstallations"]] if obj.get("CompletedInstallations") is not None else None,
            "CanSelfRestart": obj.get("CanSelfRestart"),
            "CanSelfUpdate": obj.get("CanSelfUpdate"),
            "CanLaunchWebBrowser": obj.get("CanLaunchWebBrowser"),
            "ProgramDataPath": obj.get("ProgramDataPath"),
            "ItemsByNamePath": obj.get("ItemsByNamePath"),
            "CachePath": obj.get("CachePath"),
            "LogPath": obj.get("LogPath"),
            "InternalMetadataPath": obj.get("InternalMetadataPath"),
            "TranscodingTempPath": obj.get("TranscodingTempPath"),
            "HttpServerPortNumber": obj.get("HttpServerPortNumber"),
            "SupportsHttps": obj.get("SupportsHttps"),
            "HttpsPortNumber": obj.get("HttpsPortNumber"),
            "HasUpdateAvailable": obj.get("HasUpdateAvailable"),
            "SupportsAutoRunAtStartup": obj.get("SupportsAutoRunAtStartup"),
            "HardwareAccelerationRequiresPremiere": obj.get("HardwareAccelerationRequiresPremiere"),
            "WakeOnLanInfo": [WakeOnLanInfo.from_dict(_item) for _item in obj["WakeOnLanInfo"]] if obj.get("WakeOnLanInfo") is not None else None,
            "LocalAddress": obj.get("LocalAddress"),
            "LocalAddresses": obj.get("LocalAddresses"),
            "WanAddress": obj.get("WanAddress"),
            "RemoteAddresses": obj.get("RemoteAddresses"),
            "ServerName": obj.get("ServerName"),
            "Version": obj.get("Version"),
            "Id": obj.get("Id")
        })
        return _obj


