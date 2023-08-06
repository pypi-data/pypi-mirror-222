"""
Type annotations for mediapackage service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AdMarkersType,
    AdsOnDeliveryRestrictionsType,
    AdTriggersElementType,
    CmafEncryptionMethodType,
    EncryptionMethodType,
    ManifestLayoutType,
    OriginationType,
    PlaylistTypeType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ProfileType,
    SegmentTemplateFormatType,
    StatusType,
    StreamOrderType,
    UtcTimingType,
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
    "AuthorizationTypeDef",
    "EgressAccessLogsTypeDef",
    "IngressAccessLogsTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "StreamSelectionTypeDef",
    "HlsManifestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "S3DestinationTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteOriginEndpointRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeHarvestJobRequestRequestTypeDef",
    "DescribeOriginEndpointRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "IngestEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListHarvestJobsRequestRequestTypeDef",
    "ListOriginEndpointsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RotateChannelCredentialsRequestRequestTypeDef",
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateHarvestJobRequestRequestTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "HarvestJobTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "HlsIngestTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListHarvestJobsRequestListHarvestJobsPaginateTypeDef",
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "CmafEncryptionOutputTypeDef",
    "DashEncryptionOutputTypeDef",
    "HlsEncryptionOutputTypeDef",
    "MssEncryptionOutputTypeDef",
    "CmafEncryptionTypeDef",
    "DashEncryptionTypeDef",
    "HlsEncryptionTypeDef",
    "MssEncryptionTypeDef",
    "ChannelTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "CmafPackageTypeDef",
    "DashPackageOutputTypeDef",
    "HlsPackageOutputTypeDef",
    "MssPackageOutputTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "DashPackageTypeDef",
    "HlsPackageTypeDef",
    "MssPackageTypeDef",
    "ListChannelsResponseTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "OriginEndpointTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
    "CreateOriginEndpointRequestRequestTypeDef",
    "UpdateOriginEndpointRequestRequestTypeDef",
    "ListOriginEndpointsResponseTypeDef",
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)

EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": str,
    },
    total=False,
)

IngressAccessLogsTypeDef = TypedDict(
    "IngressAccessLogsTypeDef",
    {
        "LogGroupName": str,
    },
    total=False,
)

_RequiredHlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "_RequiredHlsManifestCreateOrUpdateParametersTypeDef",
    {
        "Id": str,
    },
)
_OptionalHlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "_OptionalHlsManifestCreateOrUpdateParametersTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "AdTriggers": Sequence[AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)


class HlsManifestCreateOrUpdateParametersTypeDef(
    _RequiredHlsManifestCreateOrUpdateParametersTypeDef,
    _OptionalHlsManifestCreateOrUpdateParametersTypeDef,
):
    pass


StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": StreamOrderType,
    },
    total=False,
)

_RequiredHlsManifestTypeDef = TypedDict(
    "_RequiredHlsManifestTypeDef",
    {
        "Id": str,
    },
)
_OptionalHlsManifestTypeDef = TypedDict(
    "_OptionalHlsManifestTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
        "AdTriggers": List[AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
    },
    total=False,
)


class HlsManifestTypeDef(_RequiredHlsManifestTypeDef, _OptionalHlsManifestTypeDef):
    pass


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

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass


S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "BucketName": str,
        "ManifestKey": str,
        "RoleArn": str,
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteOriginEndpointRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeHarvestJobRequestRequestTypeDef = TypedDict(
    "DescribeHarvestJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeOriginEndpointRequestRequestTypeDef = TypedDict(
    "DescribeOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)

EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": PresetSpeke20AudioType,
        "PresetSpeke20Video": PresetSpeke20VideoType,
    },
)

IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": str,
        "Password": str,
        "Url": str,
        "Username": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHarvestJobsRequestRequestTypeDef = TypedDict(
    "ListHarvestJobsRequestRequestTypeDef",
    {
        "IncludeChannelId": str,
        "IncludeStatus": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "ListOriginEndpointsRequestRequestTypeDef",
    {
        "ChannelId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

RotateChannelCredentialsRequestRequestTypeDef = TypedDict(
    "RotateChannelCredentialsRequestRequestTypeDef",
    {
        "Id": str,
    },
)

RotateIngestEndpointCredentialsRequestRequestTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    {
        "Id": str,
        "IngestEndpointId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass


_RequiredConfigureLogsRequestRequestTypeDef = TypedDict(
    "_RequiredConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalConfigureLogsRequestRequestTypeDef = TypedDict(
    "_OptionalConfigureLogsRequestRequestTypeDef",
    {
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
    },
    total=False,
)


class ConfigureLogsRequestRequestTypeDef(
    _RequiredConfigureLogsRequestRequestTypeDef, _OptionalConfigureLogsRequestRequestTypeDef
):
    pass


EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateHarvestJobRequestRequestTypeDef = TypedDict(
    "CreateHarvestJobRequestRequestTypeDef",
    {
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
    },
)

CreateHarvestJobResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeHarvestJobResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
    },
    total=False,
)

_RequiredSpekeKeyProviderOutputTypeDef = TypedDict(
    "_RequiredSpekeKeyProviderOutputTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
    },
)
_OptionalSpekeKeyProviderOutputTypeDef = TypedDict(
    "_OptionalSpekeKeyProviderOutputTypeDef",
    {
        "CertificateArn": str,
        "EncryptionContractConfiguration": EncryptionContractConfigurationTypeDef,
    },
    total=False,
)


class SpekeKeyProviderOutputTypeDef(
    _RequiredSpekeKeyProviderOutputTypeDef, _OptionalSpekeKeyProviderOutputTypeDef
):
    pass


_RequiredSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredSpekeKeyProviderTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
    },
)
_OptionalSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalSpekeKeyProviderTypeDef",
    {
        "CertificateArn": str,
        "EncryptionContractConfiguration": EncryptionContractConfigurationTypeDef,
    },
    total=False,
)


class SpekeKeyProviderTypeDef(_RequiredSpekeKeyProviderTypeDef, _OptionalSpekeKeyProviderTypeDef):
    pass


HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef",
    {
        "IngestEndpoints": List[IngestEndpointTypeDef],
    },
    total=False,
)

ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListHarvestJobsRequestListHarvestJobsPaginateTypeDef = TypedDict(
    "ListHarvestJobsRequestListHarvestJobsPaginateTypeDef",
    {
        "IncludeChannelId": str,
        "IncludeStatus": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef = TypedDict(
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    {
        "ChannelId": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {
        "HarvestJobs": List[HarvestJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCmafEncryptionOutputTypeDef = TypedDict(
    "_RequiredCmafEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)
_OptionalCmafEncryptionOutputTypeDef = TypedDict(
    "_OptionalCmafEncryptionOutputTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": CmafEncryptionMethodType,
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)


class CmafEncryptionOutputTypeDef(
    _RequiredCmafEncryptionOutputTypeDef, _OptionalCmafEncryptionOutputTypeDef
):
    pass


_RequiredDashEncryptionOutputTypeDef = TypedDict(
    "_RequiredDashEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)
_OptionalDashEncryptionOutputTypeDef = TypedDict(
    "_OptionalDashEncryptionOutputTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)


class DashEncryptionOutputTypeDef(
    _RequiredDashEncryptionOutputTypeDef, _OptionalDashEncryptionOutputTypeDef
):
    pass


_RequiredHlsEncryptionOutputTypeDef = TypedDict(
    "_RequiredHlsEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)
_OptionalHlsEncryptionOutputTypeDef = TypedDict(
    "_OptionalHlsEncryptionOutputTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": EncryptionMethodType,
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
    },
    total=False,
)


class HlsEncryptionOutputTypeDef(
    _RequiredHlsEncryptionOutputTypeDef, _OptionalHlsEncryptionOutputTypeDef
):
    pass


MssEncryptionOutputTypeDef = TypedDict(
    "MssEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)

_RequiredCmafEncryptionTypeDef = TypedDict(
    "_RequiredCmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)
_OptionalCmafEncryptionTypeDef = TypedDict(
    "_OptionalCmafEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": CmafEncryptionMethodType,
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)


class CmafEncryptionTypeDef(_RequiredCmafEncryptionTypeDef, _OptionalCmafEncryptionTypeDef):
    pass


_RequiredDashEncryptionTypeDef = TypedDict(
    "_RequiredDashEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)
_OptionalDashEncryptionTypeDef = TypedDict(
    "_OptionalDashEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)


class DashEncryptionTypeDef(_RequiredDashEncryptionTypeDef, _OptionalDashEncryptionTypeDef):
    pass


_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": EncryptionMethodType,
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
    },
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderTypeDef,
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)

ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RotateChannelCredentialsResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": CmafEncryptionOutputTypeDef,
        "HlsManifests": List[HlsManifestTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

DashPackageOutputTypeDef = TypedDict(
    "DashPackageOutputTypeDef",
    {
        "AdTriggers": List[AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "Encryption": DashEncryptionOutputTypeDef,
        "IncludeIframeOnlyStream": bool,
        "ManifestLayout": ManifestLayoutType,
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[Literal["ADS"]],
        "Profile": ProfileType,
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": SegmentTemplateFormatType,
        "StreamSelection": StreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
        "UtcTiming": UtcTimingType,
        "UtcTimingUri": str,
    },
    total=False,
)

HlsPackageOutputTypeDef = TypedDict(
    "HlsPackageOutputTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "AdTriggers": List[AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "Encryption": HlsEncryptionOutputTypeDef,
        "IncludeDvbSubtitles": bool,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": StreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

MssPackageOutputTypeDef = TypedDict(
    "MssPackageOutputTypeDef",
    {
        "Encryption": MssEncryptionOutputTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

CmafPackageCreateOrUpdateParametersTypeDef = TypedDict(
    "CmafPackageCreateOrUpdateParametersTypeDef",
    {
        "Encryption": CmafEncryptionTypeDef,
        "HlsManifests": Sequence[HlsManifestCreateOrUpdateParametersTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": Sequence[AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "Encryption": DashEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "ManifestLayout": ManifestLayoutType,
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": Sequence[Literal["ADS"]],
        "Profile": ProfileType,
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": SegmentTemplateFormatType,
        "StreamSelection": StreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
        "UtcTiming": UtcTimingType,
        "UtcTimingUri": str,
    },
    total=False,
)

HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "AdTriggers": Sequence[AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "Encryption": HlsEncryptionTypeDef,
        "IncludeDvbSubtitles": bool,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": StreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": MssEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": StreamSelectionTypeDef,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeOriginEndpointResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelId": str,
        "Id": str,
    },
)
_OptionalCreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOriginEndpointRequestRequestTypeDef",
    {
        "Authorization": AuthorizationTypeDef,
        "CmafPackage": CmafPackageCreateOrUpdateParametersTypeDef,
        "DashPackage": DashPackageTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageTypeDef,
        "ManifestName": str,
        "MssPackage": MssPackageTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Mapping[str, str],
        "TimeDelaySeconds": int,
        "Whitelist": Sequence[str],
    },
    total=False,
)


class CreateOriginEndpointRequestRequestTypeDef(
    _RequiredCreateOriginEndpointRequestRequestTypeDef,
    _OptionalCreateOriginEndpointRequestRequestTypeDef,
):
    pass


_RequiredUpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOriginEndpointRequestRequestTypeDef",
    {
        "Authorization": AuthorizationTypeDef,
        "CmafPackage": CmafPackageCreateOrUpdateParametersTypeDef,
        "DashPackage": DashPackageTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageTypeDef,
        "ManifestName": str,
        "MssPackage": MssPackageTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "TimeDelaySeconds": int,
        "Whitelist": Sequence[str],
    },
    total=False,
)


class UpdateOriginEndpointRequestRequestTypeDef(
    _RequiredUpdateOriginEndpointRequestRequestTypeDef,
    _OptionalUpdateOriginEndpointRequestRequestTypeDef,
):
    pass


ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List[OriginEndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
