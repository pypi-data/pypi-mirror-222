"""
Type annotations for scheduler service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_scheduler/type_defs/)

Usage::

    ```python
    from mypy_boto3_scheduler.type_defs import AwsVpcConfigurationOutputTypeDef

    data: AwsVpcConfigurationOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionAfterCompletionType,
    AssignPublicIpType,
    FlexibleTimeWindowModeType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ScheduleGroupStateType,
    ScheduleStateType,
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
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "FlexibleTimeWindowTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteScheduleGroupInputRequestTypeDef",
    "DeleteScheduleInputRequestTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "EventBridgeParametersTypeDef",
    "GetScheduleGroupInputRequestTypeDef",
    "GetScheduleInputRequestTypeDef",
    "KinesisParametersTypeDef",
    "PaginatorConfigTypeDef",
    "ListScheduleGroupsInputRequestTypeDef",
    "ScheduleGroupSummaryTypeDef",
    "ListSchedulesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "RetryPolicyTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "TargetSummaryTypeDef",
    "SqsParametersTypeDef",
    "UntagResourceInputRequestTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "CreateScheduleGroupInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateScheduleGroupOutputTypeDef",
    "CreateScheduleOutputTypeDef",
    "GetScheduleGroupOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "UpdateScheduleOutputTypeDef",
    "ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef",
    "ListSchedulesInputListSchedulesPaginateTypeDef",
    "ListScheduleGroupsOutputTypeDef",
    "SageMakerPipelineParametersOutputTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "ScheduleSummaryTypeDef",
    "EcsParametersOutputTypeDef",
    "EcsParametersTypeDef",
    "ListSchedulesOutputTypeDef",
    "TargetOutputTypeDef",
    "TargetTypeDef",
    "GetScheduleOutputTypeDef",
    "CreateScheduleInputRequestTypeDef",
    "UpdateScheduleInputRequestTypeDef",
)

_RequiredAwsVpcConfigurationOutputTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationOutputTypeDef",
    {
        "Subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationOutputTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationOutputTypeDef",
    {
        "AssignPublicIp": AssignPublicIpType,
        "SecurityGroups": List[str],
    },
    total=False,
)

class AwsVpcConfigurationOutputTypeDef(
    _RequiredAwsVpcConfigurationOutputTypeDef, _OptionalAwsVpcConfigurationOutputTypeDef
):
    pass

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "Subnets": Sequence[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "AssignPublicIp": AssignPublicIpType,
        "SecurityGroups": Sequence[str],
    },
    total=False,
)

class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "base": int,
        "weight": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass

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

_RequiredFlexibleTimeWindowTypeDef = TypedDict(
    "_RequiredFlexibleTimeWindowTypeDef",
    {
        "Mode": FlexibleTimeWindowModeType,
    },
)
_OptionalFlexibleTimeWindowTypeDef = TypedDict(
    "_OptionalFlexibleTimeWindowTypeDef",
    {
        "MaximumWindowInMinutes": int,
    },
    total=False,
)

class FlexibleTimeWindowTypeDef(
    _RequiredFlexibleTimeWindowTypeDef, _OptionalFlexibleTimeWindowTypeDef
):
    pass

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredDeleteScheduleGroupInputRequestTypeDef = TypedDict(
    "_RequiredDeleteScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteScheduleGroupInputRequestTypeDef = TypedDict(
    "_OptionalDeleteScheduleGroupInputRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteScheduleGroupInputRequestTypeDef(
    _RequiredDeleteScheduleGroupInputRequestTypeDef, _OptionalDeleteScheduleGroupInputRequestTypeDef
):
    pass

_RequiredDeleteScheduleInputRequestTypeDef = TypedDict(
    "_RequiredDeleteScheduleInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteScheduleInputRequestTypeDef = TypedDict(
    "_OptionalDeleteScheduleInputRequestTypeDef",
    {
        "ClientToken": str,
        "GroupName": str,
    },
    total=False,
)

class DeleteScheduleInputRequestTypeDef(
    _RequiredDeleteScheduleInputRequestTypeDef, _OptionalDeleteScheduleInputRequestTypeDef
):
    pass

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "expression": str,
        "type": PlacementConstraintTypeType,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "field": str,
        "type": PlacementStrategyTypeType,
    },
    total=False,
)

EventBridgeParametersTypeDef = TypedDict(
    "EventBridgeParametersTypeDef",
    {
        "DetailType": str,
        "Source": str,
    },
)

GetScheduleGroupInputRequestTypeDef = TypedDict(
    "GetScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredGetScheduleInputRequestTypeDef = TypedDict(
    "_RequiredGetScheduleInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetScheduleInputRequestTypeDef = TypedDict(
    "_OptionalGetScheduleInputRequestTypeDef",
    {
        "GroupName": str,
    },
    total=False,
)

class GetScheduleInputRequestTypeDef(
    _RequiredGetScheduleInputRequestTypeDef, _OptionalGetScheduleInputRequestTypeDef
):
    pass

KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKey": str,
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

ListScheduleGroupsInputRequestTypeDef = TypedDict(
    "ListScheduleGroupsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NamePrefix": str,
        "NextToken": str,
    },
    total=False,
)

ScheduleGroupSummaryTypeDef = TypedDict(
    "ScheduleGroupSummaryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleGroupStateType,
    },
    total=False,
)

ListSchedulesInputRequestTypeDef = TypedDict(
    "ListSchedulesInputRequestTypeDef",
    {
        "GroupName": str,
        "MaxResults": int,
        "NamePrefix": str,
        "NextToken": str,
        "State": ScheduleStateType,
    },
    total=False,
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumEventAgeInSeconds": int,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "Arn": str,
    },
)

SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": str,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "awsvpcConfiguration": AwsVpcConfigurationOutputTypeDef,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": AwsVpcConfigurationTypeDef,
    },
    total=False,
)

_RequiredCreateScheduleGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateScheduleGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleGroupInputRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateScheduleGroupInputRequestTypeDef(
    _RequiredCreateScheduleGroupInputRequestTypeDef, _OptionalCreateScheduleGroupInputRequestTypeDef
):
    pass

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateScheduleGroupOutputTypeDef = TypedDict(
    "CreateScheduleGroupOutputTypeDef",
    {
        "ScheduleGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateScheduleOutputTypeDef = TypedDict(
    "CreateScheduleOutputTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetScheduleGroupOutputTypeDef = TypedDict(
    "GetScheduleGroupOutputTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleGroupStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateScheduleOutputTypeDef = TypedDict(
    "UpdateScheduleOutputTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef = TypedDict(
    "ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef",
    {
        "NamePrefix": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSchedulesInputListSchedulesPaginateTypeDef = TypedDict(
    "ListSchedulesInputListSchedulesPaginateTypeDef",
    {
        "GroupName": str,
        "NamePrefix": str,
        "State": ScheduleStateType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListScheduleGroupsOutputTypeDef = TypedDict(
    "ListScheduleGroupsOutputTypeDef",
    {
        "NextToken": str,
        "ScheduleGroups": List[ScheduleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SageMakerPipelineParametersOutputTypeDef = TypedDict(
    "SageMakerPipelineParametersOutputTypeDef",
    {
        "PipelineParameterList": List[SageMakerPipelineParameterTypeDef],
    },
    total=False,
)

SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": Sequence[SageMakerPipelineParameterTypeDef],
    },
    total=False,
)

ScheduleSummaryTypeDef = TypedDict(
    "ScheduleSummaryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "GroupName": str,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleStateType,
        "Target": TargetSummaryTypeDef,
    },
    total=False,
)

_RequiredEcsParametersOutputTypeDef = TypedDict(
    "_RequiredEcsParametersOutputTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalEcsParametersOutputTypeDef = TypedDict(
    "_OptionalEcsParametersOutputTypeDef",
    {
        "CapacityProviderStrategy": List[CapacityProviderStrategyItemTypeDef],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "Group": str,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": NetworkConfigurationOutputTypeDef,
        "PlacementConstraints": List[PlacementConstraintTypeDef],
        "PlacementStrategy": List[PlacementStrategyTypeDef],
        "PlatformVersion": str,
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List[Dict[str, str]],
        "TaskCount": int,
    },
    total=False,
)

class EcsParametersOutputTypeDef(
    _RequiredEcsParametersOutputTypeDef, _OptionalEcsParametersOutputTypeDef
):
    pass

_RequiredEcsParametersTypeDef = TypedDict(
    "_RequiredEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalEcsParametersTypeDef = TypedDict(
    "_OptionalEcsParametersTypeDef",
    {
        "CapacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "Group": str,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "PlacementConstraints": Sequence[PlacementConstraintTypeDef],
        "PlacementStrategy": Sequence[PlacementStrategyTypeDef],
        "PlatformVersion": str,
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": Sequence[Mapping[str, str]],
        "TaskCount": int,
    },
    total=False,
)

class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass

ListSchedulesOutputTypeDef = TypedDict(
    "ListSchedulesOutputTypeDef",
    {
        "NextToken": str,
        "Schedules": List[ScheduleSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredTargetOutputTypeDef = TypedDict(
    "_RequiredTargetOutputTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
    },
)
_OptionalTargetOutputTypeDef = TypedDict(
    "_OptionalTargetOutputTypeDef",
    {
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "EcsParameters": EcsParametersOutputTypeDef,
        "EventBridgeParameters": EventBridgeParametersTypeDef,
        "Input": str,
        "KinesisParameters": KinesisParametersTypeDef,
        "RetryPolicy": RetryPolicyTypeDef,
        "SageMakerPipelineParameters": SageMakerPipelineParametersOutputTypeDef,
        "SqsParameters": SqsParametersTypeDef,
    },
    total=False,
)

class TargetOutputTypeDef(_RequiredTargetOutputTypeDef, _OptionalTargetOutputTypeDef):
    pass

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "EcsParameters": EcsParametersTypeDef,
        "EventBridgeParameters": EventBridgeParametersTypeDef,
        "Input": str,
        "KinesisParameters": KinesisParametersTypeDef,
        "RetryPolicy": RetryPolicyTypeDef,
        "SageMakerPipelineParameters": SageMakerPipelineParametersTypeDef,
        "SqsParameters": SqsParametersTypeDef,
    },
    total=False,
)

class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass

GetScheduleOutputTypeDef = TypedDict(
    "GetScheduleOutputTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "Arn": str,
        "CreationDate": datetime,
        "Description": str,
        "EndDate": datetime,
        "FlexibleTimeWindow": FlexibleTimeWindowTypeDef,
        "GroupName": str,
        "KmsKeyArn": str,
        "LastModificationDate": datetime,
        "Name": str,
        "ScheduleExpression": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": datetime,
        "State": ScheduleStateType,
        "Target": TargetOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateScheduleInputRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleInputRequestTypeDef",
    {
        "FlexibleTimeWindow": FlexibleTimeWindowTypeDef,
        "Name": str,
        "ScheduleExpression": str,
        "Target": TargetTypeDef,
    },
)
_OptionalCreateScheduleInputRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleInputRequestTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "ClientToken": str,
        "Description": str,
        "EndDate": Union[datetime, str],
        "GroupName": str,
        "KmsKeyArn": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": Union[datetime, str],
        "State": ScheduleStateType,
    },
    total=False,
)

class CreateScheduleInputRequestTypeDef(
    _RequiredCreateScheduleInputRequestTypeDef, _OptionalCreateScheduleInputRequestTypeDef
):
    pass

_RequiredUpdateScheduleInputRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduleInputRequestTypeDef",
    {
        "FlexibleTimeWindow": FlexibleTimeWindowTypeDef,
        "Name": str,
        "ScheduleExpression": str,
        "Target": TargetTypeDef,
    },
)
_OptionalUpdateScheduleInputRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduleInputRequestTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "ClientToken": str,
        "Description": str,
        "EndDate": Union[datetime, str],
        "GroupName": str,
        "KmsKeyArn": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": Union[datetime, str],
        "State": ScheduleStateType,
    },
    total=False,
)

class UpdateScheduleInputRequestTypeDef(
    _RequiredUpdateScheduleInputRequestTypeDef, _OptionalUpdateScheduleInputRequestTypeDef
):
    pass
