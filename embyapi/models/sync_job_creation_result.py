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
from embyapi.models.sync_job import SyncJob
from embyapi.models.sync_job_item import SyncJobItem
from typing import Optional, Set
from typing_extensions import Self

class SyncJobCreationResult(BaseModel):
    """
    SyncJobCreationResult
    """ # noqa: E501
    job: Optional[SyncJob] = Field(default=None, alias="Job")
    job_items: Optional[List[SyncJobItem]] = Field(default=None, alias="JobItems")
    __properties: ClassVar[List[str]] = ["Job", "JobItems"]

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
        """Create an instance of SyncJobCreationResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['Job'] = self.job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in job_items (list)
        _items = []
        if self.job_items:
            for _item in self.job_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['JobItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyncJobCreationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Job": SyncJob.from_dict(obj["Job"]) if obj.get("Job") is not None else None,
            "JobItems": [SyncJobItem.from_dict(_item) for _item in obj["JobItems"]] if obj.get("JobItems") is not None else None
        })
        return _obj


