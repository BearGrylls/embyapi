# MediaStream

MediaStream information.      MediaStream itens are typically included in a `MediaBrowser.Model.Dto.MediaSourceInfo` object.      `MediaBrowser.Model.Dto.MediaSourceInfo.MediaStreams`  

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **str** | The codec.    Probe Field: &#x60;codec_name&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;    Related Enums: &#x60;T:Emby.Media.Model.Enums.VideoMediaTypes&#x60;, &#x60;Emby.Media.Model.Enums.AudioMediaTypes&#x60;, &#x60;Emby.Media.Model.Enums.SubtitleMediaTypes&#x60;. | [optional] 
**codec_tag** | **str** | The codec tag.    Probe Field: &#x60;codec_tag&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**language** | **str** | The language.    Probe Field: &#x60;tags[\&quot;language\&quot;]&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**color_transfer** | **str** | The color transfer characteristics.    Probe Field: &#x60;color_transfer&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;    Related Enum: &#x60;Emby.Media.Model.Enums.ColorTransfers&#x60;. | [optional] 
**color_primaries** | **str** | The chromaticity coordinates of the source primaries.    Probe Field: &#x60;color_primaries&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;    Related Enum: &#x60;Emby.Media.Model.Enums.ColorPrimaries&#x60;. | [optional] 
**color_space** | **str** | The YUV colorspace type.    Probe Field: &#x60;color_space&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;    Related Enum: &#x60;Emby.Media.Model.Enums.ColorSpaces&#x60;. | [optional] 
**comment** | **str** | The comment.    Probe Field: &#x60;tags[\&quot;comment\&quot;]&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**stream_start_time_ticks** | **int** | The start time of the stream.    Probe Field: &#x60;start_time&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;.    Actual type: &#x60;System.TimeSpan&#x60;. | [optional] 
**time_base** | **str** | The time\\-base.    Probe Field: &#x60;time_base&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;.    Actual type: &#x60;Emby.Media.Model.Types.Rational&#x60;. | [optional] 
**title** | **str** | The title.    Probe Field: &#x60;tags[\&quot;title\&quot;]&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**extradata** | **str** | The extradata.    Probe Field: &#x60;extradata&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;.    Currently, this value is only parsed for subtitle streams with codec &#x60;Emby.Media.Model.Enums.SubtitleMediaTypes.dvb_teletext&#x60;. | [optional] 
**video_range** | **str** |  | [optional] 
**display_title** | **str** | The display title.    Custom property set by the application. | [optional] 
**display_language** | **str** | The display language.    Custom property set by the application. | [optional] 
**nal_length_size** | **str** | The nal length size.    Probe Field: &#x60;nal_length_size&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60; of type &#x60;Emby.Media.Model.Enums.VideoMediaTypes.h264&#x60;.    Actual type: &#x60;System.Int32&#x60;. | [optional] 
**is_interlaced** | **bool** | A value indicating whether this instance is interlaced.    Probe Field: &#x60;field_order&#x60; \\!\\&#x3D; &#x60;progressive&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;. | [optional] 
**is_avc** | **bool** |  | [optional] 
**channel_layout** | **str** | The channel layout.    Probe Field: &#x60;channel_layout&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;    Related Enum: &#x60;MediaBrowser.Model.Entities.MediaStream.ChannelLayout&#x60;. | [optional] 
**bit_rate** | **int** | The bit rate.    Probe Field: &#x60;bit_rate&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;.    THIS VALUE IS PROCESSED BY CUSTOM LOGIC AND DOES NOT NECESSARILY MATCH FFPROBE RESULTS\\! | [optional] 
**bit_depth** | **int** | The bit depth.    Probe Field: &#x60;bits_per_sample&#x60; or &#x60;bits_per_raw_sample&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;. | [optional] 
**ref_frames** | **int** | The reference frames.    Probe Field: &#x60;refs&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;. | [optional] 
**rotation** | **int** |  | [optional] 
**channels** | **int** | The audio channel count.    Probe Field: &#x60;channels&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;. | [optional] 
**sample_rate** | **int** | The sample rate.    Probe Field: &#x60;sample_rate&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;    Related Enum: &#x60;Emby.Media.Model.Enums.SampleRates&#x60;. | [optional] 
**is_default** | **bool** | A value indicating whether this instance is default.    Probe Field: &#x60;disposition[\&quot;default\&quot;]&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**is_forced** | **bool** | A value indicating whether this instance is forced.    Probe Field: &#x60;disposition[\&quot;forced\&quot;]&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**is_hearing_impaired** | **bool** |  | [optional] 
**height** | **int** | The height.    Probe Field: &#x60;height&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;. | [optional] 
**width** | **int** | The width.    Probe Field: &#x60;width&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;. | [optional] 
**average_frame_rate** | **float** | The average frame rate..    Probe Field: &#x60;avg_frame_rate&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;.    Actual type: &#x60;Emby.Media.Model.Types.Rational&#x60;. | [optional] 
**real_frame_rate** | **float** | The real frame rate..    Probe Field: &#x60;r_frame_rate&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;.    Actual type: &#x60;Emby.Media.Model.Types.Rational&#x60;. | [optional] 
**profile** | **str** | The profile.    Probe Field: &#x60;profile&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;    Related Enums: &#x60;Emby.Media.Model.Enums.AacProfiles&#x60;, &#x60;Emby.Media.Model.Enums.AvcProfiles&#x60;, &#x60;Emby.Media.Model.Enums.H263Profiles&#x60;, &#x60;Emby.Media.Model.Enums.HevcProfiles&#x60;, &#x60;Emby.Media.Model.Enums.Mpeg2Profiles&#x60;,&#x60;Emby.Media.Model.Enums.Vc1Profiles&#x60;, &#x60;Emby.Media.Model.Enums.Mpeg4Profiles&#x60;, &#x60;Emby.Media.Model.Enums.Vp8Profiles&#x60;, &#x60;Emby.Media.Model.Enums.Vp9Profiles&#x60;. | [optional] 
**type** | [**MediaStreamType**](MediaStreamType.md) |  | [optional] 
**aspect_ratio** | **str** | The aspect ratio.    Probe Field: &#x60;display_aspect_ratio&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;.    Actual type: &#x60;Emby.Media.Model.Types.Rational&#x60;. | [optional] 
**index** | **int** | The index of the stream inside its container.    Probe Field: &#x60;index&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Audio&#x60;, &#x60;MediaBrowser.Model.Entities.MediaStreamType.Subtitle&#x60;. | [optional] 
**is_external** | **bool** | A value indicating whether this instance is external.    Custom property set by the application. | [optional] 
**delivery_method** | [**SubtitleDeliveryMethod**](SubtitleDeliveryMethod.md) |  | [optional] 
**delivery_url** | **str** | The delivery URL.    Custom property set by the application. | [optional] 
**is_external_url** | **bool** | A value indicating whether this instance is external URL.    Custom property set by the application. | [optional] 
**is_text_subtitle_stream** | **bool** |  | [optional] 
**supports_external_stream** | **bool** | A value indicating whether \\[supports external stream\\]. | [optional] 
**path** | **str** | The filename. | [optional] 
**protocol** | [**MediaProtocol**](MediaProtocol.md) |  | [optional] 
**pixel_format** | **str** | The pixel format.    Probe Field: &#x60;pix_fmt&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;.    Actual type: &#x60;MediaBrowser.Model.Entities.MediaStream.PixelFormat&#x60;. | [optional] 
**level** | **float** | The codec level.    Probe Field: &#x60;level&#x60;    Applies to: &#x60;MediaBrowser.Model.Entities.MediaStreamType.Video&#x60;    Related Enums: &#x60;Emby.Media.Model.Enums.AvcLevels&#x60;, &#x60;Emby.Media.Model.Enums.H263Levels&#x60;, &#x60;Emby.Media.Model.Enums.HevcLevels&#x60;, &#x60;Emby.Media.Model.Enums.Mpeg2Levels&#x60;,&#x60;Emby.Media.Model.Enums.Vc1Levels&#x60;, &#x60;Emby.Media.Model.Enums.Mpeg4Levels&#x60;, &#x60;Emby.Media.Model.Enums.Vp8Levels&#x60;, &#x60;Emby.Media.Model.Enums.Vp9Levels&#x60;. | [optional] 
**is_anamorphic** | **bool** | A value indicating whether this instance is anamorphic. | [optional] 
**extended_video_type** | [**ExtendedVideoTypes**](ExtendedVideoTypes.md) |  | [optional] 
**extended_video_sub_type** | [**ExtendedVideoSubTypes**](ExtendedVideoSubTypes.md) |  | [optional] 
**extended_video_sub_type_description** | **str** | The extended video sub\\-type description. | [optional] 
**item_id** | **str** | Used only by our Windows app. Not used by Emby Server. | [optional] 
**server_id** | **str** | Used only by our Windows app. Not used by Emby Server. | [optional] 
**attachment_size** | **int** | The size of the attachment. | [optional] 
**mime_type** | **str** | The type of the MIME. | [optional] 
**subtitle_location_type** | [**SubtitleLocationType**](SubtitleLocationType.md) |  | [optional] 

## Example

```python
from embyapi.models.media_stream import MediaStream

# TODO update the JSON string below
json = "{}"
# create an instance of MediaStream from a JSON string
media_stream_instance = MediaStream.from_json(json)
# print the JSON string representation of the object
print(MediaStream.to_json())

# convert the object into a dict
media_stream_dict = media_stream_instance.to_dict()
# create an instance of MediaStream from a dict
media_stream_from_dict = MediaStream.from_dict(media_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


