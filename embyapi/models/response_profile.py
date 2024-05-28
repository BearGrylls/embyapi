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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from embyapi.models.dlna_profile_type import DlnaProfileType
from embyapi.models.profile_condition import ProfileCondition
from typing import Optional, Set
from typing_extensions import Self

class ResponseProfile(BaseModel):
    """
    ResponseProfile
    """ # noqa: E501
    container: Optional[StrictStr] = Field(default=None, alias="Container")
    audio_codec: Optional[StrictStr] = Field(default=None, alias="AudioCodec")
    video_codec: Optional[StrictStr] = Field(default=None, alias="VideoCodec")
    type: Optional[DlnaProfileType] = Field(default=None, alias="Type")
    org_pn: Optional[StrictStr] = Field(default=None, alias="OrgPn")
    mime_type: Optional[StrictStr] = Field(default=None, alias="MimeType")
    conditions: Optional[List[ProfileCondition]] = Field(default=None, alias="Conditions")
    __properties: ClassVar[List[str]] = ["Container", "AudioCodec", "VideoCodec", "Type", "OrgPn", "MimeType", "Conditions"]

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
        """Create an instance of ResponseProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResponseProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Container": obj.get("Container"),
            "AudioCodec": obj.get("AudioCodec"),
            "VideoCodec": obj.get("VideoCodec"),
            "Type": obj.get("Type"),
            "OrgPn": obj.get("OrgPn"),
            "MimeType": obj.get("MimeType"),
            "Conditions": [ProfileCondition.from_dict(_item) for _item in obj["Conditions"]] if obj.get("Conditions") is not None else None
        })
        return _obj


