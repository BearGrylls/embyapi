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
from embyapi.models.common_editor_types import CommonEditorTypes
from typing import Optional, Set
from typing_extensions import Self

class EditorsEditorButtonItem(BaseModel):
    """
    EditorsEditorButtonItem
    """ # noqa: E501
    editor_type: Optional[CommonEditorTypes] = Field(default=None, alias="EditorType")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    allow_empty: Optional[StrictBool] = Field(default=None, alias="AllowEmpty")
    is_read_only: Optional[StrictBool] = Field(default=None, alias="IsReadOnly")
    is_advanced: Optional[StrictBool] = Field(default=None, alias="IsAdvanced")
    display_name: Optional[StrictStr] = Field(default=None, alias="DisplayName")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    feature_requires_premiere: Optional[StrictBool] = Field(default=None, alias="FeatureRequiresPremiere")
    parent_id: Optional[StrictStr] = Field(default=None, alias="ParentId")
    __properties: ClassVar[List[str]] = ["EditorType", "Name", "Id", "AllowEmpty", "IsReadOnly", "IsAdvanced", "DisplayName", "Description", "FeatureRequiresPremiere", "ParentId"]

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
        """Create an instance of EditorsEditorButtonItem from a JSON string"""
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
        """Create an instance of EditorsEditorButtonItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "EditorType": obj.get("EditorType"),
            "Name": obj.get("Name"),
            "Id": obj.get("Id"),
            "AllowEmpty": obj.get("AllowEmpty"),
            "IsReadOnly": obj.get("IsReadOnly"),
            "IsAdvanced": obj.get("IsAdvanced"),
            "DisplayName": obj.get("DisplayName"),
            "Description": obj.get("Description"),
            "FeatureRequiresPremiere": obj.get("FeatureRequiresPremiere"),
            "ParentId": obj.get("ParentId")
        })
        return _obj


