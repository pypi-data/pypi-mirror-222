"""
Type annotations for frauddetector service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/type_defs/)

Usage::

    ```python
    from mypy_boto3_frauddetector.type_defs import ATIMetricDataPointTypeDef

    data: ATIMetricDataPointTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AsyncJobStatusType,
    DataSourceType,
    DataTypeType,
    DetectorVersionStatusType,
    EventIngestionType,
    ListUpdateModeType,
    ModelEndpointStatusType,
    ModelInputDataFormatType,
    ModelOutputDataFormatType,
    ModelTypeEnumType,
    ModelVersionStatusType,
    RuleExecutionModeType,
    TrainingDataSourceEnumType,
    UnlabeledEventsTreatmentType,
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
    "ATIMetricDataPointTypeDef",
    "ATIModelPerformanceTypeDef",
    "AggregatedLogOddsMetricTypeDef",
    "AggregatedVariablesImpactExplanationTypeDef",
    "AllowDenyListTypeDef",
    "BatchCreateVariableErrorTypeDef",
    "TagTypeDef",
    "VariableEntryTypeDef",
    "ResponseMetadataTypeDef",
    "BatchGetVariableErrorTypeDef",
    "BatchGetVariableRequestRequestTypeDef",
    "VariableTypeDef",
    "BatchImportTypeDef",
    "BatchPredictionTypeDef",
    "CancelBatchImportJobRequestRequestTypeDef",
    "CancelBatchPredictionJobRequestRequestTypeDef",
    "ModelVersionTypeDef",
    "RuleTypeDef",
    "ExternalEventsDetailTypeDef",
    "FieldValidationMessageTypeDef",
    "FileValidationMessageTypeDef",
    "DeleteBatchImportJobRequestRequestTypeDef",
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteDetectorVersionRequestRequestTypeDef",
    "DeleteEntityTypeRequestRequestTypeDef",
    "DeleteEventRequestRequestTypeDef",
    "DeleteEventTypeRequestRequestTypeDef",
    "DeleteEventsByEventTypeRequestRequestTypeDef",
    "DeleteExternalModelRequestRequestTypeDef",
    "DeleteLabelRequestRequestTypeDef",
    "DeleteListRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteModelVersionRequestRequestTypeDef",
    "DeleteOutcomeRequestRequestTypeDef",
    "DeleteVariableRequestRequestTypeDef",
    "DescribeDetectorRequestRequestTypeDef",
    "DetectorVersionSummaryTypeDef",
    "DescribeModelVersionsRequestRequestTypeDef",
    "DetectorTypeDef",
    "EntityTypeDef",
    "EntityTypeTypeDef",
    "EvaluatedExternalModelTypeDef",
    "EvaluatedRuleTypeDef",
    "EventOrchestrationTypeDef",
    "EventPredictionSummaryTypeDef",
    "IngestedEventStatisticsTypeDef",
    "EventVariableSummaryTypeDef",
    "ExternalModelSummaryTypeDef",
    "ModelInputConfigurationTypeDef",
    "ModelOutputConfigurationOutputTypeDef",
    "FilterConditionTypeDef",
    "GetBatchImportJobsRequestRequestTypeDef",
    "GetBatchPredictionJobsRequestRequestTypeDef",
    "GetDeleteEventsByEventTypeStatusRequestRequestTypeDef",
    "GetDetectorVersionRequestRequestTypeDef",
    "GetDetectorsRequestRequestTypeDef",
    "GetEntityTypesRequestRequestTypeDef",
    "GetEventPredictionMetadataRequestRequestTypeDef",
    "ModelEndpointDataBlobTypeDef",
    "RuleResultTypeDef",
    "GetEventRequestRequestTypeDef",
    "GetEventTypesRequestRequestTypeDef",
    "GetExternalModelsRequestRequestTypeDef",
    "KMSKeyTypeDef",
    "GetLabelsRequestRequestTypeDef",
    "LabelTypeDef",
    "GetListElementsRequestRequestTypeDef",
    "GetListsMetadataRequestRequestTypeDef",
    "GetModelVersionRequestRequestTypeDef",
    "GetModelsRequestRequestTypeDef",
    "ModelTypeDef",
    "GetOutcomesRequestRequestTypeDef",
    "OutcomeTypeDef",
    "GetRulesRequestRequestTypeDef",
    "RuleDetailTypeDef",
    "GetVariablesRequestRequestTypeDef",
    "IngestedEventsTimeWindowTypeDef",
    "LabelSchemaOutputTypeDef",
    "LabelSchemaTypeDef",
    "PredictionTimeRangeTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "LogOddsMetricTypeDef",
    "MetricDataPointTypeDef",
    "ModelOutputConfigurationTypeDef",
    "OFIMetricDataPointTypeDef",
    "UncertaintyRangeTypeDef",
    "VariableImpactExplanationTypeDef",
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    "TFIMetricDataPointTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    "UpdateEventLabelRequestRequestTypeDef",
    "UpdateListRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateModelVersionStatusRequestRequestTypeDef",
    "UpdateVariableRequestRequestTypeDef",
    "ATITrainingMetricsValueTypeDef",
    "AggregatedVariablesImportanceMetricsTypeDef",
    "CreateBatchImportJobRequestRequestTypeDef",
    "CreateBatchPredictionJobRequestRequestTypeDef",
    "CreateListRequestRequestTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateVariableRequestRequestTypeDef",
    "PutDetectorRequestRequestTypeDef",
    "PutEntityTypeRequestRequestTypeDef",
    "PutLabelRequestRequestTypeDef",
    "PutOutcomeRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "BatchCreateVariableRequestRequestTypeDef",
    "BatchCreateVariableResultTypeDef",
    "CreateDetectorVersionResultTypeDef",
    "CreateModelVersionResultTypeDef",
    "DeleteEventsByEventTypeResultTypeDef",
    "GetDeleteEventsByEventTypeStatusResultTypeDef",
    "GetListElementsResultTypeDef",
    "GetListsMetadataResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "UpdateModelVersionResultTypeDef",
    "BatchGetVariableResultTypeDef",
    "GetVariablesResultTypeDef",
    "GetBatchImportJobsResultTypeDef",
    "GetBatchPredictionJobsResultTypeDef",
    "ModelScoresTypeDef",
    "CreateDetectorVersionRequestRequestTypeDef",
    "CreateRuleResultTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "GetDetectorVersionResultTypeDef",
    "UpdateDetectorVersionRequestRequestTypeDef",
    "UpdateRuleMetadataRequestRequestTypeDef",
    "UpdateRuleVersionRequestRequestTypeDef",
    "UpdateRuleVersionResultTypeDef",
    "DataValidationMetricsTypeDef",
    "DescribeDetectorResultTypeDef",
    "GetDetectorsResultTypeDef",
    "EventTypeDef",
    "SendEventRequestRequestTypeDef",
    "GetEntityTypesResultTypeDef",
    "PutEventTypeRequestRequestTypeDef",
    "ListEventPredictionsResultTypeDef",
    "EventTypeTypeDef",
    "ExternalModelOutputsTypeDef",
    "ExternalModelTypeDef",
    "GetEventPredictionRequestRequestTypeDef",
    "GetKMSEncryptionKeyResultTypeDef",
    "GetLabelsResultTypeDef",
    "GetModelsResultTypeDef",
    "GetOutcomesResultTypeDef",
    "GetRulesResultTypeDef",
    "IngestedEventsDetailTypeDef",
    "TrainingDataSchemaOutputTypeDef",
    "TrainingDataSchemaTypeDef",
    "ListEventPredictionsRequestRequestTypeDef",
    "VariableImportanceMetricsTypeDef",
    "TrainingMetricsTypeDef",
    "PutExternalModelRequestRequestTypeDef",
    "OFIModelPerformanceTypeDef",
    "TFIModelPerformanceTypeDef",
    "PredictionExplanationsTypeDef",
    "GetEventResultTypeDef",
    "GetEventTypesResultTypeDef",
    "GetEventPredictionResultTypeDef",
    "GetExternalModelsResultTypeDef",
    "UpdateModelVersionRequestRequestTypeDef",
    "GetModelVersionResultTypeDef",
    "CreateModelVersionRequestRequestTypeDef",
    "TrainingResultTypeDef",
    "OFITrainingMetricsValueTypeDef",
    "TFITrainingMetricsValueTypeDef",
    "ModelVersionEvaluationTypeDef",
    "TrainingMetricsV2TypeDef",
    "EvaluatedModelVersionTypeDef",
    "TrainingResultV2TypeDef",
    "GetEventPredictionMetadataResultTypeDef",
    "ModelVersionDetailTypeDef",
    "DescribeModelVersionsResultTypeDef",
)

ATIMetricDataPointTypeDef = TypedDict(
    "ATIMetricDataPointTypeDef",
    {
        "cr": float,
        "adr": float,
        "threshold": float,
        "atodr": float,
    },
    total=False,
)

ATIModelPerformanceTypeDef = TypedDict(
    "ATIModelPerformanceTypeDef",
    {
        "asi": float,
    },
    total=False,
)

AggregatedLogOddsMetricTypeDef = TypedDict(
    "AggregatedLogOddsMetricTypeDef",
    {
        "variableNames": List[str],
        "aggregatedVariablesImportance": float,
    },
)

AggregatedVariablesImpactExplanationTypeDef = TypedDict(
    "AggregatedVariablesImpactExplanationTypeDef",
    {
        "eventVariableNames": List[str],
        "relativeImpact": str,
        "logOddsImpact": float,
    },
    total=False,
)

_RequiredAllowDenyListTypeDef = TypedDict(
    "_RequiredAllowDenyListTypeDef",
    {
        "name": str,
    },
)
_OptionalAllowDenyListTypeDef = TypedDict(
    "_OptionalAllowDenyListTypeDef",
    {
        "description": str,
        "variableType": str,
        "createdTime": str,
        "updatedTime": str,
        "arn": str,
    },
    total=False,
)

class AllowDenyListTypeDef(_RequiredAllowDenyListTypeDef, _OptionalAllowDenyListTypeDef):
    pass

BatchCreateVariableErrorTypeDef = TypedDict(
    "BatchCreateVariableErrorTypeDef",
    {
        "name": str,
        "code": int,
        "message": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

VariableEntryTypeDef = TypedDict(
    "VariableEntryTypeDef",
    {
        "name": str,
        "dataType": str,
        "dataSource": str,
        "defaultValue": str,
        "description": str,
        "variableType": str,
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

BatchGetVariableErrorTypeDef = TypedDict(
    "BatchGetVariableErrorTypeDef",
    {
        "name": str,
        "code": int,
        "message": str,
    },
    total=False,
)

BatchGetVariableRequestRequestTypeDef = TypedDict(
    "BatchGetVariableRequestRequestTypeDef",
    {
        "names": Sequence[str],
    },
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
        "description": str,
        "variableType": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

BatchImportTypeDef = TypedDict(
    "BatchImportTypeDef",
    {
        "jobId": str,
        "status": AsyncJobStatusType,
        "failureReason": str,
        "startTime": str,
        "completionTime": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "iamRoleArn": str,
        "arn": str,
        "processedRecordsCount": int,
        "failedRecordsCount": int,
        "totalRecordsCount": int,
    },
    total=False,
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "jobId": str,
        "status": AsyncJobStatusType,
        "failureReason": str,
        "startTime": str,
        "completionTime": str,
        "lastHeartbeatTime": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "detectorVersion": str,
        "iamRoleArn": str,
        "arn": str,
        "processedRecordsCount": int,
        "totalRecordsCount": int,
    },
    total=False,
)

CancelBatchImportJobRequestRequestTypeDef = TypedDict(
    "CancelBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

CancelBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "CancelBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

_RequiredModelVersionTypeDef = TypedDict(
    "_RequiredModelVersionTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)
_OptionalModelVersionTypeDef = TypedDict(
    "_OptionalModelVersionTypeDef",
    {
        "arn": str,
    },
    total=False,
)

class ModelVersionTypeDef(_RequiredModelVersionTypeDef, _OptionalModelVersionTypeDef):
    pass

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "detectorId": str,
        "ruleId": str,
        "ruleVersion": str,
    },
)

ExternalEventsDetailTypeDef = TypedDict(
    "ExternalEventsDetailTypeDef",
    {
        "dataLocation": str,
        "dataAccessRoleArn": str,
    },
)

FieldValidationMessageTypeDef = TypedDict(
    "FieldValidationMessageTypeDef",
    {
        "fieldName": str,
        "identifier": str,
        "title": str,
        "content": str,
        "type": str,
    },
    total=False,
)

FileValidationMessageTypeDef = TypedDict(
    "FileValidationMessageTypeDef",
    {
        "title": str,
        "content": str,
        "type": str,
    },
    total=False,
)

DeleteBatchImportJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DeleteBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)

DeleteDetectorVersionRequestRequestTypeDef = TypedDict(
    "DeleteDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

DeleteEntityTypeRequestRequestTypeDef = TypedDict(
    "DeleteEntityTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredDeleteEventRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
    },
)
_OptionalDeleteEventRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteEventRequestRequestTypeDef",
    {
        "deleteAuditHistory": bool,
    },
    total=False,
)

class DeleteEventRequestRequestTypeDef(
    _RequiredDeleteEventRequestRequestTypeDef, _OptionalDeleteEventRequestRequestTypeDef
):
    pass

DeleteEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEventsByEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventsByEventTypeRequestRequestTypeDef",
    {
        "eventTypeName": str,
    },
)

DeleteExternalModelRequestRequestTypeDef = TypedDict(
    "DeleteExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
    },
)

DeleteLabelRequestRequestTypeDef = TypedDict(
    "DeleteLabelRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteListRequestRequestTypeDef = TypedDict(
    "DeleteListRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
    },
)

DeleteModelVersionRequestRequestTypeDef = TypedDict(
    "DeleteModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)

DeleteOutcomeRequestRequestTypeDef = TypedDict(
    "DeleteOutcomeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteVariableRequestRequestTypeDef = TypedDict(
    "DeleteVariableRequestRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredDescribeDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)
_OptionalDescribeDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDetectorRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeDetectorRequestRequestTypeDef(
    _RequiredDescribeDetectorRequestRequestTypeDef, _OptionalDescribeDetectorRequestRequestTypeDef
):
    pass

DetectorVersionSummaryTypeDef = TypedDict(
    "DetectorVersionSummaryTypeDef",
    {
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "description": str,
        "lastUpdatedTime": str,
    },
    total=False,
)

DescribeModelVersionsRequestRequestTypeDef = TypedDict(
    "DescribeModelVersionsRequestRequestTypeDef",
    {
        "modelId": str,
        "modelVersionNumber": str,
        "modelType": ModelTypeEnumType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorId": str,
        "description": str,
        "eventTypeName": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "entityType": str,
        "entityId": str,
    },
)

EntityTypeTypeDef = TypedDict(
    "EntityTypeTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

EvaluatedExternalModelTypeDef = TypedDict(
    "EvaluatedExternalModelTypeDef",
    {
        "modelEndpoint": str,
        "useEventVariables": bool,
        "inputVariables": Dict[str, str],
        "outputVariables": Dict[str, str],
    },
    total=False,
)

EvaluatedRuleTypeDef = TypedDict(
    "EvaluatedRuleTypeDef",
    {
        "ruleId": str,
        "ruleVersion": str,
        "expression": str,
        "expressionWithValues": str,
        "outcomes": List[str],
        "evaluated": bool,
        "matched": bool,
    },
    total=False,
)

EventOrchestrationTypeDef = TypedDict(
    "EventOrchestrationTypeDef",
    {
        "eventBridgeEnabled": bool,
    },
)

EventPredictionSummaryTypeDef = TypedDict(
    "EventPredictionSummaryTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "eventTimestamp": str,
        "predictionTimestamp": str,
        "detectorId": str,
        "detectorVersionId": str,
    },
    total=False,
)

IngestedEventStatisticsTypeDef = TypedDict(
    "IngestedEventStatisticsTypeDef",
    {
        "numberOfEvents": int,
        "eventDataSizeInBytes": int,
        "leastRecentEvent": str,
        "mostRecentEvent": str,
        "lastUpdatedTime": str,
    },
    total=False,
)

EventVariableSummaryTypeDef = TypedDict(
    "EventVariableSummaryTypeDef",
    {
        "name": str,
        "value": str,
        "source": str,
    },
    total=False,
)

ExternalModelSummaryTypeDef = TypedDict(
    "ExternalModelSummaryTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
    },
    total=False,
)

_RequiredModelInputConfigurationTypeDef = TypedDict(
    "_RequiredModelInputConfigurationTypeDef",
    {
        "useEventVariables": bool,
    },
)
_OptionalModelInputConfigurationTypeDef = TypedDict(
    "_OptionalModelInputConfigurationTypeDef",
    {
        "eventTypeName": str,
        "format": ModelInputDataFormatType,
        "jsonInputTemplate": str,
        "csvInputTemplate": str,
    },
    total=False,
)

class ModelInputConfigurationTypeDef(
    _RequiredModelInputConfigurationTypeDef, _OptionalModelInputConfigurationTypeDef
):
    pass

_RequiredModelOutputConfigurationOutputTypeDef = TypedDict(
    "_RequiredModelOutputConfigurationOutputTypeDef",
    {
        "format": ModelOutputDataFormatType,
    },
)
_OptionalModelOutputConfigurationOutputTypeDef = TypedDict(
    "_OptionalModelOutputConfigurationOutputTypeDef",
    {
        "jsonKeyToVariableMap": Dict[str, str],
        "csvIndexToVariableMap": Dict[str, str],
    },
    total=False,
)

class ModelOutputConfigurationOutputTypeDef(
    _RequiredModelOutputConfigurationOutputTypeDef, _OptionalModelOutputConfigurationOutputTypeDef
):
    pass

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "value": str,
    },
    total=False,
)

GetBatchImportJobsRequestRequestTypeDef = TypedDict(
    "GetBatchImportJobsRequestRequestTypeDef",
    {
        "jobId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetBatchPredictionJobsRequestRequestTypeDef = TypedDict(
    "GetBatchPredictionJobsRequestRequestTypeDef",
    {
        "jobId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetDeleteEventsByEventTypeStatusRequestRequestTypeDef = TypedDict(
    "GetDeleteEventsByEventTypeStatusRequestRequestTypeDef",
    {
        "eventTypeName": str,
    },
)

GetDetectorVersionRequestRequestTypeDef = TypedDict(
    "GetDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

GetDetectorsRequestRequestTypeDef = TypedDict(
    "GetDetectorsRequestRequestTypeDef",
    {
        "detectorId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEntityTypesRequestRequestTypeDef = TypedDict(
    "GetEntityTypesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEventPredictionMetadataRequestRequestTypeDef = TypedDict(
    "GetEventPredictionMetadataRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "detectorId": str,
        "detectorVersionId": str,
        "predictionTimestamp": str,
    },
)

ModelEndpointDataBlobTypeDef = TypedDict(
    "ModelEndpointDataBlobTypeDef",
    {
        "byteBuffer": Union[str, bytes, IO[Any], StreamingBody],
        "contentType": str,
    },
    total=False,
)

RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "ruleId": str,
        "outcomes": List[str],
    },
    total=False,
)

GetEventRequestRequestTypeDef = TypedDict(
    "GetEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
    },
)

GetEventTypesRequestRequestTypeDef = TypedDict(
    "GetEventTypesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetExternalModelsRequestRequestTypeDef = TypedDict(
    "GetExternalModelsRequestRequestTypeDef",
    {
        "modelEndpoint": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

KMSKeyTypeDef = TypedDict(
    "KMSKeyTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
    total=False,
)

GetLabelsRequestRequestTypeDef = TypedDict(
    "GetLabelsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredGetListElementsRequestRequestTypeDef = TypedDict(
    "_RequiredGetListElementsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetListElementsRequestRequestTypeDef = TypedDict(
    "_OptionalGetListElementsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetListElementsRequestRequestTypeDef(
    _RequiredGetListElementsRequestRequestTypeDef, _OptionalGetListElementsRequestRequestTypeDef
):
    pass

GetListsMetadataRequestRequestTypeDef = TypedDict(
    "GetListsMetadataRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetModelVersionRequestRequestTypeDef = TypedDict(
    "GetModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)

GetModelsRequestRequestTypeDef = TypedDict(
    "GetModelsRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "description": str,
        "eventTypeName": str,
        "createdTime": str,
        "lastUpdatedTime": str,
        "arn": str,
    },
    total=False,
)

GetOutcomesRequestRequestTypeDef = TypedDict(
    "GetOutcomesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

OutcomeTypeDef = TypedDict(
    "OutcomeTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredGetRulesRequestRequestTypeDef = TypedDict(
    "_RequiredGetRulesRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)
_OptionalGetRulesRequestRequestTypeDef = TypedDict(
    "_OptionalGetRulesRequestRequestTypeDef",
    {
        "ruleId": str,
        "ruleVersion": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetRulesRequestRequestTypeDef(
    _RequiredGetRulesRequestRequestTypeDef, _OptionalGetRulesRequestRequestTypeDef
):
    pass

RuleDetailTypeDef = TypedDict(
    "RuleDetailTypeDef",
    {
        "ruleId": str,
        "description": str,
        "detectorId": str,
        "ruleVersion": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

GetVariablesRequestRequestTypeDef = TypedDict(
    "GetVariablesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

IngestedEventsTimeWindowTypeDef = TypedDict(
    "IngestedEventsTimeWindowTypeDef",
    {
        "startTime": str,
        "endTime": str,
    },
)

LabelSchemaOutputTypeDef = TypedDict(
    "LabelSchemaOutputTypeDef",
    {
        "labelMapper": Dict[str, List[str]],
        "unlabeledEventsTreatment": UnlabeledEventsTreatmentType,
    },
    total=False,
)

LabelSchemaTypeDef = TypedDict(
    "LabelSchemaTypeDef",
    {
        "labelMapper": Mapping[str, Sequence[str]],
        "unlabeledEventsTreatment": UnlabeledEventsTreatmentType,
    },
    total=False,
)

PredictionTimeRangeTypeDef = TypedDict(
    "PredictionTimeRangeTypeDef",
    {
        "startTime": str,
        "endTime": str,
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

LogOddsMetricTypeDef = TypedDict(
    "LogOddsMetricTypeDef",
    {
        "variableName": str,
        "variableType": str,
        "variableImportance": float,
    },
)

MetricDataPointTypeDef = TypedDict(
    "MetricDataPointTypeDef",
    {
        "fpr": float,
        "precision": float,
        "tpr": float,
        "threshold": float,
    },
    total=False,
)

_RequiredModelOutputConfigurationTypeDef = TypedDict(
    "_RequiredModelOutputConfigurationTypeDef",
    {
        "format": ModelOutputDataFormatType,
    },
)
_OptionalModelOutputConfigurationTypeDef = TypedDict(
    "_OptionalModelOutputConfigurationTypeDef",
    {
        "jsonKeyToVariableMap": Mapping[str, str],
        "csvIndexToVariableMap": Mapping[str, str],
    },
    total=False,
)

class ModelOutputConfigurationTypeDef(
    _RequiredModelOutputConfigurationTypeDef, _OptionalModelOutputConfigurationTypeDef
):
    pass

OFIMetricDataPointTypeDef = TypedDict(
    "OFIMetricDataPointTypeDef",
    {
        "fpr": float,
        "precision": float,
        "tpr": float,
        "threshold": float,
    },
    total=False,
)

UncertaintyRangeTypeDef = TypedDict(
    "UncertaintyRangeTypeDef",
    {
        "lowerBoundValue": float,
        "upperBoundValue": float,
    },
)

VariableImpactExplanationTypeDef = TypedDict(
    "VariableImpactExplanationTypeDef",
    {
        "eventVariableName": str,
        "relativeImpact": str,
        "logOddsImpact": float,
    },
    total=False,
)

PutKMSEncryptionKeyRequestRequestTypeDef = TypedDict(
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
)

TFIMetricDataPointTypeDef = TypedDict(
    "TFIMetricDataPointTypeDef",
    {
        "fpr": float,
        "precision": float,
        "tpr": float,
        "threshold": float,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)

UpdateDetectorVersionMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
    },
)

UpdateDetectorVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
    },
)

UpdateEventLabelRequestRequestTypeDef = TypedDict(
    "UpdateEventLabelRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "assignedLabel": str,
        "labelTimestamp": str,
    },
)

_RequiredUpdateListRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateListRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateListRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateListRequestRequestTypeDef",
    {
        "elements": Sequence[str],
        "description": str,
        "updateMode": ListUpdateModeType,
        "variableType": str,
    },
    total=False,
)

class UpdateListRequestRequestTypeDef(
    _RequiredUpdateListRequestRequestTypeDef, _OptionalUpdateListRequestRequestTypeDef
):
    pass

_RequiredUpdateModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
    },
)
_OptionalUpdateModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateModelRequestRequestTypeDef(
    _RequiredUpdateModelRequestRequestTypeDef, _OptionalUpdateModelRequestRequestTypeDef
):
    pass

UpdateModelVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateModelVersionStatusRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": ModelVersionStatusType,
    },
)

_RequiredUpdateVariableRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVariableRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateVariableRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVariableRequestRequestTypeDef",
    {
        "defaultValue": str,
        "description": str,
        "variableType": str,
    },
    total=False,
)

class UpdateVariableRequestRequestTypeDef(
    _RequiredUpdateVariableRequestRequestTypeDef, _OptionalUpdateVariableRequestRequestTypeDef
):
    pass

ATITrainingMetricsValueTypeDef = TypedDict(
    "ATITrainingMetricsValueTypeDef",
    {
        "metricDataPoints": List[ATIMetricDataPointTypeDef],
        "modelPerformance": ATIModelPerformanceTypeDef,
    },
    total=False,
)

AggregatedVariablesImportanceMetricsTypeDef = TypedDict(
    "AggregatedVariablesImportanceMetricsTypeDef",
    {
        "logOddsMetrics": List[AggregatedLogOddsMetricTypeDef],
    },
    total=False,
)

_RequiredCreateBatchImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "iamRoleArn": str,
    },
)
_OptionalCreateBatchImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBatchImportJobRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateBatchImportJobRequestRequestTypeDef(
    _RequiredCreateBatchImportJobRequestRequestTypeDef,
    _OptionalCreateBatchImportJobRequestRequestTypeDef,
):
    pass

_RequiredCreateBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "iamRoleArn": str,
    },
)
_OptionalCreateBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBatchPredictionJobRequestRequestTypeDef",
    {
        "detectorVersion": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateBatchPredictionJobRequestRequestTypeDef(
    _RequiredCreateBatchPredictionJobRequestRequestTypeDef,
    _OptionalCreateBatchPredictionJobRequestRequestTypeDef,
):
    pass

_RequiredCreateListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateListRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateListRequestRequestTypeDef",
    {
        "elements": Sequence[str],
        "variableType": str,
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateListRequestRequestTypeDef(
    _RequiredCreateListRequestRequestTypeDef, _OptionalCreateListRequestRequestTypeDef
):
    pass

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "eventTypeName": str,
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "ruleId": str,
        "detectorId": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": Sequence[str],
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass

_RequiredCreateVariableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVariableRequestRequestTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
    },
)
_OptionalCreateVariableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVariableRequestRequestTypeDef",
    {
        "description": str,
        "variableType": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVariableRequestRequestTypeDef(
    _RequiredCreateVariableRequestRequestTypeDef, _OptionalCreateVariableRequestRequestTypeDef
):
    pass

_RequiredPutDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredPutDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventTypeName": str,
    },
)
_OptionalPutDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalPutDetectorRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class PutDetectorRequestRequestTypeDef(
    _RequiredPutDetectorRequestRequestTypeDef, _OptionalPutDetectorRequestRequestTypeDef
):
    pass

_RequiredPutEntityTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutEntityTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutEntityTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutEntityTypeRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class PutEntityTypeRequestRequestTypeDef(
    _RequiredPutEntityTypeRequestRequestTypeDef, _OptionalPutEntityTypeRequestRequestTypeDef
):
    pass

_RequiredPutLabelRequestRequestTypeDef = TypedDict(
    "_RequiredPutLabelRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutLabelRequestRequestTypeDef = TypedDict(
    "_OptionalPutLabelRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class PutLabelRequestRequestTypeDef(
    _RequiredPutLabelRequestRequestTypeDef, _OptionalPutLabelRequestRequestTypeDef
):
    pass

_RequiredPutOutcomeRequestRequestTypeDef = TypedDict(
    "_RequiredPutOutcomeRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutOutcomeRequestRequestTypeDef = TypedDict(
    "_OptionalPutOutcomeRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class PutOutcomeRequestRequestTypeDef(
    _RequiredPutOutcomeRequestRequestTypeDef, _OptionalPutOutcomeRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Sequence[TagTypeDef],
    },
)

_RequiredBatchCreateVariableRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateVariableRequestRequestTypeDef",
    {
        "variableEntries": Sequence[VariableEntryTypeDef],
    },
)
_OptionalBatchCreateVariableRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateVariableRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class BatchCreateVariableRequestRequestTypeDef(
    _RequiredBatchCreateVariableRequestRequestTypeDef,
    _OptionalBatchCreateVariableRequestRequestTypeDef,
):
    pass

BatchCreateVariableResultTypeDef = TypedDict(
    "BatchCreateVariableResultTypeDef",
    {
        "errors": List[BatchCreateVariableErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDetectorVersionResultTypeDef = TypedDict(
    "CreateDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelVersionResultTypeDef = TypedDict(
    "CreateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteEventsByEventTypeResultTypeDef = TypedDict(
    "DeleteEventsByEventTypeResultTypeDef",
    {
        "eventTypeName": str,
        "eventsDeletionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDeleteEventsByEventTypeStatusResultTypeDef = TypedDict(
    "GetDeleteEventsByEventTypeStatusResultTypeDef",
    {
        "eventTypeName": str,
        "eventsDeletionStatus": AsyncJobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetListElementsResultTypeDef = TypedDict(
    "GetListElementsResultTypeDef",
    {
        "elements": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetListsMetadataResultTypeDef = TypedDict(
    "GetListsMetadataResultTypeDef",
    {
        "lists": List[AllowDenyListTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List[TagTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateModelVersionResultTypeDef = TypedDict(
    "UpdateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchGetVariableResultTypeDef = TypedDict(
    "BatchGetVariableResultTypeDef",
    {
        "variables": List[VariableTypeDef],
        "errors": List[BatchGetVariableErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetVariablesResultTypeDef = TypedDict(
    "GetVariablesResultTypeDef",
    {
        "variables": List[VariableTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBatchImportJobsResultTypeDef = TypedDict(
    "GetBatchImportJobsResultTypeDef",
    {
        "batchImports": List[BatchImportTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBatchPredictionJobsResultTypeDef = TypedDict(
    "GetBatchPredictionJobsResultTypeDef",
    {
        "batchPredictions": List[BatchPredictionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ModelScoresTypeDef = TypedDict(
    "ModelScoresTypeDef",
    {
        "modelVersion": ModelVersionTypeDef,
        "scores": Dict[str, float],
    },
    total=False,
)

_RequiredCreateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "rules": Sequence[RuleTypeDef],
    },
)
_OptionalCreateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorVersionRequestRequestTypeDef",
    {
        "description": str,
        "externalModelEndpoints": Sequence[str],
        "modelVersions": Sequence[ModelVersionTypeDef],
        "ruleExecutionMode": RuleExecutionModeType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateDetectorVersionRequestRequestTypeDef(
    _RequiredCreateDetectorVersionRequestRequestTypeDef,
    _OptionalCreateDetectorVersionRequestRequestTypeDef,
):
    pass

CreateRuleResultTypeDef = TypedDict(
    "CreateRuleResultTypeDef",
    {
        "rule": RuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "rule": RuleTypeDef,
    },
)

GetDetectorVersionResultTypeDef = TypedDict(
    "GetDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List[ModelVersionTypeDef],
        "rules": List[RuleTypeDef],
        "status": DetectorVersionStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "ruleExecutionMode": RuleExecutionModeType,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "externalModelEndpoints": Sequence[str],
        "rules": Sequence[RuleTypeDef],
    },
)
_OptionalUpdateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorVersionRequestRequestTypeDef",
    {
        "description": str,
        "modelVersions": Sequence[ModelVersionTypeDef],
        "ruleExecutionMode": RuleExecutionModeType,
    },
    total=False,
)

class UpdateDetectorVersionRequestRequestTypeDef(
    _RequiredUpdateDetectorVersionRequestRequestTypeDef,
    _OptionalUpdateDetectorVersionRequestRequestTypeDef,
):
    pass

UpdateRuleMetadataRequestRequestTypeDef = TypedDict(
    "UpdateRuleMetadataRequestRequestTypeDef",
    {
        "rule": RuleTypeDef,
        "description": str,
    },
)

_RequiredUpdateRuleVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleVersionRequestRequestTypeDef",
    {
        "rule": RuleTypeDef,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": Sequence[str],
    },
)
_OptionalUpdateRuleVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleVersionRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class UpdateRuleVersionRequestRequestTypeDef(
    _RequiredUpdateRuleVersionRequestRequestTypeDef, _OptionalUpdateRuleVersionRequestRequestTypeDef
):
    pass

UpdateRuleVersionResultTypeDef = TypedDict(
    "UpdateRuleVersionResultTypeDef",
    {
        "rule": RuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DataValidationMetricsTypeDef = TypedDict(
    "DataValidationMetricsTypeDef",
    {
        "fileLevelMessages": List[FileValidationMessageTypeDef],
        "fieldLevelMessages": List[FieldValidationMessageTypeDef],
    },
    total=False,
)

DescribeDetectorResultTypeDef = TypedDict(
    "DescribeDetectorResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionSummaries": List[DetectorVersionSummaryTypeDef],
        "nextToken": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDetectorsResultTypeDef = TypedDict(
    "GetDetectorsResultTypeDef",
    {
        "detectors": List[DetectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "eventTimestamp": str,
        "eventVariables": Dict[str, str],
        "currentLabel": str,
        "labelTimestamp": str,
        "entities": List[EntityTypeDef],
    },
    total=False,
)

_RequiredSendEventRequestRequestTypeDef = TypedDict(
    "_RequiredSendEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "eventTimestamp": str,
        "eventVariables": Mapping[str, str],
        "entities": Sequence[EntityTypeDef],
    },
)
_OptionalSendEventRequestRequestTypeDef = TypedDict(
    "_OptionalSendEventRequestRequestTypeDef",
    {
        "assignedLabel": str,
        "labelTimestamp": str,
    },
    total=False,
)

class SendEventRequestRequestTypeDef(
    _RequiredSendEventRequestRequestTypeDef, _OptionalSendEventRequestRequestTypeDef
):
    pass

GetEntityTypesResultTypeDef = TypedDict(
    "GetEntityTypesResultTypeDef",
    {
        "entityTypes": List[EntityTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPutEventTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventTypeRequestRequestTypeDef",
    {
        "name": str,
        "eventVariables": Sequence[str],
        "entityTypes": Sequence[str],
    },
)
_OptionalPutEventTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventTypeRequestRequestTypeDef",
    {
        "description": str,
        "labels": Sequence[str],
        "eventIngestion": EventIngestionType,
        "tags": Sequence[TagTypeDef],
        "eventOrchestration": EventOrchestrationTypeDef,
    },
    total=False,
)

class PutEventTypeRequestRequestTypeDef(
    _RequiredPutEventTypeRequestRequestTypeDef, _OptionalPutEventTypeRequestRequestTypeDef
):
    pass

ListEventPredictionsResultTypeDef = TypedDict(
    "ListEventPredictionsResultTypeDef",
    {
        "eventPredictionSummaries": List[EventPredictionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "name": str,
        "description": str,
        "eventVariables": List[str],
        "labels": List[str],
        "entityTypes": List[str],
        "eventIngestion": EventIngestionType,
        "ingestedEventStatistics": IngestedEventStatisticsTypeDef,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
        "eventOrchestration": EventOrchestrationTypeDef,
    },
    total=False,
)

ExternalModelOutputsTypeDef = TypedDict(
    "ExternalModelOutputsTypeDef",
    {
        "externalModel": ExternalModelSummaryTypeDef,
        "outputs": Dict[str, str],
    },
    total=False,
)

ExternalModelTypeDef = TypedDict(
    "ExternalModelTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": ModelInputConfigurationTypeDef,
        "outputConfiguration": ModelOutputConfigurationOutputTypeDef,
        "modelEndpointStatus": ModelEndpointStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredGetEventPredictionRequestRequestTypeDef = TypedDict(
    "_RequiredGetEventPredictionRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventId": str,
        "eventTypeName": str,
        "entities": Sequence[EntityTypeDef],
        "eventTimestamp": str,
        "eventVariables": Mapping[str, str],
    },
)
_OptionalGetEventPredictionRequestRequestTypeDef = TypedDict(
    "_OptionalGetEventPredictionRequestRequestTypeDef",
    {
        "detectorVersionId": str,
        "externalModelEndpointDataBlobs": Mapping[str, ModelEndpointDataBlobTypeDef],
    },
    total=False,
)

class GetEventPredictionRequestRequestTypeDef(
    _RequiredGetEventPredictionRequestRequestTypeDef,
    _OptionalGetEventPredictionRequestRequestTypeDef,
):
    pass

GetKMSEncryptionKeyResultTypeDef = TypedDict(
    "GetKMSEncryptionKeyResultTypeDef",
    {
        "kmsKey": KMSKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLabelsResultTypeDef = TypedDict(
    "GetLabelsResultTypeDef",
    {
        "labels": List[LabelTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetModelsResultTypeDef = TypedDict(
    "GetModelsResultTypeDef",
    {
        "nextToken": str,
        "models": List[ModelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetOutcomesResultTypeDef = TypedDict(
    "GetOutcomesResultTypeDef",
    {
        "outcomes": List[OutcomeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRulesResultTypeDef = TypedDict(
    "GetRulesResultTypeDef",
    {
        "ruleDetails": List[RuleDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IngestedEventsDetailTypeDef = TypedDict(
    "IngestedEventsDetailTypeDef",
    {
        "ingestedEventsTimeWindow": IngestedEventsTimeWindowTypeDef,
    },
)

_RequiredTrainingDataSchemaOutputTypeDef = TypedDict(
    "_RequiredTrainingDataSchemaOutputTypeDef",
    {
        "modelVariables": List[str],
    },
)
_OptionalTrainingDataSchemaOutputTypeDef = TypedDict(
    "_OptionalTrainingDataSchemaOutputTypeDef",
    {
        "labelSchema": LabelSchemaOutputTypeDef,
    },
    total=False,
)

class TrainingDataSchemaOutputTypeDef(
    _RequiredTrainingDataSchemaOutputTypeDef, _OptionalTrainingDataSchemaOutputTypeDef
):
    pass

_RequiredTrainingDataSchemaTypeDef = TypedDict(
    "_RequiredTrainingDataSchemaTypeDef",
    {
        "modelVariables": Sequence[str],
    },
)
_OptionalTrainingDataSchemaTypeDef = TypedDict(
    "_OptionalTrainingDataSchemaTypeDef",
    {
        "labelSchema": LabelSchemaTypeDef,
    },
    total=False,
)

class TrainingDataSchemaTypeDef(
    _RequiredTrainingDataSchemaTypeDef, _OptionalTrainingDataSchemaTypeDef
):
    pass

ListEventPredictionsRequestRequestTypeDef = TypedDict(
    "ListEventPredictionsRequestRequestTypeDef",
    {
        "eventId": FilterConditionTypeDef,
        "eventType": FilterConditionTypeDef,
        "detectorId": FilterConditionTypeDef,
        "detectorVersionId": FilterConditionTypeDef,
        "predictionTimeRange": PredictionTimeRangeTypeDef,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

VariableImportanceMetricsTypeDef = TypedDict(
    "VariableImportanceMetricsTypeDef",
    {
        "logOddsMetrics": List[LogOddsMetricTypeDef],
    },
    total=False,
)

TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "auc": float,
        "metricDataPoints": List[MetricDataPointTypeDef],
    },
    total=False,
)

_RequiredPutExternalModelRequestRequestTypeDef = TypedDict(
    "_RequiredPutExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": ModelInputConfigurationTypeDef,
        "outputConfiguration": ModelOutputConfigurationTypeDef,
        "modelEndpointStatus": ModelEndpointStatusType,
    },
)
_OptionalPutExternalModelRequestRequestTypeDef = TypedDict(
    "_OptionalPutExternalModelRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class PutExternalModelRequestRequestTypeDef(
    _RequiredPutExternalModelRequestRequestTypeDef, _OptionalPutExternalModelRequestRequestTypeDef
):
    pass

OFIModelPerformanceTypeDef = TypedDict(
    "OFIModelPerformanceTypeDef",
    {
        "auc": float,
        "uncertaintyRange": UncertaintyRangeTypeDef,
    },
    total=False,
)

TFIModelPerformanceTypeDef = TypedDict(
    "TFIModelPerformanceTypeDef",
    {
        "auc": float,
        "uncertaintyRange": UncertaintyRangeTypeDef,
    },
    total=False,
)

PredictionExplanationsTypeDef = TypedDict(
    "PredictionExplanationsTypeDef",
    {
        "variableImpactExplanations": List[VariableImpactExplanationTypeDef],
        "aggregatedVariablesImpactExplanations": List[AggregatedVariablesImpactExplanationTypeDef],
    },
    total=False,
)

GetEventResultTypeDef = TypedDict(
    "GetEventResultTypeDef",
    {
        "event": EventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetEventTypesResultTypeDef = TypedDict(
    "GetEventTypesResultTypeDef",
    {
        "eventTypes": List[EventTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetEventPredictionResultTypeDef = TypedDict(
    "GetEventPredictionResultTypeDef",
    {
        "modelScores": List[ModelScoresTypeDef],
        "ruleResults": List[RuleResultTypeDef],
        "externalModelOutputs": List[ExternalModelOutputsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetExternalModelsResultTypeDef = TypedDict(
    "GetExternalModelsResultTypeDef",
    {
        "externalModels": List[ExternalModelTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateModelVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "majorVersionNumber": str,
    },
)
_OptionalUpdateModelVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelVersionRequestRequestTypeDef",
    {
        "externalEventsDetail": ExternalEventsDetailTypeDef,
        "ingestedEventsDetail": IngestedEventsDetailTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class UpdateModelVersionRequestRequestTypeDef(
    _RequiredUpdateModelVersionRequestRequestTypeDef,
    _OptionalUpdateModelVersionRequestRequestTypeDef,
):
    pass

GetModelVersionResultTypeDef = TypedDict(
    "GetModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": TrainingDataSchemaOutputTypeDef,
        "externalEventsDetail": ExternalEventsDetailTypeDef,
        "ingestedEventsDetail": IngestedEventsDetailTypeDef,
        "status": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateModelVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": TrainingDataSchemaTypeDef,
    },
)
_OptionalCreateModelVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelVersionRequestRequestTypeDef",
    {
        "externalEventsDetail": ExternalEventsDetailTypeDef,
        "ingestedEventsDetail": IngestedEventsDetailTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateModelVersionRequestRequestTypeDef(
    _RequiredCreateModelVersionRequestRequestTypeDef,
    _OptionalCreateModelVersionRequestRequestTypeDef,
):
    pass

TrainingResultTypeDef = TypedDict(
    "TrainingResultTypeDef",
    {
        "dataValidationMetrics": DataValidationMetricsTypeDef,
        "trainingMetrics": TrainingMetricsTypeDef,
        "variableImportanceMetrics": VariableImportanceMetricsTypeDef,
    },
    total=False,
)

OFITrainingMetricsValueTypeDef = TypedDict(
    "OFITrainingMetricsValueTypeDef",
    {
        "metricDataPoints": List[OFIMetricDataPointTypeDef],
        "modelPerformance": OFIModelPerformanceTypeDef,
    },
    total=False,
)

TFITrainingMetricsValueTypeDef = TypedDict(
    "TFITrainingMetricsValueTypeDef",
    {
        "metricDataPoints": List[TFIMetricDataPointTypeDef],
        "modelPerformance": TFIModelPerformanceTypeDef,
    },
    total=False,
)

ModelVersionEvaluationTypeDef = TypedDict(
    "ModelVersionEvaluationTypeDef",
    {
        "outputVariableName": str,
        "evaluationScore": str,
        "predictionExplanations": PredictionExplanationsTypeDef,
    },
    total=False,
)

TrainingMetricsV2TypeDef = TypedDict(
    "TrainingMetricsV2TypeDef",
    {
        "ofi": OFITrainingMetricsValueTypeDef,
        "tfi": TFITrainingMetricsValueTypeDef,
        "ati": ATITrainingMetricsValueTypeDef,
    },
    total=False,
)

EvaluatedModelVersionTypeDef = TypedDict(
    "EvaluatedModelVersionTypeDef",
    {
        "modelId": str,
        "modelVersion": str,
        "modelType": str,
        "evaluations": List[ModelVersionEvaluationTypeDef],
    },
    total=False,
)

TrainingResultV2TypeDef = TypedDict(
    "TrainingResultV2TypeDef",
    {
        "dataValidationMetrics": DataValidationMetricsTypeDef,
        "trainingMetricsV2": TrainingMetricsV2TypeDef,
        "variableImportanceMetrics": VariableImportanceMetricsTypeDef,
        "aggregatedVariablesImportanceMetrics": AggregatedVariablesImportanceMetricsTypeDef,
    },
    total=False,
)

GetEventPredictionMetadataResultTypeDef = TypedDict(
    "GetEventPredictionMetadataResultTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "entityId": str,
        "entityType": str,
        "eventTimestamp": str,
        "detectorId": str,
        "detectorVersionId": str,
        "detectorVersionStatus": str,
        "eventVariables": List[EventVariableSummaryTypeDef],
        "rules": List[EvaluatedRuleTypeDef],
        "ruleExecutionMode": RuleExecutionModeType,
        "outcomes": List[str],
        "evaluatedModelVersions": List[EvaluatedModelVersionTypeDef],
        "evaluatedExternalModels": List[EvaluatedExternalModelTypeDef],
        "predictionTimestamp": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ModelVersionDetailTypeDef = TypedDict(
    "ModelVersionDetailTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": TrainingDataSchemaOutputTypeDef,
        "externalEventsDetail": ExternalEventsDetailTypeDef,
        "ingestedEventsDetail": IngestedEventsDetailTypeDef,
        "trainingResult": TrainingResultTypeDef,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
        "trainingResultV2": TrainingResultV2TypeDef,
    },
    total=False,
)

DescribeModelVersionsResultTypeDef = TypedDict(
    "DescribeModelVersionsResultTypeDef",
    {
        "modelVersionDetails": List[ModelVersionDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
