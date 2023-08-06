"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs/)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Mapping, Sequence, Set, Union

from boto3.dynamodb.conditions import ConditionBase

from .literals import (
    AttributeActionType,
    BackupStatusType,
    BackupTypeFilterType,
    BackupTypeType,
    BatchStatementErrorCodeEnumType,
    BillingModeType,
    ComparisonOperatorType,
    ConditionalOperatorType,
    ContinuousBackupsStatusType,
    ContributorInsightsActionType,
    ContributorInsightsStatusType,
    DestinationStatusType,
    ExportFormatType,
    ExportStatusType,
    GlobalTableStatusType,
    ImportStatusType,
    IndexStatusType,
    InputCompressionTypeType,
    InputFormatType,
    KeyTypeType,
    PointInTimeRecoveryStatusType,
    ProjectionTypeType,
    ReplicaStatusType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValuesOnConditionCheckFailureType,
    ReturnValueType,
    S3SseAlgorithmType,
    ScalarAttributeTypeType,
    SelectType,
    SSEStatusType,
    SSETypeType,
    StreamViewTypeType,
    TableClassType,
    TableStatusType,
    TimeToLiveStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupInputRequestTypeDef",
    "KeySchemaElementTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputTypeDef",
    "ReplicaTypeDef",
    "CreateReplicaActionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "SSESpecificationTypeDef",
    "StreamSpecificationTypeDef",
    "TagTypeDef",
    "CsvOptionsOutputTypeDef",
    "CsvOptionsTypeDef",
    "DeleteBackupInputRequestTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteTableInputRequestTypeDef",
    "DescribeBackupInputRequestTypeDef",
    "DescribeContinuousBackupsInputRequestTypeDef",
    "DescribeContributorInsightsInputRequestTypeDef",
    "FailureExceptionTypeDef",
    "EndpointTypeDef",
    "DescribeExportInputRequestTypeDef",
    "ExportDescriptionTypeDef",
    "DescribeGlobalTableInputRequestTypeDef",
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    "DescribeImportInputRequestTypeDef",
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "DescribeTableInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    "DescribeTimeToLiveInputRequestTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "ExportSummaryTypeDef",
    "ExportTableToPointInTimeInputRequestTypeDef",
    "GetItemInputTableGetItemTypeDef",
    "ProjectionOutputTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "S3BucketSourceTypeDef",
    "KinesisStreamingDestinationInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListBackupsInputRequestTypeDef",
    "ListContributorInsightsInputRequestTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListGlobalTablesInputRequestTypeDef",
    "ListImportsInputRequestTypeDef",
    "ListTablesInputRequestTypeDef",
    "ListTagsOfResourceInputRequestTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "TableClassSummaryTypeDef",
    "RestoreSummaryTypeDef",
    "SSEDescriptionTypeDef",
    "TableBatchWriterRequestTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateContributorInsightsInputRequestTypeDef",
    "ArchivalSummaryResponseTypeDef",
    "BillingModeSummaryResponseTypeDef",
    "DescribeLimitsOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListTablesOutputTypeDef",
    "ProvisionedThroughputDescriptionResponseTypeDef",
    "RestoreSummaryResponseTypeDef",
    "SSEDescriptionResponseTypeDef",
    "StreamSpecificationResponseTypeDef",
    "TableClassSummaryResponseTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "AttributeValueUpdateTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementRequestTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "DeleteRequestOutputTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "ExpectedAttributeValueTypeDef",
    "GetItemInputRequestTypeDef",
    "GetTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeysAndAttributesOutputTypeDef",
    "KeysAndAttributesTypeDef",
    "ParameterizedStatementTypeDef",
    "PutRequestOutputTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "UpdateTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "CreateBackupOutputTypeDef",
    "ListBackupsOutputTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "LocalSecondaryIndexTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "SourceTableDetailsTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalTableInputRequestTypeDef",
    "GlobalTableTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "InputFormatOptionsOutputTypeDef",
    "InputFormatOptionsTypeDef",
    "ReplicaUpdateTypeDef",
    "DescribeContributorInsightsOutputTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeExportOutputTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    "DescribeTableInputTableExistsWaitTypeDef",
    "DescribeTableInputTableNotExistsWaitTypeDef",
    "DescribeTimeToLiveOutputTypeDef",
    "ListExportsOutputTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexOutputTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "ImportSummaryTypeDef",
    "ListBackupsInputListBackupsPaginateTypeDef",
    "ListTablesInputListTablesPaginateTypeDef",
    "ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    "UpdateContinuousBackupsInputRequestTypeDef",
    "UpdateTimeToLiveInputRequestTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "BatchStatementResponseTypeDef",
    "BatchExecuteStatementInputRequestTypeDef",
    "QueryInputQueryPaginateTypeDef",
    "QueryInputRequestTypeDef",
    "QueryInputTableQueryTypeDef",
    "ScanInputRequestTypeDef",
    "ScanInputScanPaginateTypeDef",
    "ScanInputTableScanTypeDef",
    "DeleteItemInputRequestTypeDef",
    "DeleteItemInputTableDeleteItemTypeDef",
    "PutItemInputRequestTypeDef",
    "PutItemInputTablePutItemTypeDef",
    "UpdateItemInputRequestTypeDef",
    "UpdateItemInputTableUpdateItemTypeDef",
    "TransactGetItemTypeDef",
    "BatchGetItemInputRequestTypeDef",
    "BatchGetItemInputServiceResourceBatchGetItemTypeDef",
    "ExecuteTransactionInputRequestTypeDef",
    "WriteRequestOutputTypeDef",
    "WriteRequestTypeDef",
    "TransactWriteItemTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "BatchGetItemOutputTypeDef",
    "DeleteItemOutputTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "GetItemOutputTypeDef",
    "PutItemOutputTypeDef",
    "QueryOutputTypeDef",
    "ScanOutputTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UpdateItemOutputTypeDef",
    "DescribeContinuousBackupsOutputTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "CreateTableInputRequestTypeDef",
    "CreateTableInputServiceResourceCreateTableTypeDef",
    "RestoreTableFromBackupInputRequestTypeDef",
    "RestoreTableToPointInTimeInputRequestTypeDef",
    "TableCreationParametersTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ReplicaDescriptionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateGlobalTableInputRequestTypeDef",
    "TableCreationParametersOutputTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "ListImportsOutputTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "TransactGetItemsInputRequestTypeDef",
    "BatchWriteItemOutputTypeDef",
    "BatchWriteItemInputRequestTypeDef",
    "BatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    "TransactWriteItemsInputRequestTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ImportTableInputRequestTypeDef",
    "GlobalTableDescriptionTypeDef",
    "TableDescriptionTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "ImportTableDescriptionTypeDef",
    "BackupDescriptionTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "DescribeGlobalTableOutputTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteTableOutputTypeDef",
    "DescribeTableOutputTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "UpdateTableOutputTypeDef",
    "UpdateTableInputRequestTypeDef",
    "UpdateTableInputTableUpdateTypeDef",
    "DescribeImportOutputTypeDef",
    "ImportTableOutputTypeDef",
    "DeleteBackupOutputTypeDef",
    "DescribeBackupOutputTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "DescribeGlobalTableSettingsOutputTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
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

ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
    },
    total=False,
)

AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": Sequence[str],
        "NS": Sequence[str],
        "BS": Sequence[bytes],
        "M": Mapping[str, Any],
        "L": Sequence[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)

class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
):
    pass

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)

class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
):
    pass

_RequiredBackupDetailsTypeDef = TypedDict(
    "_RequiredBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupCreationDateTime": datetime,
    },
)
_OptionalBackupDetailsTypeDef = TypedDict(
    "_OptionalBackupDetailsTypeDef",
    {
        "BackupSizeBytes": int,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)

class BackupDetailsTypeDef(_RequiredBackupDetailsTypeDef, _OptionalBackupDetailsTypeDef):
    pass

BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupSizeBytes": int,
    },
    total=False,
)

BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "CapacityUnits": float,
    },
    total=False,
)

PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": PointInTimeRecoveryStatusType,
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
    },
    total=False,
)

CreateBackupInputRequestTypeDef = TypedDict(
    "CreateBackupInputRequestTypeDef",
    {
        "TableName": str,
        "BackupName": str,
    },
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": Sequence[str],
    },
    total=False,
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

ReplicaTypeDef = TypedDict(
    "ReplicaTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

CreateReplicaActionTypeDef = TypedDict(
    "CreateReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

_RequiredStreamSpecificationTypeDef = TypedDict(
    "_RequiredStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationTypeDef = TypedDict(
    "_OptionalStreamSpecificationTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)

class StreamSpecificationTypeDef(
    _RequiredStreamSpecificationTypeDef, _OptionalStreamSpecificationTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CsvOptionsOutputTypeDef = TypedDict(
    "CsvOptionsOutputTypeDef",
    {
        "Delimiter": str,
        "HeaderList": List[str],
    },
    total=False,
)

CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": str,
        "HeaderList": Sequence[str],
    },
    total=False,
)

DeleteBackupInputRequestTypeDef = TypedDict(
    "DeleteBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
    },
)

DeleteReplicaActionTypeDef = TypedDict(
    "DeleteReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteTableInputRequestTypeDef = TypedDict(
    "DeleteTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeBackupInputRequestTypeDef = TypedDict(
    "DescribeBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DescribeContinuousBackupsInputRequestTypeDef = TypedDict(
    "DescribeContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
    },
)

_RequiredDescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeContributorInsightsInputRequestTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)

class DescribeContributorInsightsInputRequestTypeDef(
    _RequiredDescribeContributorInsightsInputRequestTypeDef,
    _OptionalDescribeContributorInsightsInputRequestTypeDef,
):
    pass

FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef",
    {
        "ExceptionName": str,
        "ExceptionDescription": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

DescribeExportInputRequestTypeDef = TypedDict(
    "DescribeExportInputRequestTypeDef",
    {
        "ExportArn": str,
    },
)

ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ExportManifest": str,
        "TableArn": str,
        "TableId": str,
        "ExportTime": datetime,
        "ClientToken": str,
        "S3Bucket": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "FailureCode": str,
        "FailureMessage": str,
        "ExportFormat": ExportFormatType,
        "BilledSizeBytes": int,
        "ItemCount": int,
    },
    total=False,
)

DescribeGlobalTableInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeImportInputRequestTypeDef = TypedDict(
    "DescribeImportInputRequestTypeDef",
    {
        "ImportArn": str,
    },
)

DescribeKinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
    },
)

KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "DestinationStatusDescription": str,
    },
    total=False,
)

DescribeTableInputRequestTypeDef = TypedDict(
    "DescribeTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTimeToLiveInputRequestTypeDef = TypedDict(
    "DescribeTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
    },
)

TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": TimeToLiveStatusType,
        "AttributeName": str,
    },
    total=False,
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
    },
    total=False,
)

_RequiredExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_RequiredExportTableToPointInTimeInputRequestTypeDef",
    {
        "TableArn": str,
        "S3Bucket": str,
    },
)
_OptionalExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_OptionalExportTableToPointInTimeInputRequestTypeDef",
    {
        "ExportTime": Union[datetime, str],
        "ClientToken": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "ExportFormat": ExportFormatType,
    },
    total=False,
)

class ExportTableToPointInTimeInputRequestTypeDef(
    _RequiredExportTableToPointInTimeInputRequestTypeDef,
    _OptionalExportTableToPointInTimeInputRequestTypeDef,
):
    pass

_RequiredGetItemInputTableGetItemTypeDef = TypedDict(
    "_RequiredGetItemInputTableGetItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputTableGetItemTypeDef = TypedDict(
    "_OptionalGetItemInputTableGetItemTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)

class GetItemInputTableGetItemTypeDef(
    _RequiredGetItemInputTableGetItemTypeDef, _OptionalGetItemInputTableGetItemTypeDef
):
    pass

ProjectionOutputTypeDef = TypedDict(
    "ProjectionOutputTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": List[str],
    },
    total=False,
)

ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

_RequiredS3BucketSourceTypeDef = TypedDict(
    "_RequiredS3BucketSourceTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalS3BucketSourceTypeDef = TypedDict(
    "_OptionalS3BucketSourceTypeDef",
    {
        "S3BucketOwner": str,
        "S3KeyPrefix": str,
    },
    total=False,
)

class S3BucketSourceTypeDef(_RequiredS3BucketSourceTypeDef, _OptionalS3BucketSourceTypeDef):
    pass

KinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "KinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
    },
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

ListBackupsInputRequestTypeDef = TypedDict(
    "ListBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "Limit": int,
        "TimeRangeLowerBound": Union[datetime, str],
        "TimeRangeUpperBound": Union[datetime, str],
        "ExclusiveStartBackupArn": str,
        "BackupType": BackupTypeFilterType,
    },
    total=False,
)

ListContributorInsightsInputRequestTypeDef = TypedDict(
    "ListContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "TableArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGlobalTablesInputRequestTypeDef = TypedDict(
    "ListGlobalTablesInputRequestTypeDef",
    {
        "ExclusiveStartGlobalTableName": str,
        "Limit": int,
        "RegionName": str,
    },
    total=False,
)

ListImportsInputRequestTypeDef = TypedDict(
    "ListImportsInputRequestTypeDef",
    {
        "TableArn": str,
        "PageSize": int,
        "NextToken": str,
    },
    total=False,
)

ListTablesInputRequestTypeDef = TypedDict(
    "ListTablesInputRequestTypeDef",
    {
        "ExclusiveStartTableName": str,
        "Limit": int,
    },
    total=False,
)

_RequiredListTagsOfResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsOfResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsOfResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsOfResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsOfResourceInputRequestTypeDef(
    _RequiredListTagsOfResourceInputRequestTypeDef, _OptionalListTagsOfResourceInputRequestTypeDef
):
    pass

PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef",
    {
        "PointInTimeRecoveryEnabled": bool,
    },
)

