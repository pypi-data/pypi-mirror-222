"""
Type annotations for stepfunctions service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs/)

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ExecutionStatusType,
    HistoryEventTypeType,
    LogLevelType,
    MapRunStatusType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingConfigurationListItemTypeDef",
    "TracingConfigurationTypeDef",
    "DeleteActivityInputRequestTypeDef",
    "DeleteStateMachineAliasInputRequestTypeDef",
    "DeleteStateMachineInputRequestTypeDef",
    "DeleteStateMachineVersionInputRequestTypeDef",
    "DescribeActivityInputRequestTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeMapRunInputRequestTypeDef",
    "MapRunExecutionCountsTypeDef",
    "MapRunItemCountsTypeDef",
    "DescribeStateMachineAliasInputRequestTypeDef",
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    "DescribeStateMachineInputRequestTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetExecutionHistoryInputRequestTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapRunFailedEventDetailsTypeDef",
    "MapRunStartedEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "TaskCredentialsTypeDef",
    "ListActivitiesInputRequestTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListMapRunsInputRequestTypeDef",
    "MapRunListItemTypeDef",
    "ListStateMachineAliasesInputRequestTypeDef",
    "StateMachineAliasListItemTypeDef",
    "ListStateMachineVersionsInputRequestTypeDef",
    "StateMachineVersionListItemTypeDef",
    "ListStateMachinesInputRequestTypeDef",
    "StateMachineListItemTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "PublishStateMachineVersionInputRequestTypeDef",
    "SendTaskFailureInputRequestTypeDef",
    "SendTaskHeartbeatInputRequestTypeDef",
    "SendTaskSuccessInputRequestTypeDef",
    "StartExecutionInputRequestTypeDef",
    "StartSyncExecutionInputRequestTypeDef",
    "StopExecutionInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateMapRunInputRequestTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "LogDestinationTypeDef",
    "CreateActivityInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineAliasOutputTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionOutputTypeDef",
    "GetActivityTaskOutputTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PublishStateMachineVersionOutputTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StopExecutionOutputTypeDef",
    "UpdateStateMachineAliasOutputTypeDef",
    "UpdateStateMachineOutputTypeDef",
    "CreateStateMachineAliasInputRequestTypeDef",
    "DescribeStateMachineAliasOutputTypeDef",
    "UpdateStateMachineAliasInputRequestTypeDef",
    "DescribeMapRunOutputTypeDef",
    "ListExecutionsOutputTypeDef",
    "GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef",
    "ListActivitiesInputListActivitiesPaginateTypeDef",
    "ListExecutionsInputListExecutionsPaginateTypeDef",
    "ListMapRunsInputListMapRunsPaginateTypeDef",
    "ListStateMachinesInputListStateMachinesPaginateTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "ListMapRunsOutputTypeDef",
    "ListStateMachineAliasesOutputTypeDef",
    "ListStateMachineVersionsOutputTypeDef",
    "ListStateMachinesOutputTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "HistoryEventTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "CreateStateMachineInputRequestTypeDef",
    "LoggingConfigurationUnionTypeDef",
    "UpdateStateMachineInputRequestTypeDef",
    "GetExecutionHistoryOutputTypeDef",
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
    },
)

ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

HistoryEventExecutionDataDetailsTypeDef = TypedDict(
    "HistoryEventExecutionDataDetailsTypeDef",
    {
        "truncated": bool,
    },
    total=False,
)

ActivityStartedEventDetailsTypeDef = TypedDict(
    "ActivityStartedEventDetailsTypeDef",
    {
        "workerName": str,
    },
    total=False,
)

ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

BillingDetailsTypeDef = TypedDict(
    "BillingDetailsTypeDef",
    {
        "billedMemoryUsedInMB": int,
        "billedDurationInMilliseconds": int,
    },
    total=False,
)

CloudWatchEventsExecutionDataDetailsTypeDef = TypedDict(
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    {
        "included": bool,
    },
    total=False,
)

CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef",
    {
        "logGroupArn": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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

RoutingConfigurationListItemTypeDef = TypedDict(
    "RoutingConfigurationListItemTypeDef",
    {
        "stateMachineVersionArn": str,
        "weight": int,
    },
)

TracingConfigurationTypeDef = TypedDict(
    "TracingConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

DeleteActivityInputRequestTypeDef = TypedDict(
    "DeleteActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DeleteStateMachineAliasInputRequestTypeDef = TypedDict(
    "DeleteStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)

DeleteStateMachineInputRequestTypeDef = TypedDict(
    "DeleteStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

DeleteStateMachineVersionInputRequestTypeDef = TypedDict(
    "DeleteStateMachineVersionInputRequestTypeDef",
    {
        "stateMachineVersionArn": str,
    },
)

DescribeActivityInputRequestTypeDef = TypedDict(
    "DescribeActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)

DescribeMapRunInputRequestTypeDef = TypedDict(
    "DescribeMapRunInputRequestTypeDef",
    {
        "mapRunArn": str,
    },
)

MapRunExecutionCountsTypeDef = TypedDict(
    "MapRunExecutionCountsTypeDef",
    {
        "pending": int,
        "running": int,
        "succeeded": int,
        "failed": int,
        "timedOut": int,
        "aborted": int,
        "total": int,
        "resultsWritten": int,
    },
)

MapRunItemCountsTypeDef = TypedDict(
    "MapRunItemCountsTypeDef",
    {
        "pending": int,
        "running": int,
        "succeeded": int,
        "failed": int,
        "timedOut": int,
        "aborted": int,
        "total": int,
        "resultsWritten": int,
    },
)

DescribeStateMachineAliasInputRequestTypeDef = TypedDict(
    "DescribeStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)

DescribeStateMachineForExecutionInputRequestTypeDef = TypedDict(
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)

DescribeStateMachineInputRequestTypeDef = TypedDict(
    "DescribeStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredExecutionListItemTypeDef = TypedDict(
    "_RequiredExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
    },
)
_OptionalExecutionListItemTypeDef = TypedDict(
    "_OptionalExecutionListItemTypeDef",
    {
        "stopDate": datetime,
        "mapRunArn": str,
        "itemCount": int,
        "stateMachineVersionArn": str,
        "stateMachineAliasArn": str,
    },
    total=False,
)


class ExecutionListItemTypeDef(
    _RequiredExecutionListItemTypeDef, _OptionalExecutionListItemTypeDef
):
    pass


ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredGetActivityTaskInputRequestTypeDef = TypedDict(
    "_RequiredGetActivityTaskInputRequestTypeDef",
    {
        "activityArn": str,
    },
)
_OptionalGetActivityTaskInputRequestTypeDef = TypedDict(
    "_OptionalGetActivityTaskInputRequestTypeDef",
    {
        "workerName": str,
    },
    total=False,
)


class GetActivityTaskInputRequestTypeDef(
    _RequiredGetActivityTaskInputRequestTypeDef, _OptionalGetActivityTaskInputRequestTypeDef
):
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

_RequiredGetExecutionHistoryInputRequestTypeDef = TypedDict(
    "_RequiredGetExecutionHistoryInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalGetExecutionHistoryInputRequestTypeDef = TypedDict(
    "_OptionalGetExecutionHistoryInputRequestTypeDef",
    {
        "maxResults": int,
        "reverseOrder": bool,
        "nextToken": str,
        "includeExecutionData": bool,
    },
    total=False,
)


class GetExecutionHistoryInputRequestTypeDef(
    _RequiredGetExecutionHistoryInputRequestTypeDef, _OptionalGetExecutionHistoryInputRequestTypeDef
):
    pass


LambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef",
    {
        "name": str,
        "index": int,
    },
    total=False,
)

MapRunFailedEventDetailsTypeDef = TypedDict(
    "MapRunFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

MapRunStartedEventDetailsTypeDef = TypedDict(
    "MapRunStartedEventDetailsTypeDef",
    {
        "mapRunArn": str,
    },
    total=False,
)

MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef",
    {
        "length": int,
    },
    total=False,
)

_RequiredTaskFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskFailedEventDetailsTypeDef(
    _RequiredTaskFailedEventDetailsTypeDef, _OptionalTaskFailedEventDetailsTypeDef
):
    pass


_RequiredTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskStartFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskStartFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskStartFailedEventDetailsTypeDef(
    _RequiredTaskStartFailedEventDetailsTypeDef, _OptionalTaskStartFailedEventDetailsTypeDef
):
    pass


TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)

_RequiredTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmitFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmitFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskSubmitFailedEventDetailsTypeDef(
    _RequiredTaskSubmitFailedEventDetailsTypeDef, _OptionalTaskSubmitFailedEventDetailsTypeDef
):
    pass


_RequiredTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_RequiredTaskTimedOutEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_OptionalTaskTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskTimedOutEventDetailsTypeDef(
    _RequiredTaskTimedOutEventDetailsTypeDef, _OptionalTaskTimedOutEventDetailsTypeDef
):
    pass


TaskCredentialsTypeDef = TypedDict(
    "TaskCredentialsTypeDef",
    {
        "roleArn": str,
    },
    total=False,
)

ListActivitiesInputRequestTypeDef = TypedDict(
    "ListActivitiesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExecutionsInputRequestTypeDef = TypedDict(
    "ListExecutionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "statusFilter": ExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
        "mapRunArn": str,
    },
    total=False,
)

_RequiredListMapRunsInputRequestTypeDef = TypedDict(
    "_RequiredListMapRunsInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalListMapRunsInputRequestTypeDef = TypedDict(
    "_OptionalListMapRunsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListMapRunsInputRequestTypeDef(
    _RequiredListMapRunsInputRequestTypeDef, _OptionalListMapRunsInputRequestTypeDef
):
    pass


_RequiredMapRunListItemTypeDef = TypedDict(
    "_RequiredMapRunListItemTypeDef",
    {
        "executionArn": str,
        "mapRunArn": str,
        "stateMachineArn": str,
        "startDate": datetime,
    },
)
_OptionalMapRunListItemTypeDef = TypedDict(
    "_OptionalMapRunListItemTypeDef",
    {
        "stopDate": datetime,
    },
    total=False,
)


class MapRunListItemTypeDef(_RequiredMapRunListItemTypeDef, _OptionalMapRunListItemTypeDef):
    pass


_RequiredListStateMachineAliasesInputRequestTypeDef = TypedDict(
    "_RequiredListStateMachineAliasesInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalListStateMachineAliasesInputRequestTypeDef = TypedDict(
    "_OptionalListStateMachineAliasesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListStateMachineAliasesInputRequestTypeDef(
    _RequiredListStateMachineAliasesInputRequestTypeDef,
    _OptionalListStateMachineAliasesInputRequestTypeDef,
):
    pass


StateMachineAliasListItemTypeDef = TypedDict(
    "StateMachineAliasListItemTypeDef",
    {
        "stateMachineAliasArn": str,
        "creationDate": datetime,
    },
)

_RequiredListStateMachineVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListStateMachineVersionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalListStateMachineVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListStateMachineVersionsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListStateMachineVersionsInputRequestTypeDef(
    _RequiredListStateMachineVersionsInputRequestTypeDef,
    _OptionalListStateMachineVersionsInputRequestTypeDef,
):
    pass


StateMachineVersionListItemTypeDef = TypedDict(
    "StateMachineVersionListItemTypeDef",
    {
        "stateMachineVersionArn": str,
        "creationDate": datetime,
    },
)

ListStateMachinesInputRequestTypeDef = TypedDict(
    "ListStateMachinesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

_RequiredPublishStateMachineVersionInputRequestTypeDef = TypedDict(
    "_RequiredPublishStateMachineVersionInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalPublishStateMachineVersionInputRequestTypeDef = TypedDict(
    "_OptionalPublishStateMachineVersionInputRequestTypeDef",
    {
        "revisionId": str,
        "description": str,
    },
    total=False,
)


class PublishStateMachineVersionInputRequestTypeDef(
    _RequiredPublishStateMachineVersionInputRequestTypeDef,
    _OptionalPublishStateMachineVersionInputRequestTypeDef,
):
    pass


_RequiredSendTaskFailureInputRequestTypeDef = TypedDict(
    "_RequiredSendTaskFailureInputRequestTypeDef",
    {
        "taskToken": str,
    },
)
_OptionalSendTaskFailureInputRequestTypeDef = TypedDict(
    "_OptionalSendTaskFailureInputRequestTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class SendTaskFailureInputRequestTypeDef(
    _RequiredSendTaskFailureInputRequestTypeDef, _OptionalSendTaskFailureInputRequestTypeDef
):
    pass


SendTaskHeartbeatInputRequestTypeDef = TypedDict(
    "SendTaskHeartbeatInputRequestTypeDef",
    {
        "taskToken": str,
    },
)

SendTaskSuccessInputRequestTypeDef = TypedDict(
    "SendTaskSuccessInputRequestTypeDef",
    {
        "taskToken": str,
        "output": str,
    },
)

_RequiredStartExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalStartExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartExecutionInputRequestTypeDef",
    {
        "name": str,
        "input": str,
        "traceHeader": str,
    },
    total=False,
)


class StartExecutionInputRequestTypeDef(
    _RequiredStartExecutionInputRequestTypeDef, _OptionalStartExecutionInputRequestTypeDef
):
    pass


_RequiredStartSyncExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartSyncExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalStartSyncExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartSyncExecutionInputRequestTypeDef",
    {
        "name": str,
        "input": str,
        "traceHeader": str,
    },
    total=False,
)


class StartSyncExecutionInputRequestTypeDef(
    _RequiredStartSyncExecutionInputRequestTypeDef, _OptionalStartSyncExecutionInputRequestTypeDef
):
    pass


_RequiredStopExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStopExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalStopExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStopExecutionInputRequestTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class StopExecutionInputRequestTypeDef(
    _RequiredStopExecutionInputRequestTypeDef, _OptionalStopExecutionInputRequestTypeDef
):
    pass


UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateMapRunInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMapRunInputRequestTypeDef",
    {
        "mapRunArn": str,
    },
)
_OptionalUpdateMapRunInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMapRunInputRequestTypeDef",
    {
        "maxConcurrency": int,
        "toleratedFailurePercentage": float,
        "toleratedFailureCount": int,
    },
    total=False,
)


class UpdateMapRunInputRequestTypeDef(
    _RequiredUpdateMapRunInputRequestTypeDef, _OptionalUpdateMapRunInputRequestTypeDef
):
    pass


_RequiredActivityScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredActivityScheduledEventDetailsTypeDef",
    {
        "resource": str,
    },
)
_OptionalActivityScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalActivityScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": HistoryEventExecutionDataDetailsTypeDef,
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
    },
    total=False,
)


class ActivityScheduledEventDetailsTypeDef(
    _RequiredActivityScheduledEventDetailsTypeDef, _OptionalActivityScheduledEventDetailsTypeDef
):
    pass


ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)

ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": HistoryEventExecutionDataDetailsTypeDef,
        "roleArn": str,
        "stateMachineAliasArn": str,
        "stateMachineVersionArn": str,
    },
    total=False,
)

ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)

LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)

_RequiredStateEnteredEventDetailsTypeDef = TypedDict(
    "_RequiredStateEnteredEventDetailsTypeDef",
    {
        "name": str,
    },
)
_OptionalStateEnteredEventDetailsTypeDef = TypedDict(
    "_OptionalStateEnteredEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)


class StateEnteredEventDetailsTypeDef(
    _RequiredStateEnteredEventDetailsTypeDef, _OptionalStateEnteredEventDetailsTypeDef
):
    pass


_RequiredStateExitedEventDetailsTypeDef = TypedDict(
    "_RequiredStateExitedEventDetailsTypeDef",
    {
        "name": str,
    },
)
_OptionalStateExitedEventDetailsTypeDef = TypedDict(
    "_OptionalStateExitedEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)


class StateExitedEventDetailsTypeDef(
    _RequiredStateExitedEventDetailsTypeDef, _OptionalStateExitedEventDetailsTypeDef
):
    pass


_RequiredTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmittedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmittedEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)


class TaskSubmittedEventDetailsTypeDef(
    _RequiredTaskSubmittedEventDetailsTypeDef, _OptionalTaskSubmittedEventDetailsTypeDef
):
    pass


_RequiredTaskSucceededEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSucceededEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSucceededEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": HistoryEventExecutionDataDetailsTypeDef,
    },
    total=False,
)


class TaskSucceededEventDetailsTypeDef(
    _RequiredTaskSucceededEventDetailsTypeDef, _OptionalTaskSucceededEventDetailsTypeDef
):
    pass


LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {
        "cloudWatchLogsLogGroup": CloudWatchLogsLogGroupTypeDef,
    },
    total=False,
)

_RequiredCreateActivityInputRequestTypeDef = TypedDict(
    "_RequiredCreateActivityInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateActivityInputRequestTypeDef = TypedDict(
    "_OptionalCreateActivityInputRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateActivityInputRequestTypeDef(
    _RequiredCreateActivityInputRequestTypeDef, _OptionalCreateActivityInputRequestTypeDef
):
    pass


TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

CreateActivityOutputTypeDef = TypedDict(
    "CreateActivityOutputTypeDef",
    {
        "activityArn": str,
        "creationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateStateMachineAliasOutputTypeDef = TypedDict(
    "CreateStateMachineAliasOutputTypeDef",
    {
        "stateMachineAliasArn": str,
        "creationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateStateMachineOutputTypeDef = TypedDict(
    "CreateStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "creationDate": datetime,
        "stateMachineVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeActivityOutputTypeDef = TypedDict(
    "DescribeActivityOutputTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "inputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "output": str,
        "outputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "traceHeader": str,
        "mapRunArn": str,
        "error": str,
        "cause": str,
        "stateMachineVersionArn": str,
        "stateMachineAliasArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {
        "taskToken": str,
        "input": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListActivitiesOutputTypeDef = TypedDict(
    "ListActivitiesOutputTypeDef",
    {
        "activities": List[ActivityListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PublishStateMachineVersionOutputTypeDef = TypedDict(
    "PublishStateMachineVersionOutputTypeDef",
    {
        "creationDate": datetime,
        "stateMachineVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartExecutionOutputTypeDef = TypedDict(
    "StartExecutionOutputTypeDef",
    {
        "executionArn": str,
        "startDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartSyncExecutionOutputTypeDef = TypedDict(
    "StartSyncExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": SyncExecutionStatusType,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "output": str,
        "outputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "traceHeader": str,
        "billingDetails": BillingDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopExecutionOutputTypeDef = TypedDict(
    "StopExecutionOutputTypeDef",
    {
        "stopDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateStateMachineAliasOutputTypeDef = TypedDict(
    "UpdateStateMachineAliasOutputTypeDef",
    {
        "updateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateStateMachineOutputTypeDef = TypedDict(
    "UpdateStateMachineOutputTypeDef",
    {
        "updateDate": datetime,
        "revisionId": str,
        "stateMachineVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_RequiredCreateStateMachineAliasInputRequestTypeDef",
    {
        "name": str,
        "routingConfiguration": Sequence[RoutingConfigurationListItemTypeDef],
    },
)
_OptionalCreateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_OptionalCreateStateMachineAliasInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class CreateStateMachineAliasInputRequestTypeDef(
    _RequiredCreateStateMachineAliasInputRequestTypeDef,
    _OptionalCreateStateMachineAliasInputRequestTypeDef,
):
    pass


DescribeStateMachineAliasOutputTypeDef = TypedDict(
    "DescribeStateMachineAliasOutputTypeDef",
    {
        "stateMachineAliasArn": str,
        "name": str,
        "description": str,
        "routingConfiguration": List[RoutingConfigurationListItemTypeDef],
        "creationDate": datetime,
        "updateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)
_OptionalUpdateStateMachineAliasInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStateMachineAliasInputRequestTypeDef",
    {
        "description": str,
        "routingConfiguration": Sequence[RoutingConfigurationListItemTypeDef],
    },
    total=False,
)


class UpdateStateMachineAliasInputRequestTypeDef(
    _RequiredUpdateStateMachineAliasInputRequestTypeDef,
    _OptionalUpdateStateMachineAliasInputRequestTypeDef,
):
    pass


DescribeMapRunOutputTypeDef = TypedDict(
    "DescribeMapRunOutputTypeDef",
    {
        "mapRunArn": str,
        "executionArn": str,
        "status": MapRunStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "maxConcurrency": int,
        "toleratedFailurePercentage": float,
        "toleratedFailureCount": int,
        "itemCounts": MapRunItemCountsTypeDef,
        "executionCounts": MapRunExecutionCountsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List[ExecutionListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef = TypedDict(
    "_RequiredGetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalGetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef = TypedDict(
    "_OptionalGetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef",
    {
        "reverseOrder": bool,
        "includeExecutionData": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef(
    _RequiredGetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef,
    _OptionalGetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef,
):
    pass


ListActivitiesInputListActivitiesPaginateTypeDef = TypedDict(
    "ListActivitiesInputListActivitiesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListExecutionsInputListExecutionsPaginateTypeDef = TypedDict(
    "ListExecutionsInputListExecutionsPaginateTypeDef",
    {
        "stateMachineArn": str,
        "statusFilter": ExecutionStatusType,
        "mapRunArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListMapRunsInputListMapRunsPaginateTypeDef = TypedDict(
    "_RequiredListMapRunsInputListMapRunsPaginateTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalListMapRunsInputListMapRunsPaginateTypeDef = TypedDict(
    "_OptionalListMapRunsInputListMapRunsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListMapRunsInputListMapRunsPaginateTypeDef(
    _RequiredListMapRunsInputListMapRunsPaginateTypeDef,
    _OptionalListMapRunsInputListMapRunsPaginateTypeDef,
):
    pass


ListStateMachinesInputListStateMachinesPaginateTypeDef = TypedDict(
    "ListStateMachinesInputListStateMachinesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "resource": str,
    },
)
_OptionalLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": HistoryEventExecutionDataDetailsTypeDef,
        "timeoutInSeconds": int,
        "taskCredentials": TaskCredentialsTypeDef,
    },
    total=False,
)


class LambdaFunctionScheduledEventDetailsTypeDef(
    _RequiredLambdaFunctionScheduledEventDetailsTypeDef,
    _OptionalLambdaFunctionScheduledEventDetailsTypeDef,
):
    pass


_RequiredTaskScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredTaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
    },
)
_OptionalTaskScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalTaskScheduledEventDetailsTypeDef",
    {
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
        "taskCredentials": TaskCredentialsTypeDef,
    },
    total=False,
)


class TaskScheduledEventDetailsTypeDef(
    _RequiredTaskScheduledEventDetailsTypeDef, _OptionalTaskScheduledEventDetailsTypeDef
):
    pass


ListMapRunsOutputTypeDef = TypedDict(
    "ListMapRunsOutputTypeDef",
    {
        "mapRuns": List[MapRunListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStateMachineAliasesOutputTypeDef = TypedDict(
    "ListStateMachineAliasesOutputTypeDef",
    {
        "stateMachineAliases": List[StateMachineAliasListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStateMachineVersionsOutputTypeDef = TypedDict(
    "ListStateMachineVersionsOutputTypeDef",
    {
        "stateMachineVersions": List[StateMachineVersionListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStateMachinesOutputTypeDef = TypedDict(
    "ListStateMachinesOutputTypeDef",
    {
        "stateMachines": List[StateMachineListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LoggingConfigurationOutputTypeDef = TypedDict(
    "LoggingConfigurationOutputTypeDef",
    {
        "level": LogLevelType,
        "includeExecutionData": bool,
        "destinations": List[LogDestinationTypeDef],
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "level": LogLevelType,
        "includeExecutionData": bool,
        "destinations": Sequence[LogDestinationTypeDef],
    },
    total=False,
)

_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": HistoryEventTypeType,
        "id": int,
    },
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "previousEventId": int,
        "activityFailedEventDetails": ActivityFailedEventDetailsTypeDef,
        "activityScheduleFailedEventDetails": ActivityScheduleFailedEventDetailsTypeDef,
        "activityScheduledEventDetails": ActivityScheduledEventDetailsTypeDef,
        "activityStartedEventDetails": ActivityStartedEventDetailsTypeDef,
        "activitySucceededEventDetails": ActivitySucceededEventDetailsTypeDef,
        "activityTimedOutEventDetails": ActivityTimedOutEventDetailsTypeDef,
        "taskFailedEventDetails": TaskFailedEventDetailsTypeDef,
        "taskScheduledEventDetails": TaskScheduledEventDetailsTypeDef,
        "taskStartFailedEventDetails": TaskStartFailedEventDetailsTypeDef,
        "taskStartedEventDetails": TaskStartedEventDetailsTypeDef,
        "taskSubmitFailedEventDetails": TaskSubmitFailedEventDetailsTypeDef,
        "taskSubmittedEventDetails": TaskSubmittedEventDetailsTypeDef,
        "taskSucceededEventDetails": TaskSucceededEventDetailsTypeDef,
        "taskTimedOutEventDetails": TaskTimedOutEventDetailsTypeDef,
        "executionFailedEventDetails": ExecutionFailedEventDetailsTypeDef,
        "executionStartedEventDetails": ExecutionStartedEventDetailsTypeDef,
        "executionSucceededEventDetails": ExecutionSucceededEventDetailsTypeDef,
        "executionAbortedEventDetails": ExecutionAbortedEventDetailsTypeDef,
        "executionTimedOutEventDetails": ExecutionTimedOutEventDetailsTypeDef,
        "mapStateStartedEventDetails": MapStateStartedEventDetailsTypeDef,
        "mapIterationStartedEventDetails": MapIterationEventDetailsTypeDef,
        "mapIterationSucceededEventDetails": MapIterationEventDetailsTypeDef,
        "mapIterationFailedEventDetails": MapIterationEventDetailsTypeDef,
        "mapIterationAbortedEventDetails": MapIterationEventDetailsTypeDef,
        "lambdaFunctionFailedEventDetails": LambdaFunctionFailedEventDetailsTypeDef,
        "lambdaFunctionScheduleFailedEventDetails": LambdaFunctionScheduleFailedEventDetailsTypeDef,
        "lambdaFunctionScheduledEventDetails": LambdaFunctionScheduledEventDetailsTypeDef,
        "lambdaFunctionStartFailedEventDetails": LambdaFunctionStartFailedEventDetailsTypeDef,
        "lambdaFunctionSucceededEventDetails": LambdaFunctionSucceededEventDetailsTypeDef,
        "lambdaFunctionTimedOutEventDetails": LambdaFunctionTimedOutEventDetailsTypeDef,
        "stateEnteredEventDetails": StateEnteredEventDetailsTypeDef,
        "stateExitedEventDetails": StateExitedEventDetailsTypeDef,
        "mapRunStartedEventDetails": MapRunStartedEventDetailsTypeDef,
        "mapRunFailedEventDetails": MapRunFailedEventDetailsTypeDef,
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


DescribeStateMachineForExecutionOutputTypeDef = TypedDict(
    "DescribeStateMachineForExecutionOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
        "loggingConfiguration": LoggingConfigurationOutputTypeDef,
        "tracingConfiguration": TracingConfigurationTypeDef,
        "mapRunArn": str,
        "label": str,
        "revisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStateMachineOutputTypeDef = TypedDict(
    "DescribeStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": StateMachineStatusType,
        "definition": str,
        "roleArn": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
        "loggingConfiguration": LoggingConfigurationOutputTypeDef,
        "tracingConfiguration": TracingConfigurationTypeDef,
        "label": str,
        "revisionId": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateStateMachineInputRequestTypeDef = TypedDict(
    "_RequiredCreateStateMachineInputRequestTypeDef",
    {
        "name": str,
        "definition": str,
        "roleArn": str,
    },
)
_OptionalCreateStateMachineInputRequestTypeDef = TypedDict(
    "_OptionalCreateStateMachineInputRequestTypeDef",
    {
        "type": StateMachineTypeType,
        "loggingConfiguration": LoggingConfigurationTypeDef,
        "tags": Sequence[TagTypeDef],
        "tracingConfiguration": TracingConfigurationTypeDef,
        "publish": bool,
        "versionDescription": str,
    },
    total=False,
)


class CreateStateMachineInputRequestTypeDef(
    _RequiredCreateStateMachineInputRequestTypeDef, _OptionalCreateStateMachineInputRequestTypeDef
):
    pass


LoggingConfigurationUnionTypeDef = Union[
    LoggingConfigurationTypeDef, LoggingConfigurationOutputTypeDef
]
_RequiredUpdateStateMachineInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalUpdateStateMachineInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStateMachineInputRequestTypeDef",
    {
        "definition": str,
        "roleArn": str,
        "loggingConfiguration": LoggingConfigurationTypeDef,
        "tracingConfiguration": TracingConfigurationTypeDef,
        "publish": bool,
        "versionDescription": str,
    },
    total=False,
)


class UpdateStateMachineInputRequestTypeDef(
    _RequiredUpdateStateMachineInputRequestTypeDef, _OptionalUpdateStateMachineInputRequestTypeDef
):
    pass


GetExecutionHistoryOutputTypeDef = TypedDict(
    "GetExecutionHistoryOutputTypeDef",
    {
        "events": List[HistoryEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
