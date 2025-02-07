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
from embyapi.models.attributes_simple_condition import AttributesSimpleCondition
from embyapi.models.attributes_value_condition import AttributesValueCondition
from embyapi.models.conditions_property_condition_type import ConditionsPropertyConditionType
from typing import Optional, Set
from typing_extensions import Self

class ConditionsPropertyCondition(BaseModel):
    """
    ConditionsPropertyCondition
    """ # noqa: E501
    affected_property_id: Optional[StrictStr] = Field(default=None, alias="AffectedPropertyId")
    condition_type: Optional[ConditionsPropertyConditionType] = Field(default=None, alias="ConditionType")
    target_property_id: Optional[StrictStr] = Field(default=None, description="The target property name or path.", alias="TargetPropertyId")
    simple_condition: Optional[AttributesSimpleCondition] = Field(default=None, alias="SimpleCondition")
    value_condition: Optional[AttributesValueCondition] = Field(default=None, alias="ValueCondition")
    value: Optional[Dict[str, Any]] = Field(default=None, description="The value.", alias="Value")
    __properties: ClassVar[List[str]] = ["AffectedPropertyId", "ConditionType", "TargetPropertyId", "SimpleCondition", "ValueCondition", "Value"]

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
        """Create an instance of ConditionsPropertyCondition from a JSON string"""
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
        """Create an instance of ConditionsPropertyCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AffectedPropertyId": obj.get("AffectedPropertyId"),
            "ConditionType": obj.get("ConditionType"),
            "TargetPropertyId": obj.get("TargetPropertyId"),
            "SimpleCondition": obj.get("SimpleCondition"),
            "ValueCondition": obj.get("ValueCondition"),
            "Value": obj.get("Value")
        })
        return _obj


