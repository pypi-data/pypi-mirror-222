"""
Type annotations for lookoutmetrics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/type_defs/)

Usage::

    ```python
    from mypy_boto3_lookoutmetrics.type_defs import LambdaConfigurationTypeDef

    data: LambdaConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregationFunctionType,
    AlertStatusType,
    AlertTypeType,
    AnomalyDetectionTaskStatusType,
    AnomalyDetectorFailureTypeType,
    AnomalyDetectorStatusType,
    ConfidenceType,
    CSVFileCompressionType,
    DataQualityMetricTypeType,
    FrequencyType,
    JsonFileCompressionType,
    RelationshipTypeType,
    SnsFormatType,
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
    "LambdaConfigurationTypeDef",
    "SNSConfigurationTypeDef",
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    "DimensionFilterOutputTypeDef",
    "DimensionFilterTypeDef",
    "AlertSummaryTypeDef",
    "AnomalyDetectorConfigSummaryTypeDef",
    "AnomalyDetectorConfigTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "ItemizedMetricStatsTypeDef",
    "AnomalyGroupSummaryTypeDef",
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    "AnomalyGroupTimeSeriesTypeDef",
    "AppFlowConfigTypeDef",
    "BackTestConfigurationTypeDef",
    "AttributeValueTypeDef",
    "AutoDetectionS3SourceConfigTypeDef",
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "MetricTypeDef",
    "TimestampColumnTypeDef",
    "CsvFormatDescriptorOutputTypeDef",
    "CsvFormatDescriptorTypeDef",
    "DataQualityMetricTypeDef",
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    "DeleteAlertRequestRequestTypeDef",
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    "DescribeAlertRequestRequestTypeDef",
    "DescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    "ExecutionStatusTypeDef",
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    "DescribeMetricSetRequestRequestTypeDef",
    "DimensionValueContributionTypeDef",
    "DimensionNameValueTypeDef",
    "JsonFormatDescriptorTypeDef",
    "FilterTypeDef",
    "GetAnomalyGroupRequestRequestTypeDef",
    "GetDataQualityMetricsRequestRequestTypeDef",
    "TimeSeriesFeedbackTypeDef",
    "InterMetricImpactDetailsTypeDef",
    "ListAlertsRequestRequestTypeDef",
    "ListAnomalyDetectorsRequestRequestTypeDef",
    "ListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    "ListAnomalyGroupSummariesRequestRequestTypeDef",
    "ListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    "ListMetricSetsRequestRequestTypeDef",
    "MetricSetSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "VpcConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ActionTypeDef",
    "AlertFiltersOutputTypeDef",
    "AlertFiltersTypeDef",
    "CreateAnomalyDetectorRequestRequestTypeDef",
    "UpdateAnomalyDetectorRequestRequestTypeDef",
    "AnomalyGroupStatisticsTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "GetFeedbackRequestRequestTypeDef",
    "AthenaSourceConfigTypeDef",
    "CloudWatchConfigTypeDef",
    "DetectedFieldTypeDef",
    "AutoDetectionMetricSourceTypeDef",
    "CreateAlertResponseTypeDef",
    "CreateAnomalyDetectorResponseTypeDef",
    "CreateMetricSetResponseTypeDef",
    "DescribeAnomalyDetectorResponseTypeDef",
    "GetSampleDataResponseTypeDef",
    "ListAlertsResponseTypeDef",
    "ListAnomalyDetectorsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateAlertResponseTypeDef",
    "UpdateAnomalyDetectorResponseTypeDef",
    "UpdateMetricSetResponseTypeDef",
    "MetricSetDataQualityMetricTypeDef",
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    "DimensionContributionTypeDef",
    "TimeSeriesTypeDef",
    "FileFormatDescriptorOutputTypeDef",
    "FileFormatDescriptorTypeDef",
    "MetricSetDimensionFilterOutputTypeDef",
    "MetricSetDimensionFilterTypeDef",
    "GetFeedbackResponseTypeDef",
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    "ListMetricSetsResponseTypeDef",
    "RDSSourceConfigOutputTypeDef",
    "RedshiftSourceConfigOutputTypeDef",
    "RDSSourceConfigTypeDef",
    "RedshiftSourceConfigTypeDef",
    "AlertTypeDef",
    "CreateAlertRequestRequestTypeDef",
    "UpdateAlertRequestRequestTypeDef",
    "ListAnomalyGroupSummariesResponseTypeDef",
    "DetectedCsvFormatDescriptorTypeDef",
    "DetectedJsonFormatDescriptorTypeDef",
    "DetectMetricSetConfigRequestRequestTypeDef",
    "AnomalyDetectorDataQualityMetricTypeDef",
    "ContributionMatrixTypeDef",
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    "S3SourceConfigOutputTypeDef",
    "S3SourceConfigTypeDef",
    "SampleDataS3SourceConfigTypeDef",
    "DescribeAlertResponseTypeDef",
    "DetectedFileFormatDescriptorTypeDef",
    "GetDataQualityMetricsResponseTypeDef",
    "MetricLevelImpactTypeDef",
    "MetricSourceOutputTypeDef",
    "MetricSourceTypeDef",
    "GetSampleDataRequestRequestTypeDef",
    "DetectedS3SourceConfigTypeDef",
    "AnomalyGroupTypeDef",
    "DescribeMetricSetResponseTypeDef",
    "CreateMetricSetRequestRequestTypeDef",
    "UpdateMetricSetRequestRequestTypeDef",
    "DetectedMetricSourceTypeDef",
    "GetAnomalyGroupResponseTypeDef",
    "DetectedMetricSetConfigTypeDef",
    "DetectMetricSetConfigResponseTypeDef",
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "RoleArn": str,
        "LambdaArn": str,
    },
)

_RequiredSNSConfigurationTypeDef = TypedDict(
    "_RequiredSNSConfigurationTypeDef",
    {
        "RoleArn": str,
        "SnsTopicArn": str,
    },
)
_OptionalSNSConfigurationTypeDef = TypedDict(
    "_OptionalSNSConfigurationTypeDef",
    {
        "SnsFormat": SnsFormatType,
    },
    total=False,
)


class SNSConfigurationTypeDef(_RequiredSNSConfigurationTypeDef, _OptionalSNSConfigurationTypeDef):
    pass


ActivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DimensionFilterOutputTypeDef = TypedDict(
    "DimensionFilterOutputTypeDef",
    {
        "DimensionName": str,
        "DimensionValueList": List[str],
    },
    total=False,
)

DimensionFilterTypeDef = TypedDict(
    "DimensionFilterTypeDef",
    {
        "DimensionName": str,
        "DimensionValueList": Sequence[str],
    },
    total=False,
)

AlertSummaryTypeDef = TypedDict(
    "AlertSummaryTypeDef",
    {
        "AlertArn": str,
        "AnomalyDetectorArn": str,
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AlertType": AlertTypeType,
        "AlertStatus": AlertStatusType,
        "LastModificationTime": datetime,
        "CreationTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

AnomalyDetectorConfigSummaryTypeDef = TypedDict(
    "AnomalyDetectorConfigSummaryTypeDef",
    {
        "AnomalyDetectorFrequency": FrequencyType,
    },
    total=False,
)

AnomalyDetectorConfigTypeDef = TypedDict(
    "AnomalyDetectorConfigTypeDef",
    {
        "AnomalyDetectorFrequency": FrequencyType,
    },
    total=False,
)

AnomalyDetectorSummaryTypeDef = TypedDict(
    "AnomalyDetectorSummaryTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

ItemizedMetricStatsTypeDef = TypedDict(
    "ItemizedMetricStatsTypeDef",
    {
        "MetricName": str,
        "OccurrenceCount": int,
    },
    total=False,
)

AnomalyGroupSummaryTypeDef = TypedDict(
    "AnomalyGroupSummaryTypeDef",
    {
        "StartTime": str,
        "EndTime": str,
        "AnomalyGroupId": str,
        "AnomalyGroupScore": float,
        "PrimaryMetricName": str,
    },
    total=False,
)

AnomalyGroupTimeSeriesFeedbackTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
)

_RequiredAnomalyGroupTimeSeriesTypeDef = TypedDict(
    "_RequiredAnomalyGroupTimeSeriesTypeDef",
    {
        "AnomalyGroupId": str,
    },
)
_OptionalAnomalyGroupTimeSeriesTypeDef = TypedDict(
    "_OptionalAnomalyGroupTimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
    },
    total=False,
)


class AnomalyGroupTimeSeriesTypeDef(
    _RequiredAnomalyGroupTimeSeriesTypeDef, _OptionalAnomalyGroupTimeSeriesTypeDef
):
    pass


AppFlowConfigTypeDef = TypedDict(
    "AppFlowConfigTypeDef",
    {
        "RoleArn": str,
        "FlowName": str,
    },
    total=False,
)

BackTestConfigurationTypeDef = TypedDict(
    "BackTestConfigurationTypeDef",
    {
        "RunBackTestMode": bool,
    },
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": str,
        "B": str,
        "SS": List[str],
        "NS": List[str],
        "BS": List[str],
    },
    total=False,
)

AutoDetectionS3SourceConfigTypeDef = TypedDict(
    "AutoDetectionS3SourceConfigTypeDef",
    {
        "TemplatedPathList": Sequence[str],
        "HistoricalDataPathList": Sequence[str],
    },
    total=False,
)

BackTestAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
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

_RequiredMetricTypeDef = TypedDict(
    "_RequiredMetricTypeDef",
    {
        "MetricName": str,
        "AggregationFunction": AggregationFunctionType,
    },
)
_OptionalMetricTypeDef = TypedDict(
    "_OptionalMetricTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)


class MetricTypeDef(_RequiredMetricTypeDef, _OptionalMetricTypeDef):
    pass


TimestampColumnTypeDef = TypedDict(
    "TimestampColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnFormat": str,
    },
    total=False,
)

CsvFormatDescriptorOutputTypeDef = TypedDict(
    "CsvFormatDescriptorOutputTypeDef",
    {
        "FileCompression": CSVFileCompressionType,
        "Charset": str,
        "ContainsHeader": bool,
        "Delimiter": str,
        "HeaderList": List[str],
        "QuoteSymbol": str,
    },
    total=False,
)

CsvFormatDescriptorTypeDef = TypedDict(
    "CsvFormatDescriptorTypeDef",
    {
        "FileCompression": CSVFileCompressionType,
        "Charset": str,
        "ContainsHeader": bool,
        "Delimiter": str,
        "HeaderList": Sequence[str],
        "QuoteSymbol": str,
    },
    total=False,
)

DataQualityMetricTypeDef = TypedDict(
    "DataQualityMetricTypeDef",
    {
        "MetricType": DataQualityMetricTypeType,
        "MetricDescription": str,
        "RelatedColumnName": str,
        "MetricValue": float,
    },
    total=False,
)

DeactivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DeleteAlertRequestRequestTypeDef = TypedDict(
    "DeleteAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DeleteAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAlertRequestRequestTypeDef = TypedDict(
    "DescribeAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)

_RequiredDescribeAnomalyDetectionExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalDescribeAnomalyDetectionExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    {
        "Timestamp": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAnomalyDetectionExecutionsRequestRequestTypeDef(
    _RequiredDescribeAnomalyDetectionExecutionsRequestRequestTypeDef,
    _OptionalDescribeAnomalyDetectionExecutionsRequestRequestTypeDef,
):
    pass


ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "Timestamp": str,
        "Status": AnomalyDetectionTaskStatusType,
        "FailureReason": str,
    },
    total=False,
)

DescribeAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeMetricSetRequestRequestTypeDef = TypedDict(
    "DescribeMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)

DimensionValueContributionTypeDef = TypedDict(
    "DimensionValueContributionTypeDef",
    {
        "DimensionValue": str,
        "ContributionScore": float,
    },
    total=False,
)

DimensionNameValueTypeDef = TypedDict(
    "DimensionNameValueTypeDef",
    {
        "DimensionName": str,
        "DimensionValue": str,
    },
)

JsonFormatDescriptorTypeDef = TypedDict(
    "JsonFormatDescriptorTypeDef",
    {
        "FileCompression": JsonFileCompressionType,
        "Charset": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "DimensionValue": str,
        "FilterOperation": Literal["EQUALS"],
    },
    total=False,
)

GetAnomalyGroupRequestRequestTypeDef = TypedDict(
    "GetAnomalyGroupRequestRequestTypeDef",
    {
        "AnomalyGroupId": str,
        "AnomalyDetectorArn": str,
    },
)

_RequiredGetDataQualityMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDataQualityMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalGetDataQualityMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDataQualityMetricsRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
    total=False,
)


class GetDataQualityMetricsRequestRequestTypeDef(
    _RequiredGetDataQualityMetricsRequestRequestTypeDef,
    _OptionalGetDataQualityMetricsRequestRequestTypeDef,
):
    pass


TimeSeriesFeedbackTypeDef = TypedDict(
    "TimeSeriesFeedbackTypeDef",
    {
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
    total=False,
)

InterMetricImpactDetailsTypeDef = TypedDict(
    "InterMetricImpactDetailsTypeDef",
    {
        "MetricName": str,
        "AnomalyGroupId": str,
        "RelationshipType": RelationshipTypeType,
        "ContributionPercentage": float,
    },
    total=False,
)

ListAlertsRequestRequestTypeDef = TypedDict(
    "ListAlertsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAnomalyDetectorsRequestRequestTypeDef = TypedDict(
    "ListAnomalyDetectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListAnomalyGroupRelatedMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
    },
)
_OptionalListAnomalyGroupRelatedMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    {
        "RelationshipTypeFilter": RelationshipTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAnomalyGroupRelatedMetricsRequestRequestTypeDef(
    _RequiredListAnomalyGroupRelatedMetricsRequestRequestTypeDef,
    _OptionalListAnomalyGroupRelatedMetricsRequestRequestTypeDef,
):
    pass


_RequiredListAnomalyGroupSummariesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupSummariesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "SensitivityThreshold": int,
    },
)
_OptionalListAnomalyGroupSummariesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupSummariesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAnomalyGroupSummariesRequestRequestTypeDef(
    _RequiredListAnomalyGroupSummariesRequestRequestTypeDef,
    _OptionalListAnomalyGroupSummariesRequestRequestTypeDef,
):
    pass


_RequiredListAnomalyGroupTimeSeriesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "MetricName": str,
    },
)
_OptionalListAnomalyGroupTimeSeriesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAnomalyGroupTimeSeriesRequestRequestTypeDef(
    _RequiredListAnomalyGroupTimeSeriesRequestRequestTypeDef,
    _OptionalListAnomalyGroupTimeSeriesRequestRequestTypeDef,
):
    pass


ListMetricSetsRequestRequestTypeDef = TypedDict(
    "ListMetricSetsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

MetricSetSummaryTypeDef = TypedDict(
    "MetricSetSummaryTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetDescription": str,
        "MetricSetName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

VpcConfigurationOutputTypeDef = TypedDict(
    "VpcConfigurationOutputTypeDef",
    {
        "SubnetIdList": List[str],
        "SecurityGroupIdList": List[str],
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIdList": Sequence[str],
        "SecurityGroupIdList": Sequence[str],
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

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "SNSConfiguration": SNSConfigurationTypeDef,
        "LambdaConfiguration": LambdaConfigurationTypeDef,
    },
    total=False,
)

AlertFiltersOutputTypeDef = TypedDict(
    "AlertFiltersOutputTypeDef",
    {
        "MetricList": List[str],
        "DimensionFilterList": List[DimensionFilterOutputTypeDef],
    },
    total=False,
)

AlertFiltersTypeDef = TypedDict(
    "AlertFiltersTypeDef",
    {
        "MetricList": Sequence[str],
        "DimensionFilterList": Sequence[DimensionFilterTypeDef],
    },
    total=False,
)

_RequiredCreateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorName": str,
        "AnomalyDetectorConfig": AnomalyDetectorConfigTypeDef,
    },
)
_OptionalCreateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorDescription": str,
        "KmsKeyArn": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateAnomalyDetectorRequestRequestTypeDef(
    _RequiredCreateAnomalyDetectorRequestRequestTypeDef,
    _OptionalCreateAnomalyDetectorRequestRequestTypeDef,
):
    pass


_RequiredUpdateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalUpdateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalyDetectorRequestRequestTypeDef",
    {
        "KmsKeyArn": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": AnomalyDetectorConfigTypeDef,
    },
    total=False,
)


class UpdateAnomalyDetectorRequestRequestTypeDef(
    _RequiredUpdateAnomalyDetectorRequestRequestTypeDef,
    _OptionalUpdateAnomalyDetectorRequestRequestTypeDef,
):
    pass


AnomalyGroupStatisticsTypeDef = TypedDict(
    "AnomalyGroupStatisticsTypeDef",
    {
        "EvaluationStartDate": str,
        "TotalCount": int,
        "ItemizedMetricStatsList": List[ItemizedMetricStatsTypeDef],
    },
    total=False,
)

PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": AnomalyGroupTimeSeriesFeedbackTypeDef,
    },
)

_RequiredGetFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredGetFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": AnomalyGroupTimeSeriesTypeDef,
    },
)
_OptionalGetFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalGetFeedbackRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetFeedbackRequestRequestTypeDef(
    _RequiredGetFeedbackRequestRequestTypeDef, _OptionalGetFeedbackRequestRequestTypeDef
):
    pass


AthenaSourceConfigTypeDef = TypedDict(
    "AthenaSourceConfigTypeDef",
    {
        "RoleArn": str,
        "DatabaseName": str,
        "DataCatalog": str,
        "TableName": str,
        "WorkGroupName": str,
        "S3ResultsPath": str,
        "BackTestConfiguration": BackTestConfigurationTypeDef,
    },
    total=False,
)

CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "RoleArn": str,
        "BackTestConfiguration": BackTestConfigurationTypeDef,
    },
    total=False,
)

DetectedFieldTypeDef = TypedDict(
    "DetectedFieldTypeDef",
    {
        "Value": AttributeValueTypeDef,
        "Confidence": ConfidenceType,
        "Message": str,
    },
    total=False,
)

AutoDetectionMetricSourceTypeDef = TypedDict(
    "AutoDetectionMetricSourceTypeDef",
    {
        "S3SourceConfig": AutoDetectionS3SourceConfigTypeDef,
    },
    total=False,
)

CreateAlertResponseTypeDef = TypedDict(
    "CreateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAnomalyDetectorResponseTypeDef = TypedDict(
    "CreateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMetricSetResponseTypeDef = TypedDict(
    "CreateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAnomalyDetectorResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": AnomalyDetectorConfigSummaryTypeDef,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "FailureReason": str,
        "KmsKeyArn": str,
        "FailureType": AnomalyDetectorFailureTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSampleDataResponseTypeDef = TypedDict(
    "GetSampleDataResponseTypeDef",
    {
        "HeaderValues": List[str],
        "SampleRows": List[List[str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAlertsResponseTypeDef = TypedDict(
    "ListAlertsResponseTypeDef",
    {
        "AlertSummaryList": List[AlertSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAnomalyDetectorsResponseTypeDef = TypedDict(
    "ListAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectorSummaryList": List[AnomalyDetectorSummaryTypeDef],
        "NextToken": str,
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

UpdateAlertResponseTypeDef = TypedDict(
    "UpdateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAnomalyDetectorResponseTypeDef = TypedDict(
    "UpdateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateMetricSetResponseTypeDef = TypedDict(
    "UpdateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MetricSetDataQualityMetricTypeDef = TypedDict(
    "MetricSetDataQualityMetricTypeDef",
    {
        "MetricSetArn": str,
        "DataQualityMetricList": List[DataQualityMetricTypeDef],
    },
    total=False,
)

DescribeAnomalyDetectionExecutionsResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    {
        "ExecutionList": List[ExecutionStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DimensionContributionTypeDef = TypedDict(
    "DimensionContributionTypeDef",
    {
        "DimensionName": str,
        "DimensionValueContributionList": List[DimensionValueContributionTypeDef],
    },
    total=False,
)

TimeSeriesTypeDef = TypedDict(
    "TimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
        "DimensionList": List[DimensionNameValueTypeDef],
        "MetricValueList": List[float],
    },
)

FileFormatDescriptorOutputTypeDef = TypedDict(
    "FileFormatDescriptorOutputTypeDef",
    {
        "CsvFormatDescriptor": CsvFormatDescriptorOutputTypeDef,
        "JsonFormatDescriptor": JsonFormatDescriptorTypeDef,
    },
    total=False,
)

FileFormatDescriptorTypeDef = TypedDict(
    "FileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": CsvFormatDescriptorTypeDef,
        "JsonFormatDescriptor": JsonFormatDescriptorTypeDef,
    },
    total=False,
)

MetricSetDimensionFilterOutputTypeDef = TypedDict(
    "MetricSetDimensionFilterOutputTypeDef",
    {
        "Name": str,
        "FilterList": List[FilterTypeDef],
    },
    total=False,
)

MetricSetDimensionFilterTypeDef = TypedDict(
    "MetricSetDimensionFilterTypeDef",
    {
        "Name": str,
        "FilterList": Sequence[FilterTypeDef],
    },
    total=False,
)

GetFeedbackResponseTypeDef = TypedDict(
    "GetFeedbackResponseTypeDef",
    {
        "AnomalyGroupTimeSeriesFeedback": List[TimeSeriesFeedbackTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAnomalyGroupRelatedMetricsResponseTypeDef = TypedDict(
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    {
        "InterMetricImpactList": List[InterMetricImpactDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMetricSetsResponseTypeDef = TypedDict(
    "ListMetricSetsResponseTypeDef",
    {
        "MetricSetSummaryList": List[MetricSetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RDSSourceConfigOutputTypeDef = TypedDict(
    "RDSSourceConfigOutputTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": VpcConfigurationOutputTypeDef,
    },
    total=False,
)

RedshiftSourceConfigOutputTypeDef = TypedDict(
    "RedshiftSourceConfigOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": VpcConfigurationOutputTypeDef,
    },
    total=False,
)

RDSSourceConfigTypeDef = TypedDict(
    "RDSSourceConfigTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": VpcConfigurationTypeDef,
    },
    total=False,
)

RedshiftSourceConfigTypeDef = TypedDict(
    "RedshiftSourceConfigTypeDef",
    {
        "ClusterIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": VpcConfigurationTypeDef,
    },
    total=False,
)

AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "Action": ActionTypeDef,
        "AlertDescription": str,
        "AlertArn": str,
        "AnomalyDetectorArn": str,
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AlertType": AlertTypeType,
        "AlertStatus": AlertStatusType,
        "LastModificationTime": datetime,
        "CreationTime": datetime,
        "AlertFilters": AlertFiltersOutputTypeDef,
    },
    total=False,
)

_RequiredCreateAlertRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAlertRequestRequestTypeDef",
    {
        "AlertName": str,
        "AnomalyDetectorArn": str,
        "Action": ActionTypeDef,
    },
)
_OptionalCreateAlertRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAlertRequestRequestTypeDef",
    {
        "AlertSensitivityThreshold": int,
        "AlertDescription": str,
        "Tags": Mapping[str, str],
        "AlertFilters": AlertFiltersTypeDef,
    },
    total=False,
)


class CreateAlertRequestRequestTypeDef(
    _RequiredCreateAlertRequestRequestTypeDef, _OptionalCreateAlertRequestRequestTypeDef
):
    pass


_RequiredUpdateAlertRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)
_OptionalUpdateAlertRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAlertRequestRequestTypeDef",
    {
        "AlertDescription": str,
        "AlertSensitivityThreshold": int,
        "Action": ActionTypeDef,
        "AlertFilters": AlertFiltersTypeDef,
    },
    total=False,
)


class UpdateAlertRequestRequestTypeDef(
    _RequiredUpdateAlertRequestRequestTypeDef, _OptionalUpdateAlertRequestRequestTypeDef
):
    pass


ListAnomalyGroupSummariesResponseTypeDef = TypedDict(
    "ListAnomalyGroupSummariesResponseTypeDef",
    {
        "AnomalyGroupSummaryList": List[AnomalyGroupSummaryTypeDef],
        "AnomalyGroupStatistics": AnomalyGroupStatisticsTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DetectedCsvFormatDescriptorTypeDef = TypedDict(
    "DetectedCsvFormatDescriptorTypeDef",
    {
        "FileCompression": DetectedFieldTypeDef,
        "Charset": DetectedFieldTypeDef,
        "ContainsHeader": DetectedFieldTypeDef,
        "Delimiter": DetectedFieldTypeDef,
        "HeaderList": DetectedFieldTypeDef,
        "QuoteSymbol": DetectedFieldTypeDef,
    },
    total=False,
)

DetectedJsonFormatDescriptorTypeDef = TypedDict(
    "DetectedJsonFormatDescriptorTypeDef",
    {
        "FileCompression": DetectedFieldTypeDef,
        "Charset": DetectedFieldTypeDef,
    },
    total=False,
)

DetectMetricSetConfigRequestRequestTypeDef = TypedDict(
    "DetectMetricSetConfigRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AutoDetectionMetricSource": AutoDetectionMetricSourceTypeDef,
    },
)

AnomalyDetectorDataQualityMetricTypeDef = TypedDict(
    "AnomalyDetectorDataQualityMetricTypeDef",
    {
        "StartTimestamp": datetime,
        "MetricSetDataQualityMetricList": List[MetricSetDataQualityMetricTypeDef],
    },
    total=False,
)

ContributionMatrixTypeDef = TypedDict(
    "ContributionMatrixTypeDef",
    {
        "DimensionContributionList": List[DimensionContributionTypeDef],
    },
    total=False,
)

ListAnomalyGroupTimeSeriesResponseTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    {
        "AnomalyGroupId": str,
        "MetricName": str,
        "TimestampList": List[str],
        "NextToken": str,
        "TimeSeriesList": List[TimeSeriesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

S3SourceConfigOutputTypeDef = TypedDict(
    "S3SourceConfigOutputTypeDef",
    {
        "RoleArn": str,
        "TemplatedPathList": List[str],
        "HistoricalDataPathList": List[str],
        "FileFormatDescriptor": FileFormatDescriptorOutputTypeDef,
    },
    total=False,
)

S3SourceConfigTypeDef = TypedDict(
    "S3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "TemplatedPathList": Sequence[str],
        "HistoricalDataPathList": Sequence[str],
        "FileFormatDescriptor": FileFormatDescriptorTypeDef,
    },
    total=False,
)

_RequiredSampleDataS3SourceConfigTypeDef = TypedDict(
    "_RequiredSampleDataS3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "FileFormatDescriptor": FileFormatDescriptorTypeDef,
    },
)
_OptionalSampleDataS3SourceConfigTypeDef = TypedDict(
    "_OptionalSampleDataS3SourceConfigTypeDef",
    {
        "TemplatedPathList": Sequence[str],
        "HistoricalDataPathList": Sequence[str],
    },
    total=False,
)


class SampleDataS3SourceConfigTypeDef(
    _RequiredSampleDataS3SourceConfigTypeDef, _OptionalSampleDataS3SourceConfigTypeDef
):
    pass


DescribeAlertResponseTypeDef = TypedDict(
    "DescribeAlertResponseTypeDef",
    {
        "Alert": AlertTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DetectedFileFormatDescriptorTypeDef = TypedDict(
    "DetectedFileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": DetectedCsvFormatDescriptorTypeDef,
        "JsonFormatDescriptor": DetectedJsonFormatDescriptorTypeDef,
    },
    total=False,
)

GetDataQualityMetricsResponseTypeDef = TypedDict(
    "GetDataQualityMetricsResponseTypeDef",
    {
        "AnomalyDetectorDataQualityMetricList": List[AnomalyDetectorDataQualityMetricTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MetricLevelImpactTypeDef = TypedDict(
    "MetricLevelImpactTypeDef",
    {
        "MetricName": str,
        "NumTimeSeries": int,
        "ContributionMatrix": ContributionMatrixTypeDef,
    },
    total=False,
)

MetricSourceOutputTypeDef = TypedDict(
    "MetricSourceOutputTypeDef",
    {
        "S3SourceConfig": S3SourceConfigOutputTypeDef,
        "AppFlowConfig": AppFlowConfigTypeDef,
        "CloudWatchConfig": CloudWatchConfigTypeDef,
        "RDSSourceConfig": RDSSourceConfigOutputTypeDef,
        "RedshiftSourceConfig": RedshiftSourceConfigOutputTypeDef,
        "AthenaSourceConfig": AthenaSourceConfigTypeDef,
    },
    total=False,
)

MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "S3SourceConfig": S3SourceConfigTypeDef,
        "AppFlowConfig": AppFlowConfigTypeDef,
        "CloudWatchConfig": CloudWatchConfigTypeDef,
        "RDSSourceConfig": RDSSourceConfigTypeDef,
        "RedshiftSourceConfig": RedshiftSourceConfigTypeDef,
        "AthenaSourceConfig": AthenaSourceConfigTypeDef,
    },
    total=False,
)

GetSampleDataRequestRequestTypeDef = TypedDict(
    "GetSampleDataRequestRequestTypeDef",
    {
        "S3SourceConfig": SampleDataS3SourceConfigTypeDef,
    },
    total=False,
)

DetectedS3SourceConfigTypeDef = TypedDict(
    "DetectedS3SourceConfigTypeDef",
    {
        "FileFormatDescriptor": DetectedFileFormatDescriptorTypeDef,
    },
    total=False,
)

AnomalyGroupTypeDef = TypedDict(
    "AnomalyGroupTypeDef",
    {
        "StartTime": str,
        "EndTime": str,
        "AnomalyGroupId": str,
        "AnomalyGroupScore": float,
        "PrimaryMetricName": str,
        "MetricLevelImpactList": List[MetricLevelImpactTypeDef],
    },
    total=False,
)

DescribeMetricSetResponseTypeDef = TypedDict(
    "DescribeMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricSetDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Offset": int,
        "MetricList": List[MetricTypeDef],
        "TimestampColumn": TimestampColumnTypeDef,
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "MetricSource": MetricSourceOutputTypeDef,
        "DimensionFilterList": List[MetricSetDimensionFilterOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateMetricSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMetricSetRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricList": Sequence[MetricTypeDef],
        "MetricSource": MetricSourceTypeDef,
    },
)
_OptionalCreateMetricSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMetricSetRequestRequestTypeDef",
    {
        "MetricSetDescription": str,
        "Offset": int,
        "TimestampColumn": TimestampColumnTypeDef,
        "DimensionList": Sequence[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "Tags": Mapping[str, str],
        "DimensionFilterList": Sequence[
            Union[MetricSetDimensionFilterTypeDef, MetricSetDimensionFilterOutputTypeDef]
        ],
    },
    total=False,
)


class CreateMetricSetRequestRequestTypeDef(
    _RequiredCreateMetricSetRequestRequestTypeDef, _OptionalCreateMetricSetRequestRequestTypeDef
):
    pass


_RequiredUpdateMetricSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)
_OptionalUpdateMetricSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMetricSetRequestRequestTypeDef",
    {
        "MetricSetDescription": str,
        "MetricList": Sequence[MetricTypeDef],
        "Offset": int,
        "TimestampColumn": TimestampColumnTypeDef,
        "DimensionList": Sequence[str],
        "MetricSetFrequency": FrequencyType,
        "MetricSource": MetricSourceTypeDef,
        "DimensionFilterList": Sequence[
            Union[MetricSetDimensionFilterTypeDef, MetricSetDimensionFilterOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateMetricSetRequestRequestTypeDef(
    _RequiredUpdateMetricSetRequestRequestTypeDef, _OptionalUpdateMetricSetRequestRequestTypeDef
):
    pass


DetectedMetricSourceTypeDef = TypedDict(
    "DetectedMetricSourceTypeDef",
    {
        "S3SourceConfig": DetectedS3SourceConfigTypeDef,
    },
    total=False,
)

GetAnomalyGroupResponseTypeDef = TypedDict(
    "GetAnomalyGroupResponseTypeDef",
    {
        "AnomalyGroup": AnomalyGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DetectedMetricSetConfigTypeDef = TypedDict(
    "DetectedMetricSetConfigTypeDef",
    {
        "Offset": DetectedFieldTypeDef,
        "MetricSetFrequency": DetectedFieldTypeDef,
        "MetricSource": DetectedMetricSourceTypeDef,
    },
    total=False,
)

DetectMetricSetConfigResponseTypeDef = TypedDict(
    "DetectMetricSetConfigResponseTypeDef",
    {
        "DetectedMetricSetConfig": DetectedMetricSetConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
