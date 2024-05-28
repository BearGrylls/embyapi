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
from embyapi.models.base_item_dto import BaseItemDto
from embyapi.models.queue_item import QueueItem
from typing import Optional, Set
from typing_extensions import Self

class PlaybackStopInfo(BaseModel):
    """
    Class PlaybackStopInfo.  
    """ # noqa: E501
    now_playing_queue: Optional[List[QueueItem]] = Field(default=None, alias="NowPlayingQueue")
    playlist_item_id: Optional[StrictStr] = Field(default=None, alias="PlaylistItemId")
    playlist_index: Optional[StrictInt] = Field(default=None, alias="PlaylistIndex")
    playlist_length: Optional[StrictInt] = Field(default=None, alias="PlaylistLength")
    item: Optional[BaseItemDto] = Field(default=None, alias="Item")
    item_id: Optional[StrictStr] = Field(default=None, description="The item identifier.", alias="ItemId")
    session_id: Optional[StrictStr] = Field(default=None, description="The session id.", alias="SessionId")
    media_source_id: Optional[StrictStr] = Field(default=None, description="The media version identifier.", alias="MediaSourceId")
    position_ticks: Optional[StrictInt] = Field(default=None, description="The position ticks.", alias="PositionTicks")
    live_stream_id: Optional[StrictStr] = Field(default=None, description="The live stream identifier.", alias="LiveStreamId")
    play_session_id: Optional[StrictStr] = Field(default=None, description="The play session identifier.", alias="PlaySessionId")
    failed: Optional[StrictBool] = Field(default=None, description="A value indicating whether this `MediaBrowser.Model.Session.PlaybackStopInfo` is failed.", alias="Failed")
    is_automated: Optional[StrictBool] = Field(default=None, alias="IsAutomated")
    next_media_type: Optional[StrictStr] = Field(default=None, alias="NextMediaType")
    __properties: ClassVar[List[str]] = ["NowPlayingQueue", "PlaylistItemId", "PlaylistIndex", "PlaylistLength", "Item", "ItemId", "SessionId", "MediaSourceId", "PositionTicks", "LiveStreamId", "PlaySessionId", "Failed", "IsAutomated", "NextMediaType"]

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
        """Create an instance of PlaybackStopInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in now_playing_queue (list)
        _items = []
        if self.now_playing_queue:
            for _item in self.now_playing_queue:
                if _item:
                    _items.append(_item.to_dict())
            _dict['NowPlayingQueue'] = _items
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['Item'] = self.item.to_dict()
        # set to None if position_ticks (nullable) is None
        # and model_fields_set contains the field
        if self.position_ticks is None and "position_ticks" in self.model_fields_set:
            _dict['PositionTicks'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlaybackStopInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NowPlayingQueue": [QueueItem.from_dict(_item) for _item in obj["NowPlayingQueue"]] if obj.get("NowPlayingQueue") is not None else None,
            "PlaylistItemId": obj.get("PlaylistItemId"),
            "PlaylistIndex": obj.get("PlaylistIndex"),
            "PlaylistLength": obj.get("PlaylistLength"),
            "Item": BaseItemDto.from_dict(obj["Item"]) if obj.get("Item") is not None else None,
            "ItemId": obj.get("ItemId"),
            "SessionId": obj.get("SessionId"),
            "MediaSourceId": obj.get("MediaSourceId"),
            "PositionTicks": obj.get("PositionTicks"),
            "LiveStreamId": obj.get("LiveStreamId"),
            "PlaySessionId": obj.get("PlaySessionId"),
            "Failed": obj.get("Failed"),
            "IsAutomated": obj.get("IsAutomated"),
            "NextMediaType": obj.get("NextMediaType")
        })
        return _obj


