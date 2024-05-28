# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LiveTvKeywordType(str, Enum):
    """
    LiveTvKeywordType
    """

    """
    allowed enum values
    """
    NAME = 'Name'
    EPISODETITLE = 'EpisodeTitle'
    OVERVIEW = 'Overview'
    ACTOR = 'Actor'
    DIRECTOR = 'Director'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LiveTvKeywordType from a JSON string"""
        return cls(json.loads(json_str))