TableClassSummaryTypeDef = TypedDict(
    "TableClassSummaryTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
    },
    total=False,
)

_RequiredRestoreSummaryTypeDef = TypedDict(
    "_RequiredRestoreSummaryTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
)
_OptionalRestoreSummaryTypeDef = TypedDict(
    "_OptionalRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
    },
    total=False,
)

class RestoreSummaryTypeDef(_RequiredRestoreSummaryTypeDef, _OptionalRestoreSummaryTypeDef):
    pass

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

TableBatchWriterRequestTypeDef = TypedDict(
    "TableBatchWriterRequestTypeDef",
    {
        "overwrite_by_pkeys": List[str],
    },
    total=False,
)

TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "ContributorInsightsAction": ContributorInsightsActionType,
    },
)
_OptionalUpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateContributorInsightsInputRequestTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)

class UpdateContributorInsightsInputRequestTypeDef(
    _RequiredUpdateContributorInsightsInputRequestTypeDef,
    _OptionalUpdateContributorInsightsInputRequestTypeDef,
):
    pass

ArchivalSummaryResponseTypeDef = TypedDict(
    "ArchivalSummaryResponseTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BillingModeSummaryResponseTypeDef = TypedDict(
    "BillingModeSummaryResponseTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

KinesisStreamingDestinationOutputTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTablesOutputTypeDef = TypedDict(
    "ListTablesOutputTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ProvisionedThroughputDescriptionResponseTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionResponseTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RestoreSummaryResponseTypeDef = TypedDict(
    "RestoreSummaryResponseTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SSEDescriptionResponseTypeDef = TypedDict(
    "SSEDescriptionResponseTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StreamSpecificationResponseTypeDef = TypedDict(
    "StreamSpecificationResponseTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": StreamViewTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TableClassSummaryResponseTypeDef = TypedDict(
    "TableClassSummaryResponseTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateContributorInsightsOutputTypeDef = TypedDict(
    "UpdateContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": Union[
            AttributeValueTypeDef,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
        "Action": AttributeActionType,
    },
    total=False,
)

BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef",
    {
        "Code": BatchStatementErrorCodeEnumType,
        "Message": str,
        "Item": Dict[str, AttributeValueTypeDef],
    },
    total=False,
)

_RequiredBatchStatementRequestTypeDef = TypedDict(
    "_RequiredBatchStatementRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalBatchStatementRequestTypeDef = TypedDict(
    "_OptionalBatchStatementRequestTypeDef",
    {
        "Parameters": Sequence[
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
        "ConsistentRead": bool,
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class BatchStatementRequestTypeDef(
    _RequiredBatchStatementRequestTypeDef, _OptionalBatchStatementRequestTypeDef
):
    pass

_RequiredConditionCheckTypeDef = TypedDict(
    "_RequiredConditionCheckTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ConditionExpression": str,
    },
)
_OptionalConditionCheckTypeDef = TypedDict(
    "_OptionalConditionCheckTypeDef",
    {
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class ConditionCheckTypeDef(_RequiredConditionCheckTypeDef, _OptionalConditionCheckTypeDef):
    pass

_RequiredConditionTypeDef = TypedDict(
    "_RequiredConditionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalConditionTypeDef = TypedDict(
    "_OptionalConditionTypeDef",
    {
        "AttributeValueList": Sequence[
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

class ConditionTypeDef(_RequiredConditionTypeDef, _OptionalConditionTypeDef):
    pass

DeleteRequestOutputTypeDef = TypedDict(
    "DeleteRequestOutputTypeDef",
    {
        "Key": Dict[str, AttributeValueTypeDef],
    },
)

DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass

_RequiredExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementInputRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementInputRequestTypeDef",
    {
        "Parameters": Sequence[
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
        "ConsistentRead": bool,
        "NextToken": str,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "Limit": int,
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class ExecuteStatementInputRequestTypeDef(
    _RequiredExecuteStatementInputRequestTypeDef, _OptionalExecuteStatementInputRequestTypeDef
):
    pass

ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": Union[
            AttributeValueTypeDef,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
        "Exists": bool,
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": Sequence[
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

_RequiredGetItemInputRequestTypeDef = TypedDict(
    "_RequiredGetItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputRequestTypeDef = TypedDict(
    "_OptionalGetItemInputRequestTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)

class GetItemInputRequestTypeDef(
    _RequiredGetItemInputRequestTypeDef, _OptionalGetItemInputRequestTypeDef
):
    pass

_RequiredGetTypeDef = TypedDict(
    "_RequiredGetTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalGetTypeDef = TypedDict(
    "_OptionalGetTypeDef",
    {
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)

class GetTypeDef(_RequiredGetTypeDef, _OptionalGetTypeDef):
    pass

ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[str, AttributeValueTypeDef],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
    },
    total=False,
)

_RequiredKeysAndAttributesOutputTypeDef = TypedDict(
    "_RequiredKeysAndAttributesOutputTypeDef",
    {
        "Keys": List[Dict[str, AttributeValueTypeDef]],
    },
)
_OptionalKeysAndAttributesOutputTypeDef = TypedDict(
    "_OptionalKeysAndAttributesOutputTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

class KeysAndAttributesOutputTypeDef(
    _RequiredKeysAndAttributesOutputTypeDef, _OptionalKeysAndAttributesOutputTypeDef
):
    pass

_RequiredKeysAndAttributesTypeDef = TypedDict(
    "_RequiredKeysAndAttributesTypeDef",
    {
        "Keys": Sequence[
            Mapping[
                str,
                Union[
                    AttributeValueTypeDef,
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)
_OptionalKeysAndAttributesTypeDef = TypedDict(
    "_OptionalKeysAndAttributesTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)

class KeysAndAttributesTypeDef(
    _RequiredKeysAndAttributesTypeDef, _OptionalKeysAndAttributesTypeDef
):
    pass

_RequiredParameterizedStatementTypeDef = TypedDict(
    "_RequiredParameterizedStatementTypeDef",
    {
        "Statement": str,
    },
)
_OptionalParameterizedStatementTypeDef = TypedDict(
    "_OptionalParameterizedStatementTypeDef",
    {
        "Parameters": Sequence[
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class ParameterizedStatementTypeDef(
    _RequiredParameterizedStatementTypeDef, _OptionalParameterizedStatementTypeDef
):
    pass

PutRequestOutputTypeDef = TypedDict(
    "PutRequestOutputTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
    },
)

PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)

_RequiredPutTypeDef = TypedDict(
    "_RequiredPutTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalPutTypeDef = TypedDict(
    "_OptionalPutTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class PutTypeDef(_RequiredPutTypeDef, _OptionalPutTypeDef):
    pass

_RequiredUpdateTypeDef = TypedDict(
    "_RequiredUpdateTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "UpdateExpression": str,
        "TableName": str,
    },
)
_OptionalUpdateTypeDef = TypedDict(
    "_OptionalUpdateTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class UpdateTypeDef(_RequiredUpdateTypeDef, _OptionalUpdateTypeDef):
    pass

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": (
            AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef
        ),
    },
    total=False,
)

_RequiredAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": (
            AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef
        ),
    },
)
_OptionalAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

class AutoScalingPolicyUpdateTypeDef(
    _RequiredAutoScalingPolicyUpdateTypeDef, _OptionalAutoScalingPolicyUpdateTypeDef
):
    pass

CreateBackupOutputTypeDef = TypedDict(
    "CreateBackupOutputTypeDef",
    {
        "BackupDetails": BackupDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupsOutputTypeDef = TypedDict(
    "ListBackupsOutputTypeDef",
    {
        "BackupSummaries": List[BackupSummaryTypeDef],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": CapacityTypeDef,
        "LocalSecondaryIndexes": Dict[str, CapacityTypeDef],
        "GlobalSecondaryIndexes": Dict[str, CapacityTypeDef],
    },
    total=False,
)

_RequiredContinuousBackupsDescriptionTypeDef = TypedDict(
    "_RequiredContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": ContinuousBackupsStatusType,
    },
)
_OptionalContinuousBackupsDescriptionTypeDef = TypedDict(
    "_OptionalContinuousBackupsDescriptionTypeDef",
    {
        "PointInTimeRecoveryDescription": PointInTimeRecoveryDescriptionTypeDef,
    },
    total=False,
)

class ContinuousBackupsDescriptionTypeDef(
    _RequiredContinuousBackupsDescriptionTypeDef, _OptionalContinuousBackupsDescriptionTypeDef
):
    pass

ListContributorInsightsOutputTypeDef = TypedDict(
    "ListContributorInsightsOutputTypeDef",
    {
        "ContributorInsightsSummaries": List[ContributorInsightsSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)

_RequiredCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_RequiredCreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)
_OptionalCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_OptionalCreateGlobalSecondaryIndexActionTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
    total=False,
)

class CreateGlobalSecondaryIndexActionTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTypeDef,
    _OptionalCreateGlobalSecondaryIndexActionTypeDef,
):
    pass

_RequiredGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)
_OptionalGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
    total=False,
)

class GlobalSecondaryIndexTypeDef(
    _RequiredGlobalSecondaryIndexTypeDef, _OptionalGlobalSecondaryIndexTypeDef
):
    pass

_RequiredSourceTableDetailsTypeDef = TypedDict(
    "_RequiredSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
)
_OptionalSourceTableDetailsTypeDef = TypedDict(
    "_OptionalSourceTableDetailsTypeDef",
    {
        "TableArn": str,
        "TableSizeBytes": int,
        "ItemCount": int,
        "BillingMode": BillingModeType,
    },
    total=False,
)

class SourceTableDetailsTypeDef(
    _RequiredSourceTableDetailsTypeDef, _OptionalSourceTableDetailsTypeDef
):
    pass

UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
)

CreateGlobalTableInputRequestTypeDef = TypedDict(
    "CreateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": Sequence[ReplicaTypeDef],
    },
)

GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List[ReplicaTypeDef],
    },
    total=False,
)

ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

class ReplicaGlobalSecondaryIndexTypeDef(
    _RequiredReplicaGlobalSecondaryIndexTypeDef, _OptionalReplicaGlobalSecondaryIndexTypeDef
):
    pass

ListTagsOfResourceOutputTypeDef = TypedDict(
    "ListTagsOfResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

InputFormatOptionsOutputTypeDef = TypedDict(
    "InputFormatOptionsOutputTypeDef",
    {
        "Csv": CsvOptionsOutputTypeDef,
    },
    total=False,
)

InputFormatOptionsTypeDef = TypedDict(
    "InputFormatOptionsTypeDef",
    {
        "Csv": CsvOptionsTypeDef,
    },
    total=False,
)

ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {
        "Create": CreateReplicaActionTypeDef,
        "Delete": DeleteReplicaActionTypeDef,
    },
    total=False,
)

DescribeContributorInsightsOutputTypeDef = TypedDict(
    "DescribeContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "LastUpdateDateTime": datetime,
        "FailureException": FailureExceptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeExportOutputTypeDef = TypedDict(
    "DescribeExportOutputTypeDef",
    {
        "ExportDescription": ExportDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExportTableToPointInTimeOutputTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputTypeDef",
    {
        "ExportDescription": ExportDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeKinesisStreamingDestinationOutputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List[KinesisDataStreamDestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDescribeTableInputTableExistsWaitTypeDef = TypedDict(
    "_RequiredDescribeTableInputTableExistsWaitTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeTableInputTableExistsWaitTypeDef = TypedDict(
    "_OptionalDescribeTableInputTableExistsWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeTableInputTableExistsWaitTypeDef(
    _RequiredDescribeTableInputTableExistsWaitTypeDef,
    _OptionalDescribeTableInputTableExistsWaitTypeDef,
):
    pass

_RequiredDescribeTableInputTableNotExistsWaitTypeDef = TypedDict(
    "_RequiredDescribeTableInputTableNotExistsWaitTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeTableInputTableNotExistsWaitTypeDef = TypedDict(
    "_OptionalDescribeTableInputTableNotExistsWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeTableInputTableNotExistsWaitTypeDef(
    _RequiredDescribeTableInputTableNotExistsWaitTypeDef,
    _OptionalDescribeTableInputTableNotExistsWaitTypeDef,
):
    pass

DescribeTimeToLiveOutputTypeDef = TypedDict(
    "DescribeTimeToLiveOutputTypeDef",
    {
        "TimeToLiveDescription": TimeToLiveDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "ExportSummaries": List[ExportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "Projection": ProjectionOutputTypeDef,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
    total=False,
)

_RequiredGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexOutputTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "Projection": ProjectionOutputTypeDef,
    },
)
_OptionalGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexOutputTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
    total=False,
)

class GlobalSecondaryIndexOutputTypeDef(
    _RequiredGlobalSecondaryIndexOutputTypeDef, _OptionalGlobalSecondaryIndexOutputTypeDef
):
    pass

LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "Projection": ProjectionOutputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "Projection": ProjectionOutputTypeDef,
    },
    total=False,
)

GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "Projection": ProjectionOutputTypeDef,
        "IndexStatus": IndexStatusType,
        "Backfilling": bool,
        "ProvisionedThroughput": ProvisionedThroughputDescriptionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "ImportArn": str,
        "ImportStatus": ImportStatusType,
        "TableArn": str,
        "S3BucketSource": S3BucketSourceTypeDef,
        "CloudWatchLogGroupArn": str,
        "InputFormat": InputFormatType,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ListBackupsInputListBackupsPaginateTypeDef = TypedDict(
    "ListBackupsInputListBackupsPaginateTypeDef",
    {
        "TableName": str,
        "TimeRangeLowerBound": Union[datetime, str],
        "TimeRangeUpperBound": Union[datetime, str],
        "BackupType": BackupTypeFilterType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListTablesInputListTablesPaginateTypeDef = TypedDict(
    "ListTablesInputListTablesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListTagsOfResourceInputListTagsOfResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsOfResourceInputListTagsOfResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef(
    _RequiredListTagsOfResourceInputListTagsOfResourcePaginateTypeDef,
    _OptionalListTagsOfResourceInputListTagsOfResourcePaginateTypeDef,
):
    pass

UpdateContinuousBackupsInputRequestTypeDef = TypedDict(
    "UpdateContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "PointInTimeRecoverySpecification": PointInTimeRecoverySpecificationTypeDef,
    },
)

UpdateTimeToLiveInputRequestTypeDef = TypedDict(
    "UpdateTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
        "TimeToLiveSpecification": TimeToLiveSpecificationTypeDef,
    },
)

UpdateTimeToLiveOutputTypeDef = TypedDict(
    "UpdateTimeToLiveOutputTypeDef",
    {
        "TimeToLiveSpecification": TimeToLiveSpecificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": BatchStatementErrorTypeDef,
        "TableName": str,
        "Item": Dict[str, AttributeValueTypeDef],
    },
    total=False,
)

_RequiredBatchExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredBatchExecuteStatementInputRequestTypeDef",
    {
        "Statements": Sequence[BatchStatementRequestTypeDef],
    },
)
_OptionalBatchExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalBatchExecuteStatementInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class BatchExecuteStatementInputRequestTypeDef(
    _RequiredBatchExecuteStatementInputRequestTypeDef,
    _OptionalBatchExecuteStatementInputRequestTypeDef,
):
    pass

_RequiredQueryInputQueryPaginateTypeDef = TypedDict(
    "_RequiredQueryInputQueryPaginateTypeDef",
    {
        "TableName": str,
    },
)
_OptionalQueryInputQueryPaginateTypeDef = TypedDict(
    "_OptionalQueryInputQueryPaginateTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "KeyConditions": Mapping[str, ConditionTypeDef],
        "QueryFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "KeyConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class QueryInputQueryPaginateTypeDef(
    _RequiredQueryInputQueryPaginateTypeDef, _OptionalQueryInputQueryPaginateTypeDef
):
    pass

_RequiredQueryInputRequestTypeDef = TypedDict(
    "_RequiredQueryInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalQueryInputRequestTypeDef = TypedDict(
    "_OptionalQueryInputRequestTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Mapping[str, ConditionTypeDef],
        "QueryFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "KeyConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class QueryInputRequestTypeDef(
    _RequiredQueryInputRequestTypeDef, _OptionalQueryInputRequestTypeDef
):
    pass

QueryInputTableQueryTypeDef = TypedDict(
    "QueryInputTableQueryTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Mapping[str, ConditionTypeDef],
        "QueryFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "KeyConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

_RequiredScanInputRequestTypeDef = TypedDict(
    "_RequiredScanInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalScanInputRequestTypeDef = TypedDict(
    "_OptionalScanInputRequestTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

class ScanInputRequestTypeDef(_RequiredScanInputRequestTypeDef, _OptionalScanInputRequestTypeDef):
    pass

_RequiredScanInputScanPaginateTypeDef = TypedDict(
    "_RequiredScanInputScanPaginateTypeDef",
    {
        "TableName": str,
    },
)
_OptionalScanInputScanPaginateTypeDef = TypedDict(
    "_OptionalScanInputScanPaginateTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": Sequence[str],
        "Select": SelectType,
        "ScanFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ScanInputScanPaginateTypeDef(
    _RequiredScanInputScanPaginateTypeDef, _OptionalScanInputScanPaginateTypeDef
):
    pass

ScanInputTableScanTypeDef = TypedDict(
    "ScanInputTableScanTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

_RequiredDeleteItemInputRequestTypeDef = TypedDict(
    "_RequiredDeleteItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputRequestTypeDef = TypedDict(
    "_OptionalDeleteItemInputRequestTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class DeleteItemInputRequestTypeDef(
    _RequiredDeleteItemInputRequestTypeDef, _OptionalDeleteItemInputRequestTypeDef
):
    pass

_RequiredDeleteItemInputTableDeleteItemTypeDef = TypedDict(
    "_RequiredDeleteItemInputTableDeleteItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputTableDeleteItemTypeDef = TypedDict(
    "_OptionalDeleteItemInputTableDeleteItemTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class DeleteItemInputTableDeleteItemTypeDef(
    _RequiredDeleteItemInputTableDeleteItemTypeDef, _OptionalDeleteItemInputTableDeleteItemTypeDef
):
    pass

_RequiredPutItemInputRequestTypeDef = TypedDict(
    "_RequiredPutItemInputRequestTypeDef",
    {
        "TableName": str,
        "Item": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputRequestTypeDef = TypedDict(
    "_OptionalPutItemInputRequestTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class PutItemInputRequestTypeDef(
    _RequiredPutItemInputRequestTypeDef, _OptionalPutItemInputRequestTypeDef
):
    pass

_RequiredPutItemInputTablePutItemTypeDef = TypedDict(
    "_RequiredPutItemInputTablePutItemTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputTablePutItemTypeDef = TypedDict(
    "_OptionalPutItemInputTablePutItemTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class PutItemInputTablePutItemTypeDef(
    _RequiredPutItemInputTablePutItemTypeDef, _OptionalPutItemInputTablePutItemTypeDef
):
    pass

_RequiredUpdateItemInputRequestTypeDef = TypedDict(
    "_RequiredUpdateItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputRequestTypeDef = TypedDict(
    "_OptionalUpdateItemInputRequestTypeDef",
    {
        "AttributeUpdates": Mapping[str, AttributeValueUpdateTypeDef],
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class UpdateItemInputRequestTypeDef(
    _RequiredUpdateItemInputRequestTypeDef, _OptionalUpdateItemInputRequestTypeDef
):
    pass

_RequiredUpdateItemInputTableUpdateItemTypeDef = TypedDict(
    "_RequiredUpdateItemInputTableUpdateItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputTableUpdateItemTypeDef = TypedDict(
    "_OptionalUpdateItemInputTableUpdateItemTypeDef",
    {
        "AttributeUpdates": Mapping[str, AttributeValueUpdateTypeDef],
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class UpdateItemInputTableUpdateItemTypeDef(
    _RequiredUpdateItemInputTableUpdateItemTypeDef, _OptionalUpdateItemInputTableUpdateItemTypeDef
):
    pass

TransactGetItemTypeDef = TypedDict(
    "TransactGetItemTypeDef",
    {
        "Get": GetTypeDef,
    },
)

_RequiredBatchGetItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchGetItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, KeysAndAttributesTypeDef],
    },
)
_OptionalBatchGetItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchGetItemInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class BatchGetItemInputRequestTypeDef(
    _RequiredBatchGetItemInputRequestTypeDef, _OptionalBatchGetItemInputRequestTypeDef
):
    pass

_RequiredBatchGetItemInputServiceResourceBatchGetItemTypeDef = TypedDict(
    "_RequiredBatchGetItemInputServiceResourceBatchGetItemTypeDef",
    {
        "RequestItems": Mapping[str, KeysAndAttributesTypeDef],
    },
)
_OptionalBatchGetItemInputServiceResourceBatchGetItemTypeDef = TypedDict(
    "_OptionalBatchGetItemInputServiceResourceBatchGetItemTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class BatchGetItemInputServiceResourceBatchGetItemTypeDef(
    _RequiredBatchGetItemInputServiceResourceBatchGetItemTypeDef,
    _OptionalBatchGetItemInputServiceResourceBatchGetItemTypeDef,
):
    pass

_RequiredExecuteTransactionInputRequestTypeDef = TypedDict(
    "_RequiredExecuteTransactionInputRequestTypeDef",
    {
        "TransactStatements": Sequence[ParameterizedStatementTypeDef],
    },
)
_OptionalExecuteTransactionInputRequestTypeDef = TypedDict(
    "_OptionalExecuteTransactionInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class ExecuteTransactionInputRequestTypeDef(
    _RequiredExecuteTransactionInputRequestTypeDef, _OptionalExecuteTransactionInputRequestTypeDef
):
    pass

WriteRequestOutputTypeDef = TypedDict(
    "WriteRequestOutputTypeDef",
    {
        "PutRequest": PutRequestOutputTypeDef,
        "DeleteRequest": DeleteRequestOutputTypeDef,
    },
    total=False,
)

WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {
        "PutRequest": PutRequestTypeDef,
        "DeleteRequest": DeleteRequestTypeDef,
    },
    total=False,
)

TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": ConditionCheckTypeDef,
        "Put": PutTypeDef,
        "Delete": DeleteTypeDef,
        "Update": UpdateTypeDef,
    },
    total=False,
)

AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[AutoScalingPolicyDescriptionTypeDef],
    },
    total=False,
)

AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": AutoScalingPolicyUpdateTypeDef,
    },
    total=False,
)

BatchGetItemOutputTypeDef = TypedDict(
    "BatchGetItemOutputTypeDef",
    {
        "Responses": Dict[str, List[Dict[str, AttributeValueTypeDef]]],
        "UnprocessedKeys": Dict[str, KeysAndAttributesOutputTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteItemOutputTypeDef = TypedDict(
    "DeleteItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "NextToken": str,
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExecuteTransactionOutputTypeDef = TypedDict(
    "ExecuteTransactionOutputTypeDef",
    {
        "Responses": List[ItemResponseTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetItemOutputTypeDef = TypedDict(
    "GetItemOutputTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutItemOutputTypeDef = TypedDict(
    "PutItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ScanOutputTypeDef = TypedDict(
    "ScanOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TransactGetItemsOutputTypeDef = TypedDict(
    "TransactGetItemsOutputTypeDef",
    {
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "Responses": List[ItemResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TransactWriteItemsOutputTypeDef = TypedDict(
    "TransactWriteItemsOutputTypeDef",
    {
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateItemOutputTypeDef = TypedDict(
    "UpdateItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeContinuousBackupsOutputTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": ContinuousBackupsDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateContinuousBackupsOutputTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": ContinuousBackupsDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateTableInputRequestTypeDef = TypedDict(
    "_RequiredCreateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "TableName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
    },
)
_OptionalCreateTableInputRequestTypeDef = TypedDict(
    "_OptionalCreateTableInputRequestTypeDef",
    {
        "LocalSecondaryIndexes": Sequence[LocalSecondaryIndexTypeDef],
        "GlobalSecondaryIndexes": Sequence[GlobalSecondaryIndexTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "StreamSpecification": StreamSpecificationTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class CreateTableInputRequestTypeDef(
    _RequiredCreateTableInputRequestTypeDef, _OptionalCreateTableInputRequestTypeDef
):
    pass

_RequiredCreateTableInputServiceResourceCreateTableTypeDef = TypedDict(
    "_RequiredCreateTableInputServiceResourceCreateTableTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "TableName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
    },
)
_OptionalCreateTableInputServiceResourceCreateTableTypeDef = TypedDict(
    "_OptionalCreateTableInputServiceResourceCreateTableTypeDef",
    {
        "LocalSecondaryIndexes": Sequence[LocalSecondaryIndexTypeDef],
        "GlobalSecondaryIndexes": Sequence[GlobalSecondaryIndexTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "StreamSpecification": StreamSpecificationTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class CreateTableInputServiceResourceCreateTableTypeDef(
    _RequiredCreateTableInputServiceResourceCreateTableTypeDef,
    _OptionalCreateTableInputServiceResourceCreateTableTypeDef,
):
    pass

_RequiredRestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "_RequiredRestoreTableFromBackupInputRequestTypeDef",
    {
        "TargetTableName": str,
        "BackupArn": str,
    },
)
_OptionalRestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "_OptionalRestoreTableFromBackupInputRequestTypeDef",
    {
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": Sequence[GlobalSecondaryIndexTypeDef],
        "LocalSecondaryIndexOverride": Sequence[LocalSecondaryIndexTypeDef],
        "ProvisionedThroughputOverride": ProvisionedThroughputTypeDef,
        "SSESpecificationOverride": SSESpecificationTypeDef,
    },
    total=False,
)

class RestoreTableFromBackupInputRequestTypeDef(
    _RequiredRestoreTableFromBackupInputRequestTypeDef,
    _OptionalRestoreTableFromBackupInputRequestTypeDef,
):
    pass

_RequiredRestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_RequiredRestoreTableToPointInTimeInputRequestTypeDef",
    {
        "TargetTableName": str,
    },
)
_OptionalRestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_OptionalRestoreTableToPointInTimeInputRequestTypeDef",
    {
        "SourceTableArn": str,
        "SourceTableName": str,
        "UseLatestRestorableTime": bool,
        "RestoreDateTime": Union[datetime, str],
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": Sequence[GlobalSecondaryIndexTypeDef],
        "LocalSecondaryIndexOverride": Sequence[LocalSecondaryIndexTypeDef],
        "ProvisionedThroughputOverride": ProvisionedThroughputTypeDef,
        "SSESpecificationOverride": SSESpecificationTypeDef,
    },
    total=False,
)

class RestoreTableToPointInTimeInputRequestTypeDef(
    _RequiredRestoreTableToPointInTimeInputRequestTypeDef,
    _OptionalRestoreTableToPointInTimeInputRequestTypeDef,
):
    pass

_RequiredTableCreationParametersTypeDef = TypedDict(
    "_RequiredTableCreationParametersTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "KeySchema": Sequence[KeySchemaElementTypeDef],
    },
)
_OptionalTableCreationParametersTypeDef = TypedDict(
    "_OptionalTableCreationParametersTypeDef",
    {
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "GlobalSecondaryIndexes": Sequence[GlobalSecondaryIndexTypeDef],
    },
    total=False,
)

class TableCreationParametersTypeDef(
    _RequiredTableCreationParametersTypeDef, _OptionalTableCreationParametersTypeDef
):
    pass

GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": UpdateGlobalSecondaryIndexActionTypeDef,
        "Create": CreateGlobalSecondaryIndexActionTypeDef,
        "Delete": DeleteGlobalSecondaryIndexActionTypeDef,
    },
    total=False,
)

ListGlobalTablesOutputTypeDef = TypedDict(
    "ListGlobalTablesOutputTypeDef",
    {
        "GlobalTables": List[GlobalTableTypeDef],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[ReplicaGlobalSecondaryIndexDescriptionTypeDef],
        "ReplicaInaccessibleDateTime": datetime,
        "ReplicaTableClassSummary": TableClassSummaryTypeDef,
    },
    total=False,
)

_RequiredCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": Sequence[ReplicaGlobalSecondaryIndexTypeDef],
        "TableClassOverride": TableClassType,
    },
    total=False,
)

class CreateReplicationGroupMemberActionTypeDef(
    _RequiredCreateReplicationGroupMemberActionTypeDef,
    _OptionalCreateReplicationGroupMemberActionTypeDef,
):
    pass

_RequiredUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredUpdateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalUpdateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": Sequence[ReplicaGlobalSecondaryIndexTypeDef],
        "TableClassOverride": TableClassType,
    },
    total=False,
)

class UpdateReplicationGroupMemberActionTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTypeDef,
    _OptionalUpdateReplicationGroupMemberActionTypeDef,
):
    pass

UpdateGlobalTableInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaUpdates": Sequence[ReplicaUpdateTypeDef],
    },
)

_RequiredTableCreationParametersOutputTypeDef = TypedDict(
    "_RequiredTableCreationParametersOutputTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": List[AttributeDefinitionTypeDef],
        "KeySchema": List[KeySchemaElementTypeDef],
    },
)
_OptionalTableCreationParametersOutputTypeDef = TypedDict(
    "_OptionalTableCreationParametersOutputTypeDef",
    {
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexOutputTypeDef],
    },
    total=False,
)

class TableCreationParametersOutputTypeDef(
    _RequiredTableCreationParametersOutputTypeDef, _OptionalTableCreationParametersOutputTypeDef
):
    pass

SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List[LocalSecondaryIndexInfoTypeDef],
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexInfoTypeDef],
        "StreamDescription": StreamSpecificationTypeDef,
        "TimeToLiveDescription": TimeToLiveDescriptionTypeDef,
        "SSEDescription": SSEDescriptionTypeDef,
    },
    total=False,
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "ImportSummaryList": List[ImportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "Responses": List[BatchStatementResponseTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredTransactGetItemsInputRequestTypeDef = TypedDict(
    "_RequiredTransactGetItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence[TransactGetItemTypeDef],
    },
)
_OptionalTransactGetItemsInputRequestTypeDef = TypedDict(
    "_OptionalTransactGetItemsInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class TransactGetItemsInputRequestTypeDef(
    _RequiredTransactGetItemsInputRequestTypeDef, _OptionalTransactGetItemsInputRequestTypeDef
):
    pass

BatchWriteItemOutputTypeDef = TypedDict(
    "BatchWriteItemOutputTypeDef",
    {
        "UnprocessedItems": Dict[str, List[WriteRequestOutputTypeDef]],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsTypeDef]],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBatchWriteItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, Sequence[WriteRequestTypeDef]],
    },
)
_OptionalBatchWriteItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)

class BatchWriteItemInputRequestTypeDef(
    _RequiredBatchWriteItemInputRequestTypeDef, _OptionalBatchWriteItemInputRequestTypeDef
):
    pass

_RequiredBatchWriteItemInputServiceResourceBatchWriteItemTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    {
        "RequestItems": Mapping[str, Sequence[WriteRequestTypeDef]],
    },
)
_OptionalBatchWriteItemInputServiceResourceBatchWriteItemTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)

class BatchWriteItemInputServiceResourceBatchWriteItemTypeDef(
    _RequiredBatchWriteItemInputServiceResourceBatchWriteItemTypeDef,
    _OptionalBatchWriteItemInputServiceResourceBatchWriteItemTypeDef,
):
    pass

_RequiredTransactWriteItemsInputRequestTypeDef = TypedDict(
    "_RequiredTransactWriteItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence[TransactWriteItemTypeDef],
    },
)
_OptionalTransactWriteItemsInputRequestTypeDef = TypedDict(
    "_OptionalTransactWriteItemsInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ClientRequestToken": str,
    },
    total=False,
)

