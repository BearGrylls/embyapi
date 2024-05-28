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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserNotificationInfo(BaseModel):
    """
    UserNotificationInfo
    """ # noqa: E501
    notifier_key: Optional[StrictStr] = Field(default=None, alias="NotifierKey")
    setup_module_url: Optional[StrictStr] = Field(default=None, alias="SetupModuleUrl")
    service_name: Optional[StrictStr] = Field(default=None, alias="ServiceName")
    plugin_id: Optional[StrictStr] = Field(default=None, alias="PluginId")
    friendly_name: Optional[StrictStr] = Field(default=None, alias="FriendlyName")
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    enabled: Optional[StrictBool] = Field(default=None, alias="Enabled")
    user_ids: Optional[List[StrictStr]] = Field(default=None, description="Limit events based on user ids, for admin notifications", alias="UserIds")
    device_ids: Optional[List[StrictStr]] = Field(default=None, alias="DeviceIds")
    library_ids: Optional[List[StrictStr]] = Field(default=None, alias="LibraryIds")
    event_ids: Optional[List[StrictStr]] = Field(default=None, alias="EventIds")
    user_id: Optional[StrictStr] = Field(default=None, description="Notification intended for a specific user", alias="UserId")
    is_self_notification: Optional[StrictBool] = Field(default=None, alias="IsSelfNotification")
    group_items: Optional[StrictBool] = Field(default=None, alias="GroupItems")
    options: Optional[Dict[str, StrictStr]] = Field(default=None, description="This is for webhooks since this will cause xml serialization to fail", alias="Options")
    __properties: ClassVar[List[str]] = ["NotifierKey", "SetupModuleUrl", "ServiceName", "PluginId", "FriendlyName", "Id", "Enabled", "UserIds", "DeviceIds", "LibraryIds", "EventIds", "UserId", "IsSelfNotification", "GroupItems", "Options"]

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
        """Create an instance of UserNotificationInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserNotificationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NotifierKey": obj.get("NotifierKey"),
            "SetupModuleUrl": obj.get("SetupModuleUrl"),
            "ServiceName": obj.get("ServiceName"),
            "PluginId": obj.get("PluginId"),
            "FriendlyName": obj.get("FriendlyName"),
            "Id": obj.get("Id"),
            "Enabled": obj.get("Enabled"),
            "UserIds": obj.get("UserIds"),
            "DeviceIds": obj.get("DeviceIds"),
            "LibraryIds": obj.get("LibraryIds"),
            "EventIds": obj.get("EventIds"),
            "UserId": obj.get("UserId"),
            "IsSelfNotification": obj.get("IsSelfNotification"),
            "GroupItems": obj.get("GroupItems"),
            "Options": obj.get("Options")
        })
        return _obj


