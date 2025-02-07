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
from embyapi.models.sync_category import SyncCategory
from embyapi.models.sync_job_status import SyncJobStatus
from typing import Optional, Set
from typing_extensions import Self

class SyncJob(BaseModel):
    """
    SyncJob
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The identifier.", alias="Id")
    target_id: Optional[StrictStr] = Field(default=None, description="The device identifier.", alias="TargetId")
    internal_target_id: Optional[StrictInt] = Field(default=None, alias="InternalTargetId")
    target_name: Optional[StrictStr] = Field(default=None, description="The name of the target.", alias="TargetName")
    quality: Optional[StrictStr] = Field(default=None, description="The quality.", alias="Quality")
    bitrate: Optional[StrictInt] = Field(default=None, description="The bitrate.", alias="Bitrate")
    container: Optional[StrictStr] = Field(default=None, alias="Container")
    video_codec: Optional[StrictStr] = Field(default=None, alias="VideoCodec")
    audio_codec: Optional[StrictStr] = Field(default=None, alias="AudioCodec")
    profile: Optional[StrictStr] = Field(default=None, description="The profile.", alias="Profile")
    category: Optional[SyncCategory] = Field(default=None, alias="Category")
    parent_id: Optional[StrictInt] = Field(default=None, description="The parent identifier.", alias="ParentId")
    progress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current progress.", alias="Progress")
    name: Optional[StrictStr] = Field(default=None, description="The name.", alias="Name")
    status: Optional[SyncJobStatus] = Field(default=None, alias="Status")
    user_id: Optional[StrictInt] = Field(default=None, description="The user identifier.", alias="UserId")
    unwatched_only: Optional[StrictBool] = Field(default=None, description="A value indicating whether \\[unwatched only\\].", alias="UnwatchedOnly")
    sync_new_content: Optional[StrictBool] = Field(default=None, description="A value indicating whether \\[synchronize new content\\].", alias="SyncNewContent")
    item_limit: Optional[StrictInt] = Field(default=None, description="The item limit.", alias="ItemLimit")
    requested_item_ids: Optional[List[StrictInt]] = Field(default=None, description="The requested item ids.", alias="RequestedItemIds")
    item_id: Optional[StrictInt] = Field(default=None, alias="ItemId")
    date_created: Optional[datetime] = Field(default=None, description="The date created.", alias="DateCreated")
    date_last_modified: Optional[datetime] = Field(default=None, description="The date last modified.", alias="DateLastModified")
    item_count: Optional[StrictInt] = Field(default=None, description="The item count.", alias="ItemCount")
    parent_name: Optional[StrictStr] = Field(default=None, alias="ParentName")
    primary_image_item_id: Optional[StrictStr] = Field(default=None, alias="PrimaryImageItemId")
    primary_image_tag: Optional[StrictStr] = Field(default=None, alias="PrimaryImageTag")
    __properties: ClassVar[List[str]] = ["Id", "TargetId", "InternalTargetId", "TargetName", "Quality", "Bitrate", "Container", "VideoCodec", "AudioCodec", "Profile", "Category", "ParentId", "Progress", "Name", "Status", "UserId", "UnwatchedOnly", "SyncNewContent", "ItemLimit", "RequestedItemIds", "ItemId", "DateCreated", "DateLastModified", "ItemCount", "ParentName", "PrimaryImageItemId", "PrimaryImageTag"]

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
        """Create an instance of SyncJob from a JSON string"""
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
        # set to None if bitrate (nullable) is None
        # and model_fields_set contains the field
        if self.bitrate is None and "bitrate" in self.model_fields_set:
            _dict['Bitrate'] = None

        # set to None if item_limit (nullable) is None
        # and model_fields_set contains the field
        if self.item_limit is None and "item_limit" in self.model_fields_set:
            _dict['ItemLimit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyncJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "TargetId": obj.get("TargetId"),
            "InternalTargetId": obj.get("InternalTargetId"),
            "TargetName": obj.get("TargetName"),
            "Quality": obj.get("Quality"),
            "Bitrate": obj.get("Bitrate"),
            "Container": obj.get("Container"),
            "VideoCodec": obj.get("VideoCodec"),
            "AudioCodec": obj.get("AudioCodec"),
            "Profile": obj.get("Profile"),
            "Category": obj.get("Category"),
            "ParentId": obj.get("ParentId"),
            "Progress": obj.get("Progress"),
            "Name": obj.get("Name"),
            "Status": obj.get("Status"),
            "UserId": obj.get("UserId"),
            "UnwatchedOnly": obj.get("UnwatchedOnly"),
            "SyncNewContent": obj.get("SyncNewContent"),
            "ItemLimit": obj.get("ItemLimit"),
            "RequestedItemIds": obj.get("RequestedItemIds"),
            "ItemId": obj.get("ItemId"),
            "DateCreated": obj.get("DateCreated"),
            "DateLastModified": obj.get("DateLastModified"),
            "ItemCount": obj.get("ItemCount"),
            "ParentName": obj.get("ParentName"),
            "PrimaryImageItemId": obj.get("PrimaryImageItemId"),
            "PrimaryImageTag": obj.get("PrimaryImageTag")
        })
        return _obj


