"""
Type annotations for codepipeline service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/type_defs/)

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionCategoryType,
    ActionConfigurationPropertyTypeType,
    ActionExecutionStatusType,
    ActionOwnerType,
    ApprovalStatusType,
    ExecutorTypeType,
    FailureTypeType,
    JobStatusType,
    PipelineExecutionStatusType,
    StageExecutionStatusType,
    StageTransitionTypeType,
    TriggerTypeType,
    WebhookAuthenticationTypeType,
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
    "AWSSessionCredentialsTypeDef",
    "AcknowledgeJobInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionTypeIdTypeDef",
    "InputArtifactTypeDef",
    "OutputArtifactTypeDef",
    "ActionExecutionFilterTypeDef",
    "ActionExecutionResultTypeDef",
    "ErrorDetailsTypeDef",
    "ActionRevisionOutputTypeDef",
    "TimestampTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeIdentifierTypeDef",
    "ActionTypePermissionsOutputTypeDef",
    "ActionTypePropertyTypeDef",
    "ActionTypeUrlsTypeDef",
    "ActionTypePermissionsTypeDef",
    "ActionTypeSettingsTypeDef",
    "ArtifactDetailsTypeDef",
    "ApprovalResultTypeDef",
    "S3LocationTypeDef",
    "S3ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "EncryptionKeyTypeDef",
    "BlockerDeclarationTypeDef",
    "TagTypeDef",
    "DeleteCustomActionTypeInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "DeleteWebhookInputRequestTypeDef",
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    "DisableStageTransitionInputRequestTypeDef",
    "EnableStageTransitionInputRequestTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "JobWorkerExecutorConfigurationOutputTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeInputRequestTypeDef",
    "GetJobDetailsInputRequestTypeDef",
    "GetPipelineExecutionInputRequestTypeDef",
    "GetPipelineInputRequestTypeDef",
    "PipelineMetadataTypeDef",
    "GetPipelineStateInputRequestTypeDef",
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListActionTypesInputRequestTypeDef",
    "ListPipelineExecutionsInputRequestTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "PipelineSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListWebhooksInputRequestTypeDef",
    "StageContextTypeDef",
    "SourceRevisionTypeDef",
    "StopExecutionTriggerTypeDef",
    "ThirdPartyJobTypeDef",
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    "RetryStageExecutionInputRequestTypeDef",
    "StageExecutionTypeDef",
    "TransitionStateTypeDef",
    "StartPipelineExecutionInputRequestTypeDef",
    "StopPipelineExecutionInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookFilterRuleTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultOutputTypeDef",
    "RetryStageExecutionOutputTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "PollForJobsInputRequestTypeDef",
    "PollForThirdPartyJobsInputRequestTypeDef",
    "ActionDeclarationOutputTypeDef",
    "ActionDeclarationTypeDef",
    "ListActionExecutionsInputRequestTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionTypeDef",
    "CurrentRevisionTypeDef",
    "ActionTypeTypeDef",
    "PutApprovalResultInputRequestTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactLocationTypeDef",
    "PipelineExecutionTypeDef",
    "ArtifactStoreTypeDef",
    "CreateCustomActionTypeInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "ExecutorConfigurationOutputTypeDef",
    "ExecutorConfigurationTypeDef",
    "PutJobFailureResultInputRequestTypeDef",
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    "ListActionExecutionsInputListActionExecutionsPaginateTypeDef",
    "ListActionTypesInputListActionTypesPaginateTypeDef",
    "ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef",
    "ListPipelinesInputListPipelinesPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ListWebhooksInputListWebhooksPaginateTypeDef",
    "ListPipelinesOutputTypeDef",
    "PipelineContextTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "WebhookDefinitionOutputTypeDef",
    "WebhookDefinitionTypeDef",
    "StageDeclarationOutputTypeDef",
    "StageDeclarationTypeDef",
    "ActionStateTypeDef",
    "ActionRevisionUnionTypeDef",
    "PutActionRevisionInputRequestTypeDef",
    "PutJobSuccessResultInputRequestTypeDef",
    "PutThirdPartyJobSuccessResultInputRequestTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "ListActionTypesOutputTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ArtifactTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "ActionTypeExecutorOutputTypeDef",
    "ActionTypeExecutorTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "ListWebhookItemTypeDef",
    "PutWebhookInputRequestTypeDef",
    "WebhookDefinitionUnionTypeDef",
    "PipelineDeclarationOutputTypeDef",
    "PipelineDeclarationTypeDef",
    "StageStateTypeDef",
    "ActionExecutionDetailTypeDef",
    "JobDataTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ActionTypeDeclarationOutputTypeDef",
    "ActionTypeDeclarationTypeDef",
    "ListWebhooksOutputTypeDef",
    "PutWebhookOutputTypeDef",
    "CreatePipelineOutputTypeDef",
    "GetPipelineOutputTypeDef",
    "UpdatePipelineOutputTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "PipelineDeclarationUnionTypeDef",
    "UpdatePipelineInputRequestTypeDef",
    "GetPipelineStateOutputTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "GetActionTypeOutputTypeDef",
    "ActionTypeDeclarationUnionTypeDef",
    "UpdateActionTypeInputRequestTypeDef",
    "GetJobDetailsOutputTypeDef",
    "PollForJobsOutputTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
)

AWSSessionCredentialsTypeDef = TypedDict(
    "AWSSessionCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
)

AcknowledgeJobInputRequestTypeDef = TypedDict(
    "AcknowledgeJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
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

AcknowledgeThirdPartyJobInputRequestTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
        "clientToken": str,
    },
)

_RequiredActionConfigurationPropertyTypeDef = TypedDict(
    "_RequiredActionConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
    },
)
_OptionalActionConfigurationPropertyTypeDef = TypedDict(
    "_OptionalActionConfigurationPropertyTypeDef",
    {
        "queryable": bool,
        "description": str,
        "type": ActionConfigurationPropertyTypeType,
    },
    total=False,
)

class ActionConfigurationPropertyTypeDef(
    _RequiredActionConfigurationPropertyTypeDef, _OptionalActionConfigurationPropertyTypeDef
):
    pass

ActionConfigurationTypeDef = TypedDict(
    "ActionConfigurationTypeDef",
    {
        "configuration": Dict[str, str],
    },
    total=False,
)

ActionContextTypeDef = TypedDict(
    "ActionContextTypeDef",
    {
        "name": str,
        "actionExecutionId": str,
    },
    total=False,
)

ActionTypeIdTypeDef = TypedDict(
    "ActionTypeIdTypeDef",
    {
        "category": ActionCategoryType,
        "owner": ActionOwnerType,
        "provider": str,
        "version": str,
    },
)

InputArtifactTypeDef = TypedDict(
    "InputArtifactTypeDef",
    {
        "name": str,
    },
)

OutputArtifactTypeDef = TypedDict(
    "OutputArtifactTypeDef",
    {
        "name": str,
    },
)

ActionExecutionFilterTypeDef = TypedDict(
    "ActionExecutionFilterTypeDef",
    {
        "pipelineExecutionId": str,
    },
    total=False,
)

ActionExecutionResultTypeDef = TypedDict(
    "ActionExecutionResultTypeDef",
    {
        "externalExecutionId": str,
        "externalExecutionSummary": str,
        "externalExecutionUrl": str,
    },
    total=False,
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

ActionRevisionOutputTypeDef = TypedDict(
    "ActionRevisionOutputTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": datetime,
    },
)

TimestampTypeDef = Union[datetime, str]
ActionTypeArtifactDetailsTypeDef = TypedDict(
    "ActionTypeArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

ActionTypeIdentifierTypeDef = TypedDict(
    "ActionTypeIdentifierTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

ActionTypePermissionsOutputTypeDef = TypedDict(
    "ActionTypePermissionsOutputTypeDef",
    {
        "allowedAccounts": List[str],
    },
)

_RequiredActionTypePropertyTypeDef = TypedDict(
    "_RequiredActionTypePropertyTypeDef",
    {
        "name": str,
        "optional": bool,
        "key": bool,
        "noEcho": bool,
    },
)
_OptionalActionTypePropertyTypeDef = TypedDict(
    "_OptionalActionTypePropertyTypeDef",
    {
        "queryable": bool,
        "description": str,
    },
    total=False,
)

class ActionTypePropertyTypeDef(
    _RequiredActionTypePropertyTypeDef, _OptionalActionTypePropertyTypeDef
):
    pass

ActionTypeUrlsTypeDef = TypedDict(
    "ActionTypeUrlsTypeDef",
    {
        "configurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ActionTypePermissionsTypeDef = TypedDict(
    "ActionTypePermissionsTypeDef",
    {
        "allowedAccounts": Sequence[str],
    },
)

ActionTypeSettingsTypeDef = TypedDict(
    "ActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ArtifactDetailsTypeDef = TypedDict(
    "ArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

ApprovalResultTypeDef = TypedDict(
    "ApprovalResultTypeDef",
    {
        "summary": str,
        "status": ApprovalStatusType,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

S3ArtifactLocationTypeDef = TypedDict(
    "S3ArtifactLocationTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)

ArtifactRevisionTypeDef = TypedDict(
    "ArtifactRevisionTypeDef",
    {
        "name": str,
        "revisionId": str,
        "revisionChangeIdentifier": str,
        "revisionSummary": str,
        "created": datetime,
        "revisionUrl": str,
    },
    total=False,
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "id": str,
        "type": Literal["KMS"],
    },
)

BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef",
    {
        "name": str,
        "type": Literal["Schedule"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

DeleteCustomActionTypeInputRequestTypeDef = TypedDict(
    "DeleteCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
    },
)

DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteWebhookInputRequestTypeDef = TypedDict(
    "DeleteWebhookInputRequestTypeDef",
    {
        "name": str,
    },
)

DeregisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": str,
    },
    total=False,
)

DisableStageTransitionInputRequestTypeDef = TypedDict(
    "DisableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
        "reason": str,
    },
)

EnableStageTransitionInputRequestTypeDef = TypedDict(
    "EnableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
    },
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "summary": str,
        "externalExecutionId": str,
        "percentComplete": int,
    },
    total=False,
)

ExecutionTriggerTypeDef = TypedDict(
    "ExecutionTriggerTypeDef",
    {
        "triggerType": TriggerTypeType,
        "triggerDetail": str,
    },
    total=False,
)

JobWorkerExecutorConfigurationOutputTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationOutputTypeDef",
    {
        "pollingAccounts": List[str],
        "pollingServicePrincipals": List[str],
    },
    total=False,
)

LambdaExecutorConfigurationTypeDef = TypedDict(
    "LambdaExecutorConfigurationTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

JobWorkerExecutorConfigurationTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationTypeDef",
    {
        "pollingAccounts": Sequence[str],
        "pollingServicePrincipals": Sequence[str],
    },
    total=False,
)

_RequiredFailureDetailsTypeDef = TypedDict(
    "_RequiredFailureDetailsTypeDef",
    {
        "type": FailureTypeType,
        "message": str,
    },
)
_OptionalFailureDetailsTypeDef = TypedDict(
    "_OptionalFailureDetailsTypeDef",
    {
        "externalExecutionId": str,
    },
    total=False,
)

class FailureDetailsTypeDef(_RequiredFailureDetailsTypeDef, _OptionalFailureDetailsTypeDef):
    pass

GetActionTypeInputRequestTypeDef = TypedDict(
    "GetActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

GetJobDetailsInputRequestTypeDef = TypedDict(
    "GetJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
    },
)

GetPipelineExecutionInputRequestTypeDef = TypedDict(
    "GetPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)

_RequiredGetPipelineInputRequestTypeDef = TypedDict(
    "_RequiredGetPipelineInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetPipelineInputRequestTypeDef = TypedDict(
    "_OptionalGetPipelineInputRequestTypeDef",
    {
        "version": int,
    },
    total=False,
)

class GetPipelineInputRequestTypeDef(
    _RequiredGetPipelineInputRequestTypeDef, _OptionalGetPipelineInputRequestTypeDef
):
    pass

PipelineMetadataTypeDef = TypedDict(
    "PipelineMetadataTypeDef",
    {
        "pipelineArn": str,
        "created": datetime,
        "updated": datetime,
        "pollingDisabledAt": datetime,
    },
    total=False,
)

GetPipelineStateInputRequestTypeDef = TypedDict(
    "GetPipelineStateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetThirdPartyJobDetailsInputRequestTypeDef = TypedDict(
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
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

ListActionTypesInputRequestTypeDef = TypedDict(
    "ListActionTypesInputRequestTypeDef",
    {
        "actionOwnerFilter": ActionOwnerType,
        "nextToken": str,
        "regionFilter": str,
    },
    total=False,
)

_RequiredListPipelineExecutionsInputRequestTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListPipelineExecutionsInputRequestTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPipelineExecutionsInputRequestTypeDef(
    _RequiredListPipelineExecutionsInputRequestTypeDef,
    _OptionalListPipelineExecutionsInputRequestTypeDef,
):
    pass

ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "name": str,
        "version": int,
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListWebhooksInputRequestTypeDef = TypedDict(
    "ListWebhooksInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

StageContextTypeDef = TypedDict(
    "StageContextTypeDef",
    {
        "name": str,
    },
    total=False,
)

_RequiredSourceRevisionTypeDef = TypedDict(
    "_RequiredSourceRevisionTypeDef",
    {
        "actionName": str,
    },
)
_OptionalSourceRevisionTypeDef = TypedDict(
    "_OptionalSourceRevisionTypeDef",
    {
        "revisionId": str,
        "revisionSummary": str,
        "revisionUrl": str,
    },
    total=False,
)

class SourceRevisionTypeDef(_RequiredSourceRevisionTypeDef, _OptionalSourceRevisionTypeDef):
    pass

StopExecutionTriggerTypeDef = TypedDict(
    "StopExecutionTriggerTypeDef",
    {
        "reason": str,
    },
    total=False,
)

ThirdPartyJobTypeDef = TypedDict(
    "ThirdPartyJobTypeDef",
    {
        "clientId": str,
        "jobId": str,
    },
    total=False,
)

RegisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": str,
    },
    total=False,
)

RetryStageExecutionInputRequestTypeDef = TypedDict(
    "RetryStageExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "pipelineExecutionId": str,
        "retryMode": Literal["FAILED_ACTIONS"],
    },
)

StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": StageExecutionStatusType,
    },
)

TransitionStateTypeDef = TypedDict(
    "TransitionStateTypeDef",
    {
        "enabled": bool,
        "lastChangedBy": str,
        "lastChangedAt": datetime,
        "disabledReason": str,
    },
    total=False,
)

_RequiredStartPipelineExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartPipelineExecutionInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalStartPipelineExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartPipelineExecutionInputRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class StartPipelineExecutionInputRequestTypeDef(
    _RequiredStartPipelineExecutionInputRequestTypeDef,
    _OptionalStartPipelineExecutionInputRequestTypeDef,
):
    pass

_RequiredStopPipelineExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStopPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)
_OptionalStopPipelineExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStopPipelineExecutionInputRequestTypeDef",
    {
        "abandon": bool,
        "reason": str,
    },
    total=False,
)

class StopPipelineExecutionInputRequestTypeDef(
    _RequiredStopPipelineExecutionInputRequestTypeDef,
    _OptionalStopPipelineExecutionInputRequestTypeDef,
):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

WebhookAuthConfigurationTypeDef = TypedDict(
    "WebhookAuthConfigurationTypeDef",
    {
        "AllowedIPRange": str,
        "SecretToken": str,
    },
    total=False,
)

_RequiredWebhookFilterRuleTypeDef = TypedDict(
    "_RequiredWebhookFilterRuleTypeDef",
    {
        "jsonPath": str,
    },
)
_OptionalWebhookFilterRuleTypeDef = TypedDict(
    "_OptionalWebhookFilterRuleTypeDef",
    {
        "matchEquals": str,
    },
    total=False,
)

class WebhookFilterRuleTypeDef(
    _RequiredWebhookFilterRuleTypeDef, _OptionalWebhookFilterRuleTypeDef
):
    pass

AcknowledgeJobOutputTypeDef = TypedDict(
    "AcknowledgeJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AcknowledgeThirdPartyJobOutputTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutActionRevisionOutputTypeDef = TypedDict(
    "PutActionRevisionOutputTypeDef",
    {
        "newRevision": bool,
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutApprovalResultOutputTypeDef = TypedDict(
    "PutApprovalResultOutputTypeDef",
    {
        "approvedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RetryStageExecutionOutputTypeDef = TypedDict(
    "RetryStageExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartPipelineExecutionOutputTypeDef = TypedDict(
    "StartPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopPipelineExecutionOutputTypeDef = TypedDict(
    "StopPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPollForJobsInputRequestTypeDef = TypedDict(
    "_RequiredPollForJobsInputRequestTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
    },
)
_OptionalPollForJobsInputRequestTypeDef = TypedDict(
    "_OptionalPollForJobsInputRequestTypeDef",
    {
        "maxBatchSize": int,
        "queryParam": Mapping[str, str],
    },
    total=False,
)

class PollForJobsInputRequestTypeDef(
    _RequiredPollForJobsInputRequestTypeDef, _OptionalPollForJobsInputRequestTypeDef
):
    pass

_RequiredPollForThirdPartyJobsInputRequestTypeDef = TypedDict(
    "_RequiredPollForThirdPartyJobsInputRequestTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
    },
)
_OptionalPollForThirdPartyJobsInputRequestTypeDef = TypedDict(
    "_OptionalPollForThirdPartyJobsInputRequestTypeDef",
    {
        "maxBatchSize": int,
    },
    total=False,
)

class PollForThirdPartyJobsInputRequestTypeDef(
    _RequiredPollForThirdPartyJobsInputRequestTypeDef,
    _OptionalPollForThirdPartyJobsInputRequestTypeDef,
):
    pass

_RequiredActionDeclarationOutputTypeDef = TypedDict(
    "_RequiredActionDeclarationOutputTypeDef",
    {
        "name": str,
        "actionTypeId": ActionTypeIdTypeDef,
    },
)
_OptionalActionDeclarationOutputTypeDef = TypedDict(
    "_OptionalActionDeclarationOutputTypeDef",
    {
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[OutputArtifactTypeDef],
        "inputArtifacts": List[InputArtifactTypeDef],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

class ActionDeclarationOutputTypeDef(
    _RequiredActionDeclarationOutputTypeDef, _OptionalActionDeclarationOutputTypeDef
):
    pass

_RequiredActionDeclarationTypeDef = TypedDict(
    "_RequiredActionDeclarationTypeDef",
    {
        "name": str,
        "actionTypeId": ActionTypeIdTypeDef,
    },
)
_OptionalActionDeclarationTypeDef = TypedDict(
    "_OptionalActionDeclarationTypeDef",
    {
        "runOrder": int,
        "configuration": Mapping[str, str],
        "outputArtifacts": Sequence[OutputArtifactTypeDef],
        "inputArtifacts": Sequence[InputArtifactTypeDef],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

class ActionDeclarationTypeDef(
    _RequiredActionDeclarationTypeDef, _OptionalActionDeclarationTypeDef
):
    pass

_RequiredListActionExecutionsInputRequestTypeDef = TypedDict(
    "_RequiredListActionExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListActionExecutionsInputRequestTypeDef = TypedDict(
    "_OptionalListActionExecutionsInputRequestTypeDef",
    {
        "filter": ActionExecutionFilterTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListActionExecutionsInputRequestTypeDef(
    _RequiredListActionExecutionsInputRequestTypeDef,
    _OptionalListActionExecutionsInputRequestTypeDef,
):
    pass

ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "actionExecutionId": str,
        "status": ActionExecutionStatusType,
        "summary": str,
        "lastStatusChange": datetime,
        "token": str,
        "lastUpdatedBy": str,
        "externalExecutionId": str,
        "externalExecutionUrl": str,
        "percentComplete": int,
        "errorDetails": ErrorDetailsTypeDef,
    },
    total=False,
)

ActionRevisionTypeDef = TypedDict(
    "ActionRevisionTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": TimestampTypeDef,
    },
)

_RequiredCurrentRevisionTypeDef = TypedDict(
    "_RequiredCurrentRevisionTypeDef",
    {
        "revision": str,
        "changeIdentifier": str,
    },
)
_OptionalCurrentRevisionTypeDef = TypedDict(
    "_OptionalCurrentRevisionTypeDef",
    {
        "created": TimestampTypeDef,
        "revisionSummary": str,
    },
    total=False,
)

class CurrentRevisionTypeDef(_RequiredCurrentRevisionTypeDef, _OptionalCurrentRevisionTypeDef):
    pass

_RequiredActionTypeTypeDef = TypedDict(
    "_RequiredActionTypeTypeDef",
    {
        "id": ActionTypeIdTypeDef,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "outputArtifactDetails": ArtifactDetailsTypeDef,
    },
)
_OptionalActionTypeTypeDef = TypedDict(
    "_OptionalActionTypeTypeDef",
    {
        "settings": ActionTypeSettingsTypeDef,
        "actionConfigurationProperties": List[ActionConfigurationPropertyTypeDef],
    },
    total=False,
)

class ActionTypeTypeDef(_RequiredActionTypeTypeDef, _OptionalActionTypeTypeDef):
    pass

PutApprovalResultInputRequestTypeDef = TypedDict(
    "PutApprovalResultInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "result": ApprovalResultTypeDef,
        "token": str,
    },
)

ArtifactDetailTypeDef = TypedDict(
    "ArtifactDetailTypeDef",
    {
        "name": str,
        "s3location": S3LocationTypeDef,
    },
    total=False,
)

ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {
        "type": Literal["S3"],
        "s3Location": S3ArtifactLocationTypeDef,
    },
    total=False,
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "pipelineExecutionId": str,
        "status": PipelineExecutionStatusType,
        "statusSummary": str,
        "artifactRevisions": List[ArtifactRevisionTypeDef],
    },
    total=False,
)

_RequiredArtifactStoreTypeDef = TypedDict(
    "_RequiredArtifactStoreTypeDef",
    {
        "type": Literal["S3"],
        "location": str,
    },
)
_OptionalArtifactStoreTypeDef = TypedDict(
    "_OptionalArtifactStoreTypeDef",
    {
        "encryptionKey": EncryptionKeyTypeDef,
    },
    total=False,
)

class ArtifactStoreTypeDef(_RequiredArtifactStoreTypeDef, _OptionalArtifactStoreTypeDef):
    pass

_RequiredCreateCustomActionTypeInputRequestTypeDef = TypedDict(
    "_RequiredCreateCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "outputArtifactDetails": ArtifactDetailsTypeDef,
    },
)
_OptionalCreateCustomActionTypeInputRequestTypeDef = TypedDict(
    "_OptionalCreateCustomActionTypeInputRequestTypeDef",
    {
        "settings": ActionTypeSettingsTypeDef,
        "configurationProperties": Sequence[ActionConfigurationPropertyTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateCustomActionTypeInputRequestTypeDef(
    _RequiredCreateCustomActionTypeInputRequestTypeDef,
    _OptionalCreateCustomActionTypeInputRequestTypeDef,
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List[TagTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

ExecutorConfigurationOutputTypeDef = TypedDict(
    "ExecutorConfigurationOutputTypeDef",
    {
        "lambdaExecutorConfiguration": LambdaExecutorConfigurationTypeDef,
        "jobWorkerExecutorConfiguration": JobWorkerExecutorConfigurationOutputTypeDef,
    },
    total=False,
)

ExecutorConfigurationTypeDef = TypedDict(
    "ExecutorConfigurationTypeDef",
    {
        "lambdaExecutorConfiguration": LambdaExecutorConfigurationTypeDef,
        "jobWorkerExecutorConfiguration": JobWorkerExecutorConfigurationTypeDef,
    },
    total=False,
)

PutJobFailureResultInputRequestTypeDef = TypedDict(
    "PutJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "failureDetails": FailureDetailsTypeDef,
    },
)

PutThirdPartyJobFailureResultInputRequestTypeDef = TypedDict(
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "failureDetails": FailureDetailsTypeDef,
    },
)

_RequiredListActionExecutionsInputListActionExecutionsPaginateTypeDef = TypedDict(
    "_RequiredListActionExecutionsInputListActionExecutionsPaginateTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListActionExecutionsInputListActionExecutionsPaginateTypeDef = TypedDict(
    "_OptionalListActionExecutionsInputListActionExecutionsPaginateTypeDef",
    {
        "filter": ActionExecutionFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListActionExecutionsInputListActionExecutionsPaginateTypeDef(
    _RequiredListActionExecutionsInputListActionExecutionsPaginateTypeDef,
    _OptionalListActionExecutionsInputListActionExecutionsPaginateTypeDef,
):
    pass

ListActionTypesInputListActionTypesPaginateTypeDef = TypedDict(
    "ListActionTypesInputListActionTypesPaginateTypeDef",
    {
        "actionOwnerFilter": ActionOwnerType,
        "regionFilter": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef(
    _RequiredListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef,
    _OptionalListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef,
):
    pass

ListPipelinesInputListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesInputListPipelinesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(
    _RequiredListTagsForResourceInputListTagsForResourcePaginateTypeDef,
    _OptionalListTagsForResourceInputListTagsForResourcePaginateTypeDef,
):
    pass

ListWebhooksInputListWebhooksPaginateTypeDef = TypedDict(
    "ListWebhooksInputListWebhooksPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelines": List[PipelineSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PipelineContextTypeDef = TypedDict(
    "PipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": StageContextTypeDef,
        "action": ActionContextTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)

PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "pipelineExecutionId": str,
        "status": PipelineExecutionStatusType,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List[SourceRevisionTypeDef],
        "trigger": ExecutionTriggerTypeDef,
        "stopTrigger": StopExecutionTriggerTypeDef,
    },
    total=False,
)

PollForThirdPartyJobsOutputTypeDef = TypedDict(
    "PollForThirdPartyJobsOutputTypeDef",
    {
        "jobs": List[ThirdPartyJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

WebhookDefinitionOutputTypeDef = TypedDict(
    "WebhookDefinitionOutputTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[WebhookFilterRuleTypeDef],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": WebhookAuthConfigurationTypeDef,
    },
)

WebhookDefinitionTypeDef = TypedDict(
    "WebhookDefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": Sequence[WebhookFilterRuleTypeDef],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": WebhookAuthConfigurationTypeDef,
    },
)

_RequiredStageDeclarationOutputTypeDef = TypedDict(
    "_RequiredStageDeclarationOutputTypeDef",
    {
        "name": str,
        "actions": List[ActionDeclarationOutputTypeDef],
    },
)
_OptionalStageDeclarationOutputTypeDef = TypedDict(
    "_OptionalStageDeclarationOutputTypeDef",
    {
        "blockers": List[BlockerDeclarationTypeDef],
    },
    total=False,
)

class StageDeclarationOutputTypeDef(
    _RequiredStageDeclarationOutputTypeDef, _OptionalStageDeclarationOutputTypeDef
):
    pass

_RequiredStageDeclarationTypeDef = TypedDict(
    "_RequiredStageDeclarationTypeDef",
    {
        "name": str,
        "actions": Sequence[ActionDeclarationTypeDef],
    },
)
_OptionalStageDeclarationTypeDef = TypedDict(
    "_OptionalStageDeclarationTypeDef",
    {
        "blockers": Sequence[BlockerDeclarationTypeDef],
    },
    total=False,
)

class StageDeclarationTypeDef(_RequiredStageDeclarationTypeDef, _OptionalStageDeclarationTypeDef):
    pass

ActionStateTypeDef = TypedDict(
    "ActionStateTypeDef",
    {
        "actionName": str,
        "currentRevision": ActionRevisionOutputTypeDef,
        "latestExecution": ActionExecutionTypeDef,
        "entityUrl": str,
        "revisionUrl": str,
    },
    total=False,
)

ActionRevisionUnionTypeDef = Union[ActionRevisionTypeDef, ActionRevisionOutputTypeDef]
PutActionRevisionInputRequestTypeDef = TypedDict(
    "PutActionRevisionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "actionRevision": ActionRevisionTypeDef,
    },
)

_RequiredPutJobSuccessResultInputRequestTypeDef = TypedDict(
    "_RequiredPutJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalPutJobSuccessResultInputRequestTypeDef = TypedDict(
    "_OptionalPutJobSuccessResultInputRequestTypeDef",
    {
        "currentRevision": CurrentRevisionTypeDef,
        "continuationToken": str,
        "executionDetails": ExecutionDetailsTypeDef,
        "outputVariables": Mapping[str, str],
    },
    total=False,
)

class PutJobSuccessResultInputRequestTypeDef(
    _RequiredPutJobSuccessResultInputRequestTypeDef, _OptionalPutJobSuccessResultInputRequestTypeDef
):
    pass

_RequiredPutThirdPartyJobSuccessResultInputRequestTypeDef = TypedDict(
    "_RequiredPutThirdPartyJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)
_OptionalPutThirdPartyJobSuccessResultInputRequestTypeDef = TypedDict(
    "_OptionalPutThirdPartyJobSuccessResultInputRequestTypeDef",
    {
        "currentRevision": CurrentRevisionTypeDef,
        "continuationToken": str,
        "executionDetails": ExecutionDetailsTypeDef,
    },
    total=False,
)

class PutThirdPartyJobSuccessResultInputRequestTypeDef(
    _RequiredPutThirdPartyJobSuccessResultInputRequestTypeDef,
    _OptionalPutThirdPartyJobSuccessResultInputRequestTypeDef,
):
    pass

CreateCustomActionTypeOutputTypeDef = TypedDict(
    "CreateCustomActionTypeOutputTypeDef",
    {
        "actionType": ActionTypeTypeDef,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListActionTypesOutputTypeDef = TypedDict(
    "ListActionTypesOutputTypeDef",
    {
        "actionTypes": List[ActionTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ActionExecutionInputTypeDef = TypedDict(
    "ActionExecutionInputTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List[ArtifactDetailTypeDef],
        "namespace": str,
    },
    total=False,
)

ActionExecutionOutputTypeDef = TypedDict(
    "ActionExecutionOutputTypeDef",
    {
        "outputArtifacts": List[ArtifactDetailTypeDef],
        "executionResult": ActionExecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ArtifactLocationTypeDef,
    },
    total=False,
)

GetPipelineExecutionOutputTypeDef = TypedDict(
    "GetPipelineExecutionOutputTypeDef",
    {
        "pipelineExecution": PipelineExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredActionTypeExecutorOutputTypeDef = TypedDict(
    "_RequiredActionTypeExecutorOutputTypeDef",
    {
        "configuration": ExecutorConfigurationOutputTypeDef,
        "type": ExecutorTypeType,
    },
)
_OptionalActionTypeExecutorOutputTypeDef = TypedDict(
    "_OptionalActionTypeExecutorOutputTypeDef",
    {
        "policyStatementsTemplate": str,
        "jobTimeout": int,
    },
    total=False,
)

class ActionTypeExecutorOutputTypeDef(
    _RequiredActionTypeExecutorOutputTypeDef, _OptionalActionTypeExecutorOutputTypeDef
):
    pass

_RequiredActionTypeExecutorTypeDef = TypedDict(
    "_RequiredActionTypeExecutorTypeDef",
    {
        "configuration": ExecutorConfigurationTypeDef,
        "type": ExecutorTypeType,
    },
)
_OptionalActionTypeExecutorTypeDef = TypedDict(
    "_OptionalActionTypeExecutorTypeDef",
    {
        "policyStatementsTemplate": str,
        "jobTimeout": int,
    },
    total=False,
)

class ActionTypeExecutorTypeDef(
    _RequiredActionTypeExecutorTypeDef, _OptionalActionTypeExecutorTypeDef
):
    pass

ListPipelineExecutionsOutputTypeDef = TypedDict(
    "ListPipelineExecutionsOutputTypeDef",
    {
        "pipelineExecutionSummaries": List[PipelineExecutionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListWebhookItemTypeDef = TypedDict(
    "_RequiredListWebhookItemTypeDef",
    {
        "definition": WebhookDefinitionOutputTypeDef,
        "url": str,
    },
)
_OptionalListWebhookItemTypeDef = TypedDict(
    "_OptionalListWebhookItemTypeDef",
    {
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[TagTypeDef],
    },
    total=False,
)

class ListWebhookItemTypeDef(_RequiredListWebhookItemTypeDef, _OptionalListWebhookItemTypeDef):
    pass

_RequiredPutWebhookInputRequestTypeDef = TypedDict(
    "_RequiredPutWebhookInputRequestTypeDef",
    {
        "webhook": WebhookDefinitionTypeDef,
    },
)
_OptionalPutWebhookInputRequestTypeDef = TypedDict(
    "_OptionalPutWebhookInputRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class PutWebhookInputRequestTypeDef(
    _RequiredPutWebhookInputRequestTypeDef, _OptionalPutWebhookInputRequestTypeDef
):
    pass

WebhookDefinitionUnionTypeDef = Union[WebhookDefinitionTypeDef, WebhookDefinitionOutputTypeDef]
_RequiredPipelineDeclarationOutputTypeDef = TypedDict(
    "_RequiredPipelineDeclarationOutputTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": List[StageDeclarationOutputTypeDef],
    },
)
_OptionalPipelineDeclarationOutputTypeDef = TypedDict(
    "_OptionalPipelineDeclarationOutputTypeDef",
    {
        "artifactStore": ArtifactStoreTypeDef,
        "artifactStores": Dict[str, ArtifactStoreTypeDef],
        "version": int,
    },
    total=False,
)

class PipelineDeclarationOutputTypeDef(
    _RequiredPipelineDeclarationOutputTypeDef, _OptionalPipelineDeclarationOutputTypeDef
):
    pass

_RequiredPipelineDeclarationTypeDef = TypedDict(
    "_RequiredPipelineDeclarationTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": Sequence[StageDeclarationTypeDef],
    },
)
_OptionalPipelineDeclarationTypeDef = TypedDict(
    "_OptionalPipelineDeclarationTypeDef",
    {
        "artifactStore": ArtifactStoreTypeDef,
        "artifactStores": Mapping[str, ArtifactStoreTypeDef],
        "version": int,
    },
    total=False,
)

class PipelineDeclarationTypeDef(
    _RequiredPipelineDeclarationTypeDef, _OptionalPipelineDeclarationTypeDef
):
    pass

StageStateTypeDef = TypedDict(
    "StageStateTypeDef",
    {
        "stageName": str,
        "inboundExecution": StageExecutionTypeDef,
        "inboundTransitionState": TransitionStateTypeDef,
        "actionStates": List[ActionStateTypeDef],
        "latestExecution": StageExecutionTypeDef,
    },
    total=False,
)

ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": ActionExecutionStatusType,
        "input": ActionExecutionInputTypeDef,
        "output": ActionExecutionOutputTypeDef,
    },
    total=False,
)

JobDataTypeDef = TypedDict(
    "JobDataTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
        "actionConfiguration": ActionConfigurationTypeDef,
        "pipelineContext": PipelineContextTypeDef,
        "inputArtifacts": List[ArtifactTypeDef],
        "outputArtifacts": List[ArtifactTypeDef],
        "artifactCredentials": AWSSessionCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": EncryptionKeyTypeDef,
    },
    total=False,
)

ThirdPartyJobDataTypeDef = TypedDict(
    "ThirdPartyJobDataTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
        "actionConfiguration": ActionConfigurationTypeDef,
        "pipelineContext": PipelineContextTypeDef,
        "inputArtifacts": List[ArtifactTypeDef],
        "outputArtifacts": List[ArtifactTypeDef],
        "artifactCredentials": AWSSessionCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": EncryptionKeyTypeDef,
    },
    total=False,
)

_RequiredActionTypeDeclarationOutputTypeDef = TypedDict(
    "_RequiredActionTypeDeclarationOutputTypeDef",
    {
        "executor": ActionTypeExecutorOutputTypeDef,
        "id": ActionTypeIdentifierTypeDef,
        "inputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "outputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
    },
)
_OptionalActionTypeDeclarationOutputTypeDef = TypedDict(
    "_OptionalActionTypeDeclarationOutputTypeDef",
    {
        "description": str,
        "permissions": ActionTypePermissionsOutputTypeDef,
        "properties": List[ActionTypePropertyTypeDef],
        "urls": ActionTypeUrlsTypeDef,
    },
    total=False,
)

class ActionTypeDeclarationOutputTypeDef(
    _RequiredActionTypeDeclarationOutputTypeDef, _OptionalActionTypeDeclarationOutputTypeDef
):
    pass

_RequiredActionTypeDeclarationTypeDef = TypedDict(
    "_RequiredActionTypeDeclarationTypeDef",
    {
        "executor": ActionTypeExecutorTypeDef,
        "id": ActionTypeIdentifierTypeDef,
        "inputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "outputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
    },
)
_OptionalActionTypeDeclarationTypeDef = TypedDict(
    "_OptionalActionTypeDeclarationTypeDef",
    {
        "description": str,
        "permissions": ActionTypePermissionsTypeDef,
        "properties": Sequence[ActionTypePropertyTypeDef],
        "urls": ActionTypeUrlsTypeDef,
    },
    total=False,
)

class ActionTypeDeclarationTypeDef(
    _RequiredActionTypeDeclarationTypeDef, _OptionalActionTypeDeclarationTypeDef
):
    pass

ListWebhooksOutputTypeDef = TypedDict(
    "ListWebhooksOutputTypeDef",
    {
        "webhooks": List[ListWebhookItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutWebhookOutputTypeDef = TypedDict(
    "PutWebhookOutputTypeDef",
    {
        "webhook": ListWebhookItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipeline": PipelineDeclarationOutputTypeDef,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPipelineOutputTypeDef = TypedDict(
    "GetPipelineOutputTypeDef",
    {
        "pipeline": PipelineDeclarationOutputTypeDef,
        "metadata": PipelineMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePipelineOutputTypeDef = TypedDict(
    "UpdatePipelineOutputTypeDef",
    {
        "pipeline": PipelineDeclarationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreatePipelineInputRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineInputRequestTypeDef",
    {
        "pipeline": PipelineDeclarationTypeDef,
    },
)
_OptionalCreatePipelineInputRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineInputRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreatePipelineInputRequestTypeDef(
    _RequiredCreatePipelineInputRequestTypeDef, _OptionalCreatePipelineInputRequestTypeDef
):
    pass

PipelineDeclarationUnionTypeDef = Union[
    PipelineDeclarationTypeDef, PipelineDeclarationOutputTypeDef
]
UpdatePipelineInputRequestTypeDef = TypedDict(
    "UpdatePipelineInputRequestTypeDef",
    {
        "pipeline": PipelineDeclarationTypeDef,
    },
)

GetPipelineStateOutputTypeDef = TypedDict(
    "GetPipelineStateOutputTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List[StageStateTypeDef],
        "created": datetime,
        "updated": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListActionExecutionsOutputTypeDef = TypedDict(
    "ListActionExecutionsOutputTypeDef",
    {
        "actionExecutionDetails": List[ActionExecutionDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "id": str,
        "data": JobDataTypeDef,
        "accountId": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "id": str,
        "data": JobDataTypeDef,
        "nonce": str,
        "accountId": str,
    },
    total=False,
)

ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {
        "id": str,
        "data": ThirdPartyJobDataTypeDef,
        "nonce": str,
    },
    total=False,
)

GetActionTypeOutputTypeDef = TypedDict(
    "GetActionTypeOutputTypeDef",
    {
        "actionType": ActionTypeDeclarationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ActionTypeDeclarationUnionTypeDef = Union[
    ActionTypeDeclarationTypeDef, ActionTypeDeclarationOutputTypeDef
]
UpdateActionTypeInputRequestTypeDef = TypedDict(
    "UpdateActionTypeInputRequestTypeDef",
    {
        "actionType": ActionTypeDeclarationTypeDef,
    },
)

GetJobDetailsOutputTypeDef = TypedDict(
    "GetJobDetailsOutputTypeDef",
    {
        "jobDetails": JobDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PollForJobsOutputTypeDef = TypedDict(
    "PollForJobsOutputTypeDef",
    {
        "jobs": List[JobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetThirdPartyJobDetailsOutputTypeDef = TypedDict(
    "GetThirdPartyJobDetailsOutputTypeDef",
    {
        "jobDetails": ThirdPartyJobDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
