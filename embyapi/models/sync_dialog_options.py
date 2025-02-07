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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from embyapi.models.sync_job_option import SyncJobOption
from embyapi.models.sync_profile_option import SyncProfileOption
from embyapi.models.sync_quality_option import SyncQualityOption
from embyapi.models.sync_target import SyncTarget
from typing import Optional, Set
from typing_extensions import Self

class SyncDialogOptions(BaseModel):
    """
    SyncDialogOptions
    """ # noqa: E501
    targets: Optional[List[SyncTarget]] = Field(default=None, alias="Targets")
    options: Optional[List[SyncJobOption]] = Field(default=None, alias="Options")
    quality_options: Optional[List[SyncQualityOption]] = Field(default=None, alias="QualityOptions")
    profile_options: Optional[List[SyncProfileOption]] = Field(default=None, alias="ProfileOptions")
    __properties: ClassVar[List[str]] = ["Targets", "Options", "QualityOptions", "ProfileOptions"]

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
        """Create an instance of SyncDialogOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item in self.targets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Targets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in quality_options (list)
        _items = []
        if self.quality_options:
            for _item in self.quality_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['QualityOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in profile_options (list)
        _items = []
        if self.profile_options:
            for _item in self.profile_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ProfileOptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyncDialogOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Targets": [SyncTarget.from_dict(_item) for _item in obj["Targets"]] if obj.get("Targets") is not None else None,
            "Options": obj.get("Options"),
            "QualityOptions": [SyncQualityOption.from_dict(_item) for _item in obj["QualityOptions"]] if obj.get("QualityOptions") is not None else None,
            "ProfileOptions": [SyncProfileOption.from_dict(_item) for _item in obj["ProfileOptions"]] if obj.get("ProfileOptions") is not None else None
        })
        return _obj