class TransactWriteItemsInputRequestTypeDef(
    _RequiredTransactWriteItemsInputRequestTypeDef, _OptionalTransactWriteItemsInputRequestTypeDef
):
    pass

ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
    },
    total=False,
)

class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
):
    pass

GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass

ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass

_RequiredImportTableInputRequestTypeDef = TypedDict(
    "_RequiredImportTableInputRequestTypeDef",
    {
        "S3BucketSource": S3BucketSourceTypeDef,
        "InputFormat": InputFormatType,
        "TableCreationParameters": TableCreationParametersTypeDef,
    },
)
_OptionalImportTableInputRequestTypeDef = TypedDict(
    "_OptionalImportTableInputRequestTypeDef",
    {
        "ClientToken": str,
        "InputFormatOptions": InputFormatOptionsTypeDef,
        "InputCompressionType": InputCompressionTypeType,
    },
    total=False,
)

class ImportTableInputRequestTypeDef(
    _RequiredImportTableInputRequestTypeDef, _OptionalImportTableInputRequestTypeDef
):
    pass

GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List[ReplicaDescriptionTypeDef],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": GlobalTableStatusType,
        "GlobalTableName": str,
    },
    total=False,
)

TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[AttributeDefinitionTypeDef],
        "TableName": str,
        "KeySchema": List[KeySchemaElementTypeDef],
        "TableStatus": TableStatusType,
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ProvisionedThroughputDescriptionTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": BillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[LocalSecondaryIndexDescriptionTypeDef],
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexDescriptionTypeDef],
        "StreamSpecification": StreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ReplicaDescriptionTypeDef],
        "RestoreSummary": RestoreSummaryTypeDef,
        "SSEDescription": SSEDescriptionTypeDef,
        "ArchivalSummary": ArchivalSummaryTypeDef,
        "TableClassSummary": TableClassSummaryTypeDef,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": CreateReplicationGroupMemberActionTypeDef,
        "Update": UpdateReplicationGroupMemberActionTypeDef,
        "Delete": DeleteReplicationGroupMemberActionTypeDef,
    },
    total=False,
)

