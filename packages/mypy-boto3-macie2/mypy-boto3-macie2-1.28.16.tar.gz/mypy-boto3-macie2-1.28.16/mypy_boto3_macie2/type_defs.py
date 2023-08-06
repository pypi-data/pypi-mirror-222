"""
Type annotations for macie2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/type_defs/)

Usage::

    ```python
    from mypy_boto3_macie2.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AdminStatusType,
    AllowListStatusCodeType,
    AllowsUnencryptedObjectUploadsType,
    AutomatedDiscoveryStatusType,
    AvailabilityCodeType,
    ClassificationScopeUpdateOperationType,
    DataIdentifierSeverityType,
    DataIdentifierTypeType,
    DayOfWeekType,
    EffectivePermissionType,
    EncryptionTypeType,
    ErrorCodeType,
    FindingCategoryType,
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingStatisticsSortAttributeNameType,
    FindingTypeType,
    GroupByType,
    IsDefinedInJobType,
    IsMonitoredByJobType,
    JobComparatorType,
    JobStatusType,
    JobTypeType,
    LastRunErrorStatusCodeType,
    ListJobsFilterKeyType,
    ListJobsSortAttributeNameType,
    MacieStatusType,
    ManagedDataIdentifierSelectorType,
    OrderByType,
    OriginTypeType,
    RelationshipStatusType,
    RevealRequestStatusType,
    RevealStatusType,
    ScopeFilterKeyType,
    SearchResourcesComparatorType,
    SearchResourcesSimpleCriterionKeyType,
    SearchResourcesSortAttributeNameType,
    SensitiveDataItemCategoryType,
    SeverityDescriptionType,
    SharedAccessType,
    SimpleCriterionKeyForJobType,
    StorageClassType,
    TimeRangeType,
    TypeType,
    UnavailabilityReasonCodeType,
    UsageStatisticsFilterComparatorType,
    UsageStatisticsFilterKeyType,
    UsageStatisticsSortKeyType,
    UsageTypeType,
    UserIdentityTypeType,
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
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccountDetailTypeDef",
    "BlockPublicAccessTypeDef",
    "AdminAccountTypeDef",
    "S3WordsListTypeDef",
    "AllowListStatusTypeDef",
    "AllowListSummaryTypeDef",
    "ApiCallDetailsTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketPolicyTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "JobDetailsTypeDef",
    "KeyValuePairTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "ReplicationDetailsTypeDef",
    "BucketSortCriteriaTypeDef",
    "SensitivityAggregationsTypeDef",
    "CellTypeDef",
    "S3DestinationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationScopeSummaryTypeDef",
    "SeverityLevelTypeDef",
    "CreateInvitationsRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "SimpleCriterionForJobOutputTypeDef",
    "SimpleCriterionForJobTypeDef",
    "CriterionAdditionalPropertiesOutputTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeleteAllowListRequestRequestTypeDef",
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    "DeleteFindingsFilterRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteMemberRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeClassificationJobRequestRequestTypeDef",
    "LastRunErrorStatusTypeDef",
    "StatisticsTypeDef",
    "UserPausedDetailsTypeDef",
    "DetectedDataDetailsTypeDef",
    "DetectionTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
    "DomainDetailsTypeDef",
    "EnableMacieRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "SeverityTypeDef",
    "FindingsFilterListItemTypeDef",
    "InvitationTypeDef",
    "GetAllowListRequestRequestTypeDef",
    "GetBucketStatisticsRequestRequestTypeDef",
    "GetClassificationScopeRequestRequestTypeDef",
    "GetCustomDataIdentifierRequestRequestTypeDef",
    "GroupCountTypeDef",
    "GetFindingsFilterRequestRequestTypeDef",
    "SecurityHubConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "GetMemberRequestRequestTypeDef",
    "GetResourceProfileRequestRequestTypeDef",
    "ResourceStatisticsTypeDef",
    "RevealConfigurationTypeDef",
    "GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetSensitiveDataOccurrencesRequestRequestTypeDef",
    "GetSensitivityInspectionTemplateRequestRequestTypeDef",
    "SensitivityInspectionTemplateExcludesOutputTypeDef",
    "SensitivityInspectionTemplateIncludesOutputTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
    "GetUsageTotalsRequestRequestTypeDef",
    "UsageTotalTypeDef",
    "IamUserTypeDef",
    "IpCityTypeDef",
    "IpCountryTypeDef",
    "IpGeoLocationTypeDef",
    "IpOwnerTypeDef",
    "MonthlyScheduleTypeDef",
    "WeeklyScheduleTypeDef",
    "SimpleScopeTermOutputTypeDef",
    "SimpleScopeTermTypeDef",
    "S3BucketDefinitionForJobOutputTypeDef",
    "ListAllowListsRequestRequestTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListClassificationScopesRequestRequestTypeDef",
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    "ListFindingsFiltersRequestRequestTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListJobsFilterTermTypeDef",
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    "ManagedDataIdentifierSummaryTypeDef",
    "ListMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListResourceProfileArtifactsRequestRequestTypeDef",
    "ResourceProfileArtifactTypeDef",
    "ListResourceProfileDetectionsRequestRequestTypeDef",
    "ListSensitivityInspectionTemplatesRequestRequestTypeDef",
    "SensitivityInspectionTemplatesEntryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "ServerSideEncryptionTypeDef",
    "S3ClassificationScopeExclusionTypeDef",
    "S3ClassificationScopeExclusionUpdateTypeDef",
    "SearchResourcesSimpleCriterionTypeDef",
    "SearchResourcesSortCriteriaTypeDef",
    "SearchResourcesTagCriterionPairTypeDef",
    "SensitivityInspectionTemplateExcludesTypeDef",
    "SensitivityInspectionTemplateIncludesTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionIssuerTypeDef",
    "SuppressDataIdentifierTypeDef",
    "TagCriterionPairForJobTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagValuePairTypeDef",
    "TestCustomDataIdentifierRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    "UpdateClassificationJobRequestRequestTypeDef",
    "UpdateMacieSessionRequestRequestTypeDef",
    "UpdateMemberSessionRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateResourceProfileRequestRequestTypeDef",
    "UserIdentityRootTypeDef",
    "CreateMemberRequestRequestTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AllowListCriteriaTypeDef",
    "FindingActionTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "CreateAllowListResponseTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateMemberResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "GetAutomatedDiscoveryConfigurationResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMacieSessionResponseTypeDef",
    "GetMemberResponseTypeDef",
    "GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    "ListAllowListsResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UpdateAllowListResponseTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "BucketLevelPermissionsTypeDef",
    "MatchingBucketTypeDef",
    "DescribeBucketsRequestRequestTypeDef",
    "BucketStatisticsBySensitivityTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ListClassificationScopesResponseTypeDef",
    "CreateCustomDataIdentifierRequestRequestTypeDef",
    "GetCustomDataIdentifierResponseTypeDef",
    "CreateInvitationsResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "FindingCriteriaOutputTypeDef",
    "FindingCriteriaTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "DescribeBucketsRequestDescribeBucketsPaginateTypeDef",
    "ListAllowListsRequestListAllowListsPaginateTypeDef",
    "ListClassificationScopesRequestListClassificationScopesPaginateTypeDef",
    "ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef",
    "ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef",
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    "ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    "ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef",
    "ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef",
    "ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef",
    "GetSensitiveDataOccurrencesResponseTypeDef",
    "ListResourceProfileDetectionsResponseTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "GetFindingStatisticsResponseTypeDef",
    "GetFindingsPublicationConfigurationResponseTypeDef",
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetResourceProfileResponseTypeDef",
    "GetRevealConfigurationResponseTypeDef",
    "UpdateRevealConfigurationRequestRequestTypeDef",
    "UpdateRevealConfigurationResponseTypeDef",
    "GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef",
    "GetSensitivityInspectionTemplateResponseTypeDef",
    "GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageTotalsResponseTypeDef",
    "IpAddressDetailsTypeDef",
    "JobScheduleFrequencyOutputTypeDef",
    "JobScheduleFrequencyTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListManagedDataIdentifiersResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListResourceProfileArtifactsResponseTypeDef",
    "ListSensitivityInspectionTemplatesResponseTypeDef",
    "PageTypeDef",
    "S3ObjectTypeDef",
    "S3ClassificationScopeTypeDef",
    "S3ClassificationScopeUpdateTypeDef",
    "SearchResourcesTagCriterionTypeDef",
    "SensitivityInspectionTemplateExcludesUnionTypeDef",
    "SensitivityInspectionTemplateIncludesUnionTypeDef",
    "UpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    "UsageByAccountTypeDef",
    "SessionContextTypeDef",
    "UpdateResourceProfileDetectionsRequestRequestTypeDef",
    "TagCriterionForJobOutputTypeDef",
    "TagCriterionForJobTypeDef",
    "TagScopeTermOutputTypeDef",
    "TagScopeTermTypeDef",
    "CreateAllowListRequestRequestTypeDef",
    "GetAllowListResponseTypeDef",
    "UpdateAllowListRequestRequestTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "MatchingResourceTypeDef",
    "GetBucketStatisticsResponseTypeDef",
    "GetClassificationExportConfigurationResponseTypeDef",
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "GetFindingsFilterResponseTypeDef",
    "CreateFindingsFilterRequestRequestTypeDef",
    "FindingCriteriaUnionTypeDef",
    "GetFindingStatisticsRequestRequestTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "UpdateFindingsFilterRequestRequestTypeDef",
    "JobScheduleFrequencyUnionTypeDef",
    "ListClassificationJobsRequestListClassificationJobsPaginateTypeDef",
    "ListClassificationJobsRequestRequestTypeDef",
    "OccurrencesTypeDef",
    "GetClassificationScopeResponseTypeDef",
    "UpdateClassificationScopeRequestRequestTypeDef",
    "SearchResourcesCriteriaTypeDef",
    "UsageRecordTypeDef",
    "AssumedRoleTypeDef",
    "FederatedUserTypeDef",
    "CriteriaForJobOutputTypeDef",
    "CriteriaForJobTypeDef",
    "JobScopeTermOutputTypeDef",
    "JobScopeTermTypeDef",
    "BucketPublicAccessTypeDef",
    "SearchResourcesResponseTypeDef",
    "CustomDetectionTypeDef",
    "DefaultDetectionTypeDef",
    "SearchResourcesCriteriaBlockTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "UserIdentityTypeDef",
    "CriteriaBlockForJobOutputTypeDef",
    "CriteriaBlockForJobTypeDef",
    "JobScopingBlockOutputTypeDef",
    "JobScopingBlockTypeDef",
    "BucketMetadataTypeDef",
    "S3BucketTypeDef",
    "CustomDataIdentifiersTypeDef",
    "SensitiveDataItemTypeDef",
    "SearchResourcesBucketCriteriaTypeDef",
    "FindingActorTypeDef",
    "S3BucketCriteriaForJobOutputTypeDef",
    "S3BucketCriteriaForJobTypeDef",
    "ScopingOutputTypeDef",
    "ScopingTypeDef",
    "DescribeBucketsResponseTypeDef",
    "ResourcesAffectedTypeDef",
    "ClassificationResultTypeDef",
    "SearchResourcesRequestRequestTypeDef",
    "SearchResourcesRequestSearchResourcesPaginateTypeDef",
    "PolicyDetailsTypeDef",
    "JobSummaryTypeDef",
    "S3JobDefinitionOutputTypeDef",
    "S3JobDefinitionTypeDef",
    "ClassificationDetailsTypeDef",
    "ListClassificationJobsResponseTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "CreateClassificationJobRequestRequestTypeDef",
    "S3JobDefinitionUnionTypeDef",
    "FindingTypeDef",
    "GetFindingsResponseTypeDef",
)

_RequiredAcceptInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptInvitationRequestRequestTypeDef",
    {
        "invitationId": str,
    },
)
_OptionalAcceptInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptInvitationRequestRequestTypeDef",
    {
        "administratorAccountId": str,
        "masterAccount": str,
    },
    total=False,
)


class AcceptInvitationRequestRequestTypeDef(
    _RequiredAcceptInvitationRequestRequestTypeDef, _OptionalAcceptInvitationRequestRequestTypeDef
):
    pass


AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "allowsPublicReadAccess": bool,
        "allowsPublicWriteAccess": bool,
    },
    total=False,
)

AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "accountId": str,
        "email": str,
    },
)

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "blockPublicAcls": bool,
        "blockPublicPolicy": bool,
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "accountId": str,
        "status": AdminStatusType,
    },
    total=False,
)

S3WordsListTypeDef = TypedDict(
    "S3WordsListTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)

_RequiredAllowListStatusTypeDef = TypedDict(
    "_RequiredAllowListStatusTypeDef",
    {
        "code": AllowListStatusCodeType,
    },
)
_OptionalAllowListStatusTypeDef = TypedDict(
    "_OptionalAllowListStatusTypeDef",
    {
        "description": str,
    },
    total=False,
)


class AllowListStatusTypeDef(_RequiredAllowListStatusTypeDef, _OptionalAllowListStatusTypeDef):
    pass


AllowListSummaryTypeDef = TypedDict(
    "AllowListSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
    },
    total=False,
)

ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {
        "api": str,
        "apiServiceName": str,
        "firstSeen": datetime,
        "lastSeen": datetime,
    },
    total=False,
)

AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef",
    {
        "accountId": str,
        "principalId": str,
    },
    total=False,
)

AwsServiceTypeDef = TypedDict(
    "AwsServiceTypeDef",
    {
        "invokedBy": str,
    },
    total=False,
)

BatchGetCustomDataIdentifierSummaryTypeDef = TypedDict(
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)

BatchGetCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    {
        "ids": Sequence[str],
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

BucketCountByEffectivePermissionTypeDef = TypedDict(
    "BucketCountByEffectivePermissionTypeDef",
    {
        "publiclyAccessible": int,
        "publiclyReadable": int,
        "publiclyWritable": int,
        "unknown": int,
    },
    total=False,
)

BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {
        "external": int,
        "internal": int,
        "notShared": int,
        "unknown": int,
    },
    total=False,
)

BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef = TypedDict(
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    {
        "allowsUnencryptedObjectUploads": int,
        "deniesUnencryptedObjectUploads": int,
        "unknown": int,
    },
    total=False,
)

BucketCriteriaAdditionalPropertiesTypeDef = TypedDict(
    "BucketCriteriaAdditionalPropertiesTypeDef",
    {
        "eq": Sequence[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": Sequence[str],
        "prefix": str,
    },
    total=False,
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "allowsPublicReadAccess": bool,
        "allowsPublicWriteAccess": bool,
    },
    total=False,
)

BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef",
    {
        "kmsMasterKeyId": str,
        "type": TypeType,
    },
    total=False,
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": IsDefinedInJobType,
        "isMonitoredByJob": IsMonitoredByJobType,
        "lastJobId": str,
        "lastJobRunTime": datetime,
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {
        "customerManaged": int,
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {
        "fileType": int,
        "storageClass": int,
        "total": int,
    },
    total=False,
)

ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {
        "replicated": bool,
        "replicatedExternally": bool,
        "replicationAccounts": List[str],
    },
    total=False,
)

BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

SensitivityAggregationsTypeDef = TypedDict(
    "SensitivityAggregationsTypeDef",
    {
        "classifiableSizeInBytes": int,
        "publiclyAccessibleCount": int,
        "totalCount": int,
        "totalSizeInBytes": int,
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "cellReference": str,
        "column": int,
        "columnName": str,
        "row": int,
    },
    total=False,
)

_RequiredS3DestinationTypeDef = TypedDict(
    "_RequiredS3DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
    },
)
_OptionalS3DestinationTypeDef = TypedDict(
    "_OptionalS3DestinationTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, _OptionalS3DestinationTypeDef):
    pass


ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef",
    {
        "code": str,
        "reason": str,
    },
    total=False,
)

ClassificationScopeSummaryTypeDef = TypedDict(
    "ClassificationScopeSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "occurrencesThreshold": int,
        "severity": DataIdentifierSeverityType,
    },
)

_RequiredCreateInvitationsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)
_OptionalCreateInvitationsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInvitationsRequestRequestTypeDef",
    {
        "disableEmailNotification": bool,
        "message": str,
    },
    total=False,
)


class CreateInvitationsRequestRequestTypeDef(
    _RequiredCreateInvitationsRequestRequestTypeDef, _OptionalCreateInvitationsRequestRequestTypeDef
):
    pass


UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "accountId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

CreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestRequestTypeDef",
    {
        "findingTypes": Sequence[FindingTypeType],
    },
    total=False,
)

SimpleCriterionForJobOutputTypeDef = TypedDict(
    "SimpleCriterionForJobOutputTypeDef",
    {
        "comparator": JobComparatorType,
        "key": SimpleCriterionKeyForJobType,
        "values": List[str],
    },
    total=False,
)

SimpleCriterionForJobTypeDef = TypedDict(
    "SimpleCriterionForJobTypeDef",
    {
        "comparator": JobComparatorType,
        "key": SimpleCriterionKeyForJobType,
        "values": Sequence[str],
    },
    total=False,
)

CriterionAdditionalPropertiesOutputTypeDef = TypedDict(
    "CriterionAdditionalPropertiesOutputTypeDef",
    {
        "eq": List[str],
        "eqExactMatch": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
    },
    total=False,
)

CriterionAdditionalPropertiesTypeDef = TypedDict(
    "CriterionAdditionalPropertiesTypeDef",
    {
        "eq": Sequence[str],
        "eqExactMatch": Sequence[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": Sequence[str],
    },
    total=False,
)

CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)

_RequiredDeleteAllowListRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAllowListRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteAllowListRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAllowListRequestRequestTypeDef",
    {
        "ignoreJobChecks": str,
    },
    total=False,
)


class DeleteAllowListRequestRequestTypeDef(
    _RequiredDeleteAllowListRequestRequestTypeDef, _OptionalDeleteAllowListRequestRequestTypeDef
):
    pass


DeleteCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteFindingsFilterRequestRequestTypeDef = TypedDict(
    "DeleteFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)

DeleteMemberRequestRequestTypeDef = TypedDict(
    "DeleteMemberRequestRequestTypeDef",
    {
        "id": str,
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

DescribeClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef",
    {
        "code": LastRunErrorStatusCodeType,
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "approximateNumberOfObjectsToProcess": float,
        "numberOfRuns": float,
    },
    total=False,
)

UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {
        "jobExpiresAt": datetime,
        "jobImminentExpirationHealthEventArn": str,
        "jobPausedAt": datetime,
    },
    total=False,
)

DetectedDataDetailsTypeDef = TypedDict(
    "DetectedDataDetailsTypeDef",
    {
        "value": str,
    },
)

DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "arn": str,
        "count": int,
        "id": str,
        "name": str,
        "suppressed": bool,
        "type": DataIdentifierTypeType,
    },
    total=False,
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

EnableMacieRequestRequestTypeDef = TypedDict(
    "EnableMacieRequestRequestTypeDef",
    {
        "clientToken": str,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "status": MacieStatusType,
    },
    total=False,
)

_RequiredEnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredEnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)
_OptionalEnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalEnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class EnableOrganizationAdminAccountRequestRequestTypeDef(
    _RequiredEnableOrganizationAdminAccountRequestRequestTypeDef,
    _OptionalEnableOrganizationAdminAccountRequestRequestTypeDef,
):
    pass


FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {
        "attributeName": FindingStatisticsSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "description": SeverityDescriptionType,
        "score": int,
    },
    total=False,
)

FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "id": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": str,
        "invitationId": str,
        "invitedAt": datetime,
        "relationshipStatus": RelationshipStatusType,
    },
    total=False,
)

GetAllowListRequestRequestTypeDef = TypedDict(
    "GetAllowListRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetBucketStatisticsRequestRequestTypeDef = TypedDict(
    "GetBucketStatisticsRequestRequestTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

GetClassificationScopeRequestRequestTypeDef = TypedDict(
    "GetClassificationScopeRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "GetCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)

GroupCountTypeDef = TypedDict(
    "GroupCountTypeDef",
    {
        "count": int,
        "groupKey": str,
    },
    total=False,
)

GetFindingsFilterRequestRequestTypeDef = TypedDict(
    "GetFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)

SecurityHubConfigurationTypeDef = TypedDict(
    "SecurityHubConfigurationTypeDef",
    {
        "publishClassificationFindings": bool,
        "publishPolicyFindings": bool,
    },
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetResourceProfileRequestRequestTypeDef = TypedDict(
    "GetResourceProfileRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ResourceStatisticsTypeDef = TypedDict(
    "ResourceStatisticsTypeDef",
    {
        "totalBytesClassified": int,
        "totalDetections": int,
        "totalDetectionsSuppressed": int,
        "totalItemsClassified": int,
        "totalItemsSensitive": int,
        "totalItemsSkipped": int,
        "totalItemsSkippedInvalidEncryption": int,
        "totalItemsSkippedInvalidKms": int,
        "totalItemsSkippedPermissionDenied": int,
    },
    total=False,
)

_RequiredRevealConfigurationTypeDef = TypedDict(
    "_RequiredRevealConfigurationTypeDef",
    {
        "status": RevealStatusType,
    },
)
_OptionalRevealConfigurationTypeDef = TypedDict(
    "_OptionalRevealConfigurationTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)


class RevealConfigurationTypeDef(
    _RequiredRevealConfigurationTypeDef, _OptionalRevealConfigurationTypeDef
):
    pass


GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef",
    {
        "findingId": str,
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

GetSensitiveDataOccurrencesRequestRequestTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesRequestRequestTypeDef",
    {
        "findingId": str,
    },
)

GetSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "GetSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

SensitivityInspectionTemplateExcludesOutputTypeDef = TypedDict(
    "SensitivityInspectionTemplateExcludesOutputTypeDef",
    {
        "managedDataIdentifierIds": List[str],
    },
    total=False,
)

SensitivityInspectionTemplateIncludesOutputTypeDef = TypedDict(
    "SensitivityInspectionTemplateIncludesOutputTypeDef",
    {
        "allowListIds": List[str],
        "customDataIdentifierIds": List[str],
        "managedDataIdentifierIds": List[str],
    },
    total=False,
)

UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": UsageStatisticsFilterComparatorType,
        "key": UsageStatisticsFilterKeyType,
        "values": Sequence[str],
    },
    total=False,
)

UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef",
    {
        "key": UsageStatisticsSortKeyType,
        "orderBy": OrderByType,
    },
    total=False,
)

GetUsageTotalsRequestRequestTypeDef = TypedDict(
    "GetUsageTotalsRequestRequestTypeDef",
    {
        "timeRange": str,
    },
    total=False,
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "type": UsageTypeType,
    },
    total=False,
)

IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
        "userName": str,
    },
    total=False,
)

IpCityTypeDef = TypedDict(
    "IpCityTypeDef",
    {
        "name": str,
    },
    total=False,
)

IpCountryTypeDef = TypedDict(
    "IpCountryTypeDef",
    {
        "code": str,
        "name": str,
    },
    total=False,
)

IpGeoLocationTypeDef = TypedDict(
    "IpGeoLocationTypeDef",
    {
        "lat": float,
        "lon": float,
    },
    total=False,
)

IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef",
    {
        "asn": str,
        "asnOrg": str,
        "isp": str,
        "org": str,
    },
    total=False,
)

MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "dayOfMonth": int,
    },
    total=False,
)

WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "dayOfWeek": DayOfWeekType,
    },
    total=False,
)

SimpleScopeTermOutputTypeDef = TypedDict(
    "SimpleScopeTermOutputTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ScopeFilterKeyType,
        "values": List[str],
    },
    total=False,
)

SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ScopeFilterKeyType,
        "values": Sequence[str],
    },
    total=False,
)

S3BucketDefinitionForJobOutputTypeDef = TypedDict(
    "S3BucketDefinitionForJobOutputTypeDef",
    {
        "accountId": str,
        "buckets": List[str],
    },
)

ListAllowListsRequestRequestTypeDef = TypedDict(
    "ListAllowListsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {
        "attributeName": ListJobsSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

ListClassificationScopesRequestRequestTypeDef = TypedDict(
    "ListClassificationScopesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
    },
    total=False,
)

ListCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListFindingsFiltersRequestRequestTypeDef = TypedDict(
    "ListFindingsFiltersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": ListJobsFilterKeyType,
        "values": Sequence[str],
    },
    total=False,
)

ListManagedDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ManagedDataIdentifierSummaryTypeDef = TypedDict(
    "ManagedDataIdentifierSummaryTypeDef",
    {
        "category": SensitiveDataItemCategoryType,
        "id": str,
    },
    total=False,
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "onlyAssociated": str,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListResourceProfileArtifactsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceProfileArtifactsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListResourceProfileArtifactsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceProfileArtifactsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListResourceProfileArtifactsRequestRequestTypeDef(
    _RequiredListResourceProfileArtifactsRequestRequestTypeDef,
    _OptionalListResourceProfileArtifactsRequestRequestTypeDef,
):
    pass


_RequiredResourceProfileArtifactTypeDef = TypedDict(
    "_RequiredResourceProfileArtifactTypeDef",
    {
        "arn": str,
        "classificationResultStatus": str,
    },
)
_OptionalResourceProfileArtifactTypeDef = TypedDict(
    "_OptionalResourceProfileArtifactTypeDef",
    {
        "sensitive": bool,
    },
    total=False,
)


class ResourceProfileArtifactTypeDef(
    _RequiredResourceProfileArtifactTypeDef, _OptionalResourceProfileArtifactTypeDef
):
    pass


_RequiredListResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceProfileDetectionsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceProfileDetectionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListResourceProfileDetectionsRequestRequestTypeDef(
    _RequiredListResourceProfileDetectionsRequestRequestTypeDef,
    _OptionalListResourceProfileDetectionsRequestRequestTypeDef,
):
    pass


ListSensitivityInspectionTemplatesRequestRequestTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

SensitivityInspectionTemplatesEntryTypeDef = TypedDict(
    "SensitivityInspectionTemplatesEntryTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "end": int,
        "start": int,
        "startColumn": int,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "jsonPath": str,
        "recordIndex": int,
    },
    total=False,
)

S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef",
    {
        "accountId": str,
        "buckets": Sequence[str],
    },
)

S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef",
    {
        "displayName": str,
        "id": str,
    },
    total=False,
)

ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsMasterKeyId": str,
    },
    total=False,
)

S3ClassificationScopeExclusionTypeDef = TypedDict(
    "S3ClassificationScopeExclusionTypeDef",
    {
        "bucketNames": List[str],
    },
)

S3ClassificationScopeExclusionUpdateTypeDef = TypedDict(
    "S3ClassificationScopeExclusionUpdateTypeDef",
    {
        "bucketNames": Sequence[str],
        "operation": ClassificationScopeUpdateOperationType,
    },
)

SearchResourcesSimpleCriterionTypeDef = TypedDict(
    "SearchResourcesSimpleCriterionTypeDef",
    {
        "comparator": SearchResourcesComparatorType,
        "key": SearchResourcesSimpleCriterionKeyType,
        "values": Sequence[str],
    },
    total=False,
)

SearchResourcesSortCriteriaTypeDef = TypedDict(
    "SearchResourcesSortCriteriaTypeDef",
    {
        "attributeName": SearchResourcesSortAttributeNameType,
        "orderBy": OrderByType,
    },
    total=False,
)

SearchResourcesTagCriterionPairTypeDef = TypedDict(
    "SearchResourcesTagCriterionPairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

SensitivityInspectionTemplateExcludesTypeDef = TypedDict(
    "SensitivityInspectionTemplateExcludesTypeDef",
    {
        "managedDataIdentifierIds": Sequence[str],
    },
    total=False,
)

SensitivityInspectionTemplateIncludesTypeDef = TypedDict(
    "SensitivityInspectionTemplateIncludesTypeDef",
    {
        "allowListIds": Sequence[str],
        "customDataIdentifierIds": Sequence[str],
        "managedDataIdentifierIds": Sequence[str],
    },
    total=False,
)

ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef",
    {
        "isServiceLimited": bool,
        "unit": Literal["TERABYTES"],
        "value": int,
    },
    total=False,
)

SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {
        "creationDate": datetime,
        "mfaAuthenticated": bool,
    },
    total=False,
)

SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
        "type": str,
        "userName": str,
    },
    total=False,
)

SuppressDataIdentifierTypeDef = TypedDict(
    "SuppressDataIdentifierTypeDef",
    {
        "id": str,
        "type": DataIdentifierTypeType,
    },
    total=False,
)

TagCriterionPairForJobTypeDef = TypedDict(
    "TagCriterionPairForJobTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TagValuePairTypeDef = TypedDict(
    "TagValuePairTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredTestCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_RequiredTestCustomDataIdentifierRequestRequestTypeDef",
    {
        "regex": str,
        "sampleText": str,
    },
)
_OptionalTestCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_OptionalTestCustomDataIdentifierRequestRequestTypeDef",
    {
        "ignoreWords": Sequence[str],
        "keywords": Sequence[str],
        "maximumMatchDistance": int,
    },
    total=False,
)


class TestCustomDataIdentifierRequestRequestTypeDef(
    _RequiredTestCustomDataIdentifierRequestRequestTypeDef,
    _OptionalTestCustomDataIdentifierRequestRequestTypeDef,
):
    pass


UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    {
        "status": AutomatedDiscoveryStatusType,
    },
)

UpdateClassificationJobRequestRequestTypeDef = TypedDict(
    "UpdateClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
        "jobStatus": JobStatusType,
    },
)

UpdateMacieSessionRequestRequestTypeDef = TypedDict(
    "UpdateMacieSessionRequestRequestTypeDef",
    {
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "status": MacieStatusType,
    },
    total=False,
)

UpdateMemberSessionRequestRequestTypeDef = TypedDict(
    "UpdateMemberSessionRequestRequestTypeDef",
    {
        "id": str,
        "status": MacieStatusType,
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": bool,
    },
)

_RequiredUpdateResourceProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceProfileRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalUpdateResourceProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceProfileRequestRequestTypeDef",
    {
        "sensitivityScoreOverride": int,
    },
    total=False,
)


class UpdateResourceProfileRequestRequestTypeDef(
    _RequiredUpdateResourceProfileRequestRequestTypeDef,
    _OptionalUpdateResourceProfileRequestRequestTypeDef,
):
    pass


UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef",
    {
        "accountId": str,
        "arn": str,
        "principalId": str,
    },
    total=False,
)

_RequiredCreateMemberRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMemberRequestRequestTypeDef",
    {
        "account": AccountDetailTypeDef,
    },
)
_OptionalCreateMemberRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMemberRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateMemberRequestRequestTypeDef(
    _RequiredCreateMemberRequestRequestTypeDef, _OptionalCreateMemberRequestRequestTypeDef
):
    pass


AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "blockPublicAccess": BlockPublicAccessTypeDef,
    },
    total=False,
)

AllowListCriteriaTypeDef = TypedDict(
    "AllowListCriteriaTypeDef",
    {
        "regex": str,
        "s3WordsList": S3WordsListTypeDef,
    },
    total=False,
)

FindingActionTypeDef = TypedDict(
    "FindingActionTypeDef",
    {
        "actionType": Literal["AWS_API_CALL"],
        "apiCallDetails": ApiCallDetailsTypeDef,
    },
    total=False,
)

BatchGetCustomDataIdentifiersResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    {
        "customDataIdentifiers": List[BatchGetCustomDataIdentifierSummaryTypeDef],
        "notFoundIdentifierIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAllowListResponseTypeDef = TypedDict(
    "CreateAllowListResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateClassificationJobResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateCustomDataIdentifierResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseTypeDef",
    {
        "customDataIdentifierId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMemberResponseTypeDef = TypedDict(
    "CreateMemberResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": bool,
        "maxAccountLimitReached": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAutomatedDiscoveryConfigurationResponseTypeDef = TypedDict(
    "GetAutomatedDiscoveryConfigurationResponseTypeDef",
    {
        "classificationScopeId": str,
        "disabledAt": datetime,
        "firstEnabledAt": datetime,
        "lastUpdatedAt": datetime,
        "sensitivityInspectionTemplateId": str,
        "status": AutomatedDiscoveryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "invitationsCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMacieSessionResponseTypeDef = TypedDict(
    "GetMacieSessionResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "serviceRole": str,
        "status": MacieStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSensitiveDataOccurrencesAvailabilityResponseTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    {
        "code": AvailabilityCodeType,
        "reasons": List[UnavailabilityReasonCodeType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAllowListsResponseTypeDef = TypedDict(
    "ListAllowListsResponseTypeDef",
    {
        "allowLists": List[AllowListSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingIds": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "adminAccounts": List[AdminAccountTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TestCustomDataIdentifierResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseTypeDef",
    {
        "matchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAllowListResponseTypeDef = TypedDict(
    "UpdateAllowListResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "accessControlList": AccessControlListTypeDef,
        "blockPublicAccess": BlockPublicAccessTypeDef,
        "bucketPolicy": BucketPolicyTypeDef,
    },
    total=False,
)

MatchingBucketTypeDef = TypedDict(
    "MatchingBucketTypeDef",
    {
        "accountId": str,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "errorCode": Literal["ACCESS_DENIED"],
        "errorMessage": str,
        "jobDetails": JobDetailsTypeDef,
        "lastAutomatedDiscoveryTime": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": ObjectCountByEncryptionTypeTypeDef,
        "sensitivityScore": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": ObjectLevelStatisticsTypeDef,
        "unclassifiableObjectSizeInBytes": ObjectLevelStatisticsTypeDef,
    },
    total=False,
)

DescribeBucketsRequestRequestTypeDef = TypedDict(
    "DescribeBucketsRequestRequestTypeDef",
    {
        "criteria": Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef],
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": BucketSortCriteriaTypeDef,
    },
    total=False,
)

BucketStatisticsBySensitivityTypeDef = TypedDict(
    "BucketStatisticsBySensitivityTypeDef",
    {
        "classificationError": SensitivityAggregationsTypeDef,
        "notClassified": SensitivityAggregationsTypeDef,
        "notSensitive": SensitivityAggregationsTypeDef,
        "sensitive": SensitivityAggregationsTypeDef,
    },
    total=False,
)

ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {
        "s3Destination": S3DestinationTypeDef,
    },
    total=False,
)

ListClassificationScopesResponseTypeDef = TypedDict(
    "ListClassificationScopesResponseTypeDef",
    {
        "classificationScopes": List[ClassificationScopeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomDataIdentifierRequestRequestTypeDef",
    {
        "name": str,
        "regex": str,
    },
)
_OptionalCreateCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomDataIdentifierRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "ignoreWords": Sequence[str],
        "keywords": Sequence[str],
        "maximumMatchDistance": int,
        "severityLevels": Sequence[SeverityLevelTypeDef],
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateCustomDataIdentifierRequestRequestTypeDef(
    _RequiredCreateCustomDataIdentifierRequestRequestTypeDef,
    _OptionalCreateCustomDataIdentifierRequestRequestTypeDef,
):
    pass


GetCustomDataIdentifierResponseTypeDef = TypedDict(
    "GetCustomDataIdentifierResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "severityLevels": List[SeverityLevelTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateInvitationsResponseTypeDef = TypedDict(
    "CreateInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FindingCriteriaOutputTypeDef = TypedDict(
    "FindingCriteriaOutputTypeDef",
    {
        "criterion": Dict[str, CriterionAdditionalPropertiesOutputTypeDef],
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "criterion": Mapping[str, CriterionAdditionalPropertiesTypeDef],
    },
    total=False,
)

ListCustomDataIdentifiersResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseTypeDef",
    {
        "items": List[CustomDataIdentifierSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeBucketsRequestDescribeBucketsPaginateTypeDef = TypedDict(
    "DescribeBucketsRequestDescribeBucketsPaginateTypeDef",
    {
        "criteria": Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef],
        "sortCriteria": BucketSortCriteriaTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAllowListsRequestListAllowListsPaginateTypeDef = TypedDict(
    "ListAllowListsRequestListAllowListsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListClassificationScopesRequestListClassificationScopesPaginateTypeDef = TypedDict(
    "ListClassificationScopesRequestListClassificationScopesPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef = TypedDict(
    "ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListInvitationsRequestListInvitationsPaginateTypeDef = TypedDict(
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef = TypedDict(
    "ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListMembersRequestListMembersPaginateTypeDef = TypedDict(
    "ListMembersRequestListMembersPaginateTypeDef",
    {
        "onlyAssociated": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef = TypedDict(
    "_RequiredListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef = TypedDict(
    "_OptionalListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef(
    _RequiredListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef,
    _OptionalListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef,
):
    pass


_RequiredListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef = (
    TypedDict(
        "_RequiredListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef",
        {
            "resourceArn": str,
        },
    )
)
_OptionalListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef = (
    TypedDict(
        "_OptionalListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef",
        {
            "PaginationConfig": PaginatorConfigTypeDef,
        },
        total=False,
    )
)


class ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef(
    _RequiredListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef,
    _OptionalListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef,
):
    pass


ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetSensitiveDataOccurrencesResponseTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesResponseTypeDef",
    {
        "error": str,
        "sensitiveDataOccurrences": Dict[str, List[DetectedDataDetailsTypeDef]],
        "status": RevealRequestStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourceProfileDetectionsResponseTypeDef = TypedDict(
    "ListResourceProfileDetectionsResponseTypeDef",
    {
        "detections": List[DetectionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFindingsFiltersResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseTypeDef",
    {
        "findingsFilterListItems": List[FindingsFilterListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "administrator": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "master": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "invitations": List[InvitationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFindingStatisticsResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseTypeDef",
    {
        "countsByGroup": List[GroupCountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFindingsPublicationConfigurationResponseTypeDef = TypedDict(
    "GetFindingsPublicationConfigurationResponseTypeDef",
    {
        "securityHubConfiguration": SecurityHubConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutFindingsPublicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityHubConfiguration": SecurityHubConfigurationTypeDef,
    },
    total=False,
)

_RequiredGetFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingsRequestRequestTypeDef",
    {
        "findingIds": Sequence[str],
    },
)
_OptionalGetFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingsRequestRequestTypeDef",
    {
        "sortCriteria": SortCriteriaTypeDef,
    },
    total=False,
)


class GetFindingsRequestRequestTypeDef(
    _RequiredGetFindingsRequestRequestTypeDef, _OptionalGetFindingsRequestRequestTypeDef
):
    pass


GetResourceProfileResponseTypeDef = TypedDict(
    "GetResourceProfileResponseTypeDef",
    {
        "profileUpdatedAt": datetime,
        "sensitivityScore": int,
        "sensitivityScoreOverridden": bool,
        "statistics": ResourceStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRevealConfigurationResponseTypeDef = TypedDict(
    "GetRevealConfigurationResponseTypeDef",
    {
        "configuration": RevealConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRevealConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateRevealConfigurationRequestRequestTypeDef",
    {
        "configuration": RevealConfigurationTypeDef,
    },
)

UpdateRevealConfigurationResponseTypeDef = TypedDict(
    "UpdateRevealConfigurationResponseTypeDef",
    {
        "configuration": RevealConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef = TypedDict(
    "_RequiredGetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef",
    {
        "findingId": str,
    },
)
_OptionalGetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef = TypedDict(
    "_OptionalGetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef(
    _RequiredGetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef,
    _OptionalGetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef,
):
    pass


GetSensitivityInspectionTemplateResponseTypeDef = TypedDict(
    "GetSensitivityInspectionTemplateResponseTypeDef",
    {
        "description": str,
        "excludes": SensitivityInspectionTemplateExcludesOutputTypeDef,
        "includes": SensitivityInspectionTemplateIncludesOutputTypeDef,
        "name": str,
        "sensitivityInspectionTemplateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef = TypedDict(
    "GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef",
    {
        "filterBy": Sequence[UsageStatisticsFilterTypeDef],
        "sortBy": UsageStatisticsSortByTypeDef,
        "timeRange": TimeRangeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestRequestTypeDef",
    {
        "filterBy": Sequence[UsageStatisticsFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
        "sortBy": UsageStatisticsSortByTypeDef,
        "timeRange": TimeRangeType,
    },
    total=False,
)

GetUsageTotalsResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseTypeDef",
    {
        "timeRange": TimeRangeType,
        "usageTotals": List[UsageTotalTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IpAddressDetailsTypeDef = TypedDict(
    "IpAddressDetailsTypeDef",
    {
        "ipAddressV4": str,
        "ipCity": IpCityTypeDef,
        "ipCountry": IpCountryTypeDef,
        "ipGeoLocation": IpGeoLocationTypeDef,
        "ipOwner": IpOwnerTypeDef,
    },
    total=False,
)

JobScheduleFrequencyOutputTypeDef = TypedDict(
    "JobScheduleFrequencyOutputTypeDef",
    {
        "dailySchedule": Dict[str, Any],
        "monthlySchedule": MonthlyScheduleTypeDef,
        "weeklySchedule": WeeklyScheduleTypeDef,
    },
    total=False,
)

JobScheduleFrequencyTypeDef = TypedDict(
    "JobScheduleFrequencyTypeDef",
    {
        "dailySchedule": Mapping[str, Any],
        "monthlySchedule": MonthlyScheduleTypeDef,
        "weeklySchedule": WeeklyScheduleTypeDef,
    },
    total=False,
)

ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {
        "excludes": Sequence[ListJobsFilterTermTypeDef],
        "includes": Sequence[ListJobsFilterTermTypeDef],
    },
    total=False,
)

ListManagedDataIdentifiersResponseTypeDef = TypedDict(
    "ListManagedDataIdentifiersResponseTypeDef",
    {
        "items": List[ManagedDataIdentifierSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "members": List[MemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourceProfileArtifactsResponseTypeDef = TypedDict(
    "ListResourceProfileArtifactsResponseTypeDef",
    {
        "artifacts": List[ResourceProfileArtifactTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSensitivityInspectionTemplatesResponseTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "sensitivityInspectionTemplates": List[SensitivityInspectionTemplatesEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "lineRange": RangeTypeDef,
        "offsetRange": RangeTypeDef,
        "pageNumber": int,
    },
    total=False,
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucketArn": str,
        "eTag": str,
        "extension": str,
        "key": str,
        "lastModified": datetime,
        "path": str,
        "publicAccess": bool,
        "serverSideEncryption": ServerSideEncryptionTypeDef,
        "size": int,
        "storageClass": StorageClassType,
        "tags": List[KeyValuePairTypeDef],
        "versionId": str,
    },
    total=False,
)

S3ClassificationScopeTypeDef = TypedDict(
    "S3ClassificationScopeTypeDef",
    {
        "excludes": S3ClassificationScopeExclusionTypeDef,
    },
)

S3ClassificationScopeUpdateTypeDef = TypedDict(
    "S3ClassificationScopeUpdateTypeDef",
    {
        "excludes": S3ClassificationScopeExclusionUpdateTypeDef,
    },
)

SearchResourcesTagCriterionTypeDef = TypedDict(
    "SearchResourcesTagCriterionTypeDef",
    {
        "comparator": SearchResourcesComparatorType,
        "tagValues": Sequence[SearchResourcesTagCriterionPairTypeDef],
    },
    total=False,
)

SensitivityInspectionTemplateExcludesUnionTypeDef = Union[
    SensitivityInspectionTemplateExcludesTypeDef, SensitivityInspectionTemplateExcludesOutputTypeDef
]
SensitivityInspectionTemplateIncludesUnionTypeDef = Union[
    SensitivityInspectionTemplateIncludesTypeDef, SensitivityInspectionTemplateIncludesOutputTypeDef
]
_RequiredUpdateSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "description": str,
        "excludes": SensitivityInspectionTemplateExcludesTypeDef,
        "includes": SensitivityInspectionTemplateIncludesTypeDef,
    },
    total=False,
)


class UpdateSensitivityInspectionTemplateRequestRequestTypeDef(
    _RequiredUpdateSensitivityInspectionTemplateRequestRequestTypeDef,
    _OptionalUpdateSensitivityInspectionTemplateRequestRequestTypeDef,
):
    pass


UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "serviceLimit": ServiceLimitTypeDef,
        "type": UsageTypeType,
    },
    total=False,
)

SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {
        "attributes": SessionContextAttributesTypeDef,
        "sessionIssuer": SessionIssuerTypeDef,
    },
    total=False,
)

_RequiredUpdateResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceProfileDetectionsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalUpdateResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceProfileDetectionsRequestRequestTypeDef",
    {
        "suppressDataIdentifiers": Sequence[SuppressDataIdentifierTypeDef],
    },
    total=False,
)


class UpdateResourceProfileDetectionsRequestRequestTypeDef(
    _RequiredUpdateResourceProfileDetectionsRequestRequestTypeDef,
    _OptionalUpdateResourceProfileDetectionsRequestRequestTypeDef,
):
    pass


TagCriterionForJobOutputTypeDef = TypedDict(
    "TagCriterionForJobOutputTypeDef",
    {
        "comparator": JobComparatorType,
        "tagValues": List[TagCriterionPairForJobTypeDef],
    },
    total=False,
)

TagCriterionForJobTypeDef = TypedDict(
    "TagCriterionForJobTypeDef",
    {
        "comparator": JobComparatorType,
        "tagValues": Sequence[TagCriterionPairForJobTypeDef],
    },
    total=False,
)

TagScopeTermOutputTypeDef = TypedDict(
    "TagScopeTermOutputTypeDef",
    {
        "comparator": JobComparatorType,
        "key": str,
        "tagValues": List[TagValuePairTypeDef],
        "target": Literal["S3_OBJECT"],
    },
    total=False,
)

TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": JobComparatorType,
        "key": str,
        "tagValues": Sequence[TagValuePairTypeDef],
        "target": Literal["S3_OBJECT"],
    },
    total=False,
)

_RequiredCreateAllowListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAllowListRequestRequestTypeDef",
    {
        "clientToken": str,
        "criteria": AllowListCriteriaTypeDef,
        "name": str,
    },
)
_OptionalCreateAllowListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAllowListRequestRequestTypeDef",
    {
        "description": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateAllowListRequestRequestTypeDef(
    _RequiredCreateAllowListRequestRequestTypeDef, _OptionalCreateAllowListRequestRequestTypeDef
):
    pass


GetAllowListResponseTypeDef = TypedDict(
    "GetAllowListResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "criteria": AllowListCriteriaTypeDef,
        "description": str,
        "id": str,
        "name": str,
        "status": AllowListStatusTypeDef,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateAllowListRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAllowListRequestRequestTypeDef",
    {
        "criteria": AllowListCriteriaTypeDef,
        "id": str,
        "name": str,
    },
)
_OptionalUpdateAllowListRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAllowListRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateAllowListRequestRequestTypeDef(
    _RequiredUpdateAllowListRequestRequestTypeDef, _OptionalUpdateAllowListRequestRequestTypeDef
):
    pass


BucketPermissionConfigurationTypeDef = TypedDict(
    "BucketPermissionConfigurationTypeDef",
    {
        "accountLevelPermissions": AccountLevelPermissionsTypeDef,
        "bucketLevelPermissions": BucketLevelPermissionsTypeDef,
    },
    total=False,
)

MatchingResourceTypeDef = TypedDict(
    "MatchingResourceTypeDef",
    {
        "matchingBucket": MatchingBucketTypeDef,
    },
    total=False,
)

GetBucketStatisticsResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": BucketCountByEffectivePermissionTypeDef,
        "bucketCountByEncryptionType": BucketCountByEncryptionTypeTypeDef,
        "bucketCountByObjectEncryptionRequirement": (
            BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef
        ),
        "bucketCountBySharedAccessType": BucketCountBySharedAccessTypeTypeDef,
        "bucketStatisticsBySensitivity": BucketStatisticsBySensitivityTypeDef,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": ObjectLevelStatisticsTypeDef,
        "unclassifiableObjectSizeInBytes": ObjectLevelStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetClassificationExportConfigurationResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": ClassificationExportConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutClassificationExportConfigurationRequestRequestTypeDef = TypedDict(
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    {
        "configuration": ClassificationExportConfigurationTypeDef,
    },
)

PutClassificationExportConfigurationResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": ClassificationExportConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFindingsFilterResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "description": str,
        "findingCriteria": FindingCriteriaOutputTypeDef,
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFindingsFilterRequestRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "findingCriteria": FindingCriteriaTypeDef,
        "name": str,
    },
)
_OptionalCreateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFindingsFilterRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "position": int,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateFindingsFilterRequestRequestTypeDef(
    _RequiredCreateFindingsFilterRequestRequestTypeDef,
    _OptionalCreateFindingsFilterRequestRequestTypeDef,
):
    pass


FindingCriteriaUnionTypeDef = Union[FindingCriteriaTypeDef, FindingCriteriaOutputTypeDef]
_RequiredGetFindingStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingStatisticsRequestRequestTypeDef",
    {
        "groupBy": GroupByType,
    },
)
_OptionalGetFindingStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingStatisticsRequestRequestTypeDef",
    {
        "findingCriteria": FindingCriteriaTypeDef,
        "size": int,
        "sortCriteria": FindingStatisticsSortCriteriaTypeDef,
    },
    total=False,
)


class GetFindingStatisticsRequestRequestTypeDef(
    _RequiredGetFindingStatisticsRequestRequestTypeDef,
    _OptionalGetFindingStatisticsRequestRequestTypeDef,
):
    pass


ListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "ListFindingsRequestListFindingsPaginateTypeDef",
    {
        "findingCriteria": FindingCriteriaTypeDef,
        "sortCriteria": SortCriteriaTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "findingCriteria": FindingCriteriaTypeDef,
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": SortCriteriaTypeDef,
    },
    total=False,
)

_RequiredUpdateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateFindingsFilterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsFilterRequestRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "clientToken": str,
        "description": str,
        "findingCriteria": FindingCriteriaTypeDef,
        "name": str,
        "position": int,
    },
    total=False,
)


class UpdateFindingsFilterRequestRequestTypeDef(
    _RequiredUpdateFindingsFilterRequestRequestTypeDef,
    _OptionalUpdateFindingsFilterRequestRequestTypeDef,
):
    pass


JobScheduleFrequencyUnionTypeDef = Union[
    JobScheduleFrequencyTypeDef, JobScheduleFrequencyOutputTypeDef
]
ListClassificationJobsRequestListClassificationJobsPaginateTypeDef = TypedDict(
    "ListClassificationJobsRequestListClassificationJobsPaginateTypeDef",
    {
        "filterCriteria": ListJobsFilterCriteriaTypeDef,
        "sortCriteria": ListJobsSortCriteriaTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListClassificationJobsRequestRequestTypeDef",
    {
        "filterCriteria": ListJobsFilterCriteriaTypeDef,
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": ListJobsSortCriteriaTypeDef,
    },
    total=False,
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "cells": List[CellTypeDef],
        "lineRanges": List[RangeTypeDef],
        "offsetRanges": List[RangeTypeDef],
        "pages": List[PageTypeDef],
        "records": List[RecordTypeDef],
    },
    total=False,
)

GetClassificationScopeResponseTypeDef = TypedDict(
    "GetClassificationScopeResponseTypeDef",
    {
        "id": str,
        "name": str,
        "s3": S3ClassificationScopeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateClassificationScopeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClassificationScopeRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateClassificationScopeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClassificationScopeRequestRequestTypeDef",
    {
        "s3": S3ClassificationScopeUpdateTypeDef,
    },
    total=False,
)


class UpdateClassificationScopeRequestRequestTypeDef(
    _RequiredUpdateClassificationScopeRequestRequestTypeDef,
    _OptionalUpdateClassificationScopeRequestRequestTypeDef,
):
    pass


SearchResourcesCriteriaTypeDef = TypedDict(
    "SearchResourcesCriteriaTypeDef",
    {
        "simpleCriterion": SearchResourcesSimpleCriterionTypeDef,
        "tagCriterion": SearchResourcesTagCriterionTypeDef,
    },
    total=False,
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "accountId": str,
        "automatedDiscoveryFreeTrialStartDate": datetime,
        "freeTrialStartDate": datetime,
        "usage": List[UsageByAccountTypeDef],
    },
    total=False,
)

AssumedRoleTypeDef = TypedDict(
    "AssumedRoleTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": SessionContextTypeDef,
    },
    total=False,
)

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": SessionContextTypeDef,
    },
    total=False,
)

CriteriaForJobOutputTypeDef = TypedDict(
    "CriteriaForJobOutputTypeDef",
    {
        "simpleCriterion": SimpleCriterionForJobOutputTypeDef,
        "tagCriterion": TagCriterionForJobOutputTypeDef,
    },
    total=False,
)

CriteriaForJobTypeDef = TypedDict(
    "CriteriaForJobTypeDef",
    {
        "simpleCriterion": SimpleCriterionForJobTypeDef,
        "tagCriterion": TagCriterionForJobTypeDef,
    },
    total=False,
)

JobScopeTermOutputTypeDef = TypedDict(
    "JobScopeTermOutputTypeDef",
    {
        "simpleScopeTerm": SimpleScopeTermOutputTypeDef,
        "tagScopeTerm": TagScopeTermOutputTypeDef,
    },
    total=False,
)

JobScopeTermTypeDef = TypedDict(
    "JobScopeTermTypeDef",
    {
        "simpleScopeTerm": SimpleScopeTermTypeDef,
        "tagScopeTerm": TagScopeTermTypeDef,
    },
    total=False,
)

BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": EffectivePermissionType,
        "permissionConfiguration": BucketPermissionConfigurationTypeDef,
    },
    total=False,
)

SearchResourcesResponseTypeDef = TypedDict(
    "SearchResourcesResponseTypeDef",
    {
        "matchingResources": List[MatchingResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {
        "arn": str,
        "count": int,
        "name": str,
        "occurrences": OccurrencesTypeDef,
    },
    total=False,
)

DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {
        "count": int,
        "occurrences": OccurrencesTypeDef,
        "type": str,
    },
    total=False,
)

SearchResourcesCriteriaBlockTypeDef = TypedDict(
    "SearchResourcesCriteriaBlockTypeDef",
    {
        "and": Sequence[SearchResourcesCriteriaTypeDef],
    },
    total=False,
)

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "nextToken": str,
        "records": List[UsageRecordTypeDef],
        "timeRange": TimeRangeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "assumedRole": AssumedRoleTypeDef,
        "awsAccount": AwsAccountTypeDef,
        "awsService": AwsServiceTypeDef,
        "federatedUser": FederatedUserTypeDef,
        "iamUser": IamUserTypeDef,
        "root": UserIdentityRootTypeDef,
        "type": UserIdentityTypeType,
    },
    total=False,
)

CriteriaBlockForJobOutputTypeDef = TypedDict(
    "CriteriaBlockForJobOutputTypeDef",
    {
        "and": List[CriteriaForJobOutputTypeDef],
    },
    total=False,
)

CriteriaBlockForJobTypeDef = TypedDict(
    "CriteriaBlockForJobTypeDef",
    {
        "and": Sequence[CriteriaForJobTypeDef],
    },
    total=False,
)

JobScopingBlockOutputTypeDef = TypedDict(
    "JobScopingBlockOutputTypeDef",
    {
        "and": List[JobScopeTermOutputTypeDef],
    },
    total=False,
)

JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef",
    {
        "and": Sequence[JobScopeTermTypeDef],
    },
    total=False,
)

BucketMetadataTypeDef = TypedDict(
    "BucketMetadataTypeDef",
    {
        "accountId": str,
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploadsType,
        "bucketArn": str,
        "bucketCreatedAt": datetime,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "errorCode": Literal["ACCESS_DENIED"],
        "errorMessage": str,
        "jobDetails": JobDetailsTypeDef,
        "lastAutomatedDiscoveryTime": datetime,
        "lastUpdated": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": ObjectCountByEncryptionTypeTypeDef,
        "publicAccess": BucketPublicAccessTypeDef,
        "region": str,
        "replicationDetails": ReplicationDetailsTypeDef,
        "sensitivityScore": int,
        "serverSideEncryption": BucketServerSideEncryptionTypeDef,
        "sharedAccess": SharedAccessType,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "tags": List[KeyValuePairTypeDef],
        "unclassifiableObjectCount": ObjectLevelStatisticsTypeDef,
        "unclassifiableObjectSizeInBytes": ObjectLevelStatisticsTypeDef,
        "versioning": bool,
    },
    total=False,
)

S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploadsType,
        "arn": str,
        "createdAt": datetime,
        "defaultServerSideEncryption": ServerSideEncryptionTypeDef,
        "name": str,
        "owner": S3BucketOwnerTypeDef,
        "publicAccess": BucketPublicAccessTypeDef,
        "tags": List[KeyValuePairTypeDef],
    },
    total=False,
)

CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {
        "detections": List[CustomDetectionTypeDef],
        "totalCount": int,
    },
    total=False,
)

SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": SensitiveDataItemCategoryType,
        "detections": List[DefaultDetectionTypeDef],
        "totalCount": int,
    },
    total=False,
)

SearchResourcesBucketCriteriaTypeDef = TypedDict(
    "SearchResourcesBucketCriteriaTypeDef",
    {
        "excludes": SearchResourcesCriteriaBlockTypeDef,
        "includes": SearchResourcesCriteriaBlockTypeDef,
    },
    total=False,
)

FindingActorTypeDef = TypedDict(
    "FindingActorTypeDef",
    {
        "domainDetails": DomainDetailsTypeDef,
        "ipAddressDetails": IpAddressDetailsTypeDef,
        "userIdentity": UserIdentityTypeDef,
    },
    total=False,
)

S3BucketCriteriaForJobOutputTypeDef = TypedDict(
    "S3BucketCriteriaForJobOutputTypeDef",
    {
        "excludes": CriteriaBlockForJobOutputTypeDef,
        "includes": CriteriaBlockForJobOutputTypeDef,
    },
    total=False,
)

S3BucketCriteriaForJobTypeDef = TypedDict(
    "S3BucketCriteriaForJobTypeDef",
    {
        "excludes": CriteriaBlockForJobTypeDef,
        "includes": CriteriaBlockForJobTypeDef,
    },
    total=False,
)

ScopingOutputTypeDef = TypedDict(
    "ScopingOutputTypeDef",
    {
        "excludes": JobScopingBlockOutputTypeDef,
        "includes": JobScopingBlockOutputTypeDef,
    },
    total=False,
)

ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {
        "excludes": JobScopingBlockTypeDef,
        "includes": JobScopingBlockTypeDef,
    },
    total=False,
)

DescribeBucketsResponseTypeDef = TypedDict(
    "DescribeBucketsResponseTypeDef",
    {
        "buckets": List[BucketMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {
        "s3Bucket": S3BucketTypeDef,
        "s3Object": S3ObjectTypeDef,
    },
    total=False,
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "additionalOccurrences": bool,
        "customDataIdentifiers": CustomDataIdentifiersTypeDef,
        "mimeType": str,
        "sensitiveData": List[SensitiveDataItemTypeDef],
        "sizeClassified": int,
        "status": ClassificationResultStatusTypeDef,
    },
    total=False,
)

SearchResourcesRequestRequestTypeDef = TypedDict(
    "SearchResourcesRequestRequestTypeDef",
    {
        "bucketCriteria": SearchResourcesBucketCriteriaTypeDef,
        "maxResults": int,
        "nextToken": str,
        "sortCriteria": SearchResourcesSortCriteriaTypeDef,
    },
    total=False,
)

SearchResourcesRequestSearchResourcesPaginateTypeDef = TypedDict(
    "SearchResourcesRequestSearchResourcesPaginateTypeDef",
    {
        "bucketCriteria": SearchResourcesBucketCriteriaTypeDef,
        "sortCriteria": SearchResourcesSortCriteriaTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "action": FindingActionTypeDef,
        "actor": FindingActorTypeDef,
    },
    total=False,
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketCriteria": S3BucketCriteriaForJobOutputTypeDef,
        "bucketDefinitions": List[S3BucketDefinitionForJobOutputTypeDef],
        "createdAt": datetime,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": LastRunErrorStatusTypeDef,
        "name": str,
        "userPausedDetails": UserPausedDetailsTypeDef,
    },
    total=False,
)

S3JobDefinitionOutputTypeDef = TypedDict(
    "S3JobDefinitionOutputTypeDef",
    {
        "bucketCriteria": S3BucketCriteriaForJobOutputTypeDef,
        "bucketDefinitions": List[S3BucketDefinitionForJobOutputTypeDef],
        "scoping": ScopingOutputTypeDef,
    },
    total=False,
)

S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {
        "bucketCriteria": S3BucketCriteriaForJobTypeDef,
        "bucketDefinitions": Sequence[S3BucketDefinitionForJobTypeDef],
        "scoping": ScopingTypeDef,
    },
    total=False,
)

ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": str,
        "jobArn": str,
        "jobId": str,
        "originType": OriginTypeType,
        "result": ClassificationResultTypeDef,
    },
    total=False,
)

ListClassificationJobsResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseTypeDef",
    {
        "items": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeClassificationJobResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseTypeDef",
    {
        "allowListIds": List[str],
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": LastRunErrorStatusTypeDef,
        "lastRunTime": datetime,
        "managedDataIdentifierIds": List[str],
        "managedDataIdentifierSelector": ManagedDataIdentifierSelectorType,
        "name": str,
        "s3JobDefinition": S3JobDefinitionOutputTypeDef,
        "samplingPercentage": int,
        "scheduleFrequency": JobScheduleFrequencyOutputTypeDef,
        "statistics": StatisticsTypeDef,
        "tags": Dict[str, str],
        "userPausedDetails": UserPausedDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateClassificationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClassificationJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "jobType": JobTypeType,
        "name": str,
        "s3JobDefinition": S3JobDefinitionTypeDef,
    },
)
_OptionalCreateClassificationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClassificationJobRequestRequestTypeDef",
    {
        "allowListIds": Sequence[str],
        "customDataIdentifierIds": Sequence[str],
        "description": str,
        "initialRun": bool,
        "managedDataIdentifierIds": Sequence[str],
        "managedDataIdentifierSelector": ManagedDataIdentifierSelectorType,
        "samplingPercentage": int,
        "scheduleFrequency": JobScheduleFrequencyTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateClassificationJobRequestRequestTypeDef(
    _RequiredCreateClassificationJobRequestRequestTypeDef,
    _OptionalCreateClassificationJobRequestRequestTypeDef,
):
    pass


S3JobDefinitionUnionTypeDef = Union[S3JobDefinitionTypeDef, S3JobDefinitionOutputTypeDef]
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": str,
        "archived": bool,
        "category": FindingCategoryType,
        "classificationDetails": ClassificationDetailsTypeDef,
        "count": int,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "partition": str,
        "policyDetails": PolicyDetailsTypeDef,
        "region": str,
        "resourcesAffected": ResourcesAffectedTypeDef,
        "sample": bool,
        "schemaVersion": str,
        "severity": SeverityTypeDef,
        "title": str,
        "type": FindingTypeType,
        "updatedAt": datetime,
    },
    total=False,
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "findings": List[FindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
