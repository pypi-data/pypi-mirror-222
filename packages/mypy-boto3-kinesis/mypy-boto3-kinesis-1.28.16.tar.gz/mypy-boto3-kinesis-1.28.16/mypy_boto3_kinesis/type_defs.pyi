"""
Type annotations for kinesis service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import AddTagsToStreamInputRequestTypeDef

    data: AddTagsToStreamInputRequestTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    ConsumerStatusType,
    EncryptionTypeType,
    MetricsNameType,
    ShardFilterTypeType,
    ShardIteratorTypeType,
    StreamModeType,
    StreamStatusType,
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
    "AddTagsToStreamInputRequestTypeDef",
    "BlobTypeDef",
    "HashKeyRangeTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "StreamModeDetailsTypeDef",
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DeregisterStreamConsumerInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeStreamConsumerInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeStreamSummaryInputRequestTypeDef",
    "DisableEnhancedMonitoringInputRequestTypeDef",
    "EnableEnhancedMonitoringInputRequestTypeDef",
    "EnhancedMetricsTypeDef",
    "GetRecordsInputRequestTypeDef",
    "RecordTypeDef",
    "TimestampTypeDef",
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "TagTypeDef",
    "MergeShardsInputRequestTypeDef",
    "PutRecordsResultEntryTypeDef",
    "RegisterStreamConsumerInputRequestTypeDef",
    "RemoveTagsFromStreamInputRequestTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "SequenceNumberRangeTypeDef",
    "SplitShardInputRequestTypeDef",
    "StartStreamEncryptionInputRequestTypeDef",
    "StopStreamEncryptionInputRequestTypeDef",
    "UpdateShardCountInputRequestTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "ChildShardTypeDef",
    "CreateStreamInputRequestTypeDef",
    "StreamSummaryTypeDef",
    "UpdateStreamModeInputRequestTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "PutRecordOutputTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "UpdateShardCountOutputTypeDef",
    "DescribeStreamInputDescribeStreamPaginateTypeDef",
    "ListStreamsInputListStreamsPaginateTypeDef",
    "DescribeStreamInputStreamExistsWaitTypeDef",
    "DescribeStreamInputStreamNotExistsWaitTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "ListStreamConsumersInputListStreamConsumersPaginateTypeDef",
    "ListStreamConsumersInputRequestTypeDef",
    "ShardFilterTypeDef",
    "StartingPositionTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PutRecordsOutputTypeDef",
    "ShardTypeDef",
    "PutRecordsInputRequestTypeDef",
    "GetRecordsOutputTypeDef",
    "SubscribeToShardEventTypeDef",
    "ListStreamsOutputTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "ListShardsInputListShardsPaginateTypeDef",
    "ListShardsInputRequestTypeDef",
    "SubscribeToShardInputRequestTypeDef",
    "ListShardsOutputTypeDef",
    "StreamDescriptionTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "DescribeStreamOutputTypeDef",
    "SubscribeToShardOutputTypeDef",
)

_RequiredAddTagsToStreamInputRequestTypeDef = TypedDict(
    "_RequiredAddTagsToStreamInputRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
)
_OptionalAddTagsToStreamInputRequestTypeDef = TypedDict(
    "_OptionalAddTagsToStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class AddTagsToStreamInputRequestTypeDef(
    _RequiredAddTagsToStreamInputRequestTypeDef, _OptionalAddTagsToStreamInputRequestTypeDef
):
    pass

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef",
    {
        "StartingHashKey": str,
        "EndingHashKey": str,
    },
)

ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
    },
)

StreamModeDetailsTypeDef = TypedDict(
    "StreamModeDetailsTypeDef",
    {
        "StreamMode": StreamModeType,
    },
)

_RequiredDecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_RequiredDecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "RetentionPeriodHours": int,
    },
)
_OptionalDecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_OptionalDecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class DecreaseStreamRetentionPeriodInputRequestTypeDef(
    _RequiredDecreaseStreamRetentionPeriodInputRequestTypeDef,
    _OptionalDecreaseStreamRetentionPeriodInputRequestTypeDef,
):
    pass

DeleteStreamInputRequestTypeDef = TypedDict(
    "DeleteStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "EnforceConsumerDeletion": bool,
        "StreamARN": str,
    },
    total=False,
)

DeregisterStreamConsumerInputRequestTypeDef = TypedDict(
    "DeregisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
        "ConsumerARN": str,
    },
    total=False,
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

DescribeStreamConsumerInputRequestTypeDef = TypedDict(
    "DescribeStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
        "ConsumerARN": str,
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

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "Limit": int,
        "ExclusiveStartShardId": str,
        "StreamARN": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeStreamSummaryInputRequestTypeDef = TypedDict(
    "DescribeStreamSummaryInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

_RequiredDisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_RequiredDisableEnhancedMonitoringInputRequestTypeDef",
    {
        "ShardLevelMetrics": Sequence[MetricsNameType],
    },
)
_OptionalDisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_OptionalDisableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class DisableEnhancedMonitoringInputRequestTypeDef(
    _RequiredDisableEnhancedMonitoringInputRequestTypeDef,
    _OptionalDisableEnhancedMonitoringInputRequestTypeDef,
):
    pass

_RequiredEnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_RequiredEnableEnhancedMonitoringInputRequestTypeDef",
    {
        "ShardLevelMetrics": Sequence[MetricsNameType],
    },
)
_OptionalEnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_OptionalEnableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class EnableEnhancedMonitoringInputRequestTypeDef(
    _RequiredEnableEnhancedMonitoringInputRequestTypeDef,
    _OptionalEnableEnhancedMonitoringInputRequestTypeDef,
):
    pass

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": List[MetricsNameType],
    },
    total=False,
)

_RequiredGetRecordsInputRequestTypeDef = TypedDict(
    "_RequiredGetRecordsInputRequestTypeDef",
    {
        "ShardIterator": str,
    },
)
_OptionalGetRecordsInputRequestTypeDef = TypedDict(
    "_OptionalGetRecordsInputRequestTypeDef",
    {
        "Limit": int,
        "StreamARN": str,
    },
    total=False,
)

class GetRecordsInputRequestTypeDef(
    _RequiredGetRecordsInputRequestTypeDef, _OptionalGetRecordsInputRequestTypeDef
):
    pass

_RequiredRecordTypeDef = TypedDict(
    "_RequiredRecordTypeDef",
    {
        "SequenceNumber": str,
        "Data": bytes,
        "PartitionKey": str,
    },
)
_OptionalRecordTypeDef = TypedDict(
    "_OptionalRecordTypeDef",
    {
        "ApproximateArrivalTimestamp": datetime,
        "EncryptionType": EncryptionTypeType,
    },
    total=False,
)

class RecordTypeDef(_RequiredRecordTypeDef, _OptionalRecordTypeDef):
    pass

TimestampTypeDef = Union[datetime, str]
_RequiredIncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_RequiredIncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "RetentionPeriodHours": int,
    },
)
_OptionalIncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_OptionalIncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class IncreaseStreamRetentionPeriodInputRequestTypeDef(
    _RequiredIncreaseStreamRetentionPeriodInputRequestTypeDef,
    _OptionalIncreaseStreamRetentionPeriodInputRequestTypeDef,
):
    pass

InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSOptInRequiredTypeDef = TypedDict(
    "KMSOptInRequiredTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartStreamName": str,
        "NextToken": str,
    },
    total=False,
)

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "ExclusiveStartTagKey": str,
        "Limit": int,
        "StreamARN": str,
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredMergeShardsInputRequestTypeDef = TypedDict(
    "_RequiredMergeShardsInputRequestTypeDef",
    {
        "ShardToMerge": str,
        "AdjacentShardToMerge": str,
    },
)
_OptionalMergeShardsInputRequestTypeDef = TypedDict(
    "_OptionalMergeShardsInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class MergeShardsInputRequestTypeDef(
    _RequiredMergeShardsInputRequestTypeDef, _OptionalMergeShardsInputRequestTypeDef
):
    pass

PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {
        "SequenceNumber": str,
        "ShardId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

RegisterStreamConsumerInputRequestTypeDef = TypedDict(
    "RegisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
    },
)

_RequiredRemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "_RequiredRemoveTagsFromStreamInputRequestTypeDef",
    {
        "TagKeys": Sequence[str],
    },
)
_OptionalRemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "_OptionalRemoveTagsFromStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class RemoveTagsFromStreamInputRequestTypeDef(
    _RequiredRemoveTagsFromStreamInputRequestTypeDef,
    _OptionalRemoveTagsFromStreamInputRequestTypeDef,
):
    pass

ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

_RequiredSequenceNumberRangeTypeDef = TypedDict(
    "_RequiredSequenceNumberRangeTypeDef",
    {
        "StartingSequenceNumber": str,
    },
)
_OptionalSequenceNumberRangeTypeDef = TypedDict(
    "_OptionalSequenceNumberRangeTypeDef",
    {
        "EndingSequenceNumber": str,
    },
    total=False,
)

class SequenceNumberRangeTypeDef(
    _RequiredSequenceNumberRangeTypeDef, _OptionalSequenceNumberRangeTypeDef
):
    pass

_RequiredSplitShardInputRequestTypeDef = TypedDict(
    "_RequiredSplitShardInputRequestTypeDef",
    {
        "ShardToSplit": str,
        "NewStartingHashKey": str,
    },
)
_OptionalSplitShardInputRequestTypeDef = TypedDict(
    "_OptionalSplitShardInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class SplitShardInputRequestTypeDef(
    _RequiredSplitShardInputRequestTypeDef, _OptionalSplitShardInputRequestTypeDef
):
    pass

_RequiredStartStreamEncryptionInputRequestTypeDef = TypedDict(
    "_RequiredStartStreamEncryptionInputRequestTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)
_OptionalStartStreamEncryptionInputRequestTypeDef = TypedDict(
    "_OptionalStartStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class StartStreamEncryptionInputRequestTypeDef(
    _RequiredStartStreamEncryptionInputRequestTypeDef,
    _OptionalStartStreamEncryptionInputRequestTypeDef,
):
    pass

_RequiredStopStreamEncryptionInputRequestTypeDef = TypedDict(
    "_RequiredStopStreamEncryptionInputRequestTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)
_OptionalStopStreamEncryptionInputRequestTypeDef = TypedDict(
    "_OptionalStopStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class StopStreamEncryptionInputRequestTypeDef(
    _RequiredStopStreamEncryptionInputRequestTypeDef,
    _OptionalStopStreamEncryptionInputRequestTypeDef,
):
    pass

_RequiredUpdateShardCountInputRequestTypeDef = TypedDict(
    "_RequiredUpdateShardCountInputRequestTypeDef",
    {
        "TargetShardCount": int,
        "ScalingType": Literal["UNIFORM_SCALING"],
    },
)
_OptionalUpdateShardCountInputRequestTypeDef = TypedDict(
    "_OptionalUpdateShardCountInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class UpdateShardCountInputRequestTypeDef(
    _RequiredUpdateShardCountInputRequestTypeDef, _OptionalUpdateShardCountInputRequestTypeDef
):
    pass

_RequiredPutRecordInputRequestTypeDef = TypedDict(
    "_RequiredPutRecordInputRequestTypeDef",
    {
        "Data": BlobTypeDef,
        "PartitionKey": str,
    },
)
_OptionalPutRecordInputRequestTypeDef = TypedDict(
    "_OptionalPutRecordInputRequestTypeDef",
    {
        "StreamName": str,
        "ExplicitHashKey": str,
        "SequenceNumberForOrdering": str,
        "StreamARN": str,
    },
    total=False,
)

class PutRecordInputRequestTypeDef(
    _RequiredPutRecordInputRequestTypeDef, _OptionalPutRecordInputRequestTypeDef
):
    pass

_RequiredPutRecordsRequestEntryTypeDef = TypedDict(
    "_RequiredPutRecordsRequestEntryTypeDef",
    {
        "Data": BlobTypeDef,
        "PartitionKey": str,
    },
)
_OptionalPutRecordsRequestEntryTypeDef = TypedDict(
    "_OptionalPutRecordsRequestEntryTypeDef",
    {
        "ExplicitHashKey": str,
    },
    total=False,
)

class PutRecordsRequestEntryTypeDef(
    _RequiredPutRecordsRequestEntryTypeDef, _OptionalPutRecordsRequestEntryTypeDef
):
    pass

ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {
        "ShardId": str,
        "ParentShards": List[str],
        "HashKeyRange": HashKeyRangeTypeDef,
    },
)

_RequiredCreateStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalCreateStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateStreamInputRequestTypeDef",
    {
        "ShardCount": int,
        "StreamModeDetails": StreamModeDetailsTypeDef,
    },
    total=False,
)

class CreateStreamInputRequestTypeDef(
    _RequiredCreateStreamInputRequestTypeDef, _OptionalCreateStreamInputRequestTypeDef
):
    pass

_RequiredStreamSummaryTypeDef = TypedDict(
    "_RequiredStreamSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
    },
)
_OptionalStreamSummaryTypeDef = TypedDict(
    "_OptionalStreamSummaryTypeDef",
    {
        "StreamModeDetails": StreamModeDetailsTypeDef,
        "StreamCreationTimestamp": datetime,
    },
    total=False,
)

class StreamSummaryTypeDef(_RequiredStreamSummaryTypeDef, _OptionalStreamSummaryTypeDef):
    pass

UpdateStreamModeInputRequestTypeDef = TypedDict(
    "UpdateStreamModeInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamModeDetails": StreamModeDetailsTypeDef,
    },
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "ShardLimit": int,
        "OpenShardCount": int,
        "OnDemandStreamCount": int,
        "OnDemandStreamCountLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStreamConsumerOutputTypeDef = TypedDict(
    "DescribeStreamConsumerOutputTypeDef",
    {
        "ConsumerDescription": ConsumerDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EnhancedMonitoringOutputTypeDef = TypedDict(
    "EnhancedMonitoringOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[MetricsNameType],
        "DesiredShardLevelMetrics": List[MetricsNameType],
        "StreamARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {
        "Consumers": List[ConsumerTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "ShardId": str,
        "SequenceNumber": str,
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RegisterStreamConsumerOutputTypeDef = TypedDict(
    "RegisterStreamConsumerOutputTypeDef",
    {
        "Consumer": ConsumerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "StreamARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStreamInputDescribeStreamPaginateTypeDef = TypedDict(
    "DescribeStreamInputDescribeStreamPaginateTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListStreamsInputListStreamsPaginateTypeDef = TypedDict(
    "ListStreamsInputListStreamsPaginateTypeDef",
    {
        "ExclusiveStartStreamName": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeStreamInputStreamExistsWaitTypeDef = TypedDict(
    "DescribeStreamInputStreamExistsWaitTypeDef",
    {
        "StreamName": str,
        "Limit": int,
        "ExclusiveStartShardId": str,
        "StreamARN": str,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

DescribeStreamInputStreamNotExistsWaitTypeDef = TypedDict(
    "DescribeStreamInputStreamNotExistsWaitTypeDef",
    {
        "StreamName": str,
        "Limit": int,
        "ExclusiveStartShardId": str,
        "StreamARN": str,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

_RequiredStreamDescriptionSummaryTypeDef = TypedDict(
    "_RequiredStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[EnhancedMetricsTypeDef],
        "OpenShardCount": int,
    },
)
_OptionalStreamDescriptionSummaryTypeDef = TypedDict(
    "_OptionalStreamDescriptionSummaryTypeDef",
    {
        "StreamModeDetails": StreamModeDetailsTypeDef,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
        "ConsumerCount": int,
    },
    total=False,
)

class StreamDescriptionSummaryTypeDef(
    _RequiredStreamDescriptionSummaryTypeDef, _OptionalStreamDescriptionSummaryTypeDef
):
    pass

_RequiredGetShardIteratorInputRequestTypeDef = TypedDict(
    "_RequiredGetShardIteratorInputRequestTypeDef",
    {
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
    },
)
_OptionalGetShardIteratorInputRequestTypeDef = TypedDict(
    "_OptionalGetShardIteratorInputRequestTypeDef",
    {
        "StreamName": str,
        "StartingSequenceNumber": str,
        "Timestamp": TimestampTypeDef,
        "StreamARN": str,
    },
    total=False,
)

class GetShardIteratorInputRequestTypeDef(
    _RequiredGetShardIteratorInputRequestTypeDef, _OptionalGetShardIteratorInputRequestTypeDef
):
    pass

_RequiredListStreamConsumersInputListStreamConsumersPaginateTypeDef = TypedDict(
    "_RequiredListStreamConsumersInputListStreamConsumersPaginateTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalListStreamConsumersInputListStreamConsumersPaginateTypeDef = TypedDict(
    "_OptionalListStreamConsumersInputListStreamConsumersPaginateTypeDef",
    {
        "StreamCreationTimestamp": TimestampTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListStreamConsumersInputListStreamConsumersPaginateTypeDef(
    _RequiredListStreamConsumersInputListStreamConsumersPaginateTypeDef,
    _OptionalListStreamConsumersInputListStreamConsumersPaginateTypeDef,
):
    pass

_RequiredListStreamConsumersInputRequestTypeDef = TypedDict(
    "_RequiredListStreamConsumersInputRequestTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalListStreamConsumersInputRequestTypeDef = TypedDict(
    "_OptionalListStreamConsumersInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StreamCreationTimestamp": TimestampTypeDef,
    },
    total=False,
)

class ListStreamConsumersInputRequestTypeDef(
    _RequiredListStreamConsumersInputRequestTypeDef, _OptionalListStreamConsumersInputRequestTypeDef
):
    pass

_RequiredShardFilterTypeDef = TypedDict(
    "_RequiredShardFilterTypeDef",
    {
        "Type": ShardFilterTypeType,
    },
)
_OptionalShardFilterTypeDef = TypedDict(
    "_OptionalShardFilterTypeDef",
    {
        "ShardId": str,
        "Timestamp": TimestampTypeDef,
    },
    total=False,
)

class ShardFilterTypeDef(_RequiredShardFilterTypeDef, _OptionalShardFilterTypeDef):
    pass

_RequiredStartingPositionTypeDef = TypedDict(
    "_RequiredStartingPositionTypeDef",
    {
        "Type": ShardIteratorTypeType,
    },
)
_OptionalStartingPositionTypeDef = TypedDict(
    "_OptionalStartingPositionTypeDef",
    {
        "SequenceNumber": str,
        "Timestamp": TimestampTypeDef,
    },
    total=False,
)

class StartingPositionTypeDef(_RequiredStartingPositionTypeDef, _OptionalStartingPositionTypeDef):
    pass

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "HasMoreTags": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutRecordsOutputTypeDef = TypedDict(
    "PutRecordsOutputTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List[PutRecordsResultEntryTypeDef],
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredShardTypeDef = TypedDict(
    "_RequiredShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": HashKeyRangeTypeDef,
        "SequenceNumberRange": SequenceNumberRangeTypeDef,
    },
)
_OptionalShardTypeDef = TypedDict(
    "_OptionalShardTypeDef",
    {
        "ParentShardId": str,
        "AdjacentParentShardId": str,
    },
    total=False,
)

class ShardTypeDef(_RequiredShardTypeDef, _OptionalShardTypeDef):
    pass

_RequiredPutRecordsInputRequestTypeDef = TypedDict(
    "_RequiredPutRecordsInputRequestTypeDef",
    {
        "Records": Sequence[PutRecordsRequestEntryTypeDef],
    },
)
_OptionalPutRecordsInputRequestTypeDef = TypedDict(
    "_OptionalPutRecordsInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class PutRecordsInputRequestTypeDef(
    _RequiredPutRecordsInputRequestTypeDef, _OptionalPutRecordsInputRequestTypeDef
):
    pass

GetRecordsOutputTypeDef = TypedDict(
    "GetRecordsOutputTypeDef",
    {
        "Records": List[RecordTypeDef],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
        "ChildShards": List[ChildShardTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredSubscribeToShardEventTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventTypeDef",
    {
        "Records": List[RecordTypeDef],
        "ContinuationSequenceNumber": str,
        "MillisBehindLatest": int,
    },
)
_OptionalSubscribeToShardEventTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventTypeDef",
    {
        "ChildShards": List[ChildShardTypeDef],
    },
    total=False,
)

class SubscribeToShardEventTypeDef(
    _RequiredSubscribeToShardEventTypeDef, _OptionalSubscribeToShardEventTypeDef
):
    pass

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamNames": List[str],
        "HasMoreStreams": bool,
        "NextToken": str,
        "StreamSummaries": List[StreamSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStreamSummaryOutputTypeDef = TypedDict(
    "DescribeStreamSummaryOutputTypeDef",
    {
        "StreamDescriptionSummary": StreamDescriptionSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListShardsInputListShardsPaginateTypeDef = TypedDict(
    "ListShardsInputListShardsPaginateTypeDef",
    {
        "StreamName": str,
        "ExclusiveStartShardId": str,
        "StreamCreationTimestamp": TimestampTypeDef,
        "ShardFilter": ShardFilterTypeDef,
        "StreamARN": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListShardsInputRequestTypeDef = TypedDict(
    "ListShardsInputRequestTypeDef",
    {
        "StreamName": str,
        "NextToken": str,
        "ExclusiveStartShardId": str,
        "MaxResults": int,
        "StreamCreationTimestamp": TimestampTypeDef,
        "ShardFilter": ShardFilterTypeDef,
        "StreamARN": str,
    },
    total=False,
)

SubscribeToShardInputRequestTypeDef = TypedDict(
    "SubscribeToShardInputRequestTypeDef",
    {
        "ConsumerARN": str,
        "ShardId": str,
        "StartingPosition": StartingPositionTypeDef,
    },
)

ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef",
    {
        "Shards": List[ShardTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStreamDescriptionTypeDef = TypedDict(
    "_RequiredStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "Shards": List[ShardTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[EnhancedMetricsTypeDef],
    },
)
_OptionalStreamDescriptionTypeDef = TypedDict(
    "_OptionalStreamDescriptionTypeDef",
    {
        "StreamModeDetails": StreamModeDetailsTypeDef,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
    total=False,
)

class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
    pass

_RequiredSubscribeToShardEventStreamTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventStreamTypeDef",
    {
        "SubscribeToShardEvent": SubscribeToShardEventTypeDef,
    },
)
_OptionalSubscribeToShardEventStreamTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventStreamTypeDef",
    {
        "ResourceNotFoundException": ResourceNotFoundExceptionTypeDef,
        "ResourceInUseException": ResourceInUseExceptionTypeDef,
        "KMSDisabledException": KMSDisabledExceptionTypeDef,
        "KMSInvalidStateException": KMSInvalidStateExceptionTypeDef,
        "KMSAccessDeniedException": KMSAccessDeniedExceptionTypeDef,
        "KMSNotFoundException": KMSNotFoundExceptionTypeDef,
        "KMSOptInRequired": KMSOptInRequiredTypeDef,
        "KMSThrottlingException": KMSThrottlingExceptionTypeDef,
        "InternalFailureException": InternalFailureExceptionTypeDef,
    },
    total=False,
)

class SubscribeToShardEventStreamTypeDef(
    _RequiredSubscribeToShardEventStreamTypeDef, _OptionalSubscribeToShardEventStreamTypeDef
):
    pass

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamDescription": StreamDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SubscribeToShardOutputTypeDef = TypedDict(
    "SubscribeToShardOutputTypeDef",
    {
        "EventStream": "EventStream[SubscribeToShardEventStreamTypeDef]",
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