ImportTableDescriptionTypeDef = TypedDict(
    "ImportTableDescriptionTypeDef",
    {
        "ImportArn": str,
        "ImportStatus": ImportStatusType,
        "TableArn": str,
        "TableId": str,
        "ClientToken": str,
        "S3BucketSource": S3BucketSourceTypeDef,
        "ErrorCount": int,
        "CloudWatchLogGroupArn": str,
        "InputFormat": InputFormatType,
        "InputFormatOptions": InputFormatOptionsOutputTypeDef,
        "InputCompressionType": InputCompressionTypeType,
        "TableCreationParameters": TableCreationParametersOutputTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "ProcessedSizeBytes": int,
        "ProcessedItemCount": int,
        "ImportedItemCount": int,
        "FailureCode": str,
        "FailureMessage": str,
    },
    total=False,
)

BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": BackupDetailsTypeDef,
        "SourceTableDetails": SourceTableDetailsTypeDef,
        "SourceTableFeatureDetails": SourceTableFeatureDetailsTypeDef,
    },
    total=False,
)

ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List[ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaStatus": ReplicaStatusType,
    },
    total=False,
)

_RequiredReplicaSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaSettingsDescriptionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaSettingsDescriptionTypeDef",
    {
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaBillingModeSummary": BillingModeSummaryTypeDef,
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaGlobalSecondaryIndexSettings": List[
            ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef
        ],
        "ReplicaTableClassSummary": TableClassSummaryTypeDef,
    },
    total=False,
)

