"""
Type annotations for chime-sdk-media-pipelines service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.type_defs import ActiveSpeakerOnlyConfigurationTypeDef

    data: ActiveSpeakerOnlyConfigurationTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActiveSpeakerPositionType,
    ArtifactsConcatenationStateType,
    ArtifactsStateType,
    AudioChannelsOptionType,
    AudioMuxTypeType,
    BorderColorType,
    CallAnalyticsLanguageCodeType,
    CanvasOrientationType,
    ContentRedactionOutputType,
    ContentShareLayoutOptionType,
    FragmentSelectorTypeType,
    HighlightColorType,
    HorizontalTilePositionType,
    LiveConnectorMuxTypeType,
    MediaInsightsPipelineConfigurationElementTypeType,
    MediaPipelineStatusType,
    MediaPipelineStatusUpdateType,
    PartialResultsStabilityType,
    ParticipantRoleType,
    PresenterPositionType,
    RealTimeAlertRuleTypeType,
    RecordingFileFormatType,
    ResolutionOptionType,
    TileOrderType,
    VerticalTilePositionType,
    VocabularyFilterMethodType,
    VoiceAnalyticsConfigurationStatusType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveSpeakerOnlyConfigurationTypeDef",
    "PostCallAnalyticsSettingsTypeDef",
    "AmazonTranscribeProcessorConfigurationTypeDef",
    "AudioConcatenationConfigurationTypeDef",
    "CompositedVideoConcatenationConfigurationTypeDef",
    "ContentConcatenationConfigurationTypeDef",
    "DataChannelConcatenationConfigurationTypeDef",
    "MeetingEventsConcatenationConfigurationTypeDef",
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    "VideoConcatenationConfigurationTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "ChannelDefinitionTypeDef",
    "S3BucketSinkConfigurationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "DeleteMediaPipelineRequestRequestTypeDef",
    "TimestampRangeOutputTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "GetMediaPipelineRequestRequestTypeDef",
    "HorizontalLayoutConfigurationTypeDef",
    "PresenterOnlyConfigurationTypeDef",
    "VerticalLayoutConfigurationTypeDef",
    "VideoAttributeTypeDef",
    "IssueDetectionConfigurationTypeDef",
    "KeywordMatchConfigurationOutputTypeDef",
    "KeywordMatchConfigurationTypeDef",
    "KinesisDataStreamSinkConfigurationTypeDef",
    "RecordingStreamConfigurationTypeDef",
    "LambdaFunctionSinkConfigurationTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "MediaCapturePipelineSummaryTypeDef",
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    "ListMediaPipelinesRequestRequestTypeDef",
    "MediaPipelineSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "LiveConnectorRTMPConfigurationTypeDef",
    "S3RecordingSinkConfigurationTypeDef",
    "SnsTopicSinkConfigurationTypeDef",
    "SqsQueueSinkConfigurationTypeDef",
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    "SentimentConfigurationTypeDef",
    "SelectedVideoStreamsOutputTypeDef",
    "SelectedVideoStreamsTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    "ArtifactsConcatenationConfigurationTypeDef",
    "StreamChannelDefinitionOutputTypeDef",
    "StreamChannelDefinitionTypeDef",
    "ConcatenationSinkTypeDef",
    "TagResourceRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "FragmentSelectorOutputTypeDef",
    "GridViewConfigurationTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    "ListMediaPipelinesResponseTypeDef",
    "LiveConnectorSinkConfigurationTypeDef",
    "RealTimeAlertRuleOutputTypeDef",
    "RealTimeAlertRuleTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "TimestampRangeTypeDef",
    "MediaInsightsPipelineConfigurationElementOutputTypeDef",
    "MediaInsightsPipelineConfigurationElementTypeDef",
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    "StreamConfigurationOutputTypeDef",
    "StreamConfigurationTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef",
    "CompositedVideoArtifactsConfigurationTypeDef",
    "RealTimeAlertConfigurationOutputTypeDef",
    "RealTimeAlertConfigurationTypeDef",
    "FragmentSelectorTypeDef",
    "MediaInsightsPipelineConfigurationElementUnionTypeDef",
    "MediaCapturePipelineSourceConfigurationTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    "ArtifactsConfigurationTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    "MediaInsightsPipelineConfigurationTypeDef",
    "RealTimeAlertConfigurationUnionTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    "CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "ConcatenationSourceTypeDef",
    "MediaInsightsPipelineTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationUnionTypeDef",
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "LiveConnectorSourceConfigurationOutputTypeDef",
    "LiveConnectorSourceConfigurationTypeDef",
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    "CreateMediaInsightsPipelineRequestRequestTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationUnionTypeDef",
    "CreateMediaConcatenationPipelineRequestRequestTypeDef",
    "MediaConcatenationPipelineTypeDef",
    "CreateMediaInsightsPipelineResponseTypeDef",
    "MediaCapturePipelineTypeDef",
    "ChimeSdkMeetingConfigurationUnionTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "MediaLiveConnectorPipelineTypeDef",
    "LiveConnectorSourceConfigurationUnionTypeDef",
    "CreateMediaConcatenationPipelineResponseTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    "MediaPipelineTypeDef",
    "CreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    "GetMediaPipelineResponseTypeDef",
)

ActiveSpeakerOnlyConfigurationTypeDef = TypedDict(
    "ActiveSpeakerOnlyConfigurationTypeDef",
    {
        "ActiveSpeakerPosition": ActiveSpeakerPositionType,
    },
    total=False,
)

_RequiredPostCallAnalyticsSettingsTypeDef = TypedDict(
    "_RequiredPostCallAnalyticsSettingsTypeDef",
    {
        "OutputLocation": str,
        "DataAccessRoleArn": str,
    },
)
_OptionalPostCallAnalyticsSettingsTypeDef = TypedDict(
    "_OptionalPostCallAnalyticsSettingsTypeDef",
    {
        "ContentRedactionOutput": ContentRedactionOutputType,
        "OutputEncryptionKMSKeyId": str,
    },
    total=False,
)


class PostCallAnalyticsSettingsTypeDef(
    _RequiredPostCallAnalyticsSettingsTypeDef, _OptionalPostCallAnalyticsSettingsTypeDef
):
    pass


AmazonTranscribeProcessorConfigurationTypeDef = TypedDict(
    "AmazonTranscribeProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "ShowSpeakerLabel": bool,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "FilterPartialResults": bool,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": CallAnalyticsLanguageCodeType,
        "VocabularyNames": str,
        "VocabularyFilterNames": str,
    },
    total=False,
)

AudioConcatenationConfigurationTypeDef = TypedDict(
    "AudioConcatenationConfigurationTypeDef",
    {
        "State": Literal["Enabled"],
    },
)

CompositedVideoConcatenationConfigurationTypeDef = TypedDict(
    "CompositedVideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

ContentConcatenationConfigurationTypeDef = TypedDict(
    "ContentConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

DataChannelConcatenationConfigurationTypeDef = TypedDict(
    "DataChannelConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

MeetingEventsConcatenationConfigurationTypeDef = TypedDict(
    "MeetingEventsConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

TranscriptionMessagesConcatenationConfigurationTypeDef = TypedDict(
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

VideoConcatenationConfigurationTypeDef = TypedDict(
    "VideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)

_RequiredContentArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredContentArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalContentArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalContentArtifactsConfigurationTypeDef",
    {
        "MuxType": Literal["ContentOnly"],
    },
    total=False,
)


class ContentArtifactsConfigurationTypeDef(
    _RequiredContentArtifactsConfigurationTypeDef, _OptionalContentArtifactsConfigurationTypeDef
):
    pass


_RequiredVideoArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredVideoArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalVideoArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalVideoArtifactsConfigurationTypeDef",
    {
        "MuxType": Literal["VideoOnly"],
    },
    total=False,
)


class VideoArtifactsConfigurationTypeDef(
    _RequiredVideoArtifactsConfigurationTypeDef, _OptionalVideoArtifactsConfigurationTypeDef
):
    pass


_RequiredChannelDefinitionTypeDef = TypedDict(
    "_RequiredChannelDefinitionTypeDef",
    {
        "ChannelId": int,
    },
)
_OptionalChannelDefinitionTypeDef = TypedDict(
    "_OptionalChannelDefinitionTypeDef",
    {
        "ParticipantRole": ParticipantRoleType,
    },
    total=False,
)


class ChannelDefinitionTypeDef(
    _RequiredChannelDefinitionTypeDef, _OptionalChannelDefinitionTypeDef
):
    pass


S3BucketSinkConfigurationTypeDef = TypedDict(
    "S3BucketSinkConfigurationTypeDef",
    {
        "Destination": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

S3RecordingSinkRuntimeConfigurationTypeDef = TypedDict(
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
)

DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteMediaPipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

TimestampRangeOutputTypeDef = TypedDict(
    "TimestampRangeOutputTypeDef",
    {
        "StartTimestamp": datetime,
        "EndTimestamp": datetime,
    },
)

GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetMediaPipelineRequestRequestTypeDef = TypedDict(
    "GetMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

HorizontalLayoutConfigurationTypeDef = TypedDict(
    "HorizontalLayoutConfigurationTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": HorizontalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

PresenterOnlyConfigurationTypeDef = TypedDict(
    "PresenterOnlyConfigurationTypeDef",
    {
        "PresenterPosition": PresenterPositionType,
    },
    total=False,
)

VerticalLayoutConfigurationTypeDef = TypedDict(
    "VerticalLayoutConfigurationTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": VerticalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

VideoAttributeTypeDef = TypedDict(
    "VideoAttributeTypeDef",
    {
        "CornerRadius": int,
        "BorderColor": BorderColorType,
        "HighlightColor": HighlightColorType,
        "BorderThickness": int,
    },
    total=False,
)

IssueDetectionConfigurationTypeDef = TypedDict(
    "IssueDetectionConfigurationTypeDef",
    {
        "RuleName": str,
    },
)

_RequiredKeywordMatchConfigurationOutputTypeDef = TypedDict(
    "_RequiredKeywordMatchConfigurationOutputTypeDef",
    {
        "RuleName": str,
        "Keywords": List[str],
    },
)
_OptionalKeywordMatchConfigurationOutputTypeDef = TypedDict(
    "_OptionalKeywordMatchConfigurationOutputTypeDef",
    {
        "Negate": bool,
    },
    total=False,
)


class KeywordMatchConfigurationOutputTypeDef(
    _RequiredKeywordMatchConfigurationOutputTypeDef, _OptionalKeywordMatchConfigurationOutputTypeDef
):
    pass


_RequiredKeywordMatchConfigurationTypeDef = TypedDict(
    "_RequiredKeywordMatchConfigurationTypeDef",
    {
        "RuleName": str,
        "Keywords": Sequence[str],
    },
)
_OptionalKeywordMatchConfigurationTypeDef = TypedDict(
    "_OptionalKeywordMatchConfigurationTypeDef",
    {
        "Negate": bool,
    },
    total=False,
)


class KeywordMatchConfigurationTypeDef(
    _RequiredKeywordMatchConfigurationTypeDef, _OptionalKeywordMatchConfigurationTypeDef
):
    pass


KinesisDataStreamSinkConfigurationTypeDef = TypedDict(
    "KinesisDataStreamSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

RecordingStreamConfigurationTypeDef = TypedDict(
    "RecordingStreamConfigurationTypeDef",
    {
        "StreamArn": str,
    },
    total=False,
)

LambdaFunctionSinkConfigurationTypeDef = TypedDict(
    "LambdaFunctionSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MediaCapturePipelineSummaryTypeDef = TypedDict(
    "MediaCapturePipelineSummaryTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
    },
    total=False,
)

ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MediaInsightsPipelineConfigurationSummaryTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "MediaInsightsPipelineConfigurationId": str,
        "MediaInsightsPipelineConfigurationArn": str,
    },
    total=False,
)

ListMediaPipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaPipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MediaPipelineSummaryTypeDef = TypedDict(
    "MediaPipelineSummaryTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

_RequiredLiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "_RequiredLiveConnectorRTMPConfigurationTypeDef",
    {
        "Url": str,
    },
)
_OptionalLiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "_OptionalLiveConnectorRTMPConfigurationTypeDef",
    {
        "AudioChannels": AudioChannelsOptionType,
        "AudioSampleRate": str,
    },
    total=False,
)


class LiveConnectorRTMPConfigurationTypeDef(
    _RequiredLiveConnectorRTMPConfigurationTypeDef, _OptionalLiveConnectorRTMPConfigurationTypeDef
):
    pass


S3RecordingSinkConfigurationTypeDef = TypedDict(
    "S3RecordingSinkConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
    total=False,
)

SnsTopicSinkConfigurationTypeDef = TypedDict(
    "SnsTopicSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

SqsQueueSinkConfigurationTypeDef = TypedDict(
    "SqsQueueSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

VoiceAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    {
        "SpeakerSearchStatus": VoiceAnalyticsConfigurationStatusType,
        "VoiceToneAnalysisStatus": VoiceAnalyticsConfigurationStatusType,
    },
    total=False,
)

SentimentConfigurationTypeDef = TypedDict(
    "SentimentConfigurationTypeDef",
    {
        "RuleName": str,
        "SentimentType": Literal["NEGATIVE"],
        "TimePeriod": int,
    },
)

SelectedVideoStreamsOutputTypeDef = TypedDict(
    "SelectedVideoStreamsOutputTypeDef",
    {
        "AttendeeIds": List[str],
        "ExternalUserIds": List[str],
    },
    total=False,
)

SelectedVideoStreamsTypeDef = TypedDict(
    "SelectedVideoStreamsTypeDef",
    {
        "AttendeeIds": Sequence[str],
        "ExternalUserIds": Sequence[str],
    },
    total=False,
)

TimestampTypeDef = Union[datetime, str]
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateMediaInsightsPipelineStatusRequestRequestTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    {
        "Identifier": str,
        "UpdateStatus": MediaPipelineStatusUpdateType,
    },
)

_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef = TypedDict(
    "_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
    },
)
_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef = TypedDict(
    "_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    {
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "LanguageModelName": str,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "FilterPartialResults": bool,
        "PostCallAnalyticsSettings": PostCallAnalyticsSettingsTypeDef,
        "CallAnalyticsStreamCategories": List[str],
    },
    total=False,
)


class AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef(
    _RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef,
    _OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef,
):
    pass


_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
    },
)
_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "LanguageModelName": str,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "FilterPartialResults": bool,
        "PostCallAnalyticsSettings": PostCallAnalyticsSettingsTypeDef,
        "CallAnalyticsStreamCategories": Sequence[str],
    },
    total=False,
)


class AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef(
    _RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
    _OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
):
    pass


ArtifactsConcatenationConfigurationTypeDef = TypedDict(
    "ArtifactsConcatenationConfigurationTypeDef",
    {
        "Audio": AudioConcatenationConfigurationTypeDef,
        "Video": VideoConcatenationConfigurationTypeDef,
        "Content": ContentConcatenationConfigurationTypeDef,
        "DataChannel": DataChannelConcatenationConfigurationTypeDef,
        "TranscriptionMessages": TranscriptionMessagesConcatenationConfigurationTypeDef,
        "MeetingEvents": MeetingEventsConcatenationConfigurationTypeDef,
        "CompositedVideo": CompositedVideoConcatenationConfigurationTypeDef,
    },
)

_RequiredStreamChannelDefinitionOutputTypeDef = TypedDict(
    "_RequiredStreamChannelDefinitionOutputTypeDef",
    {
        "NumberOfChannels": int,
    },
)
_OptionalStreamChannelDefinitionOutputTypeDef = TypedDict(
    "_OptionalStreamChannelDefinitionOutputTypeDef",
    {
        "ChannelDefinitions": List[ChannelDefinitionTypeDef],
    },
    total=False,
)


class StreamChannelDefinitionOutputTypeDef(
    _RequiredStreamChannelDefinitionOutputTypeDef, _OptionalStreamChannelDefinitionOutputTypeDef
):
    pass


_RequiredStreamChannelDefinitionTypeDef = TypedDict(
    "_RequiredStreamChannelDefinitionTypeDef",
    {
        "NumberOfChannels": int,
    },
)
_OptionalStreamChannelDefinitionTypeDef = TypedDict(
    "_OptionalStreamChannelDefinitionTypeDef",
    {
        "ChannelDefinitions": Sequence[ChannelDefinitionTypeDef],
    },
    total=False,
)


class StreamChannelDefinitionTypeDef(
    _RequiredStreamChannelDefinitionTypeDef, _OptionalStreamChannelDefinitionTypeDef
):
    pass


ConcatenationSinkTypeDef = TypedDict(
    "ConcatenationSinkTypeDef",
    {
        "Type": Literal["S3Bucket"],
        "S3BucketSinkConfiguration": S3BucketSinkConfigurationTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FragmentSelectorOutputTypeDef = TypedDict(
    "FragmentSelectorOutputTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeOutputTypeDef,
    },
)

_RequiredGridViewConfigurationTypeDef = TypedDict(
    "_RequiredGridViewConfigurationTypeDef",
    {
        "ContentShareLayout": ContentShareLayoutOptionType,
    },
)
_OptionalGridViewConfigurationTypeDef = TypedDict(
    "_OptionalGridViewConfigurationTypeDef",
    {
        "PresenterOnlyConfiguration": PresenterOnlyConfigurationTypeDef,
        "ActiveSpeakerOnlyConfiguration": ActiveSpeakerOnlyConfigurationTypeDef,
        "HorizontalLayoutConfiguration": HorizontalLayoutConfigurationTypeDef,
        "VerticalLayoutConfiguration": VerticalLayoutConfigurationTypeDef,
        "VideoAttribute": VideoAttributeTypeDef,
        "CanvasOrientation": CanvasOrientationType,
    },
    total=False,
)


class GridViewConfigurationTypeDef(
    _RequiredGridViewConfigurationTypeDef, _OptionalGridViewConfigurationTypeDef
):
    pass


ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List[MediaCapturePipelineSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMediaInsightsPipelineConfigurationsResponseTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    {
        "MediaInsightsPipelineConfigurations": List[
            MediaInsightsPipelineConfigurationSummaryTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMediaPipelinesResponseTypeDef = TypedDict(
    "ListMediaPipelinesResponseTypeDef",
    {
        "MediaPipelines": List[MediaPipelineSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LiveConnectorSinkConfigurationTypeDef = TypedDict(
    "LiveConnectorSinkConfigurationTypeDef",
    {
        "SinkType": Literal["RTMP"],
        "RTMPConfiguration": LiveConnectorRTMPConfigurationTypeDef,
    },
)

_RequiredRealTimeAlertRuleOutputTypeDef = TypedDict(
    "_RequiredRealTimeAlertRuleOutputTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
    },
)
_OptionalRealTimeAlertRuleOutputTypeDef = TypedDict(
    "_OptionalRealTimeAlertRuleOutputTypeDef",
    {
        "KeywordMatchConfiguration": KeywordMatchConfigurationOutputTypeDef,
        "SentimentConfiguration": SentimentConfigurationTypeDef,
        "IssueDetectionConfiguration": IssueDetectionConfigurationTypeDef,
    },
    total=False,
)


class RealTimeAlertRuleOutputTypeDef(
    _RequiredRealTimeAlertRuleOutputTypeDef, _OptionalRealTimeAlertRuleOutputTypeDef
):
    pass


_RequiredRealTimeAlertRuleTypeDef = TypedDict(
    "_RequiredRealTimeAlertRuleTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
    },
)
_OptionalRealTimeAlertRuleTypeDef = TypedDict(
    "_OptionalRealTimeAlertRuleTypeDef",
    {
        "KeywordMatchConfiguration": KeywordMatchConfigurationTypeDef,
        "SentimentConfiguration": SentimentConfigurationTypeDef,
        "IssueDetectionConfiguration": IssueDetectionConfigurationTypeDef,
    },
    total=False,
)


class RealTimeAlertRuleTypeDef(
    _RequiredRealTimeAlertRuleTypeDef, _OptionalRealTimeAlertRuleTypeDef
):
    pass


SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "SelectedVideoStreams": SelectedVideoStreamsOutputTypeDef,
    },
    total=False,
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "SelectedVideoStreams": SelectedVideoStreamsTypeDef,
    },
    total=False,
)

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": TimestampTypeDef,
        "EndTimestamp": TimestampTypeDef,
    },
)

_RequiredMediaInsightsPipelineConfigurationElementOutputTypeDef = TypedDict(
    "_RequiredMediaInsightsPipelineConfigurationElementOutputTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
    },
)
_OptionalMediaInsightsPipelineConfigurationElementOutputTypeDef = TypedDict(
    "_OptionalMediaInsightsPipelineConfigurationElementOutputTypeDef",
    {
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": (
            AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef
        ),
        "AmazonTranscribeProcessorConfiguration": AmazonTranscribeProcessorConfigurationTypeDef,
        "KinesisDataStreamSinkConfiguration": KinesisDataStreamSinkConfigurationTypeDef,
        "S3RecordingSinkConfiguration": S3RecordingSinkConfigurationTypeDef,
        "VoiceAnalyticsProcessorConfiguration": VoiceAnalyticsProcessorConfigurationTypeDef,
        "LambdaFunctionSinkConfiguration": LambdaFunctionSinkConfigurationTypeDef,
        "SqsQueueSinkConfiguration": SqsQueueSinkConfigurationTypeDef,
        "SnsTopicSinkConfiguration": SnsTopicSinkConfigurationTypeDef,
    },
    total=False,
)


class MediaInsightsPipelineConfigurationElementOutputTypeDef(
    _RequiredMediaInsightsPipelineConfigurationElementOutputTypeDef,
    _OptionalMediaInsightsPipelineConfigurationElementOutputTypeDef,
):
    pass


_RequiredMediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "_RequiredMediaInsightsPipelineConfigurationElementTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
    },
)
_OptionalMediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "_OptionalMediaInsightsPipelineConfigurationElementTypeDef",
    {
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": (
            AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef
        ),
        "AmazonTranscribeProcessorConfiguration": AmazonTranscribeProcessorConfigurationTypeDef,
        "KinesisDataStreamSinkConfiguration": KinesisDataStreamSinkConfigurationTypeDef,
        "S3RecordingSinkConfiguration": S3RecordingSinkConfigurationTypeDef,
        "VoiceAnalyticsProcessorConfiguration": VoiceAnalyticsProcessorConfigurationTypeDef,
        "LambdaFunctionSinkConfiguration": LambdaFunctionSinkConfigurationTypeDef,
        "SqsQueueSinkConfiguration": SqsQueueSinkConfigurationTypeDef,
        "SnsTopicSinkConfiguration": SnsTopicSinkConfigurationTypeDef,
    },
    total=False,
)


class MediaInsightsPipelineConfigurationElementTypeDef(
    _RequiredMediaInsightsPipelineConfigurationElementTypeDef,
    _OptionalMediaInsightsPipelineConfigurationElementTypeDef,
):
    pass


ChimeSdkMeetingConcatenationConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    {
        "ArtifactsConfiguration": ArtifactsConcatenationConfigurationTypeDef,
    },
)

_RequiredStreamConfigurationOutputTypeDef = TypedDict(
    "_RequiredStreamConfigurationOutputTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": StreamChannelDefinitionOutputTypeDef,
    },
)
_OptionalStreamConfigurationOutputTypeDef = TypedDict(
    "_OptionalStreamConfigurationOutputTypeDef",
    {
        "FragmentNumber": str,
    },
    total=False,
)


class StreamConfigurationOutputTypeDef(
    _RequiredStreamConfigurationOutputTypeDef, _OptionalStreamConfigurationOutputTypeDef
):
    pass


_RequiredStreamConfigurationTypeDef = TypedDict(
    "_RequiredStreamConfigurationTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": StreamChannelDefinitionTypeDef,
    },
)
_OptionalStreamConfigurationTypeDef = TypedDict(
    "_OptionalStreamConfigurationTypeDef",
    {
        "FragmentNumber": str,
    },
    total=False,
)


class StreamConfigurationTypeDef(
    _RequiredStreamConfigurationTypeDef, _OptionalStreamConfigurationTypeDef
):
    pass


KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef",
    {
        "Streams": List[RecordingStreamConfigurationTypeDef],
        "FragmentSelector": FragmentSelectorOutputTypeDef,
    },
)

_RequiredCompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredCompositedVideoArtifactsConfigurationTypeDef",
    {
        "GridViewConfiguration": GridViewConfigurationTypeDef,
    },
)
_OptionalCompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalCompositedVideoArtifactsConfigurationTypeDef",
    {
        "Layout": Literal["GridView"],
        "Resolution": ResolutionOptionType,
    },
    total=False,
)


class CompositedVideoArtifactsConfigurationTypeDef(
    _RequiredCompositedVideoArtifactsConfigurationTypeDef,
    _OptionalCompositedVideoArtifactsConfigurationTypeDef,
):
    pass


RealTimeAlertConfigurationOutputTypeDef = TypedDict(
    "RealTimeAlertConfigurationOutputTypeDef",
    {
        "Disabled": bool,
        "Rules": List[RealTimeAlertRuleOutputTypeDef],
    },
    total=False,
)

RealTimeAlertConfigurationTypeDef = TypedDict(
    "RealTimeAlertConfigurationTypeDef",
    {
        "Disabled": bool,
        "Rules": Sequence[RealTimeAlertRuleTypeDef],
    },
    total=False,
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeTypeDef,
    },
)

MediaInsightsPipelineConfigurationElementUnionTypeDef = Union[
    MediaInsightsPipelineConfigurationElementTypeDef,
    MediaInsightsPipelineConfigurationElementOutputTypeDef,
]
MediaCapturePipelineSourceConfigurationTypeDef = TypedDict(
    "MediaCapturePipelineSourceConfigurationTypeDef",
    {
        "MediaPipelineArn": str,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConcatenationConfigurationTypeDef,
    },
)

KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef",
    {
        "Streams": List[StreamConfigurationOutputTypeDef],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)

KinesisVideoStreamSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    {
        "Streams": Sequence[StreamConfigurationTypeDef],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)

_RequiredArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredArtifactsConfigurationTypeDef",
    {
        "Audio": AudioArtifactsConfigurationTypeDef,
        "Video": VideoArtifactsConfigurationTypeDef,
        "Content": ContentArtifactsConfigurationTypeDef,
    },
)
_OptionalArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalArtifactsConfigurationTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationTypeDef,
    },
    total=False,
)


class ArtifactsConfigurationTypeDef(
    _RequiredArtifactsConfigurationTypeDef, _OptionalArtifactsConfigurationTypeDef
):
    pass


_RequiredChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef = TypedDict(
    "_RequiredChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
    },
)
_OptionalChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef = TypedDict(
    "_OptionalChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationTypeDef,
        "SourceConfiguration": SourceConfigurationOutputTypeDef,
    },
    total=False,
)


class ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef(
    _RequiredChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef,
    _OptionalChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef,
):
    pass


_RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "_RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
    },
)
_OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "_OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationTypeDef,
        "SourceConfiguration": SourceConfigurationTypeDef,
    },
    total=False,
)


class ChimeSdkMeetingLiveConnectorConfigurationTypeDef(
    _RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef,
    _OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef,
):
    pass


MediaInsightsPipelineConfigurationTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "MediaInsightsPipelineConfigurationArn": str,
        "ResourceAccessRoleArn": str,
        "RealTimeAlertConfiguration": RealTimeAlertConfigurationOutputTypeDef,
        "Elements": List[MediaInsightsPipelineConfigurationElementOutputTypeDef],
        "MediaInsightsPipelineConfigurationId": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

RealTimeAlertConfigurationUnionTypeDef = Union[
    RealTimeAlertConfigurationTypeDef, RealTimeAlertConfigurationOutputTypeDef
]
KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    {
        "Streams": Sequence[RecordingStreamConfigurationTypeDef],
        "FragmentSelector": FragmentSelectorTypeDef,
    },
)

_RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "ResourceAccessRoleArn": str,
        "Elements": Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef],
    },
)
_OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "RealTimeAlertConfiguration": RealTimeAlertConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef(
    _RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
    _OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "ResourceAccessRoleArn": str,
        "Elements": Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef],
    },
)
_OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "RealTimeAlertConfiguration": RealTimeAlertConfigurationTypeDef,
    },
    total=False,
)


class UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef(
    _RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
    _OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
):
    pass


ConcatenationSourceTypeDef = TypedDict(
    "ConcatenationSourceTypeDef",
    {
        "Type": Literal["MediaCapturePipeline"],
        "MediaCapturePipelineSourceConfiguration": MediaCapturePipelineSourceConfigurationTypeDef,
    },
)

MediaInsightsPipelineTypeDef = TypedDict(
    "MediaInsightsPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "MediaInsightsPipelineConfigurationArn": str,
        "Status": MediaPipelineStatusType,
        "KinesisVideoStreamSourceRuntimeConfiguration": (
            KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef
        ),
        "MediaInsightsRuntimeMetadata": Dict[str, str],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": (
            KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef
        ),
        "S3RecordingSinkRuntimeConfiguration": S3RecordingSinkRuntimeConfigurationTypeDef,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

KinesisVideoStreamSourceRuntimeConfigurationUnionTypeDef = Union[
    KinesisVideoStreamSourceRuntimeConfigurationTypeDef,
    KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef,
]
ChimeSdkMeetingConfigurationOutputTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    {
        "SourceConfiguration": SourceConfigurationOutputTypeDef,
        "ArtifactsConfiguration": ArtifactsConfigurationTypeDef,
    },
    total=False,
)

ChimeSdkMeetingConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationTypeDef",
    {
        "SourceConfiguration": SourceConfigurationTypeDef,
        "ArtifactsConfiguration": ArtifactsConfigurationTypeDef,
    },
    total=False,
)

LiveConnectorSourceConfigurationOutputTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationOutputTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": (
            ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef
        ),
    },
)

LiveConnectorSourceConfigurationTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": (
            ChimeSdkMeetingLiveConnectorConfigurationTypeDef
        ),
    },
)

CreateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationArn": str,
    },
)
_OptionalCreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "KinesisVideoStreamSourceRuntimeConfiguration": (
            KinesisVideoStreamSourceRuntimeConfigurationTypeDef
        ),
        "MediaInsightsRuntimeMetadata": Mapping[str, str],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": (
            KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef
        ),
        "S3RecordingSinkRuntimeConfiguration": S3RecordingSinkRuntimeConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateMediaInsightsPipelineRequestRequestTypeDef(
    _RequiredCreateMediaInsightsPipelineRequestRequestTypeDef,
    _OptionalCreateMediaInsightsPipelineRequestRequestTypeDef,
):
    pass


KinesisVideoStreamRecordingSourceRuntimeConfigurationUnionTypeDef = Union[
    KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef,
    KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef,
]
_RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[ConcatenationSourceTypeDef],
        "Sinks": Sequence[ConcatenationSinkTypeDef],
    },
)
_OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateMediaConcatenationPipelineRequestRequestTypeDef(
    _RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef,
    _OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef,
):
    pass


MediaConcatenationPipelineTypeDef = TypedDict(
    "MediaConcatenationPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "Sources": List[ConcatenationSourceTypeDef],
        "Sinks": List[ConcatenationSinkTypeDef],
        "Status": MediaPipelineStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

CreateMediaInsightsPipelineResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineResponseTypeDef",
    {
        "MediaInsightsPipeline": MediaInsightsPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "Status": MediaPipelineStatusType,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConfigurationOutputTypeDef,
    },
    total=False,
)

ChimeSdkMeetingConfigurationUnionTypeDef = Union[
    ChimeSdkMeetingConfigurationTypeDef, ChimeSdkMeetingConfigurationOutputTypeDef
]
_RequiredCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
    },
)
_OptionalCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateMediaCapturePipelineRequestRequestTypeDef(
    _RequiredCreateMediaCapturePipelineRequestRequestTypeDef,
    _OptionalCreateMediaCapturePipelineRequestRequestTypeDef,
):
    pass


MediaLiveConnectorPipelineTypeDef = TypedDict(
    "MediaLiveConnectorPipelineTypeDef",
    {
        "Sources": List[LiveConnectorSourceConfigurationOutputTypeDef],
        "Sinks": List[LiveConnectorSinkConfigurationTypeDef],
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "Status": MediaPipelineStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

LiveConnectorSourceConfigurationUnionTypeDef = Union[
    LiveConnectorSourceConfigurationTypeDef, LiveConnectorSourceConfigurationOutputTypeDef
]
CreateMediaConcatenationPipelineResponseTypeDef = TypedDict(
    "CreateMediaConcatenationPipelineResponseTypeDef",
    {
        "MediaConcatenationPipeline": MediaConcatenationPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMediaLiveConnectorPipelineResponseTypeDef = TypedDict(
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    {
        "MediaLiveConnectorPipeline": MediaLiveConnectorPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MediaPipelineTypeDef = TypedDict(
    "MediaPipelineTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "MediaLiveConnectorPipeline": MediaLiveConnectorPipelineTypeDef,
        "MediaConcatenationPipeline": MediaConcatenationPipelineTypeDef,
        "MediaInsightsPipeline": MediaInsightsPipelineTypeDef,
    },
    total=False,
)

_RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[LiveConnectorSourceConfigurationUnionTypeDef],
        "Sinks": Sequence[LiveConnectorSinkConfigurationTypeDef],
    },
)
_OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateMediaLiveConnectorPipelineRequestRequestTypeDef(
    _RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef,
    _OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef,
):
    pass


GetMediaPipelineResponseTypeDef = TypedDict(
    "GetMediaPipelineResponseTypeDef",
    {
        "MediaPipeline": MediaPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
