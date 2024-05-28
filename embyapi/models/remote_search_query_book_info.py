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
from embyapi.models.book_info import BookInfo
from typing import Optional, Set
from typing_extensions import Self

class RemoteSearchQueryBookInfo(BaseModel):
    """
    RemoteSearchQueryBookInfo
    """ # noqa: E501
    search_info: Optional[BookInfo] = Field(default=None, alias="SearchInfo")
    item_id: Optional[StrictInt] = Field(default=None, alias="ItemId")
    search_provider_name: Optional[StrictStr] = Field(default=None, alias="SearchProviderName")
    providers: Optional[List[StrictStr]] = Field(default=None, alias="Providers")
    include_disabled_providers: Optional[StrictBool] = Field(default=None, alias="IncludeDisabledProviders")
    __properties: ClassVar[List[str]] = ["SearchInfo", "ItemId", "SearchProviderName", "Providers", "IncludeDisabledProviders"]

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
        """Create an instance of RemoteSearchQueryBookInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of search_info
        if self.search_info:
            _dict['SearchInfo'] = self.search_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemoteSearchQueryBookInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "SearchInfo": BookInfo.from_dict(obj["SearchInfo"]) if obj.get("SearchInfo") is not None else None,
            "ItemId": obj.get("ItemId"),
            "SearchProviderName": obj.get("SearchProviderName"),
            "Providers": obj.get("Providers"),
            "IncludeDisabledProviders": obj.get("IncludeDisabledProviders")
        })
        return _obj


