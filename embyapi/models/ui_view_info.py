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
from embyapi.models.enums_ui_view_type import EnumsUIViewType
from embyapi.models.generic_edit_i_edit_object_container import GenericEditIEditObjectContainer
from embyapi.models.ui_command import UICommand
from embyapi.models.ui_tab_page_info import UITabPageInfo
from typing import Optional, Set
from typing_extensions import Self

class UIViewInfo(BaseModel):
    """
    UIViewInfo
    """ # noqa: E501
    view_id: Optional[StrictStr] = Field(default=None, alias="ViewId")
    page_id: Optional[StrictStr] = Field(default=None, alias="PageId")
    caption: Optional[StrictStr] = Field(default=None, alias="Caption")
    sub_caption: Optional[StrictStr] = Field(default=None, alias="SubCaption")
    plugin_id: Optional[StrictStr] = Field(default=None, alias="PluginId")
    view_type: Optional[EnumsUIViewType] = Field(default=None, alias="ViewType")
    show_dialog_full_screen: Optional[StrictBool] = Field(default=None, alias="ShowDialogFullScreen")
    is_in_sequence: Optional[StrictBool] = Field(default=None, alias="IsInSequence")
    redirect_view_url: Optional[StrictStr] = Field(default=None, alias="RedirectViewUrl")
    edit_object_container: Optional[GenericEditIEditObjectContainer] = Field(default=None, alias="EditObjectContainer")
    commands: Optional[List[UICommand]] = Field(default=None, alias="Commands")
    tab_page_infos: Optional[List[UITabPageInfo]] = Field(default=None, alias="TabPageInfos")
    is_page_change_info: Optional[StrictBool] = Field(default=None, alias="IsPageChangeInfo")
    __properties: ClassVar[List[str]] = ["ViewId", "PageId", "Caption", "SubCaption", "PluginId", "ViewType", "ShowDialogFullScreen", "IsInSequence", "RedirectViewUrl", "EditObjectContainer", "Commands", "TabPageInfos", "IsPageChangeInfo"]

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
        """Create an instance of UIViewInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of edit_object_container
        if self.edit_object_container:
            _dict['EditObjectContainer'] = self.edit_object_container.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in commands (list)
        _items = []
        if self.commands:
            for _item in self.commands:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Commands'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tab_page_infos (list)
        _items = []
        if self.tab_page_infos:
            for _item in self.tab_page_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TabPageInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UIViewInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ViewId": obj.get("ViewId"),
            "PageId": obj.get("PageId"),
            "Caption": obj.get("Caption"),
            "SubCaption": obj.get("SubCaption"),
            "PluginId": obj.get("PluginId"),
            "ViewType": obj.get("ViewType"),
            "ShowDialogFullScreen": obj.get("ShowDialogFullScreen"),
            "IsInSequence": obj.get("IsInSequence"),
            "RedirectViewUrl": obj.get("RedirectViewUrl"),
            "EditObjectContainer": GenericEditIEditObjectContainer.from_dict(obj["EditObjectContainer"]) if obj.get("EditObjectContainer") is not None else None,
            "Commands": [UICommand.from_dict(_item) for _item in obj["Commands"]] if obj.get("Commands") is not None else None,
            "TabPageInfos": [UITabPageInfo.from_dict(_item) for _item in obj["TabPageInfos"]] if obj.get("TabPageInfos") is not None else None,
            "IsPageChangeInfo": obj.get("IsPageChangeInfo")
        })
        return _obj


