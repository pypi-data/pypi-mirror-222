"""
Type annotations for application-insights service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/type_defs/)

Usage::

    ```python
    from mypy_boto3_application_insights.type_defs import WorkloadConfigurationTypeDef

    data: WorkloadConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    CloudWatchEventSourceType,
    ConfigurationEventResourceTypeType,
    ConfigurationEventStatusType,
    DiscoveryTypeType,
    FeedbackValueType,
    LogFilterType,
    OsTypeType,
    RecommendationTypeType,
    ResolutionMethodType,
    SeverityLevelType,
    StatusType,
    TierType,
    VisibilityType,
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
    "WorkloadConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "TagTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateLogPatternRequestRequestTypeDef",
    "LogPatternTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteLogPatternRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    "DescribeComponentConfigurationRequestRequestTypeDef",
    "DescribeComponentRequestRequestTypeDef",
    "DescribeLogPatternRequestRequestTypeDef",
    "DescribeObservationRequestRequestTypeDef",
    "ObservationTypeDef",
    "DescribeProblemObservationsRequestRequestTypeDef",
    "DescribeProblemRequestRequestTypeDef",
    "ProblemTypeDef",
    "DescribeWorkloadRequestRequestTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListConfigurationHistoryRequestRequestTypeDef",
    "ListLogPatternSetsRequestRequestTypeDef",
    "ListLogPatternsRequestRequestTypeDef",
    "ListProblemsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWorkloadsRequestRequestTypeDef",
    "WorkloadTypeDef",
    "RemoveWorkloadRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateComponentConfigurationRequestRequestTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateLogPatternRequestRequestTypeDef",
    "UpdateProblemRequestRequestTypeDef",
    "AddWorkloadRequestRequestTypeDef",
    "UpdateWorkloadRequestRequestTypeDef",
    "AddWorkloadResponseTypeDef",
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    "DescribeComponentConfigurationResponseTypeDef",
    "DescribeWorkloadResponseTypeDef",
    "ListLogPatternSetsResponseTypeDef",
    "UpdateWorkloadResponseTypeDef",
    "DescribeComponentResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "ListConfigurationHistoryResponseTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateLogPatternResponseTypeDef",
    "DescribeLogPatternResponseTypeDef",
    "ListLogPatternsResponseTypeDef",
    "UpdateLogPatternResponseTypeDef",
    "DescribeObservationResponseTypeDef",
    "RelatedObservationsTypeDef",
    "DescribeProblemResponseTypeDef",
    "ListProblemsResponseTypeDef",
    "ListWorkloadsResponseTypeDef",
    "DescribeProblemObservationsResponseTypeDef",
)

WorkloadConfigurationTypeDef = TypedDict(
    "WorkloadConfigurationTypeDef",
    {
        "WorkloadName": str,
        "Tier": TierType,
        "Configuration": str,
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

ApplicationComponentTypeDef = TypedDict(
    "ApplicationComponentTypeDef",
    {
        "ComponentName": str,
        "ComponentRemarks": str,
        "ResourceType": str,
        "OsType": OsTypeType,
        "Tier": TierType,
        "Monitor": bool,
        "DetectedWorkload": Dict[TierType, Dict[str, str]],
    },
    total=False,
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "AccountId": str,
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "Remarks": str,
        "AutoConfigEnabled": bool,
        "DiscoveryType": DiscoveryTypeType,
    },
    total=False,
)

ConfigurationEventTypeDef = TypedDict(
    "ConfigurationEventTypeDef",
    {
        "ResourceGroupName": str,
        "AccountId": str,
        "MonitoredResourceARN": str,
        "EventStatus": ConfigurationEventStatusType,
        "EventResourceType": ConfigurationEventResourceTypeType,
        "EventTime": datetime,
        "EventDetail": str,
        "EventResourceName": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "ResourceList": Sequence[str],
    },
)

CreateLogPatternRequestRequestTypeDef = TypedDict(
    "CreateLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
)

LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
    total=False,
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DeleteLogPatternRequestRequestTypeDef = TypedDict(
    "DeleteLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

_RequiredDescribeApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalDescribeApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeApplicationRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeApplicationRequestRequestTypeDef(
    _RequiredDescribeApplicationRequestRequestTypeDef,
    _OptionalDescribeApplicationRequestRequestTypeDef,
):
    pass

_RequiredDescribeComponentConfigurationRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "Tier": TierType,
    },
)
_OptionalDescribeComponentConfigurationRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    {
        "RecommendationType": RecommendationTypeType,
    },
    total=False,
)

class DescribeComponentConfigurationRecommendationRequestRequestTypeDef(
    _RequiredDescribeComponentConfigurationRecommendationRequestRequestTypeDef,
    _OptionalDescribeComponentConfigurationRecommendationRequestRequestTypeDef,
):
    pass

_RequiredDescribeComponentConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeComponentConfigurationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalDescribeComponentConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeComponentConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeComponentConfigurationRequestRequestTypeDef(
    _RequiredDescribeComponentConfigurationRequestRequestTypeDef,
    _OptionalDescribeComponentConfigurationRequestRequestTypeDef,
):
    pass

_RequiredDescribeComponentRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalDescribeComponentRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeComponentRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeComponentRequestRequestTypeDef(
    _RequiredDescribeComponentRequestRequestTypeDef, _OptionalDescribeComponentRequestRequestTypeDef
):
    pass

_RequiredDescribeLogPatternRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)
_OptionalDescribeLogPatternRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeLogPatternRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeLogPatternRequestRequestTypeDef(
    _RequiredDescribeLogPatternRequestRequestTypeDef,
    _OptionalDescribeLogPatternRequestRequestTypeDef,
):
    pass

_RequiredDescribeObservationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeObservationRequestRequestTypeDef",
    {
        "ObservationId": str,
    },
)
_OptionalDescribeObservationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeObservationRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeObservationRequestRequestTypeDef(
    _RequiredDescribeObservationRequestRequestTypeDef,
    _OptionalDescribeObservationRequestRequestTypeDef,
):
    pass

ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": LogFilterType,
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
        "CloudWatchEventId": str,
        "CloudWatchEventSource": CloudWatchEventSourceType,
        "CloudWatchEventDetailType": str,
        "HealthEventArn": str,
        "HealthService": str,
        "HealthEventTypeCode": str,
        "HealthEventTypeCategory": str,
        "HealthEventDescription": str,
        "CodeDeployDeploymentId": str,
        "CodeDeployDeploymentGroup": str,
        "CodeDeployState": str,
        "CodeDeployApplication": str,
        "CodeDeployInstanceGroupId": str,
        "Ec2State": str,
        "RdsEventCategories": str,
        "RdsEventMessage": str,
        "S3EventName": str,
        "StatesExecutionArn": str,
        "StatesArn": str,
        "StatesStatus": str,
        "StatesInput": str,
        "EbsEvent": str,
        "EbsResult": str,
        "EbsCause": str,
        "EbsRequestId": str,
        "XRayFaultPercent": int,
        "XRayThrottlePercent": int,
        "XRayErrorPercent": int,
        "XRayRequestCount": int,
        "XRayRequestAverageLatency": int,
        "XRayNodeName": str,
        "XRayNodeType": str,
    },
    total=False,
)

_RequiredDescribeProblemObservationsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeProblemObservationsRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)
_OptionalDescribeProblemObservationsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeProblemObservationsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeProblemObservationsRequestRequestTypeDef(
    _RequiredDescribeProblemObservationsRequestRequestTypeDef,
    _OptionalDescribeProblemObservationsRequestRequestTypeDef,
):
    pass

_RequiredDescribeProblemRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeProblemRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)
_OptionalDescribeProblemRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeProblemRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeProblemRequestRequestTypeDef(
    _RequiredDescribeProblemRequestRequestTypeDef, _OptionalDescribeProblemRequestRequestTypeDef
):
    pass

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": StatusType,
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": SeverityLevelType,
        "AccountId": str,
        "ResourceGroupName": str,
        "Feedback": Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType],
        "RecurringCount": int,
        "LastRecurrenceTime": datetime,
        "Visibility": VisibilityType,
        "ResolutionMethod": ResolutionMethodType,
    },
    total=False,
)

_RequiredDescribeWorkloadRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeWorkloadRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "WorkloadId": str,
    },
)
_OptionalDescribeWorkloadRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeWorkloadRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DescribeWorkloadRequestRequestTypeDef(
    _RequiredDescribeWorkloadRequestRequestTypeDef, _OptionalDescribeWorkloadRequestRequestTypeDef
):
    pass

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "AccountId": str,
    },
    total=False,
)

_RequiredListComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "AccountId": str,
    },
    total=False,
)

class ListComponentsRequestRequestTypeDef(
    _RequiredListComponentsRequestRequestTypeDef, _OptionalListComponentsRequestRequestTypeDef
):
    pass

ListConfigurationHistoryRequestRequestTypeDef = TypedDict(
    "ListConfigurationHistoryRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventStatus": ConfigurationEventStatusType,
        "MaxResults": int,
        "NextToken": str,
        "AccountId": str,
    },
    total=False,
)

_RequiredListLogPatternSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListLogPatternSetsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListLogPatternSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListLogPatternSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "AccountId": str,
    },
    total=False,
)

class ListLogPatternSetsRequestRequestTypeDef(
    _RequiredListLogPatternSetsRequestRequestTypeDef,
    _OptionalListLogPatternSetsRequestRequestTypeDef,
):
    pass

_RequiredListLogPatternsRequestRequestTypeDef = TypedDict(
    "_RequiredListLogPatternsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListLogPatternsRequestRequestTypeDef = TypedDict(
    "_OptionalListLogPatternsRequestRequestTypeDef",
    {
        "PatternSetName": str,
        "MaxResults": int,
        "NextToken": str,
        "AccountId": str,
    },
    total=False,
)

class ListLogPatternsRequestRequestTypeDef(
    _RequiredListLogPatternsRequestRequestTypeDef, _OptionalListLogPatternsRequestRequestTypeDef
):
    pass

ListProblemsRequestRequestTypeDef = TypedDict(
    "ListProblemsRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "ComponentName": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

_RequiredListWorkloadsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkloadsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalListWorkloadsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkloadsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "AccountId": str,
    },
    total=False,
)

class ListWorkloadsRequestRequestTypeDef(
    _RequiredListWorkloadsRequestRequestTypeDef, _OptionalListWorkloadsRequestRequestTypeDef
):
    pass

WorkloadTypeDef = TypedDict(
    "WorkloadTypeDef",
    {
        "WorkloadId": str,
        "ComponentName": str,
        "WorkloadName": str,
        "Tier": TierType,
        "WorkloadRemarks": str,
    },
    total=False,
)

RemoveWorkloadRequestRequestTypeDef = TypedDict(
    "RemoveWorkloadRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "WorkloadId": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "OpsItemSNSTopicArn": str,
        "RemoveSNSTopic": bool,
        "AutoConfigEnabled": bool,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

_RequiredUpdateComponentConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentConfigurationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalUpdateComponentConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentConfigurationRequestRequestTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
        "AutoConfigEnabled": bool,
    },
    total=False,
)

class UpdateComponentConfigurationRequestRequestTypeDef(
    _RequiredUpdateComponentConfigurationRequestRequestTypeDef,
    _OptionalUpdateComponentConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalUpdateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentRequestRequestTypeDef",
    {
        "NewComponentName": str,
        "ResourceList": Sequence[str],
    },
    total=False,
)

class UpdateComponentRequestRequestTypeDef(
    _RequiredUpdateComponentRequestRequestTypeDef, _OptionalUpdateComponentRequestRequestTypeDef
):
    pass

_RequiredUpdateLogPatternRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)
_OptionalUpdateLogPatternRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLogPatternRequestRequestTypeDef",
    {
        "Pattern": str,
        "Rank": int,
    },
    total=False,
)

class UpdateLogPatternRequestRequestTypeDef(
    _RequiredUpdateLogPatternRequestRequestTypeDef, _OptionalUpdateLogPatternRequestRequestTypeDef
):
    pass

_RequiredUpdateProblemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProblemRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)
_OptionalUpdateProblemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProblemRequestRequestTypeDef",
    {
        "UpdateStatus": Literal["RESOLVED"],
        "Visibility": VisibilityType,
    },
    total=False,
)

class UpdateProblemRequestRequestTypeDef(
    _RequiredUpdateProblemRequestRequestTypeDef, _OptionalUpdateProblemRequestRequestTypeDef
):
    pass

AddWorkloadRequestRequestTypeDef = TypedDict(
    "AddWorkloadRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "WorkloadConfiguration": WorkloadConfigurationTypeDef,
    },
)

_RequiredUpdateWorkloadRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkloadRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "WorkloadConfiguration": WorkloadConfigurationTypeDef,
    },
)
_OptionalUpdateWorkloadRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkloadRequestRequestTypeDef",
    {
        "WorkloadId": str,
    },
    total=False,
)

class UpdateWorkloadRequestRequestTypeDef(
    _RequiredUpdateWorkloadRequestRequestTypeDef, _OptionalUpdateWorkloadRequestRequestTypeDef
):
    pass

AddWorkloadResponseTypeDef = TypedDict(
    "AddWorkloadResponseTypeDef",
    {
        "WorkloadId": str,
        "WorkloadConfiguration": WorkloadConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    {
        "ComponentConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeComponentConfigurationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeWorkloadResponseTypeDef = TypedDict(
    "DescribeWorkloadResponseTypeDef",
    {
        "WorkloadId": str,
        "WorkloadRemarks": str,
        "WorkloadConfiguration": WorkloadConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLogPatternSetsResponseTypeDef = TypedDict(
    "ListLogPatternSetsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "AccountId": str,
        "LogPatternSets": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateWorkloadResponseTypeDef = TypedDict(
    "UpdateWorkloadResponseTypeDef",
    {
        "WorkloadId": str,
        "WorkloadConfiguration": WorkloadConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "ApplicationComponent": ApplicationComponentTypeDef,
        "ResourceList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "ApplicationComponentList": List[ApplicationComponentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationInfo": ApplicationInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationInfo": ApplicationInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationInfoList": List[ApplicationInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationInfo": ApplicationInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConfigurationHistoryResponseTypeDef = TypedDict(
    "ListConfigurationHistoryResponseTypeDef",
    {
        "EventList": List[ConfigurationEventTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "OpsItemSNSTopicArn": str,
        "Tags": Sequence[TagTypeDef],
        "AutoConfigEnabled": bool,
        "AutoCreate": bool,
        "GroupingType": Literal["ACCOUNT_BASED"],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateLogPatternResponseTypeDef = TypedDict(
    "CreateLogPatternResponseTypeDef",
    {
        "LogPattern": LogPatternTypeDef,
        "ResourceGroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLogPatternResponseTypeDef = TypedDict(
    "DescribeLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "AccountId": str,
        "LogPattern": LogPatternTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLogPatternsResponseTypeDef = TypedDict(
    "ListLogPatternsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "AccountId": str,
        "LogPatterns": List[LogPatternTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateLogPatternResponseTypeDef = TypedDict(
    "UpdateLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": LogPatternTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeObservationResponseTypeDef = TypedDict(
    "DescribeObservationResponseTypeDef",
    {
        "Observation": ObservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RelatedObservationsTypeDef = TypedDict(
    "RelatedObservationsTypeDef",
    {
        "ObservationList": List[ObservationTypeDef],
    },
    total=False,
)

DescribeProblemResponseTypeDef = TypedDict(
    "DescribeProblemResponseTypeDef",
    {
        "Problem": ProblemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListProblemsResponseTypeDef = TypedDict(
    "ListProblemsResponseTypeDef",
    {
        "ProblemList": List[ProblemTypeDef],
        "NextToken": str,
        "ResourceGroupName": str,
        "AccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListWorkloadsResponseTypeDef = TypedDict(
    "ListWorkloadsResponseTypeDef",
    {
        "WorkloadList": List[WorkloadTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeProblemObservationsResponseTypeDef = TypedDict(
    "DescribeProblemObservationsResponseTypeDef",
    {
        "RelatedObservations": RelatedObservationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
