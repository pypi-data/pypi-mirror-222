"""
Type annotations for backup service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs/)

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingOutputTypeDef

    data: AdvancedBackupSettingOutputTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    BackupJobStateType,
    BackupVaultEventType,
    CopyJobStateType,
    LegalHoldStatusType,
    RecoveryPointStatusType,
    RestoreJobStatusType,
    StorageClassType,
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
    "AdvancedBackupSettingOutputTypeDef",
    "AdvancedBackupSettingTypeDef",
    "RecoveryPointCreatorTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "LifecycleTypeDef",
    "ConditionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "CancelLegalHoldInputRequestTypeDef",
    "ConditionParameterTypeDef",
    "ControlInputParameterTypeDef",
    "ControlScopeOutputTypeDef",
    "ControlScopeTypeDef",
    "ResponseMetadataTypeDef",
    "CreateBackupVaultInputRequestTypeDef",
    "ReportDeliveryChannelTypeDef",
    "ReportSettingTypeDef",
    "DateRangeOutputTypeDef",
    "TimestampTypeDef",
    "DeleteBackupPlanInputRequestTypeDef",
    "DeleteBackupSelectionInputRequestTypeDef",
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    "DeleteBackupVaultInputRequestTypeDef",
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    "DeleteFrameworkInputRequestTypeDef",
    "DeleteRecoveryPointInputRequestTypeDef",
    "DeleteReportPlanInputRequestTypeDef",
    "DescribeBackupJobInputRequestTypeDef",
    "DescribeBackupVaultInputRequestTypeDef",
    "DescribeCopyJobInputRequestTypeDef",
    "DescribeFrameworkInputRequestTypeDef",
    "DescribeProtectedResourceInputRequestTypeDef",
    "DescribeRecoveryPointInputRequestTypeDef",
    "DescribeReportJobInputRequestTypeDef",
    "DescribeReportPlanInputRequestTypeDef",
    "DescribeRestoreJobInputRequestTypeDef",
    "DisassociateRecoveryPointFromParentInputRequestTypeDef",
    "DisassociateRecoveryPointInputRequestTypeDef",
    "ExportBackupPlanTemplateInputRequestTypeDef",
    "FrameworkTypeDef",
    "GetBackupPlanFromJSONInputRequestTypeDef",
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    "GetBackupPlanInputRequestTypeDef",
    "GetBackupSelectionInputRequestTypeDef",
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    "GetBackupVaultNotificationsInputRequestTypeDef",
    "GetLegalHoldInputRequestTypeDef",
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    "LegalHoldTypeDef",
    "PaginatorConfigTypeDef",
    "ListBackupPlanTemplatesInputRequestTypeDef",
    "ListBackupPlanVersionsInputRequestTypeDef",
    "ListBackupPlansInputRequestTypeDef",
    "ListBackupSelectionsInputRequestTypeDef",
    "ListBackupVaultsInputRequestTypeDef",
    "ListFrameworksInputRequestTypeDef",
    "ListLegalHoldsInputRequestTypeDef",
    "ListProtectedResourcesInputRequestTypeDef",
    "ProtectedResourceTypeDef",
    "ListRecoveryPointsByLegalHoldInputRequestTypeDef",
    "RecoveryPointMemberTypeDef",
    "ListRecoveryPointsByResourceInputRequestTypeDef",
    "RecoveryPointByResourceTypeDef",
    "ListReportPlansInputRequestTypeDef",
    "RestoreJobsListMemberTypeDef",
    "ListTagsInputRequestTypeDef",
    "PutBackupVaultAccessPolicyInputRequestTypeDef",
    "PutBackupVaultLockConfigurationInputRequestTypeDef",
    "PutBackupVaultNotificationsInputRequestTypeDef",
    "ReportDeliveryChannelOutputTypeDef",
    "ReportDestinationTypeDef",
    "ReportSettingOutputTypeDef",
    "StartReportJobInputRequestTypeDef",
    "StartRestoreJobInputRequestTypeDef",
    "StopBackupJobInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateRegionSettingsInputRequestTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupJobTypeDef",
    "CopyJobTypeDef",
    "CopyActionTypeDef",
    "StartBackupJobInputRequestTypeDef",
    "StartCopyJobInputRequestTypeDef",
    "UpdateRecoveryPointLifecycleInputRequestTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "ConditionsOutputTypeDef",
    "ConditionsTypeDef",
    "FrameworkControlOutputTypeDef",
    "FrameworkControlTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "CreateFrameworkOutputTypeDef",
    "CreateReportPlanOutputTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeGlobalSettingsOutputTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListTagsOutputTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartReportJobOutputTypeDef",
    "StartRestoreJobOutputTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateFrameworkOutputTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    "UpdateReportPlanOutputTypeDef",
    "CreateReportPlanInputRequestTypeDef",
    "UpdateReportPlanInputRequestTypeDef",
    "RecoveryPointSelectionOutputTypeDef",
    "DateRangeTypeDef",
    "ListBackupJobsInputRequestTypeDef",
    "ListCopyJobsInputRequestTypeDef",
    "ListRecoveryPointsByBackupVaultInputRequestTypeDef",
    "ListReportJobsInputRequestTypeDef",
    "ListRestoreJobsInputRequestTypeDef",
    "ListFrameworksOutputTypeDef",
    "ListLegalHoldsOutputTypeDef",
    "ListBackupJobsInputListBackupJobsPaginateTypeDef",
    "ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef",
    "ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef",
    "ListBackupPlansInputListBackupPlansPaginateTypeDef",
    "ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef",
    "ListBackupVaultsInputListBackupVaultsPaginateTypeDef",
    "ListCopyJobsInputListCopyJobsPaginateTypeDef",
    "ListLegalHoldsInputListLegalHoldsPaginateTypeDef",
    "ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef",
    "ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef",
    "ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef",
    "ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef",
    "ListRestoreJobsInputListRestoreJobsPaginateTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "ReportDeliveryChannelUnionTypeDef",
    "ReportJobTypeDef",
    "ReportPlanTypeDef",
    "ReportSettingUnionTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupJobsOutputTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "ListCopyJobsOutputTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "BackupSelectionOutputTypeDef",
    "BackupSelectionTypeDef",
    "DescribeFrameworkOutputTypeDef",
    "FrameworkControlUnionTypeDef",
    "CreateLegalHoldOutputTypeDef",
    "GetLegalHoldOutputTypeDef",
    "RecoveryPointSelectionTypeDef",
    "DescribeReportJobOutputTypeDef",
    "ListReportJobsOutputTypeDef",
    "DescribeReportPlanOutputTypeDef",
    "ListReportPlansOutputTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "BackupSelectionUnionTypeDef",
    "CreateBackupSelectionInputRequestTypeDef",
    "CreateFrameworkInputRequestTypeDef",
    "UpdateFrameworkInputRequestTypeDef",
    "CreateLegalHoldInputRequestTypeDef",
    "RecoveryPointSelectionUnionTypeDef",
    "CreateBackupPlanInputRequestTypeDef",
    "UpdateBackupPlanInputRequestTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanOutputTypeDef",
)

AdvancedBackupSettingOutputTypeDef = TypedDict(
    "AdvancedBackupSettingOutputTypeDef",
    {
        "ResourceType": str,
        "BackupOptions": Dict[str, str],
    },
    total=False,
)

AdvancedBackupSettingTypeDef = TypedDict(
    "AdvancedBackupSettingTypeDef",
    {
        "ResourceType": str,
        "BackupOptions": Mapping[str, str],
    },
    total=False,
)

RecoveryPointCreatorTypeDef = TypedDict(
    "RecoveryPointCreatorTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)

BackupPlanTemplatesListMemberTypeDef = TypedDict(
    "BackupPlanTemplatesListMemberTypeDef",
    {
        "BackupPlanTemplateId": str,
        "BackupPlanTemplateName": str,
    },
    total=False,
)

LifecycleTypeDef = TypedDict(
    "LifecycleTypeDef",
    {
        "MoveToColdStorageAfterDays": int,
        "DeleteAfterDays": int,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ConditionType": Literal["STRINGEQUALS"],
        "ConditionKey": str,
        "ConditionValue": str,
    },
)

BackupSelectionsListMemberTypeDef = TypedDict(
    "BackupSelectionsListMemberTypeDef",
    {
        "SelectionId": str,
        "SelectionName": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "IamRoleArn": str,
    },
    total=False,
)

BackupVaultListMemberTypeDef = TypedDict(
    "BackupVaultListMemberTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
        "Locked": bool,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "LockDate": datetime,
    },
    total=False,
)

CalculatedLifecycleTypeDef = TypedDict(
    "CalculatedLifecycleTypeDef",
    {
        "MoveToColdStorageAt": datetime,
        "DeleteAt": datetime,
    },
    total=False,
)

_RequiredCancelLegalHoldInputRequestTypeDef = TypedDict(
    "_RequiredCancelLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
        "CancelDescription": str,
    },
)
_OptionalCancelLegalHoldInputRequestTypeDef = TypedDict(
    "_OptionalCancelLegalHoldInputRequestTypeDef",
    {
        "RetainRecordInDays": int,
    },
    total=False,
)

class CancelLegalHoldInputRequestTypeDef(
    _RequiredCancelLegalHoldInputRequestTypeDef, _OptionalCancelLegalHoldInputRequestTypeDef
):
    pass

ConditionParameterTypeDef = TypedDict(
    "ConditionParameterTypeDef",
    {
        "ConditionKey": str,
        "ConditionValue": str,
    },
    total=False,
)

ControlInputParameterTypeDef = TypedDict(
    "ControlInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
    total=False,
)

ControlScopeOutputTypeDef = TypedDict(
    "ControlScopeOutputTypeDef",
    {
        "ComplianceResourceIds": List[str],
        "ComplianceResourceTypes": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ControlScopeTypeDef = TypedDict(
    "ControlScopeTypeDef",
    {
        "ComplianceResourceIds": Sequence[str],
        "ComplianceResourceTypes": Sequence[str],
        "Tags": Mapping[str, str],
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

_RequiredCreateBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredCreateBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalCreateBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalCreateBackupVaultInputRequestTypeDef",
    {
        "BackupVaultTags": Mapping[str, str],
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateBackupVaultInputRequestTypeDef(
    _RequiredCreateBackupVaultInputRequestTypeDef, _OptionalCreateBackupVaultInputRequestTypeDef
):
    pass

_RequiredReportDeliveryChannelTypeDef = TypedDict(
    "_RequiredReportDeliveryChannelTypeDef",
    {
        "S3BucketName": str,
    },
)
_OptionalReportDeliveryChannelTypeDef = TypedDict(
    "_OptionalReportDeliveryChannelTypeDef",
    {
        "S3KeyPrefix": str,
        "Formats": Sequence[str],
    },
    total=False,
)

class ReportDeliveryChannelTypeDef(
    _RequiredReportDeliveryChannelTypeDef, _OptionalReportDeliveryChannelTypeDef
):
    pass

_RequiredReportSettingTypeDef = TypedDict(
    "_RequiredReportSettingTypeDef",
    {
        "ReportTemplate": str,
    },
)
_OptionalReportSettingTypeDef = TypedDict(
    "_OptionalReportSettingTypeDef",
    {
        "FrameworkArns": Sequence[str],
        "NumberOfFrameworks": int,
        "Accounts": Sequence[str],
        "OrganizationUnits": Sequence[str],
        "Regions": Sequence[str],
    },
    total=False,
)

class ReportSettingTypeDef(_RequiredReportSettingTypeDef, _OptionalReportSettingTypeDef):
    pass

DateRangeOutputTypeDef = TypedDict(
    "DateRangeOutputTypeDef",
    {
        "FromDate": datetime,
        "ToDate": datetime,
    },
)

TimestampTypeDef = Union[datetime, str]
DeleteBackupPlanInputRequestTypeDef = TypedDict(
    "DeleteBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)

DeleteBackupSelectionInputRequestTypeDef = TypedDict(
    "DeleteBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

DeleteBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteFrameworkInputRequestTypeDef = TypedDict(
    "DeleteFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)

DeleteRecoveryPointInputRequestTypeDef = TypedDict(
    "DeleteRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DeleteReportPlanInputRequestTypeDef = TypedDict(
    "DeleteReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)

DescribeBackupJobInputRequestTypeDef = TypedDict(
    "DescribeBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
)

DescribeBackupVaultInputRequestTypeDef = TypedDict(
    "DescribeBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

DescribeCopyJobInputRequestTypeDef = TypedDict(
    "DescribeCopyJobInputRequestTypeDef",
    {
        "CopyJobId": str,
    },
)

DescribeFrameworkInputRequestTypeDef = TypedDict(
    "DescribeFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)

DescribeProtectedResourceInputRequestTypeDef = TypedDict(
    "DescribeProtectedResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeRecoveryPointInputRequestTypeDef = TypedDict(
    "DescribeRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DescribeReportJobInputRequestTypeDef = TypedDict(
    "DescribeReportJobInputRequestTypeDef",
    {
        "ReportJobId": str,
    },
)

DescribeReportPlanInputRequestTypeDef = TypedDict(
    "DescribeReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)

DescribeRestoreJobInputRequestTypeDef = TypedDict(
    "DescribeRestoreJobInputRequestTypeDef",
    {
        "RestoreJobId": str,
    },
)

DisassociateRecoveryPointFromParentInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointFromParentInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DisassociateRecoveryPointInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

ExportBackupPlanTemplateInputRequestTypeDef = TypedDict(
    "ExportBackupPlanTemplateInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "FrameworkDescription": str,
        "NumberOfControls": int,
        "CreationTime": datetime,
        "DeploymentStatus": str,
    },
    total=False,
)

GetBackupPlanFromJSONInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromJSONInputRequestTypeDef",
    {
        "BackupPlanTemplateJson": str,
    },
)

GetBackupPlanFromTemplateInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    {
        "BackupPlanTemplateId": str,
    },
)

_RequiredGetBackupPlanInputRequestTypeDef = TypedDict(
    "_RequiredGetBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalGetBackupPlanInputRequestTypeDef = TypedDict(
    "_OptionalGetBackupPlanInputRequestTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)

class GetBackupPlanInputRequestTypeDef(
    _RequiredGetBackupPlanInputRequestTypeDef, _OptionalGetBackupPlanInputRequestTypeDef
):
    pass

GetBackupSelectionInputRequestTypeDef = TypedDict(
    "GetBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

GetBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetLegalHoldInputRequestTypeDef = TypedDict(
    "GetLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
    },
)

GetRecoveryPointRestoreMetadataInputRequestTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

LegalHoldTypeDef = TypedDict(
    "LegalHoldTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "CancellationDate": datetime,
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

ListBackupPlanTemplatesInputRequestTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListBackupPlanVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListBackupPlanVersionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupPlanVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListBackupPlanVersionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListBackupPlanVersionsInputRequestTypeDef(
    _RequiredListBackupPlanVersionsInputRequestTypeDef,
    _OptionalListBackupPlanVersionsInputRequestTypeDef,
):
    pass

ListBackupPlansInputRequestTypeDef = TypedDict(
    "ListBackupPlansInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncludeDeleted": bool,
    },
    total=False,
)

_RequiredListBackupSelectionsInputRequestTypeDef = TypedDict(
    "_RequiredListBackupSelectionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupSelectionsInputRequestTypeDef = TypedDict(
    "_OptionalListBackupSelectionsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListBackupSelectionsInputRequestTypeDef(
    _RequiredListBackupSelectionsInputRequestTypeDef,
    _OptionalListBackupSelectionsInputRequestTypeDef,
):
    pass

ListBackupVaultsInputRequestTypeDef = TypedDict(
    "ListBackupVaultsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFrameworksInputRequestTypeDef = TypedDict(
    "ListFrameworksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLegalHoldsInputRequestTypeDef = TypedDict(
    "ListLegalHoldsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectedResourcesInputRequestTypeDef = TypedDict(
    "ListProtectedResourcesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ProtectedResourceTypeDef = TypedDict(
    "ProtectedResourceTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResourceName": str,
    },
    total=False,
)

_RequiredListRecoveryPointsByLegalHoldInputRequestTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
    },
)
_OptionalListRecoveryPointsByLegalHoldInputRequestTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByLegalHoldInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRecoveryPointsByLegalHoldInputRequestTypeDef(
    _RequiredListRecoveryPointsByLegalHoldInputRequestTypeDef,
    _OptionalListRecoveryPointsByLegalHoldInputRequestTypeDef,
):
    pass

RecoveryPointMemberTypeDef = TypedDict(
    "RecoveryPointMemberTypeDef",
    {
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "BackupVaultName": str,
    },
    total=False,
)

_RequiredListRecoveryPointsByResourceInputRequestTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListRecoveryPointsByResourceInputRequestTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByResourceInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRecoveryPointsByResourceInputRequestTypeDef(
    _RequiredListRecoveryPointsByResourceInputRequestTypeDef,
    _OptionalListRecoveryPointsByResourceInputRequestTypeDef,
):
    pass

RecoveryPointByResourceTypeDef = TypedDict(
    "RecoveryPointByResourceTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
        "IsParent": bool,
        "ParentRecoveryPointArn": str,
        "ResourceName": str,
    },
    total=False,
)

ListReportPlansInputRequestTypeDef = TypedDict(
    "ListReportPlansInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

RestoreJobsListMemberTypeDef = TypedDict(
    "RestoreJobsListMemberTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
    },
    total=False,
)

_RequiredListTagsInputRequestTypeDef = TypedDict(
    "_RequiredListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputRequestTypeDef = TypedDict(
    "_OptionalListTagsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsInputRequestTypeDef(
    _RequiredListTagsInputRequestTypeDef, _OptionalListTagsInputRequestTypeDef
):
    pass

_RequiredPutBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "_RequiredPutBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalPutBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "_OptionalPutBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

class PutBackupVaultAccessPolicyInputRequestTypeDef(
    _RequiredPutBackupVaultAccessPolicyInputRequestTypeDef,
    _OptionalPutBackupVaultAccessPolicyInputRequestTypeDef,
):
    pass

_RequiredPutBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredPutBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalPutBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalPutBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "ChangeableForDays": int,
    },
    total=False,
)

class PutBackupVaultLockConfigurationInputRequestTypeDef(
    _RequiredPutBackupVaultLockConfigurationInputRequestTypeDef,
    _OptionalPutBackupVaultLockConfigurationInputRequestTypeDef,
):
    pass

PutBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "PutBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": Sequence[BackupVaultEventType],
    },
)

_RequiredReportDeliveryChannelOutputTypeDef = TypedDict(
    "_RequiredReportDeliveryChannelOutputTypeDef",
    {
        "S3BucketName": str,
    },
)
_OptionalReportDeliveryChannelOutputTypeDef = TypedDict(
    "_OptionalReportDeliveryChannelOutputTypeDef",
    {
        "S3KeyPrefix": str,
        "Formats": List[str],
    },
    total=False,
)

class ReportDeliveryChannelOutputTypeDef(
    _RequiredReportDeliveryChannelOutputTypeDef, _OptionalReportDeliveryChannelOutputTypeDef
):
    pass

ReportDestinationTypeDef = TypedDict(
    "ReportDestinationTypeDef",
    {
        "S3BucketName": str,
        "S3Keys": List[str],
    },
    total=False,
)

_RequiredReportSettingOutputTypeDef = TypedDict(
    "_RequiredReportSettingOutputTypeDef",
    {
        "ReportTemplate": str,
    },
)
_OptionalReportSettingOutputTypeDef = TypedDict(
    "_OptionalReportSettingOutputTypeDef",
    {
        "FrameworkArns": List[str],
        "NumberOfFrameworks": int,
        "Accounts": List[str],
        "OrganizationUnits": List[str],
        "Regions": List[str],
    },
    total=False,
)

class ReportSettingOutputTypeDef(
    _RequiredReportSettingOutputTypeDef, _OptionalReportSettingOutputTypeDef
):
    pass

_RequiredStartReportJobInputRequestTypeDef = TypedDict(
    "_RequiredStartReportJobInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)
_OptionalStartReportJobInputRequestTypeDef = TypedDict(
    "_OptionalStartReportJobInputRequestTypeDef",
    {
        "IdempotencyToken": str,
    },
    total=False,
)

class StartReportJobInputRequestTypeDef(
    _RequiredStartReportJobInputRequestTypeDef, _OptionalStartReportJobInputRequestTypeDef
):
    pass

_RequiredStartRestoreJobInputRequestTypeDef = TypedDict(
    "_RequiredStartRestoreJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "Metadata": Mapping[str, str],
    },
)
_OptionalStartRestoreJobInputRequestTypeDef = TypedDict(
    "_OptionalStartRestoreJobInputRequestTypeDef",
    {
        "IamRoleArn": str,
        "IdempotencyToken": str,
        "ResourceType": str,
        "CopySourceTagsToRestoredResource": bool,
    },
    total=False,
)

class StartRestoreJobInputRequestTypeDef(
    _RequiredStartRestoreJobInputRequestTypeDef, _OptionalStartRestoreJobInputRequestTypeDef
):
    pass

StopBackupJobInputRequestTypeDef = TypedDict(
    "StopBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": Sequence[str],
    },
)

UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "GlobalSettings": Mapping[str, str],
    },
    total=False,
)

UpdateRegionSettingsInputRequestTypeDef = TypedDict(
    "UpdateRegionSettingsInputRequestTypeDef",
    {
        "ResourceTypeOptInPreference": Mapping[str, bool],
        "ResourceTypeManagementPreference": Mapping[str, bool],
    },
    total=False,
)

BackupPlansListMemberTypeDef = TypedDict(
    "BackupPlansListMemberTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
    },
    total=False,
)

BackupJobTypeDef = TypedDict(
    "BackupJobTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "ResourceName": str,
    },
    total=False,
)

CopyJobTypeDef = TypedDict(
    "CopyJobTypeDef",
    {
        "AccountId": str,
        "CopyJobId": str,
        "SourceBackupVaultArn": str,
        "SourceRecoveryPointArn": str,
        "DestinationBackupVaultArn": str,
        "DestinationRecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": CopyJobStateType,
        "StatusMessage": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "ResourceType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "CompositeMemberIdentifier": str,
        "NumberOfChildJobs": int,
        "ChildJobsInState": Dict[CopyJobStateType, int],
        "ResourceName": str,
    },
    total=False,
)

_RequiredCopyActionTypeDef = TypedDict(
    "_RequiredCopyActionTypeDef",
    {
        "DestinationBackupVaultArn": str,
    },
)
_OptionalCopyActionTypeDef = TypedDict(
    "_OptionalCopyActionTypeDef",
    {
        "Lifecycle": LifecycleTypeDef,
    },
    total=False,
)

class CopyActionTypeDef(_RequiredCopyActionTypeDef, _OptionalCopyActionTypeDef):
    pass

_RequiredStartBackupJobInputRequestTypeDef = TypedDict(
    "_RequiredStartBackupJobInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "ResourceArn": str,
        "IamRoleArn": str,
    },
)
_OptionalStartBackupJobInputRequestTypeDef = TypedDict(
    "_OptionalStartBackupJobInputRequestTypeDef",
    {
        "IdempotencyToken": str,
        "StartWindowMinutes": int,
        "CompleteWindowMinutes": int,
        "Lifecycle": LifecycleTypeDef,
        "RecoveryPointTags": Mapping[str, str],
        "BackupOptions": Mapping[str, str],
    },
    total=False,
)

class StartBackupJobInputRequestTypeDef(
    _RequiredStartBackupJobInputRequestTypeDef, _OptionalStartBackupJobInputRequestTypeDef
):
    pass

_RequiredStartCopyJobInputRequestTypeDef = TypedDict(
    "_RequiredStartCopyJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "SourceBackupVaultName": str,
        "DestinationBackupVaultArn": str,
        "IamRoleArn": str,
    },
)
_OptionalStartCopyJobInputRequestTypeDef = TypedDict(
    "_OptionalStartCopyJobInputRequestTypeDef",
    {
        "IdempotencyToken": str,
        "Lifecycle": LifecycleTypeDef,
    },
    total=False,
)

class StartCopyJobInputRequestTypeDef(
    _RequiredStartCopyJobInputRequestTypeDef, _OptionalStartCopyJobInputRequestTypeDef
):
    pass

_RequiredUpdateRecoveryPointLifecycleInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRecoveryPointLifecycleInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
_OptionalUpdateRecoveryPointLifecycleInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRecoveryPointLifecycleInputRequestTypeDef",
    {
        "Lifecycle": LifecycleTypeDef,
    },
    total=False,
)

class UpdateRecoveryPointLifecycleInputRequestTypeDef(
    _RequiredUpdateRecoveryPointLifecycleInputRequestTypeDef,
    _OptionalUpdateRecoveryPointLifecycleInputRequestTypeDef,
):
    pass

RecoveryPointByBackupVaultTypeDef = TypedDict(
    "RecoveryPointByBackupVaultTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": CalculatedLifecycleTypeDef,
        "Lifecycle": LifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
        "ParentRecoveryPointArn": str,
        "CompositeMemberIdentifier": str,
        "IsParent": bool,
        "ResourceName": str,
    },
    total=False,
)

ConditionsOutputTypeDef = TypedDict(
    "ConditionsOutputTypeDef",
    {
        "StringEquals": List[ConditionParameterTypeDef],
        "StringNotEquals": List[ConditionParameterTypeDef],
        "StringLike": List[ConditionParameterTypeDef],
        "StringNotLike": List[ConditionParameterTypeDef],
    },
    total=False,
)

ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "StringEquals": Sequence[ConditionParameterTypeDef],
        "StringNotEquals": Sequence[ConditionParameterTypeDef],
        "StringLike": Sequence[ConditionParameterTypeDef],
        "StringNotLike": Sequence[ConditionParameterTypeDef],
    },
    total=False,
)

_RequiredFrameworkControlOutputTypeDef = TypedDict(
    "_RequiredFrameworkControlOutputTypeDef",
    {
        "ControlName": str,
    },
)
_OptionalFrameworkControlOutputTypeDef = TypedDict(
    "_OptionalFrameworkControlOutputTypeDef",
    {
        "ControlInputParameters": List[ControlInputParameterTypeDef],
        "ControlScope": ControlScopeOutputTypeDef,
    },
    total=False,
)

class FrameworkControlOutputTypeDef(
    _RequiredFrameworkControlOutputTypeDef, _OptionalFrameworkControlOutputTypeDef
):
    pass

_RequiredFrameworkControlTypeDef = TypedDict(
    "_RequiredFrameworkControlTypeDef",
    {
        "ControlName": str,
    },
)
_OptionalFrameworkControlTypeDef = TypedDict(
    "_OptionalFrameworkControlTypeDef",
    {
        "ControlInputParameters": Sequence[ControlInputParameterTypeDef],
        "ControlScope": ControlScopeTypeDef,
    },
    total=False,
)

class FrameworkControlTypeDef(_RequiredFrameworkControlTypeDef, _OptionalFrameworkControlTypeDef):
    pass

CreateBackupPlanOutputTypeDef = TypedDict(
    "CreateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateBackupSelectionOutputTypeDef = TypedDict(
    "CreateBackupSelectionOutputTypeDef",
    {
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateBackupVaultOutputTypeDef = TypedDict(
    "CreateBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFrameworkOutputTypeDef = TypedDict(
    "CreateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateReportPlanOutputTypeDef = TypedDict(
    "CreateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteBackupPlanOutputTypeDef = TypedDict(
    "DeleteBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "DeletionDate": datetime,
        "VersionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeBackupJobOutputTypeDef = TypedDict(
    "DescribeBackupJobOutputTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "NumberOfChildJobs": int,
        "ChildJobsInState": Dict[BackupJobStateType, int],
        "ResourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeBackupVaultOutputTypeDef = TypedDict(
    "DescribeBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
        "Locked": bool,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "LockDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeGlobalSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalSettingsOutputTypeDef",
    {
        "GlobalSettings": Dict[str, str],
        "LastUpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeProtectedResourceOutputTypeDef = TypedDict(
    "DescribeProtectedResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeRecoveryPointOutputTypeDef = TypedDict(
    "DescribeRecoveryPointOutputTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": CalculatedLifecycleTypeDef,
        "Lifecycle": LifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": StorageClassType,
        "LastRestoreTime": datetime,
        "ParentRecoveryPointArn": str,
        "CompositeMemberIdentifier": str,
        "IsParent": bool,
        "ResourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeRegionSettingsOutputTypeDef = TypedDict(
    "DescribeRegionSettingsOutputTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
        "ResourceTypeManagementPreference": Dict[str, bool],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeRestoreJobOutputTypeDef = TypedDict(
    "DescribeRestoreJobOutputTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExportBackupPlanTemplateOutputTypeDef = TypedDict(
    "ExportBackupPlanTemplateOutputTypeDef",
    {
        "BackupPlanTemplateJson": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBackupVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBackupVaultNotificationsOutputTypeDef = TypedDict(
    "GetBackupVaultNotificationsOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRecoveryPointRestoreMetadataOutputTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "RestoreMetadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSupportedResourceTypesOutputTypeDef = TypedDict(
    "GetSupportedResourceTypesOutputTypeDef",
    {
        "ResourceTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupPlanTemplatesOutputTypeDef = TypedDict(
    "ListBackupPlanTemplatesOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List[BackupPlanTemplatesListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupSelectionsOutputTypeDef = TypedDict(
    "ListBackupSelectionsOutputTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List[BackupSelectionsListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupVaultsOutputTypeDef = TypedDict(
    "ListBackupVaultsOutputTypeDef",
    {
        "BackupVaultList": List[BackupVaultListMemberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartBackupJobOutputTypeDef = TypedDict(
    "StartBackupJobOutputTypeDef",
    {
        "BackupJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "IsParent": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartCopyJobOutputTypeDef = TypedDict(
    "StartCopyJobOutputTypeDef",
    {
        "CopyJobId": str,
        "CreationDate": datetime,
        "IsParent": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartReportJobOutputTypeDef = TypedDict(
    "StartReportJobOutputTypeDef",
    {
        "ReportJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartRestoreJobOutputTypeDef = TypedDict(
    "StartRestoreJobOutputTypeDef",
    {
        "RestoreJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateBackupPlanOutputTypeDef = TypedDict(
    "UpdateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFrameworkOutputTypeDef = TypedDict(
    "UpdateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRecoveryPointLifecycleOutputTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": LifecycleTypeDef,
        "CalculatedLifecycle": CalculatedLifecycleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateReportPlanOutputTypeDef = TypedDict(
    "UpdateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateReportPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "ReportDeliveryChannel": ReportDeliveryChannelTypeDef,
        "ReportSetting": ReportSettingTypeDef,
    },
)
_OptionalCreateReportPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateReportPlanInputRequestTypeDef",
    {
        "ReportPlanDescription": str,
        "ReportPlanTags": Mapping[str, str],
        "IdempotencyToken": str,
    },
    total=False,
)

class CreateReportPlanInputRequestTypeDef(
    _RequiredCreateReportPlanInputRequestTypeDef, _OptionalCreateReportPlanInputRequestTypeDef
):
    pass

_RequiredUpdateReportPlanInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)
_OptionalUpdateReportPlanInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReportPlanInputRequestTypeDef",
    {
        "ReportPlanDescription": str,
        "ReportDeliveryChannel": ReportDeliveryChannelTypeDef,
        "ReportSetting": ReportSettingTypeDef,
        "IdempotencyToken": str,
    },
    total=False,
)

class UpdateReportPlanInputRequestTypeDef(
    _RequiredUpdateReportPlanInputRequestTypeDef, _OptionalUpdateReportPlanInputRequestTypeDef
):
    pass

RecoveryPointSelectionOutputTypeDef = TypedDict(
    "RecoveryPointSelectionOutputTypeDef",
    {
        "VaultNames": List[str],
        "ResourceIdentifiers": List[str],
        "DateRange": DateRangeOutputTypeDef,
    },
    total=False,
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "FromDate": TimestampTypeDef,
        "ToDate": TimestampTypeDef,
    },
)

ListBackupJobsInputRequestTypeDef = TypedDict(
    "ListBackupJobsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByState": BackupJobStateType,
        "ByBackupVaultName": str,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByResourceType": str,
        "ByAccountId": str,
        "ByCompleteAfter": TimestampTypeDef,
        "ByCompleteBefore": TimestampTypeDef,
        "ByParentJobId": str,
    },
    total=False,
)

ListCopyJobsInputRequestTypeDef = TypedDict(
    "ListCopyJobsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByState": CopyJobStateType,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByResourceType": str,
        "ByDestinationVaultArn": str,
        "ByAccountId": str,
        "ByCompleteBefore": TimestampTypeDef,
        "ByCompleteAfter": TimestampTypeDef,
        "ByParentJobId": str,
    },
    total=False,
)

_RequiredListRecoveryPointsByBackupVaultInputRequestTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalListRecoveryPointsByBackupVaultInputRequestTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByBackupVaultInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByResourceType": str,
        "ByBackupPlanId": str,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByParentRecoveryPointArn": str,
    },
    total=False,
)

class ListRecoveryPointsByBackupVaultInputRequestTypeDef(
    _RequiredListRecoveryPointsByBackupVaultInputRequestTypeDef,
    _OptionalListRecoveryPointsByBackupVaultInputRequestTypeDef,
):
    pass

ListReportJobsInputRequestTypeDef = TypedDict(
    "ListReportJobsInputRequestTypeDef",
    {
        "ByReportPlanName": str,
        "ByCreationBefore": TimestampTypeDef,
        "ByCreationAfter": TimestampTypeDef,
        "ByStatus": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRestoreJobsInputRequestTypeDef = TypedDict(
    "ListRestoreJobsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByAccountId": str,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByStatus": RestoreJobStatusType,
        "ByCompleteBefore": TimestampTypeDef,
        "ByCompleteAfter": TimestampTypeDef,
    },
    total=False,
)

ListFrameworksOutputTypeDef = TypedDict(
    "ListFrameworksOutputTypeDef",
    {
        "Frameworks": List[FrameworkTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLegalHoldsOutputTypeDef = TypedDict(
    "ListLegalHoldsOutputTypeDef",
    {
        "NextToken": str,
        "LegalHolds": List[LegalHoldTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupJobsInputListBackupJobsPaginateTypeDef = TypedDict(
    "ListBackupJobsInputListBackupJobsPaginateTypeDef",
    {
        "ByResourceArn": str,
        "ByState": BackupJobStateType,
        "ByBackupVaultName": str,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByResourceType": str,
        "ByAccountId": str,
        "ByCompleteAfter": TimestampTypeDef,
        "ByCompleteBefore": TimestampTypeDef,
        "ByParentJobId": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef = TypedDict(
    "_RequiredListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef = TypedDict(
    "_OptionalListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef(
    _RequiredListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef,
    _OptionalListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef,
):
    pass

ListBackupPlansInputListBackupPlansPaginateTypeDef = TypedDict(
    "ListBackupPlansInputListBackupPlansPaginateTypeDef",
    {
        "IncludeDeleted": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListBackupSelectionsInputListBackupSelectionsPaginateTypeDef = TypedDict(
    "_RequiredListBackupSelectionsInputListBackupSelectionsPaginateTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupSelectionsInputListBackupSelectionsPaginateTypeDef = TypedDict(
    "_OptionalListBackupSelectionsInputListBackupSelectionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef(
    _RequiredListBackupSelectionsInputListBackupSelectionsPaginateTypeDef,
    _OptionalListBackupSelectionsInputListBackupSelectionsPaginateTypeDef,
):
    pass

ListBackupVaultsInputListBackupVaultsPaginateTypeDef = TypedDict(
    "ListBackupVaultsInputListBackupVaultsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListCopyJobsInputListCopyJobsPaginateTypeDef = TypedDict(
    "ListCopyJobsInputListCopyJobsPaginateTypeDef",
    {
        "ByResourceArn": str,
        "ByState": CopyJobStateType,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByResourceType": str,
        "ByDestinationVaultArn": str,
        "ByAccountId": str,
        "ByCompleteBefore": TimestampTypeDef,
        "ByCompleteAfter": TimestampTypeDef,
        "ByParentJobId": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListLegalHoldsInputListLegalHoldsPaginateTypeDef = TypedDict(
    "ListLegalHoldsInputListLegalHoldsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef = TypedDict(
    "ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef",
    {
        "ByResourceArn": str,
        "ByResourceType": str,
        "ByBackupPlanId": str,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByParentRecoveryPointArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef(
    _RequiredListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef,
    _OptionalListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef,
):
    pass

_RequiredListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef",
    {
        "LegalHoldId": str,
    },
)
_OptionalListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef(
    _RequiredListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef,
    _OptionalListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef,
):
    pass

_RequiredListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef(
    _RequiredListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef,
    _OptionalListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef,
):
    pass

ListRestoreJobsInputListRestoreJobsPaginateTypeDef = TypedDict(
    "ListRestoreJobsInputListRestoreJobsPaginateTypeDef",
    {
        "ByAccountId": str,
        "ByCreatedBefore": TimestampTypeDef,
        "ByCreatedAfter": TimestampTypeDef,
        "ByStatus": RestoreJobStatusType,
        "ByCompleteBefore": TimestampTypeDef,
        "ByCompleteAfter": TimestampTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListProtectedResourcesOutputTypeDef = TypedDict(
    "ListProtectedResourcesOutputTypeDef",
    {
        "Results": List[ProtectedResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRecoveryPointsByLegalHoldOutputTypeDef = TypedDict(
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    {
        "RecoveryPoints": List[RecoveryPointMemberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRecoveryPointsByResourceOutputTypeDef = TypedDict(
    "ListRecoveryPointsByResourceOutputTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[RecoveryPointByResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRestoreJobsOutputTypeDef = TypedDict(
    "ListRestoreJobsOutputTypeDef",
    {
        "RestoreJobs": List[RestoreJobsListMemberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ReportDeliveryChannelUnionTypeDef = Union[
    ReportDeliveryChannelTypeDef, ReportDeliveryChannelOutputTypeDef
]
ReportJobTypeDef = TypedDict(
    "ReportJobTypeDef",
    {
        "ReportJobId": str,
        "ReportPlanArn": str,
        "ReportTemplate": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "Status": str,
        "StatusMessage": str,
        "ReportDestination": ReportDestinationTypeDef,
    },
    total=False,
)

ReportPlanTypeDef = TypedDict(
    "ReportPlanTypeDef",
    {
        "ReportPlanArn": str,
        "ReportPlanName": str,
        "ReportPlanDescription": str,
        "ReportSetting": ReportSettingOutputTypeDef,
        "ReportDeliveryChannel": ReportDeliveryChannelOutputTypeDef,
        "DeploymentStatus": str,
        "CreationTime": datetime,
        "LastAttemptedExecutionTime": datetime,
        "LastSuccessfulExecutionTime": datetime,
    },
    total=False,
)

ReportSettingUnionTypeDef = Union[ReportSettingTypeDef, ReportSettingOutputTypeDef]
ListBackupPlanVersionsOutputTypeDef = TypedDict(
    "ListBackupPlanVersionsOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List[BackupPlansListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupPlansOutputTypeDef = TypedDict(
    "ListBackupPlansOutputTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List[BackupPlansListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBackupJobsOutputTypeDef = TypedDict(
    "ListBackupJobsOutputTypeDef",
    {
        "BackupJobs": List[BackupJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeCopyJobOutputTypeDef = TypedDict(
    "DescribeCopyJobOutputTypeDef",
    {
        "CopyJob": CopyJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCopyJobsOutputTypeDef = TypedDict(
    "ListCopyJobsOutputTypeDef",
    {
        "CopyJobs": List[CopyJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBackupRuleInputTypeDef = TypedDict(
    "_RequiredBackupRuleInputTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
    },
)
_OptionalBackupRuleInputTypeDef = TypedDict(
    "_OptionalBackupRuleInputTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": LifecycleTypeDef,
        "RecoveryPointTags": Mapping[str, str],
        "CopyActions": Sequence[CopyActionTypeDef],
        "EnableContinuousBackup": bool,
    },
    total=False,
)

class BackupRuleInputTypeDef(_RequiredBackupRuleInputTypeDef, _OptionalBackupRuleInputTypeDef):
    pass

_RequiredBackupRuleTypeDef = TypedDict(
    "_RequiredBackupRuleTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
    },
)
_OptionalBackupRuleTypeDef = TypedDict(
    "_OptionalBackupRuleTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": LifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
        "CopyActions": List[CopyActionTypeDef],
        "EnableContinuousBackup": bool,
    },
    total=False,
)

class BackupRuleTypeDef(_RequiredBackupRuleTypeDef, _OptionalBackupRuleTypeDef):
    pass

ListRecoveryPointsByBackupVaultOutputTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[RecoveryPointByBackupVaultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBackupSelectionOutputTypeDef = TypedDict(
    "_RequiredBackupSelectionOutputTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
    },
)
_OptionalBackupSelectionOutputTypeDef = TypedDict(
    "_OptionalBackupSelectionOutputTypeDef",
    {
        "Resources": List[str],
        "ListOfTags": List[ConditionTypeDef],
        "NotResources": List[str],
        "Conditions": ConditionsOutputTypeDef,
    },
    total=False,
)

class BackupSelectionOutputTypeDef(
    _RequiredBackupSelectionOutputTypeDef, _OptionalBackupSelectionOutputTypeDef
):
    pass

_RequiredBackupSelectionTypeDef = TypedDict(
    "_RequiredBackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
    },
)
_OptionalBackupSelectionTypeDef = TypedDict(
    "_OptionalBackupSelectionTypeDef",
    {
        "Resources": Sequence[str],
        "ListOfTags": Sequence[ConditionTypeDef],
        "NotResources": Sequence[str],
        "Conditions": ConditionsTypeDef,
    },
    total=False,
)

class BackupSelectionTypeDef(_RequiredBackupSelectionTypeDef, _OptionalBackupSelectionTypeDef):
    pass

DescribeFrameworkOutputTypeDef = TypedDict(
    "DescribeFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "FrameworkDescription": str,
        "FrameworkControls": List[FrameworkControlOutputTypeDef],
        "CreationTime": datetime,
        "DeploymentStatus": str,
        "FrameworkStatus": str,
        "IdempotencyToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FrameworkControlUnionTypeDef = Union[FrameworkControlTypeDef, FrameworkControlOutputTypeDef]
CreateLegalHoldOutputTypeDef = TypedDict(
    "CreateLegalHoldOutputTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "RecoveryPointSelection": RecoveryPointSelectionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLegalHoldOutputTypeDef = TypedDict(
    "GetLegalHoldOutputTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "CancelDescription": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "CancellationDate": datetime,
        "RetainRecordUntil": datetime,
        "RecoveryPointSelection": RecoveryPointSelectionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RecoveryPointSelectionTypeDef = TypedDict(
    "RecoveryPointSelectionTypeDef",
    {
        "VaultNames": Sequence[str],
        "ResourceIdentifiers": Sequence[str],
        "DateRange": DateRangeTypeDef,
    },
    total=False,
)

DescribeReportJobOutputTypeDef = TypedDict(
    "DescribeReportJobOutputTypeDef",
    {
        "ReportJob": ReportJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListReportJobsOutputTypeDef = TypedDict(
    "ListReportJobsOutputTypeDef",
    {
        "ReportJobs": List[ReportJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeReportPlanOutputTypeDef = TypedDict(
    "DescribeReportPlanOutputTypeDef",
    {
        "ReportPlan": ReportPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListReportPlansOutputTypeDef = TypedDict(
    "ListReportPlansOutputTypeDef",
    {
        "ReportPlans": List[ReportPlanTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBackupPlanInputTypeDef = TypedDict(
    "_RequiredBackupPlanInputTypeDef",
    {
        "BackupPlanName": str,
        "Rules": Sequence[BackupRuleInputTypeDef],
    },
)
_OptionalBackupPlanInputTypeDef = TypedDict(
    "_OptionalBackupPlanInputTypeDef",
    {
        "AdvancedBackupSettings": Sequence[AdvancedBackupSettingTypeDef],
    },
    total=False,
)

class BackupPlanInputTypeDef(_RequiredBackupPlanInputTypeDef, _OptionalBackupPlanInputTypeDef):
    pass

_RequiredBackupPlanTypeDef = TypedDict(
    "_RequiredBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[BackupRuleTypeDef],
    },
)
_OptionalBackupPlanTypeDef = TypedDict(
    "_OptionalBackupPlanTypeDef",
    {
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
    },
    total=False,
)

class BackupPlanTypeDef(_RequiredBackupPlanTypeDef, _OptionalBackupPlanTypeDef):
    pass

GetBackupSelectionOutputTypeDef = TypedDict(
    "GetBackupSelectionOutputTypeDef",
    {
        "BackupSelection": BackupSelectionOutputTypeDef,
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BackupSelectionUnionTypeDef = Union[BackupSelectionTypeDef, BackupSelectionOutputTypeDef]
_RequiredCreateBackupSelectionInputRequestTypeDef = TypedDict(
    "_RequiredCreateBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupSelection": BackupSelectionTypeDef,
    },
)
_OptionalCreateBackupSelectionInputRequestTypeDef = TypedDict(
    "_OptionalCreateBackupSelectionInputRequestTypeDef",
    {
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateBackupSelectionInputRequestTypeDef(
    _RequiredCreateBackupSelectionInputRequestTypeDef,
    _OptionalCreateBackupSelectionInputRequestTypeDef,
):
    pass

_RequiredCreateFrameworkInputRequestTypeDef = TypedDict(
    "_RequiredCreateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
        "FrameworkControls": Sequence[FrameworkControlUnionTypeDef],
    },
)
_OptionalCreateFrameworkInputRequestTypeDef = TypedDict(
    "_OptionalCreateFrameworkInputRequestTypeDef",
    {
        "FrameworkDescription": str,
        "IdempotencyToken": str,
        "FrameworkTags": Mapping[str, str],
    },
    total=False,
)

class CreateFrameworkInputRequestTypeDef(
    _RequiredCreateFrameworkInputRequestTypeDef, _OptionalCreateFrameworkInputRequestTypeDef
):
    pass

_RequiredUpdateFrameworkInputRequestTypeDef = TypedDict(
    "_RequiredUpdateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)
_OptionalUpdateFrameworkInputRequestTypeDef = TypedDict(
    "_OptionalUpdateFrameworkInputRequestTypeDef",
    {
        "FrameworkDescription": str,
        "FrameworkControls": Sequence[FrameworkControlUnionTypeDef],
        "IdempotencyToken": str,
    },
    total=False,
)

class UpdateFrameworkInputRequestTypeDef(
    _RequiredUpdateFrameworkInputRequestTypeDef, _OptionalUpdateFrameworkInputRequestTypeDef
):
    pass

_RequiredCreateLegalHoldInputRequestTypeDef = TypedDict(
    "_RequiredCreateLegalHoldInputRequestTypeDef",
    {
        "Title": str,
        "Description": str,
    },
)
_OptionalCreateLegalHoldInputRequestTypeDef = TypedDict(
    "_OptionalCreateLegalHoldInputRequestTypeDef",
    {
        "IdempotencyToken": str,
        "RecoveryPointSelection": RecoveryPointSelectionTypeDef,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreateLegalHoldInputRequestTypeDef(
    _RequiredCreateLegalHoldInputRequestTypeDef, _OptionalCreateLegalHoldInputRequestTypeDef
):
    pass

RecoveryPointSelectionUnionTypeDef = Union[
    RecoveryPointSelectionTypeDef, RecoveryPointSelectionOutputTypeDef
]
_RequiredCreateBackupPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateBackupPlanInputRequestTypeDef",
    {
        "BackupPlan": BackupPlanInputTypeDef,
    },
)
_OptionalCreateBackupPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateBackupPlanInputRequestTypeDef",
    {
        "BackupPlanTags": Mapping[str, str],
        "CreatorRequestId": str,
    },
    total=False,
)

class CreateBackupPlanInputRequestTypeDef(
    _RequiredCreateBackupPlanInputRequestTypeDef, _OptionalCreateBackupPlanInputRequestTypeDef
):
    pass

UpdateBackupPlanInputRequestTypeDef = TypedDict(
    "UpdateBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlan": BackupPlanInputTypeDef,
    },
)

GetBackupPlanFromJSONOutputTypeDef = TypedDict(
    "GetBackupPlanFromJSONOutputTypeDef",
    {
        "BackupPlan": BackupPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBackupPlanFromTemplateOutputTypeDef = TypedDict(
    "GetBackupPlanFromTemplateOutputTypeDef",
    {
        "BackupPlanDocument": BackupPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBackupPlanOutputTypeDef = TypedDict(
    "GetBackupPlanOutputTypeDef",
    {
        "BackupPlan": BackupPlanTypeDef,
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
