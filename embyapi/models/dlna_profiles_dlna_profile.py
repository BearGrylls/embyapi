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
from embyapi.models.codec_profile import CodecProfile
from embyapi.models.container_profile import ContainerProfile
from embyapi.models.direct_play_profile import DirectPlayProfile
from embyapi.models.dlna_profiles_device_identification import DlnaProfilesDeviceIdentification
from embyapi.models.dlna_profiles_device_profile_type import DlnaProfilesDeviceProfileType
from embyapi.models.dlna_profiles_protocol_info_detection import DlnaProfilesProtocolInfoDetection
from embyapi.models.response_profile import ResponseProfile
from embyapi.models.subtitle_profile import SubtitleProfile
from embyapi.models.transcoding_profile import TranscodingProfile
from typing import Optional, Set
from typing_extensions import Self

class DlnaProfilesDlnaProfile(BaseModel):
    """
    DlnaProfilesDlnaProfile
    """ # noqa: E501
    type: Optional[DlnaProfilesDeviceProfileType] = Field(default=None, alias="Type")
    path: Optional[StrictStr] = Field(default=None, alias="Path")
    user_id: Optional[StrictStr] = Field(default=None, alias="UserId")
    album_art_pn: Optional[StrictStr] = Field(default=None, alias="AlbumArtPn")
    max_album_art_width: Optional[StrictInt] = Field(default=None, alias="MaxAlbumArtWidth")
    max_album_art_height: Optional[StrictInt] = Field(default=None, alias="MaxAlbumArtHeight")
    max_icon_width: Optional[StrictInt] = Field(default=None, alias="MaxIconWidth")
    max_icon_height: Optional[StrictInt] = Field(default=None, alias="MaxIconHeight")
    friendly_name: Optional[StrictStr] = Field(default=None, alias="FriendlyName")
    manufacturer: Optional[StrictStr] = Field(default=None, alias="Manufacturer")
    manufacturer_url: Optional[StrictStr] = Field(default=None, alias="ManufacturerUrl")
    model_name: Optional[StrictStr] = Field(default=None, alias="ModelName")
    model_description: Optional[StrictStr] = Field(default=None, alias="ModelDescription")
    model_number: Optional[StrictStr] = Field(default=None, alias="ModelNumber")
    model_url: Optional[StrictStr] = Field(default=None, alias="ModelUrl")
    serial_number: Optional[StrictStr] = Field(default=None, alias="SerialNumber")
    enable_album_art_in_didl: Optional[StrictBool] = Field(default=None, alias="EnableAlbumArtInDidl")
    enable_single_album_art_limit: Optional[StrictBool] = Field(default=None, alias="EnableSingleAlbumArtLimit")
    enable_single_subtitle_limit: Optional[StrictBool] = Field(default=None, alias="EnableSingleSubtitleLimit")
    protocol_info: Optional[StrictStr] = Field(default=None, alias="ProtocolInfo")
    timeline_offset_seconds: Optional[StrictInt] = Field(default=None, alias="TimelineOffsetSeconds")
    requires_plain_video_items: Optional[StrictBool] = Field(default=None, alias="RequiresPlainVideoItems")
    requires_plain_folders: Optional[StrictBool] = Field(default=None, alias="RequiresPlainFolders")
    ignore_transcode_byte_range_requests: Optional[StrictBool] = Field(default=None, alias="IgnoreTranscodeByteRangeRequests")
    supports_samsung_bookmark: Optional[StrictBool] = Field(default=None, alias="SupportsSamsungBookmark")
    identification: Optional[DlnaProfilesDeviceIdentification] = Field(default=None, alias="Identification")
    protocol_info_detection: Optional[DlnaProfilesProtocolInfoDetection] = Field(default=None, alias="ProtocolInfoDetection")
    name: Optional[StrictStr] = Field(default=None, description="The name.", alias="Name")
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    supported_media_types: Optional[StrictStr] = Field(default=None, alias="SupportedMediaTypes")
    max_streaming_bitrate: Optional[StrictInt] = Field(default=None, alias="MaxStreamingBitrate")
    music_streaming_transcoding_bitrate: Optional[StrictInt] = Field(default=None, alias="MusicStreamingTranscodingBitrate")
    max_static_music_bitrate: Optional[StrictInt] = Field(default=None, alias="MaxStaticMusicBitrate")
    direct_play_profiles: Optional[List[DirectPlayProfile]] = Field(default=None, description="The direct play profiles.", alias="DirectPlayProfiles")
    transcoding_profiles: Optional[List[TranscodingProfile]] = Field(default=None, description="The transcoding profiles.", alias="TranscodingProfiles")
    container_profiles: Optional[List[ContainerProfile]] = Field(default=None, alias="ContainerProfiles")
    codec_profiles: Optional[List[CodecProfile]] = Field(default=None, alias="CodecProfiles")
    response_profiles: Optional[List[ResponseProfile]] = Field(default=None, alias="ResponseProfiles")
    subtitle_profiles: Optional[List[SubtitleProfile]] = Field(default=None, alias="SubtitleProfiles")
    __properties: ClassVar[List[str]] = ["Type", "Path", "UserId", "AlbumArtPn", "MaxAlbumArtWidth", "MaxAlbumArtHeight", "MaxIconWidth", "MaxIconHeight", "FriendlyName", "Manufacturer", "ManufacturerUrl", "ModelName", "ModelDescription", "ModelNumber", "ModelUrl", "SerialNumber", "EnableAlbumArtInDidl", "EnableSingleAlbumArtLimit", "EnableSingleSubtitleLimit", "ProtocolInfo", "TimelineOffsetSeconds", "RequiresPlainVideoItems", "RequiresPlainFolders", "IgnoreTranscodeByteRangeRequests", "SupportsSamsungBookmark", "Identification", "ProtocolInfoDetection", "Name", "Id", "SupportedMediaTypes", "MaxStreamingBitrate", "MusicStreamingTranscodingBitrate", "MaxStaticMusicBitrate", "DirectPlayProfiles", "TranscodingProfiles", "ContainerProfiles", "CodecProfiles", "ResponseProfiles", "SubtitleProfiles"]

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
        """Create an instance of DlnaProfilesDlnaProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identification
        if self.identification:
            _dict['Identification'] = self.identification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of protocol_info_detection
        if self.protocol_info_detection:
            _dict['ProtocolInfoDetection'] = self.protocol_info_detection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in direct_play_profiles (list)
        _items = []
        if self.direct_play_profiles:
            for _item in self.direct_play_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['DirectPlayProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transcoding_profiles (list)
        _items = []
        if self.transcoding_profiles:
            for _item in self.transcoding_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TranscodingProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in container_profiles (list)
        _items = []
        if self.container_profiles:
            for _item in self.container_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ContainerProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in codec_profiles (list)
        _items = []
        if self.codec_profiles:
            for _item in self.codec_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['CodecProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in response_profiles (list)
        _items = []
        if self.response_profiles:
            for _item in self.response_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ResponseProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subtitle_profiles (list)
        _items = []
        if self.subtitle_profiles:
            for _item in self.subtitle_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SubtitleProfiles'] = _items
        # set to None if max_icon_width (nullable) is None
        # and model_fields_set contains the field
        if self.max_icon_width is None and "max_icon_width" in self.model_fields_set:
            _dict['MaxIconWidth'] = None

        # set to None if max_icon_height (nullable) is None
        # and model_fields_set contains the field
        if self.max_icon_height is None and "max_icon_height" in self.model_fields_set:
            _dict['MaxIconHeight'] = None

        # set to None if max_streaming_bitrate (nullable) is None
        # and model_fields_set contains the field
        if self.max_streaming_bitrate is None and "max_streaming_bitrate" in self.model_fields_set:
            _dict['MaxStreamingBitrate'] = None

        # set to None if music_streaming_transcoding_bitrate (nullable) is None
        # and model_fields_set contains the field
        if self.music_streaming_transcoding_bitrate is None and "music_streaming_transcoding_bitrate" in self.model_fields_set:
            _dict['MusicStreamingTranscodingBitrate'] = None

        # set to None if max_static_music_bitrate (nullable) is None
        # and model_fields_set contains the field
        if self.max_static_music_bitrate is None and "max_static_music_bitrate" in self.model_fields_set:
            _dict['MaxStaticMusicBitrate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DlnaProfilesDlnaProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "Path": obj.get("Path"),
            "UserId": obj.get("UserId"),
            "AlbumArtPn": obj.get("AlbumArtPn"),
            "MaxAlbumArtWidth": obj.get("MaxAlbumArtWidth"),
            "MaxAlbumArtHeight": obj.get("MaxAlbumArtHeight"),
            "MaxIconWidth": obj.get("MaxIconWidth"),
            "MaxIconHeight": obj.get("MaxIconHeight"),
            "FriendlyName": obj.get("FriendlyName"),
            "Manufacturer": obj.get("Manufacturer"),
            "ManufacturerUrl": obj.get("ManufacturerUrl"),
            "ModelName": obj.get("ModelName"),
            "ModelDescription": obj.get("ModelDescription"),
            "ModelNumber": obj.get("ModelNumber"),
            "ModelUrl": obj.get("ModelUrl"),
            "SerialNumber": obj.get("SerialNumber"),
            "EnableAlbumArtInDidl": obj.get("EnableAlbumArtInDidl"),
            "EnableSingleAlbumArtLimit": obj.get("EnableSingleAlbumArtLimit"),
            "EnableSingleSubtitleLimit": obj.get("EnableSingleSubtitleLimit"),
            "ProtocolInfo": obj.get("ProtocolInfo"),
            "TimelineOffsetSeconds": obj.get("TimelineOffsetSeconds"),
            "RequiresPlainVideoItems": obj.get("RequiresPlainVideoItems"),
            "RequiresPlainFolders": obj.get("RequiresPlainFolders"),
            "IgnoreTranscodeByteRangeRequests": obj.get("IgnoreTranscodeByteRangeRequests"),
            "SupportsSamsungBookmark": obj.get("SupportsSamsungBookmark"),
            "Identification": DlnaProfilesDeviceIdentification.from_dict(obj["Identification"]) if obj.get("Identification") is not None else None,
            "ProtocolInfoDetection": DlnaProfilesProtocolInfoDetection.from_dict(obj["ProtocolInfoDetection"]) if obj.get("ProtocolInfoDetection") is not None else None,
            "Name": obj.get("Name"),
            "Id": obj.get("Id"),
            "SupportedMediaTypes": obj.get("SupportedMediaTypes"),
            "MaxStreamingBitrate": obj.get("MaxStreamingBitrate"),
            "MusicStreamingTranscodingBitrate": obj.get("MusicStreamingTranscodingBitrate"),
            "MaxStaticMusicBitrate": obj.get("MaxStaticMusicBitrate"),
            "DirectPlayProfiles": [DirectPlayProfile.from_dict(_item) for _item in obj["DirectPlayProfiles"]] if obj.get("DirectPlayProfiles") is not None else None,
            "TranscodingProfiles": [TranscodingProfile.from_dict(_item) for _item in obj["TranscodingProfiles"]] if obj.get("TranscodingProfiles") is not None else None,
            "ContainerProfiles": [ContainerProfile.from_dict(_item) for _item in obj["ContainerProfiles"]] if obj.get("ContainerProfiles") is not None else None,
            "CodecProfiles": [CodecProfile.from_dict(_item) for _item in obj["CodecProfiles"]] if obj.get("CodecProfiles") is not None else None,
            "ResponseProfiles": [ResponseProfile.from_dict(_item) for _item in obj["ResponseProfiles"]] if obj.get("ResponseProfiles") is not None else None,
            "SubtitleProfiles": [SubtitleProfile.from_dict(_item) for _item in obj["SubtitleProfiles"]] if obj.get("SubtitleProfiles") is not None else None
        })
        return _obj


