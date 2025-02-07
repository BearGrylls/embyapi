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
from embyapi.models.segment_skip_mode import SegmentSkipMode
from embyapi.models.subtitle_playback_mode import SubtitlePlaybackMode
from typing import Optional, Set
from typing_extensions import Self

class UserConfiguration(BaseModel):
    """
    Class UserConfiguration  
    """ # noqa: E501
    audio_language_preference: Optional[StrictStr] = Field(default=None, description="The audio language preference.", alias="AudioLanguagePreference")
    play_default_audio_track: Optional[StrictBool] = Field(default=None, description="A value indicating whether \\[play default audio track\\].", alias="PlayDefaultAudioTrack")
    subtitle_language_preference: Optional[StrictStr] = Field(default=None, description="The subtitle language preference.", alias="SubtitleLanguagePreference")
    profile_pin: Optional[StrictStr] = Field(default=None, alias="ProfilePin")
    display_missing_episodes: Optional[StrictBool] = Field(default=None, alias="DisplayMissingEpisodes")
    subtitle_mode: Optional[SubtitlePlaybackMode] = Field(default=None, alias="SubtitleMode")
    ordered_views: Optional[List[StrictStr]] = Field(default=None, alias="OrderedViews")
    latest_items_excludes: Optional[List[StrictStr]] = Field(default=None, alias="LatestItemsExcludes")
    my_media_excludes: Optional[List[StrictStr]] = Field(default=None, alias="MyMediaExcludes")
    hide_played_in_latest: Optional[StrictBool] = Field(default=None, alias="HidePlayedInLatest")
    hide_played_in_more_like_this: Optional[StrictBool] = Field(default=None, alias="HidePlayedInMoreLikeThis")
    hide_played_in_suggestions: Optional[StrictBool] = Field(default=None, alias="HidePlayedInSuggestions")
    remember_audio_selections: Optional[StrictBool] = Field(default=None, alias="RememberAudioSelections")
    remember_subtitle_selections: Optional[StrictBool] = Field(default=None, alias="RememberSubtitleSelections")
    enable_next_episode_auto_play: Optional[StrictBool] = Field(default=None, alias="EnableNextEpisodeAutoPlay")
    resume_rewind_seconds: Optional[StrictInt] = Field(default=None, alias="ResumeRewindSeconds")
    intro_skip_mode: Optional[SegmentSkipMode] = Field(default=None, alias="IntroSkipMode")
    enable_local_password: Optional[StrictBool] = Field(default=None, alias="EnableLocalPassword")
    __properties: ClassVar[List[str]] = ["AudioLanguagePreference", "PlayDefaultAudioTrack", "SubtitleLanguagePreference", "ProfilePin", "DisplayMissingEpisodes", "SubtitleMode", "OrderedViews", "LatestItemsExcludes", "MyMediaExcludes", "HidePlayedInLatest", "HidePlayedInMoreLikeThis", "HidePlayedInSuggestions", "RememberAudioSelections", "RememberSubtitleSelections", "EnableNextEpisodeAutoPlay", "ResumeRewindSeconds", "IntroSkipMode", "EnableLocalPassword"]

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
        """Create an instance of UserConfiguration from a JSON string"""
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
        """Create an instance of UserConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AudioLanguagePreference": obj.get("AudioLanguagePreference"),
            "PlayDefaultAudioTrack": obj.get("PlayDefaultAudioTrack"),
            "SubtitleLanguagePreference": obj.get("SubtitleLanguagePreference"),
            "ProfilePin": obj.get("ProfilePin"),
            "DisplayMissingEpisodes": obj.get("DisplayMissingEpisodes"),
            "SubtitleMode": obj.get("SubtitleMode"),
            "OrderedViews": obj.get("OrderedViews"),
            "LatestItemsExcludes": obj.get("LatestItemsExcludes"),
            "MyMediaExcludes": obj.get("MyMediaExcludes"),
            "HidePlayedInLatest": obj.get("HidePlayedInLatest"),
            "HidePlayedInMoreLikeThis": obj.get("HidePlayedInMoreLikeThis"),
            "HidePlayedInSuggestions": obj.get("HidePlayedInSuggestions"),
            "RememberAudioSelections": obj.get("RememberAudioSelections"),
            "RememberSubtitleSelections": obj.get("RememberSubtitleSelections"),
            "EnableNextEpisodeAutoPlay": obj.get("EnableNextEpisodeAutoPlay"),
            "ResumeRewindSeconds": obj.get("ResumeRewindSeconds"),
            "IntroSkipMode": obj.get("IntroSkipMode"),
            "EnableLocalPassword": obj.get("EnableLocalPassword")
        })
        return _obj


