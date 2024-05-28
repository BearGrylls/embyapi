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
from embyapi.models.device_profile import DeviceProfile
from typing import Optional, Set
from typing_extensions import Self

class ClientCapabilities(BaseModel):
    """
    ClientCapabilities
    """ # noqa: E501
    playable_media_types: Optional[List[StrictStr]] = Field(default=None, alias="PlayableMediaTypes")
    supported_commands: Optional[List[StrictStr]] = Field(default=None, alias="SupportedCommands")
    supports_media_control: Optional[StrictBool] = Field(default=None, alias="SupportsMediaControl")
    push_token: Optional[StrictStr] = Field(default=None, alias="PushToken")
    push_token_type: Optional[StrictStr] = Field(default=None, alias="PushTokenType")
    supports_sync: Optional[StrictBool] = Field(default=None, alias="SupportsSync")
    device_profile: Optional[DeviceProfile] = Field(default=None, alias="DeviceProfile")
    icon_url: Optional[StrictStr] = Field(default=None, alias="IconUrl")
    app_id: Optional[StrictStr] = Field(default=None, alias="AppId")
    __properties: ClassVar[List[str]] = ["PlayableMediaTypes", "SupportedCommands", "SupportsMediaControl", "PushToken", "PushTokenType", "SupportsSync", "DeviceProfile", "IconUrl", "AppId"]

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
        """Create an instance of ClientCapabilities from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device_profile
        if self.device_profile:
            _dict['DeviceProfile'] = self.device_profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientCapabilities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PlayableMediaTypes": obj.get("PlayableMediaTypes"),
            "SupportedCommands": obj.get("SupportedCommands"),
            "SupportsMediaControl": obj.get("SupportsMediaControl"),
            "PushToken": obj.get("PushToken"),
            "PushTokenType": obj.get("PushTokenType"),
            "SupportsSync": obj.get("SupportsSync"),
            "DeviceProfile": DeviceProfile.from_dict(obj["DeviceProfile"]) if obj.get("DeviceProfile") is not None else None,
            "IconUrl": obj.get("IconUrl"),
            "AppId": obj.get("AppId")
        })
        return _obj


