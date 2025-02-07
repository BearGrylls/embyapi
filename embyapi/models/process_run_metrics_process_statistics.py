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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from embyapi.models.process_run_metrics_process_metric_point import ProcessRunMetricsProcessMetricPoint
from typing import Optional, Set
from typing_extensions import Self

class ProcessRunMetricsProcessStatistics(BaseModel):
    """
    ProcessRunMetricsProcessStatistics
    """ # noqa: E501
    current_cpu: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The current cpu.", alias="CurrentCpu")
    average_cpu: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The average cpu.", alias="AverageCpu")
    current_virtual_memory: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The currently allocated virtual memory.", alias="CurrentVirtualMemory")
    current_working_set: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The currently allocated working set.", alias="CurrentWorkingSet")
    metrics: Optional[List[ProcessRunMetricsProcessMetricPoint]] = Field(default=None, description="The metrics.", alias="Metrics")
    __properties: ClassVar[List[str]] = ["CurrentCpu", "AverageCpu", "CurrentVirtualMemory", "CurrentWorkingSet", "Metrics"]

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
        """Create an instance of ProcessRunMetricsProcessStatistics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item in self.metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Metrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProcessRunMetricsProcessStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CurrentCpu": obj.get("CurrentCpu"),
            "AverageCpu": obj.get("AverageCpu"),
            "CurrentVirtualMemory": obj.get("CurrentVirtualMemory"),
            "CurrentWorkingSet": obj.get("CurrentWorkingSet"),
            "Metrics": [ProcessRunMetricsProcessMetricPoint.from_dict(_item) for _item in obj["Metrics"]] if obj.get("Metrics") is not None else None
        })
        return _obj