class ReplicaSettingsDescriptionTypeDef(
    _RequiredReplicaSettingsDescriptionTypeDef, _OptionalReplicaSettingsDescriptionTypeDef
):
    pass

_RequiredReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_RequiredReplicaAutoScalingUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_OptionalReplicaAutoScalingUpdateTypeDef",
    {
        "ReplicaGlobalSecondaryIndexUpdates": Sequence[
            ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

class ReplicaAutoScalingUpdateTypeDef(
    _RequiredReplicaAutoScalingUpdateTypeDef, _OptionalReplicaAutoScalingUpdateTypeDef
):
    pass

_RequiredReplicaSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaSettingsUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaSettingsUpdateTypeDef",
    {
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": AutoScalingSettingsUpdateTypeDef,
        "ReplicaGlobalSecondaryIndexSettingsUpdate": Sequence[
            ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef
        ],
        "ReplicaTableClass": TableClassType,
    },
    total=False,
)

class ReplicaSettingsUpdateTypeDef(
    _RequiredReplicaSettingsUpdateTypeDef, _OptionalReplicaSettingsUpdateTypeDef
):
    pass

CreateGlobalTableOutputTypeDef = TypedDict(
    "CreateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeGlobalTableOutputTypeDef = TypedDict(
    "DescribeGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateGlobalTableOutputTypeDef = TypedDict(
    "UpdateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTableOutputTypeDef = TypedDict(
    "CreateTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTableOutputTypeDef = TypedDict(
    "DeleteTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTableOutputTypeDef = TypedDict(
    "DescribeTableOutputTypeDef",
    {
        "Table": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RestoreTableFromBackupOutputTypeDef = TypedDict(
    "RestoreTableFromBackupOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RestoreTableToPointInTimeOutputTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTableOutputTypeDef = TypedDict(
    "UpdateTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateTableInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "GlobalSecondaryIndexUpdates": Sequence[GlobalSecondaryIndexUpdateTypeDef],
        "StreamSpecification": StreamSpecificationTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "ReplicaUpdates": Sequence[ReplicationGroupUpdateTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdateTableInputRequestTypeDef(
    _RequiredUpdateTableInputRequestTypeDef, _OptionalUpdateTableInputRequestTypeDef
):
    pass

UpdateTableInputTableUpdateTypeDef = TypedDict(
    "UpdateTableInputTableUpdateTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "GlobalSecondaryIndexUpdates": Sequence[GlobalSecondaryIndexUpdateTypeDef],
        "StreamSpecification": StreamSpecificationTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "ReplicaUpdates": Sequence[ReplicationGroupUpdateTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

DescribeImportOutputTypeDef = TypedDict(
    "DescribeImportOutputTypeDef",
    {
        "ImportTableDescription": ImportTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ImportTableOutputTypeDef = TypedDict(
    "ImportTableOutputTypeDef",
    {
        "ImportTableDescription": ImportTableDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteBackupOutputTypeDef = TypedDict(
    "DeleteBackupOutputTypeDef",
    {
        "BackupDescription": BackupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeBackupOutputTypeDef = TypedDict(
    "DescribeBackupOutputTypeDef",
    {
        "BackupDescription": BackupDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": TableStatusType,
        "Replicas": List[ReplicaAutoScalingDescriptionTypeDef],
    },
    total=False,
)

DescribeGlobalTableSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ReplicaSettingsDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateGlobalTableSettingsOutputTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ReplicaSettingsDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "GlobalSecondaryIndexUpdates": Sequence[GlobalSecondaryIndexAutoScalingUpdateTypeDef],
        "ProvisionedWriteCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
        "ReplicaUpdates": Sequence[ReplicaAutoScalingUpdateTypeDef],
    },
    total=False,
)

class UpdateTableReplicaAutoScalingInputRequestTypeDef(
    _RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef,
    _OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef,
):
    pass

_RequiredUpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)
_OptionalUpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableBillingMode": BillingModeType,
        "GlobalTableProvisionedWriteCapacityUnits": int,
        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": (
            AutoScalingSettingsUpdateTypeDef
        ),
        "GlobalTableGlobalSecondaryIndexSettingsUpdate": Sequence[
            GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef
        ],
        "ReplicaSettingsUpdate": Sequence[ReplicaSettingsUpdateTypeDef],
    },
    total=False,
)

class UpdateGlobalTableSettingsInputRequestTypeDef(
    _RequiredUpdateGlobalTableSettingsInputRequestTypeDef,
    _OptionalUpdateGlobalTableSettingsInputRequestTypeDef,
):
    pass

DescribeTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": TableAutoScalingDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": TableAutoScalingDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
