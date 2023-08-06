"""
Type annotations for evidently service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/type_defs/)

Usage::

    ```python
    from mypy_boto3_evidently.type_defs import EvaluationRequestTypeDef

    data: EvaluationRequestTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ChangeDirectionEnumType,
    EventTypeType,
    ExperimentResultRequestTypeType,
    ExperimentResultResponseTypeType,
    ExperimentStatusType,
    ExperimentStopDesiredStateType,
    FeatureEvaluationStrategyType,
    FeatureStatusType,
    LaunchStatusType,
    LaunchStopDesiredStateType,
    ProjectStatusType,
    SegmentReferenceResourceTypeType,
    VariationValueTypeType,
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
    "EvaluationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CloudWatchLogsDestinationConfigTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "OnlineAbConfigTypeDef",
    "TreatmentConfigTypeDef",
    "LaunchGroupConfigTypeDef",
    "ProjectAppConfigResourceConfigTypeDef",
    "CreateSegmentRequestRequestTypeDef",
    "SegmentTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteFeatureRequestRequestTypeDef",
    "DeleteLaunchRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteSegmentRequestRequestTypeDef",
    "EvaluateFeatureRequestRequestTypeDef",
    "VariableValueTypeDef",
    "EvaluationRuleTypeDef",
    "TimestampTypeDef",
    "ExperimentExecutionTypeDef",
    "ExperimentReportTypeDef",
    "ExperimentResultsDataTypeDef",
    "ExperimentScheduleTypeDef",
    "OnlineAbDefinitionTypeDef",
    "TreatmentTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetFeatureRequestRequestTypeDef",
    "GetLaunchRequestRequestTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetSegmentRequestRequestTypeDef",
    "LaunchExecutionTypeDef",
    "LaunchGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListFeaturesRequestRequestTypeDef",
    "ListLaunchesRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ProjectSummaryTypeDef",
    "ListSegmentReferencesRequestRequestTypeDef",
    "RefResourceTypeDef",
    "ListSegmentsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MetricDefinitionConfigTypeDef",
    "MetricDefinitionTypeDef",
    "ProjectAppConfigResourceTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "PutProjectEventsResultEntryTypeDef",
    "SegmentOverrideTypeDef",
    "SegmentOverrideOutputTypeDef",
    "StartLaunchRequestRequestTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "StopLaunchRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestSegmentPatternRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchEvaluateFeatureRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentResponseTypeDef",
    "StopLaunchResponseTypeDef",
    "TestSegmentPatternResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "CreateSegmentResponseTypeDef",
    "GetSegmentResponseTypeDef",
    "ListSegmentsResponseTypeDef",
    "EvaluateFeatureResponseTypeDef",
    "EvaluationResultTypeDef",
    "VariationConfigTypeDef",
    "VariationTypeDef",
    "FeatureSummaryTypeDef",
    "EventTypeDef",
    "GetExperimentResultsRequestRequestTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "GetExperimentResultsResponseTypeDef",
    "ListExperimentsRequestListExperimentsPaginateTypeDef",
    "ListFeaturesRequestListFeaturesPaginateTypeDef",
    "ListLaunchesRequestListLaunchesPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef",
    "ListSegmentsRequestListSegmentsPaginateTypeDef",
    "ListProjectsResponseTypeDef",
    "ListSegmentReferencesResponseTypeDef",
    "MetricGoalConfigTypeDef",
    "MetricMonitorConfigTypeDef",
    "MetricGoalTypeDef",
    "MetricMonitorTypeDef",
    "ProjectDataDeliveryConfigTypeDef",
    "UpdateProjectDataDeliveryRequestRequestTypeDef",
    "ProjectDataDeliveryTypeDef",
    "PutProjectEventsResponseTypeDef",
    "ScheduledSplitConfigTypeDef",
    "ScheduledSplitTypeDef",
    "BatchEvaluateFeatureResponseTypeDef",
    "CreateFeatureRequestRequestTypeDef",
    "UpdateFeatureRequestRequestTypeDef",
    "FeatureTypeDef",
    "ListFeaturesResponseTypeDef",
    "PutProjectEventsRequestRequestTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "ExperimentTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "ProjectTypeDef",
    "ScheduledSplitsLaunchConfigTypeDef",
    "ScheduledSplitsLaunchDefinitionTypeDef",
    "CreateFeatureResponseTypeDef",
    "GetFeatureResponseTypeDef",
    "UpdateFeatureResponseTypeDef",
    "CreateExperimentResponseTypeDef",
    "GetExperimentResponseTypeDef",
    "ListExperimentsResponseTypeDef",
    "UpdateExperimentResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "GetProjectResponseTypeDef",
    "UpdateProjectDataDeliveryResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "CreateLaunchRequestRequestTypeDef",
    "UpdateLaunchRequestRequestTypeDef",
    "LaunchTypeDef",
    "CreateLaunchResponseTypeDef",
    "GetLaunchResponseTypeDef",
    "ListLaunchesResponseTypeDef",
    "StartLaunchResponseTypeDef",
    "UpdateLaunchResponseTypeDef",
)

_RequiredEvaluationRequestTypeDef = TypedDict(
    "_RequiredEvaluationRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
    },
)
_OptionalEvaluationRequestTypeDef = TypedDict(
    "_OptionalEvaluationRequestTypeDef",
    {
        "evaluationContext": str,
    },
    total=False,
)

class EvaluationRequestTypeDef(
    _RequiredEvaluationRequestTypeDef, _OptionalEvaluationRequestTypeDef
):
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

CloudWatchLogsDestinationConfigTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigTypeDef",
    {
        "logGroup": str,
    },
    total=False,
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "logGroup": str,
    },
    total=False,
)

OnlineAbConfigTypeDef = TypedDict(
    "OnlineAbConfigTypeDef",
    {
        "controlTreatmentName": str,
        "treatmentWeights": Mapping[str, int],
    },
    total=False,
)

_RequiredTreatmentConfigTypeDef = TypedDict(
    "_RequiredTreatmentConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
    },
)
_OptionalTreatmentConfigTypeDef = TypedDict(
    "_OptionalTreatmentConfigTypeDef",
    {
        "description": str,
    },
    total=False,
)

class TreatmentConfigTypeDef(_RequiredTreatmentConfigTypeDef, _OptionalTreatmentConfigTypeDef):
    pass

_RequiredLaunchGroupConfigTypeDef = TypedDict(
    "_RequiredLaunchGroupConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
    },
)
_OptionalLaunchGroupConfigTypeDef = TypedDict(
    "_OptionalLaunchGroupConfigTypeDef",
    {
        "description": str,
    },
    total=False,
)

class LaunchGroupConfigTypeDef(
    _RequiredLaunchGroupConfigTypeDef, _OptionalLaunchGroupConfigTypeDef
):
    pass

ProjectAppConfigResourceConfigTypeDef = TypedDict(
    "ProjectAppConfigResourceConfigTypeDef",
    {
        "applicationId": str,
        "environmentId": str,
    },
    total=False,
)

_RequiredCreateSegmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSegmentRequestRequestTypeDef",
    {
        "name": str,
        "pattern": str,
    },
)
_OptionalCreateSegmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSegmentRequestRequestTypeDef",
    {
        "description": str,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateSegmentRequestRequestTypeDef(
    _RequiredCreateSegmentRequestRequestTypeDef, _OptionalCreateSegmentRequestRequestTypeDef
):
    pass

_RequiredSegmentTypeDef = TypedDict(
    "_RequiredSegmentTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "pattern": str,
    },
)
_OptionalSegmentTypeDef = TypedDict(
    "_OptionalSegmentTypeDef",
    {
        "description": str,
        "experimentCount": int,
        "launchCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class SegmentTypeDef(_RequiredSegmentTypeDef, _OptionalSegmentTypeDef):
    pass

DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)

DeleteFeatureRequestRequestTypeDef = TypedDict(
    "DeleteFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)

DeleteLaunchRequestRequestTypeDef = TypedDict(
    "DeleteLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)

DeleteSegmentRequestRequestTypeDef = TypedDict(
    "DeleteSegmentRequestRequestTypeDef",
    {
        "segment": str,
    },
)

_RequiredEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "_RequiredEvaluateFeatureRequestRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
        "project": str,
    },
)
_OptionalEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "_OptionalEvaluateFeatureRequestRequestTypeDef",
    {
        "evaluationContext": str,
    },
    total=False,
)

class EvaluateFeatureRequestRequestTypeDef(
    _RequiredEvaluateFeatureRequestRequestTypeDef, _OptionalEvaluateFeatureRequestRequestTypeDef
):
    pass

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "boolValue": bool,
        "doubleValue": float,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

_RequiredEvaluationRuleTypeDef = TypedDict(
    "_RequiredEvaluationRuleTypeDef",
    {
        "type": str,
    },
)
_OptionalEvaluationRuleTypeDef = TypedDict(
    "_OptionalEvaluationRuleTypeDef",
    {
        "name": str,
    },
    total=False,
)

class EvaluationRuleTypeDef(_RequiredEvaluationRuleTypeDef, _OptionalEvaluationRuleTypeDef):
    pass

TimestampTypeDef = Union[datetime, str]
ExperimentExecutionTypeDef = TypedDict(
    "ExperimentExecutionTypeDef",
    {
        "endedTime": datetime,
        "startedTime": datetime,
    },
    total=False,
)

ExperimentReportTypeDef = TypedDict(
    "ExperimentReportTypeDef",
    {
        "content": str,
        "metricName": str,
        "reportName": Literal["BayesianInference"],
        "treatmentName": str,
    },
    total=False,
)

ExperimentResultsDataTypeDef = TypedDict(
    "ExperimentResultsDataTypeDef",
    {
        "metricName": str,
        "resultStat": ExperimentResultResponseTypeType,
        "treatmentName": str,
        "values": List[float],
    },
    total=False,
)

ExperimentScheduleTypeDef = TypedDict(
    "ExperimentScheduleTypeDef",
    {
        "analysisCompleteTime": datetime,
    },
    total=False,
)

OnlineAbDefinitionTypeDef = TypedDict(
    "OnlineAbDefinitionTypeDef",
    {
        "controlTreatmentName": str,
        "treatmentWeights": Dict[str, int],
    },
    total=False,
)

_RequiredTreatmentTypeDef = TypedDict(
    "_RequiredTreatmentTypeDef",
    {
        "name": str,
    },
)
_OptionalTreatmentTypeDef = TypedDict(
    "_OptionalTreatmentTypeDef",
    {
        "description": str,
        "featureVariations": Dict[str, str],
    },
    total=False,
)

class TreatmentTypeDef(_RequiredTreatmentTypeDef, _OptionalTreatmentTypeDef):
    pass

GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)

GetFeatureRequestRequestTypeDef = TypedDict(
    "GetFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)

GetLaunchRequestRequestTypeDef = TypedDict(
    "GetLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)

GetSegmentRequestRequestTypeDef = TypedDict(
    "GetSegmentRequestRequestTypeDef",
    {
        "segment": str,
    },
)

LaunchExecutionTypeDef = TypedDict(
    "LaunchExecutionTypeDef",
    {
        "endedTime": datetime,
        "startedTime": datetime,
    },
    total=False,
)

_RequiredLaunchGroupTypeDef = TypedDict(
    "_RequiredLaunchGroupTypeDef",
    {
        "featureVariations": Dict[str, str],
        "name": str,
    },
)
_OptionalLaunchGroupTypeDef = TypedDict(
    "_OptionalLaunchGroupTypeDef",
    {
        "description": str,
    },
    total=False,
)

class LaunchGroupTypeDef(_RequiredLaunchGroupTypeDef, _OptionalLaunchGroupTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredListExperimentsRequestRequestTypeDef = TypedDict(
    "_RequiredListExperimentsRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalListExperimentsRequestRequestTypeDef = TypedDict(
    "_OptionalListExperimentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": ExperimentStatusType,
    },
    total=False,
)

class ListExperimentsRequestRequestTypeDef(
    _RequiredListExperimentsRequestRequestTypeDef, _OptionalListExperimentsRequestRequestTypeDef
):
    pass

_RequiredListFeaturesRequestRequestTypeDef = TypedDict(
    "_RequiredListFeaturesRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalListFeaturesRequestRequestTypeDef = TypedDict(
    "_OptionalListFeaturesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFeaturesRequestRequestTypeDef(
    _RequiredListFeaturesRequestRequestTypeDef, _OptionalListFeaturesRequestRequestTypeDef
):
    pass

_RequiredListLaunchesRequestRequestTypeDef = TypedDict(
    "_RequiredListLaunchesRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalListLaunchesRequestRequestTypeDef = TypedDict(
    "_OptionalListLaunchesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": LaunchStatusType,
    },
    total=False,
)

class ListLaunchesRequestRequestTypeDef(
    _RequiredListLaunchesRequestRequestTypeDef, _OptionalListLaunchesRequestRequestTypeDef
):
    pass

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "activeExperimentCount": int,
        "activeLaunchCount": int,
        "description": str,
        "experimentCount": int,
        "featureCount": int,
        "launchCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

_RequiredListSegmentReferencesRequestRequestTypeDef = TypedDict(
    "_RequiredListSegmentReferencesRequestRequestTypeDef",
    {
        "segment": str,
        "type": SegmentReferenceResourceTypeType,
    },
)
_OptionalListSegmentReferencesRequestRequestTypeDef = TypedDict(
    "_OptionalListSegmentReferencesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSegmentReferencesRequestRequestTypeDef(
    _RequiredListSegmentReferencesRequestRequestTypeDef,
    _OptionalListSegmentReferencesRequestRequestTypeDef,
):
    pass

_RequiredRefResourceTypeDef = TypedDict(
    "_RequiredRefResourceTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalRefResourceTypeDef = TypedDict(
    "_OptionalRefResourceTypeDef",
    {
        "arn": str,
        "endTime": str,
        "lastUpdatedOn": str,
        "startTime": str,
        "status": str,
    },
    total=False,
)

class RefResourceTypeDef(_RequiredRefResourceTypeDef, _OptionalRefResourceTypeDef):
    pass

ListSegmentsRequestRequestTypeDef = TypedDict(
    "ListSegmentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

_RequiredMetricDefinitionConfigTypeDef = TypedDict(
    "_RequiredMetricDefinitionConfigTypeDef",
    {
        "entityIdKey": str,
        "name": str,
        "valueKey": str,
    },
)
_OptionalMetricDefinitionConfigTypeDef = TypedDict(
    "_OptionalMetricDefinitionConfigTypeDef",
    {
        "eventPattern": str,
        "unitLabel": str,
    },
    total=False,
)

class MetricDefinitionConfigTypeDef(
    _RequiredMetricDefinitionConfigTypeDef, _OptionalMetricDefinitionConfigTypeDef
):
    pass

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "entityIdKey": str,
        "eventPattern": str,
        "name": str,
        "unitLabel": str,
        "valueKey": str,
    },
    total=False,
)

ProjectAppConfigResourceTypeDef = TypedDict(
    "ProjectAppConfigResourceTypeDef",
    {
        "applicationId": str,
        "configurationProfileId": str,
        "environmentId": str,
    },
)

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

PutProjectEventsResultEntryTypeDef = TypedDict(
    "PutProjectEventsResultEntryTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "eventId": str,
    },
    total=False,
)

SegmentOverrideTypeDef = TypedDict(
    "SegmentOverrideTypeDef",
    {
        "evaluationOrder": int,
        "segment": str,
        "weights": Mapping[str, int],
    },
)

SegmentOverrideOutputTypeDef = TypedDict(
    "SegmentOverrideOutputTypeDef",
    {
        "evaluationOrder": int,
        "segment": str,
        "weights": Dict[str, int],
    },
)

StartLaunchRequestRequestTypeDef = TypedDict(
    "StartLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

_RequiredStopExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredStopExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)
_OptionalStopExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalStopExperimentRequestRequestTypeDef",
    {
        "desiredState": ExperimentStopDesiredStateType,
        "reason": str,
    },
    total=False,
)

class StopExperimentRequestRequestTypeDef(
    _RequiredStopExperimentRequestRequestTypeDef, _OptionalStopExperimentRequestRequestTypeDef
):
    pass

_RequiredStopLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredStopLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
_OptionalStopLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalStopLaunchRequestRequestTypeDef",
    {
        "desiredState": LaunchStopDesiredStateType,
        "reason": str,
    },
    total=False,
)

class StopLaunchRequestRequestTypeDef(
    _RequiredStopLaunchRequestRequestTypeDef, _OptionalStopLaunchRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TestSegmentPatternRequestRequestTypeDef = TypedDict(
    "TestSegmentPatternRequestRequestTypeDef",
    {
        "pattern": str,
        "payload": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

BatchEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "BatchEvaluateFeatureRequestRequestTypeDef",
    {
        "project": str,
        "requests": Sequence[EvaluationRequestTypeDef],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "startedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopLaunchResponseTypeDef = TypedDict(
    "StopLaunchResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TestSegmentPatternResponseTypeDef = TypedDict(
    "TestSegmentPatternResponseTypeDef",
    {
        "match": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "appConfigResource": ProjectAppConfigResourceConfigTypeDef,
        "description": str,
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

CreateSegmentResponseTypeDef = TypedDict(
    "CreateSegmentResponseTypeDef",
    {
        "segment": SegmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSegmentResponseTypeDef = TypedDict(
    "GetSegmentResponseTypeDef",
    {
        "segment": SegmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSegmentsResponseTypeDef = TypedDict(
    "ListSegmentsResponseTypeDef",
    {
        "nextToken": str,
        "segments": List[SegmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EvaluateFeatureResponseTypeDef = TypedDict(
    "EvaluateFeatureResponseTypeDef",
    {
        "details": str,
        "reason": str,
        "value": VariableValueTypeDef,
        "variation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredEvaluationResultTypeDef = TypedDict(
    "_RequiredEvaluationResultTypeDef",
    {
        "entityId": str,
        "feature": str,
    },
)
_OptionalEvaluationResultTypeDef = TypedDict(
    "_OptionalEvaluationResultTypeDef",
    {
        "details": str,
        "project": str,
        "reason": str,
        "value": VariableValueTypeDef,
        "variation": str,
    },
    total=False,
)

class EvaluationResultTypeDef(_RequiredEvaluationResultTypeDef, _OptionalEvaluationResultTypeDef):
    pass

VariationConfigTypeDef = TypedDict(
    "VariationConfigTypeDef",
    {
        "name": str,
        "value": VariableValueTypeDef,
    },
)

VariationTypeDef = TypedDict(
    "VariationTypeDef",
    {
        "name": str,
        "value": VariableValueTypeDef,
    },
    total=False,
)

_RequiredFeatureSummaryTypeDef = TypedDict(
    "_RequiredFeatureSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
    },
)
_OptionalFeatureSummaryTypeDef = TypedDict(
    "_OptionalFeatureSummaryTypeDef",
    {
        "defaultVariation": str,
        "evaluationRules": List[EvaluationRuleTypeDef],
        "project": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class FeatureSummaryTypeDef(_RequiredFeatureSummaryTypeDef, _OptionalFeatureSummaryTypeDef):
    pass

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "data": str,
        "timestamp": TimestampTypeDef,
        "type": EventTypeType,
    },
)

_RequiredGetExperimentResultsRequestRequestTypeDef = TypedDict(
    "_RequiredGetExperimentResultsRequestRequestTypeDef",
    {
        "experiment": str,
        "metricNames": Sequence[str],
        "project": str,
        "treatmentNames": Sequence[str],
    },
)
_OptionalGetExperimentResultsRequestRequestTypeDef = TypedDict(
    "_OptionalGetExperimentResultsRequestRequestTypeDef",
    {
        "baseStat": Literal["Mean"],
        "endTime": TimestampTypeDef,
        "period": int,
        "reportNames": Sequence[Literal["BayesianInference"]],
        "resultStats": Sequence[ExperimentResultRequestTypeType],
        "startTime": TimestampTypeDef,
    },
    total=False,
)

class GetExperimentResultsRequestRequestTypeDef(
    _RequiredGetExperimentResultsRequestRequestTypeDef,
    _OptionalGetExperimentResultsRequestRequestTypeDef,
):
    pass

StartExperimentRequestRequestTypeDef = TypedDict(
    "StartExperimentRequestRequestTypeDef",
    {
        "analysisCompleteTime": TimestampTypeDef,
        "experiment": str,
        "project": str,
    },
)

GetExperimentResultsResponseTypeDef = TypedDict(
    "GetExperimentResultsResponseTypeDef",
    {
        "details": str,
        "reports": List[ExperimentReportTypeDef],
        "resultsData": List[ExperimentResultsDataTypeDef],
        "timestamps": List[datetime],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListExperimentsRequestListExperimentsPaginateTypeDef = TypedDict(
    "_RequiredListExperimentsRequestListExperimentsPaginateTypeDef",
    {
        "project": str,
    },
)
_OptionalListExperimentsRequestListExperimentsPaginateTypeDef = TypedDict(
    "_OptionalListExperimentsRequestListExperimentsPaginateTypeDef",
    {
        "status": ExperimentStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListExperimentsRequestListExperimentsPaginateTypeDef(
    _RequiredListExperimentsRequestListExperimentsPaginateTypeDef,
    _OptionalListExperimentsRequestListExperimentsPaginateTypeDef,
):
    pass

_RequiredListFeaturesRequestListFeaturesPaginateTypeDef = TypedDict(
    "_RequiredListFeaturesRequestListFeaturesPaginateTypeDef",
    {
        "project": str,
    },
)
_OptionalListFeaturesRequestListFeaturesPaginateTypeDef = TypedDict(
    "_OptionalListFeaturesRequestListFeaturesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListFeaturesRequestListFeaturesPaginateTypeDef(
    _RequiredListFeaturesRequestListFeaturesPaginateTypeDef,
    _OptionalListFeaturesRequestListFeaturesPaginateTypeDef,
):
    pass

_RequiredListLaunchesRequestListLaunchesPaginateTypeDef = TypedDict(
    "_RequiredListLaunchesRequestListLaunchesPaginateTypeDef",
    {
        "project": str,
    },
)
_OptionalListLaunchesRequestListLaunchesPaginateTypeDef = TypedDict(
    "_OptionalListLaunchesRequestListLaunchesPaginateTypeDef",
    {
        "status": LaunchStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListLaunchesRequestListLaunchesPaginateTypeDef(
    _RequiredListLaunchesRequestListLaunchesPaginateTypeDef,
    _OptionalListLaunchesRequestListLaunchesPaginateTypeDef,
):
    pass

ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef = TypedDict(
    "_RequiredListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef",
    {
        "segment": str,
        "type": SegmentReferenceResourceTypeType,
    },
)
_OptionalListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef = TypedDict(
    "_OptionalListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef(
    _RequiredListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef,
    _OptionalListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef,
):
    pass

ListSegmentsRequestListSegmentsPaginateTypeDef = TypedDict(
    "ListSegmentsRequestListSegmentsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "nextToken": str,
        "projects": List[ProjectSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSegmentReferencesResponseTypeDef = TypedDict(
    "ListSegmentReferencesResponseTypeDef",
    {
        "nextToken": str,
        "referencedBy": List[RefResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredMetricGoalConfigTypeDef = TypedDict(
    "_RequiredMetricGoalConfigTypeDef",
    {
        "metricDefinition": MetricDefinitionConfigTypeDef,
    },
)
_OptionalMetricGoalConfigTypeDef = TypedDict(
    "_OptionalMetricGoalConfigTypeDef",
    {
        "desiredChange": ChangeDirectionEnumType,
    },
    total=False,
)

class MetricGoalConfigTypeDef(_RequiredMetricGoalConfigTypeDef, _OptionalMetricGoalConfigTypeDef):
    pass

MetricMonitorConfigTypeDef = TypedDict(
    "MetricMonitorConfigTypeDef",
    {
        "metricDefinition": MetricDefinitionConfigTypeDef,
    },
)

_RequiredMetricGoalTypeDef = TypedDict(
    "_RequiredMetricGoalTypeDef",
    {
        "metricDefinition": MetricDefinitionTypeDef,
    },
)
_OptionalMetricGoalTypeDef = TypedDict(
    "_OptionalMetricGoalTypeDef",
    {
        "desiredChange": ChangeDirectionEnumType,
    },
    total=False,
)

class MetricGoalTypeDef(_RequiredMetricGoalTypeDef, _OptionalMetricGoalTypeDef):
    pass

MetricMonitorTypeDef = TypedDict(
    "MetricMonitorTypeDef",
    {
        "metricDefinition": MetricDefinitionTypeDef,
    },
)

ProjectDataDeliveryConfigTypeDef = TypedDict(
    "ProjectDataDeliveryConfigTypeDef",
    {
        "cloudWatchLogs": CloudWatchLogsDestinationConfigTypeDef,
        "s3Destination": S3DestinationConfigTypeDef,
    },
    total=False,
)

_RequiredUpdateProjectDataDeliveryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectDataDeliveryRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalUpdateProjectDataDeliveryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectDataDeliveryRequestRequestTypeDef",
    {
        "cloudWatchLogs": CloudWatchLogsDestinationConfigTypeDef,
        "s3Destination": S3DestinationConfigTypeDef,
    },
    total=False,
)

class UpdateProjectDataDeliveryRequestRequestTypeDef(
    _RequiredUpdateProjectDataDeliveryRequestRequestTypeDef,
    _OptionalUpdateProjectDataDeliveryRequestRequestTypeDef,
):
    pass

ProjectDataDeliveryTypeDef = TypedDict(
    "ProjectDataDeliveryTypeDef",
    {
        "cloudWatchLogs": CloudWatchLogsDestinationTypeDef,
        "s3Destination": S3DestinationTypeDef,
    },
    total=False,
)

PutProjectEventsResponseTypeDef = TypedDict(
    "PutProjectEventsResponseTypeDef",
    {
        "eventResults": List[PutProjectEventsResultEntryTypeDef],
        "failedEventCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredScheduledSplitConfigTypeDef = TypedDict(
    "_RequiredScheduledSplitConfigTypeDef",
    {
        "groupWeights": Mapping[str, int],
        "startTime": TimestampTypeDef,
    },
)
_OptionalScheduledSplitConfigTypeDef = TypedDict(
    "_OptionalScheduledSplitConfigTypeDef",
    {
        "segmentOverrides": Sequence[SegmentOverrideTypeDef],
    },
    total=False,
)

class ScheduledSplitConfigTypeDef(
    _RequiredScheduledSplitConfigTypeDef, _OptionalScheduledSplitConfigTypeDef
):
    pass

_RequiredScheduledSplitTypeDef = TypedDict(
    "_RequiredScheduledSplitTypeDef",
    {
        "startTime": datetime,
    },
)
_OptionalScheduledSplitTypeDef = TypedDict(
    "_OptionalScheduledSplitTypeDef",
    {
        "groupWeights": Dict[str, int],
        "segmentOverrides": List[SegmentOverrideOutputTypeDef],
    },
    total=False,
)

class ScheduledSplitTypeDef(_RequiredScheduledSplitTypeDef, _OptionalScheduledSplitTypeDef):
    pass

BatchEvaluateFeatureResponseTypeDef = TypedDict(
    "BatchEvaluateFeatureResponseTypeDef",
    {
        "results": List[EvaluationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateFeatureRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFeatureRequestRequestTypeDef",
    {
        "name": str,
        "project": str,
        "variations": Sequence[VariationConfigTypeDef],
    },
)
_OptionalCreateFeatureRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFeatureRequestRequestTypeDef",
    {
        "defaultVariation": str,
        "description": str,
        "entityOverrides": Mapping[str, str],
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateFeatureRequestRequestTypeDef(
    _RequiredCreateFeatureRequestRequestTypeDef, _OptionalCreateFeatureRequestRequestTypeDef
):
    pass

_RequiredUpdateFeatureRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)
_OptionalUpdateFeatureRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeatureRequestRequestTypeDef",
    {
        "addOrUpdateVariations": Sequence[VariationConfigTypeDef],
        "defaultVariation": str,
        "description": str,
        "entityOverrides": Mapping[str, str],
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "removeVariations": Sequence[str],
    },
    total=False,
)

class UpdateFeatureRequestRequestTypeDef(
    _RequiredUpdateFeatureRequestRequestTypeDef, _OptionalUpdateFeatureRequestRequestTypeDef
):
    pass

_RequiredFeatureTypeDef = TypedDict(
    "_RequiredFeatureTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
        "valueType": VariationValueTypeType,
        "variations": List[VariationTypeDef],
    },
)
_OptionalFeatureTypeDef = TypedDict(
    "_OptionalFeatureTypeDef",
    {
        "defaultVariation": str,
        "description": str,
        "entityOverrides": Dict[str, str],
        "evaluationRules": List[EvaluationRuleTypeDef],
        "project": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class FeatureTypeDef(_RequiredFeatureTypeDef, _OptionalFeatureTypeDef):
    pass

ListFeaturesResponseTypeDef = TypedDict(
    "ListFeaturesResponseTypeDef",
    {
        "features": List[FeatureSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutProjectEventsRequestRequestTypeDef = TypedDict(
    "PutProjectEventsRequestRequestTypeDef",
    {
        "events": Sequence[EventTypeDef],
        "project": str,
    },
)

_RequiredCreateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentRequestRequestTypeDef",
    {
        "metricGoals": Sequence[MetricGoalConfigTypeDef],
        "name": str,
        "project": str,
        "treatments": Sequence[TreatmentConfigTypeDef],
    },
)
_OptionalCreateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentRequestRequestTypeDef",
    {
        "description": str,
        "onlineAbConfig": OnlineAbConfigTypeDef,
        "randomizationSalt": str,
        "samplingRate": int,
        "segment": str,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateExperimentRequestRequestTypeDef(
    _RequiredCreateExperimentRequestRequestTypeDef, _OptionalCreateExperimentRequestRequestTypeDef
):
    pass

_RequiredUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)
_OptionalUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentRequestRequestTypeDef",
    {
        "description": str,
        "metricGoals": Sequence[MetricGoalConfigTypeDef],
        "onlineAbConfig": OnlineAbConfigTypeDef,
        "randomizationSalt": str,
        "removeSegment": bool,
        "samplingRate": int,
        "segment": str,
        "treatments": Sequence[TreatmentConfigTypeDef],
    },
    total=False,
)

class UpdateExperimentRequestRequestTypeDef(
    _RequiredUpdateExperimentRequestRequestTypeDef, _OptionalUpdateExperimentRequestRequestTypeDef
):
    pass

_RequiredExperimentTypeDef = TypedDict(
    "_RequiredExperimentTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ExperimentStatusType,
        "type": Literal["aws.evidently.onlineab"],
    },
)
_OptionalExperimentTypeDef = TypedDict(
    "_OptionalExperimentTypeDef",
    {
        "description": str,
        "execution": ExperimentExecutionTypeDef,
        "metricGoals": List[MetricGoalTypeDef],
        "onlineAbDefinition": OnlineAbDefinitionTypeDef,
        "project": str,
        "randomizationSalt": str,
        "samplingRate": int,
        "schedule": ExperimentScheduleTypeDef,
        "segment": str,
        "statusReason": str,
        "tags": Dict[str, str],
        "treatments": List[TreatmentTypeDef],
    },
    total=False,
)

class ExperimentTypeDef(_RequiredExperimentTypeDef, _OptionalExperimentTypeDef):
    pass

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "appConfigResource": ProjectAppConfigResourceConfigTypeDef,
        "dataDelivery": ProjectDataDeliveryConfigTypeDef,
        "description": str,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

_RequiredProjectTypeDef = TypedDict(
    "_RequiredProjectTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
    },
)
_OptionalProjectTypeDef = TypedDict(
    "_OptionalProjectTypeDef",
    {
        "activeExperimentCount": int,
        "activeLaunchCount": int,
        "appConfigResource": ProjectAppConfigResourceTypeDef,
        "dataDelivery": ProjectDataDeliveryTypeDef,
        "description": str,
        "experimentCount": int,
        "featureCount": int,
        "launchCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProjectTypeDef(_RequiredProjectTypeDef, _OptionalProjectTypeDef):
    pass

ScheduledSplitsLaunchConfigTypeDef = TypedDict(
    "ScheduledSplitsLaunchConfigTypeDef",
    {
        "steps": Sequence[ScheduledSplitConfigTypeDef],
    },
)

ScheduledSplitsLaunchDefinitionTypeDef = TypedDict(
    "ScheduledSplitsLaunchDefinitionTypeDef",
    {
        "steps": List[ScheduledSplitTypeDef],
    },
    total=False,
)

CreateFeatureResponseTypeDef = TypedDict(
    "CreateFeatureResponseTypeDef",
    {
        "feature": FeatureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFeatureResponseTypeDef = TypedDict(
    "GetFeatureResponseTypeDef",
    {
        "feature": FeatureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFeatureResponseTypeDef = TypedDict(
    "UpdateFeatureResponseTypeDef",
    {
        "feature": FeatureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List[ExperimentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetProjectResponseTypeDef = TypedDict(
    "GetProjectResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateProjectDataDeliveryResponseTypeDef = TypedDict(
    "UpdateProjectDataDeliveryResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchRequestRequestTypeDef",
    {
        "groups": Sequence[LaunchGroupConfigTypeDef],
        "name": str,
        "project": str,
    },
)
_OptionalCreateLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchRequestRequestTypeDef",
    {
        "description": str,
        "metricMonitors": Sequence[MetricMonitorConfigTypeDef],
        "randomizationSalt": str,
        "scheduledSplitsConfig": ScheduledSplitsLaunchConfigTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateLaunchRequestRequestTypeDef(
    _RequiredCreateLaunchRequestRequestTypeDef, _OptionalCreateLaunchRequestRequestTypeDef
):
    pass

_RequiredUpdateLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
_OptionalUpdateLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchRequestRequestTypeDef",
    {
        "description": str,
        "groups": Sequence[LaunchGroupConfigTypeDef],
        "metricMonitors": Sequence[MetricMonitorConfigTypeDef],
        "randomizationSalt": str,
        "scheduledSplitsConfig": ScheduledSplitsLaunchConfigTypeDef,
    },
    total=False,
)

class UpdateLaunchRequestRequestTypeDef(
    _RequiredUpdateLaunchRequestRequestTypeDef, _OptionalUpdateLaunchRequestRequestTypeDef
):
    pass

_RequiredLaunchTypeDef = TypedDict(
    "_RequiredLaunchTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": LaunchStatusType,
        "type": Literal["aws.evidently.splits"],
    },
)
_OptionalLaunchTypeDef = TypedDict(
    "_OptionalLaunchTypeDef",
    {
        "description": str,
        "execution": LaunchExecutionTypeDef,
        "groups": List[LaunchGroupTypeDef],
        "metricMonitors": List[MetricMonitorTypeDef],
        "project": str,
        "randomizationSalt": str,
        "scheduledSplitsDefinition": ScheduledSplitsLaunchDefinitionTypeDef,
        "statusReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class LaunchTypeDef(_RequiredLaunchTypeDef, _OptionalLaunchTypeDef):
    pass

CreateLaunchResponseTypeDef = TypedDict(
    "CreateLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLaunchResponseTypeDef = TypedDict(
    "GetLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLaunchesResponseTypeDef = TypedDict(
    "ListLaunchesResponseTypeDef",
    {
        "launches": List[LaunchTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartLaunchResponseTypeDef = TypedDict(
    "StartLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateLaunchResponseTypeDef = TypedDict(
    "UpdateLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
