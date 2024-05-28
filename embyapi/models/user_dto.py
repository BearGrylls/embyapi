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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from embyapi.models.connect_user_link_type import ConnectUserLinkType
from embyapi.models.user_configuration import UserConfiguration
from embyapi.models.user_item_share_level import UserItemShareLevel
from embyapi.models.user_policy import UserPolicy
from typing import Optional, Set
from typing_extensions import Self

class UserDto(BaseModel):
    """
    Class UserDto  
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name.", alias="Name")
    server_id: Optional[StrictStr] = Field(default=None, description="The server identifier.", alias="ServerId")
    server_name: Optional[StrictStr] = Field(default=None, description="The name of the server. This is not used by the server and is for client\\-side usage only.", alias="ServerName")
    prefix: Optional[StrictStr] = Field(default=None, alias="Prefix")
    connect_user_name: Optional[StrictStr] = Field(default=None, description="The name of the connect user.", alias="ConnectUserName")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    connect_link_type: Optional[ConnectUserLinkType] = Field(default=None, alias="ConnectLinkType")
    id: Optional[StrictStr] = Field(default=None, description="The id.", alias="Id")
    primary_image_tag: Optional[StrictStr] = Field(default=None, description="The primary image tag.", alias="PrimaryImageTag")
    has_password: Optional[StrictBool] = Field(default=None, description="A value indicating whether this instance has password.", alias="HasPassword")
    has_configured_password: Optional[StrictBool] = Field(default=None, description="A value indicating whether this instance has configured password.", alias="HasConfiguredPassword")
    enable_auto_login: Optional[StrictBool] = Field(default=None, alias="EnableAutoLogin")
    last_login_date: Optional[datetime] = Field(default=None, description="The last login date.", alias="LastLoginDate")
    last_activity_date: Optional[datetime] = Field(default=None, description="The last activity date.", alias="LastActivityDate")
    configuration: Optional[UserConfiguration] = Field(default=None, alias="Configuration")
    policy: Optional[UserPolicy] = Field(default=None, alias="Policy")
    primary_image_aspect_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The primary image aspect ratio.", alias="PrimaryImageAspectRatio")
    has_configured_easy_password: Optional[StrictBool] = Field(default=None, alias="HasConfiguredEasyPassword")
    user_item_share_level: Optional[UserItemShareLevel] = Field(default=None, alias="UserItemShareLevel")
    __properties: ClassVar[List[str]] = ["Name", "ServerId", "ServerName", "Prefix", "ConnectUserName", "DateCreated", "ConnectLinkType", "Id", "PrimaryImageTag", "HasPassword", "HasConfiguredPassword", "EnableAutoLogin", "LastLoginDate", "LastActivityDate", "Configuration", "Policy", "PrimaryImageAspectRatio", "HasConfiguredEasyPassword", "UserItemShareLevel"]

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
        """Create an instance of UserDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['Configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['Policy'] = self.policy.to_dict()
        # set to None if date_created (nullable) is None
        # and model_fields_set contains the field
        if self.date_created is None and "date_created" in self.model_fields_set:
            _dict['DateCreated'] = None

        # set to None if enable_auto_login (nullable) is None
        # and model_fields_set contains the field
        if self.enable_auto_login is None and "enable_auto_login" in self.model_fields_set:
            _dict['EnableAutoLogin'] = None

        # set to None if last_login_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_login_date is None and "last_login_date" in self.model_fields_set:
            _dict['LastLoginDate'] = None

        # set to None if last_activity_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_activity_date is None and "last_activity_date" in self.model_fields_set:
            _dict['LastActivityDate'] = None

        # set to None if primary_image_aspect_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.primary_image_aspect_ratio is None and "primary_image_aspect_ratio" in self.model_fields_set:
            _dict['PrimaryImageAspectRatio'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "ServerId": obj.get("ServerId"),
            "ServerName": obj.get("ServerName"),
            "Prefix": obj.get("Prefix"),
            "ConnectUserName": obj.get("ConnectUserName"),
            "DateCreated": obj.get("DateCreated"),
            "ConnectLinkType": obj.get("ConnectLinkType"),
            "Id": obj.get("Id"),
            "PrimaryImageTag": obj.get("PrimaryImageTag"),
            "HasPassword": obj.get("HasPassword"),
            "HasConfiguredPassword": obj.get("HasConfiguredPassword"),
            "EnableAutoLogin": obj.get("EnableAutoLogin"),
            "LastLoginDate": obj.get("LastLoginDate"),
            "LastActivityDate": obj.get("LastActivityDate"),
            "Configuration": UserConfiguration.from_dict(obj["Configuration"]) if obj.get("Configuration") is not None else None,
            "Policy": UserPolicy.from_dict(obj["Policy"]) if obj.get("Policy") is not None else None,
            "PrimaryImageAspectRatio": obj.get("PrimaryImageAspectRatio"),
            "HasConfiguredEasyPassword": obj.get("HasConfiguredEasyPassword"),
            "UserItemShareLevel": obj.get("UserItemShareLevel")
        })
        return _obj


