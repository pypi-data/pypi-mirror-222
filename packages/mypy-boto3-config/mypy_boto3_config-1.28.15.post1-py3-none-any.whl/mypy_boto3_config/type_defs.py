"""
Type annotations for config service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs/)

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceOutputTypeDef

    data: AccountAggregationSourceOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregateConformancePackComplianceSummaryGroupKeyType,
    AggregatedSourceStatusTypeType,
    AggregatedSourceTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ConfigRuleComplianceSummaryGroupKeyType,
    ConfigRuleStateType,
    ConfigurationItemStatusType,
    ConformancePackComplianceTypeType,
    ConformancePackStateType,
    DeliveryStatusType,
    EvaluationModeType,
    MaximumExecutionFrequencyType,
    MemberAccountRuleStatusType,
    MessageTypeType,
    OrganizationConfigRuleTriggerTypeNoSNType,
    OrganizationConfigRuleTriggerTypeType,
    OrganizationResourceDetailedStatusType,
    OrganizationResourceStatusType,
    OrganizationRuleStatusType,
    OwnerType,
    RecorderStatusType,
    RecordingStrategyTypeType,
    RemediationExecutionStateType,
    RemediationExecutionStepStateType,
    ResourceCountGroupKeyType,
    ResourceEvaluationStatusType,
    ResourceTypeType,
    SortOrderType,
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
    "AccountAggregationSourceOutputTypeDef",
    "AccountAggregationSourceTypeDef",
    "AggregateConformancePackComplianceTypeDef",
    "AggregateConformancePackComplianceCountTypeDef",
    "AggregateConformancePackComplianceFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "BaseConfigurationItemTypeDef",
    "ResponseMetadataTypeDef",
    "ResourceKeyTypeDef",
    "ComplianceContributorCountTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "EvaluationModeConfigurationTypeDef",
    "ScopeOutputTypeDef",
    "ScopeTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "OrganizationAggregationSourceOutputTypeDef",
    "RelationshipTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceScoreTypeDef",
    "ConformancePackComplianceScoresFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackInputParameterTypeDef",
    "TemplateSSMDocumentDetailsTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "CustomPolicyDetailsTypeDef",
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    "DeleteConfigRuleRequestRequestTypeDef",
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    "DeleteConformancePackRequestRequestTypeDef",
    "DeleteDeliveryChannelRequestRequestTypeDef",
    "DeleteEvaluationResultsRequestRequestTypeDef",
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    "DeleteRemediationConfigurationRequestRequestTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "DeleteResourceConfigRequestRequestTypeDef",
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    "DeleteStoredQueryRequestRequestTypeDef",
    "DeliverConfigSnapshotRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    "DescribeComplianceByResourceRequestRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    "DescribeConfigRulesFiltersTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    "DescribeConformancePackStatusRequestRequestTypeDef",
    "DescribeConformancePacksRequestRequestTypeDef",
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    "PendingAggregationRequestTypeDef",
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    "RemediationExceptionTypeDef",
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    "RetentionConfigurationTypeDef",
    "EvaluationContextTypeDef",
    "EvaluationOutputTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationStatusTypeDef",
    "EvaluationTypeDef",
    "ExclusionByResourceTypesOutputTypeDef",
    "ExclusionByResourceTypesTypeDef",
    "SsmControlsTypeDef",
    "ExternalEvaluationTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "ResourceCountFiltersTypeDef",
    "GroupedResourceCountTypeDef",
    "GetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    "GetConformancePackComplianceSummaryRequestRequestTypeDef",
    "GetCustomRulePolicyRequestRequestTypeDef",
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    "ResourceCountTypeDef",
    "StatusDetailFiltersTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "GetOrganizationCustomRulePolicyRequestRequestTypeDef",
    "GetResourceConfigHistoryRequestRequestTypeDef",
    "GetResourceEvaluationSummaryRequestRequestTypeDef",
    "ResourceDetailsTypeDef",
    "GetStoredQueryRequestRequestTypeDef",
    "StoredQueryTypeDef",
    "ResourceFiltersTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceEvaluationTypeDef",
    "ListStoredQueriesRequestRequestTypeDef",
    "StoredQueryMetadataTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef",
    "OrganizationCustomRuleMetadataOutputTypeDef",
    "OrganizationManagedRuleMetadataOutputTypeDef",
    "OrganizationCustomPolicyRuleMetadataTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "PutResourceConfigRequestRequestTypeDef",
    "PutRetentionConfigurationRequestRequestTypeDef",
    "RecordingStrategyTypeDef",
    "RemediationExecutionStepTypeDef",
    "ResourceValueTypeDef",
    "StaticValueOutputTypeDef",
    "StaticValueTypeDef",
    "TimeWindowTypeDef",
    "SelectAggregateResourceConfigRequestRequestTypeDef",
    "SelectResourceConfigRequestRequestTypeDef",
    "SourceDetailTypeDef",
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    "StartConfigurationRecorderRequestRequestTypeDef",
    "StopConfigurationRecorderRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AggregateComplianceByConformancePackTypeDef",
    "AggregateConformancePackComplianceSummaryTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    "GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    "GetAggregateResourceConfigRequestRequestTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCustomRulePolicyResponseTypeDef",
    "GetOrganizationCustomRulePolicyResponseTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutStoredQueryResponseTypeDef",
    "StartResourceEvaluationResponseTypeDef",
    "BatchGetResourceConfigRequestRequestTypeDef",
    "BatchGetResourceConfigResponseTypeDef",
    "DescribeRemediationExecutionStatusRequestRequestTypeDef",
    "StartRemediationExecutionRequestRequestTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    "GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DeliveryChannelTypeDef",
    "DeliveryChannelStatusTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConformancePackComplianceRequestRequestTypeDef",
    "ListConformancePackComplianceScoresResponseTypeDef",
    "ListConformancePackComplianceScoresRequestRequestTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "OrganizationConformancePackTypeDef",
    "PutOrganizationConformancePackRequestRequestTypeDef",
    "ConformancePackDetailTypeDef",
    "PutConformancePackRequestRequestTypeDef",
    "GetConformancePackComplianceDetailsRequestRequestTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    "DescribeRemediationExceptionsRequestRequestTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "PutRemediationExceptionsRequestRequestTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef",
    "DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateTypeDef",
    "DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef",
    "DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef",
    "DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef",
    "DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef",
    "DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef",
    "DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef",
    "DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef",
    "DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef",
    "DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef",
    "DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef",
    "GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef",
    "GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef",
    "GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef",
    "GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef",
    "ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef",
    "SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef",
    "DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef",
    "DescribeConfigRulesRequestRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "PutEvaluationsResponseTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "PutEvaluationsRequestRequestTypeDef",
    "ExecutionControlsTypeDef",
    "PutExternalEvaluationRequestRequestTypeDef",
    "QueryInfoTypeDef",
    "GetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetResourceEvaluationSummaryResponseTypeDef",
    "StartResourceEvaluationRequestRequestTypeDef",
    "GetStoredQueryResponseTypeDef",
    "ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef",
    "ListAggregateDiscoveredResourcesRequestRequestTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListResourceEvaluationsResponseTypeDef",
    "ListStoredQueriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutAggregationAuthorizationRequestRequestTypeDef",
    "PutStoredQueryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "PutConfigurationAggregatorRequestRequestTypeDef",
    "OrganizationConfigRuleTypeDef",
    "PutOrganizationConfigRuleRequestRequestTypeDef",
    "RecordingGroupOutputTypeDef",
    "RecordingGroupTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationParameterValueOutputTypeDef",
    "RemediationParameterValueTypeDef",
    "ResourceEvaluationFiltersTypeDef",
    "SourceOutputTypeDef",
    "SourceTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    "AggregateComplianceCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "PutDeliveryChannelRequestRequestTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "AggregateEvaluationResultTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "EvaluationResultTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "ConfigurationRecorderOutputTypeDef",
    "ConfigurationRecorderTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "RemediationConfigurationOutputTypeDef",
    "RemediationConfigurationTypeDef",
    "ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef",
    "ListResourceEvaluationsRequestRequestTypeDef",
    "ConfigRuleOutputTypeDef",
    "ConfigRuleTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "PutConfigurationRecorderRequestRequestTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "FailedRemediationBatchTypeDef",
    "PutRemediationConfigurationsRequestRequestTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "PutConfigRuleRequestRequestTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
)

_RequiredAccountAggregationSourceOutputTypeDef = TypedDict(
    "_RequiredAccountAggregationSourceOutputTypeDef",
    {
        "AccountIds": List[str],
    },
)
_OptionalAccountAggregationSourceOutputTypeDef = TypedDict(
    "_OptionalAccountAggregationSourceOutputTypeDef",
    {
        "AllAwsRegions": bool,
        "AwsRegions": List[str],
    },
    total=False,
)


class AccountAggregationSourceOutputTypeDef(
    _RequiredAccountAggregationSourceOutputTypeDef, _OptionalAccountAggregationSourceOutputTypeDef
):
    pass


_RequiredAccountAggregationSourceTypeDef = TypedDict(
    "_RequiredAccountAggregationSourceTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
_OptionalAccountAggregationSourceTypeDef = TypedDict(
    "_OptionalAccountAggregationSourceTypeDef",
    {
        "AllAwsRegions": bool,
        "AwsRegions": Sequence[str],
    },
    total=False,
)


class AccountAggregationSourceTypeDef(
    _RequiredAccountAggregationSourceTypeDef, _OptionalAccountAggregationSourceTypeDef
):
    pass


AggregateConformancePackComplianceTypeDef = TypedDict(
    "AggregateConformancePackComplianceTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "CompliantRuleCount": int,
        "NonCompliantRuleCount": int,
        "TotalRuleCount": int,
    },
    total=False,
)

AggregateConformancePackComplianceCountTypeDef = TypedDict(
    "AggregateConformancePackComplianceCountTypeDef",
    {
        "CompliantConformancePackCount": int,
        "NonCompliantConformancePackCount": int,
    },
    total=False,
)

AggregateConformancePackComplianceFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceFiltersTypeDef",
    {
        "ConformancePackName": str,
        "ComplianceType": ConformancePackComplianceTypeType,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateConformancePackComplianceSummaryFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    {
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

_RequiredAggregateResourceIdentifierTypeDef = TypedDict(
    "_RequiredAggregateResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalAggregateResourceIdentifierTypeDef = TypedDict(
    "_OptionalAggregateResourceIdentifierTypeDef",
    {
        "ResourceName": str,
    },
    total=False,
)


class AggregateResourceIdentifierTypeDef(
    _RequiredAggregateResourceIdentifierTypeDef, _OptionalAggregateResourceIdentifierTypeDef
):
    pass


AggregatedSourceStatusTypeDef = TypedDict(
    "AggregatedSourceStatusTypeDef",
    {
        "SourceId": str,
        "SourceType": AggregatedSourceTypeType,
        "AwsRegion": str,
        "LastUpdateStatus": AggregatedSourceStatusTypeType,
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)

AggregationAuthorizationTypeDef = TypedDict(
    "AggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

BaseConfigurationItemTypeDef = TypedDict(
    "BaseConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": ConfigurationItemStatusType,
        "configurationStateId": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
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

ResourceKeyTypeDef = TypedDict(
    "ResourceKeyTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)

ComplianceContributorCountTypeDef = TypedDict(
    "ComplianceContributorCountTypeDef",
    {
        "CappedCount": int,
        "CapExceeded": bool,
    },
    total=False,
)

ConfigExportDeliveryInfoTypeDef = TypedDict(
    "ConfigExportDeliveryInfoTypeDef",
    {
        "lastStatus": DeliveryStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)

ConfigRuleComplianceFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceFiltersTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": ComplianceTypeType,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    {
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleEvaluationStatusTypeDef = TypedDict(
    "ConfigRuleEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastDeactivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
        "LastDebugLogDeliveryStatus": str,
        "LastDebugLogDeliveryStatusReason": str,
        "LastDebugLogDeliveryTime": datetime,
    },
    total=False,
)

EvaluationModeConfigurationTypeDef = TypedDict(
    "EvaluationModeConfigurationTypeDef",
    {
        "Mode": EvaluationModeType,
    },
    total=False,
)

ScopeOutputTypeDef = TypedDict(
    "ScopeOutputTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "ComplianceResourceTypes": Sequence[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

ConfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": MaximumExecutionFrequencyType,
    },
    total=False,
)

ConfigStreamDeliveryInfoTypeDef = TypedDict(
    "ConfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": DeliveryStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

_RequiredOrganizationAggregationSourceOutputTypeDef = TypedDict(
    "_RequiredOrganizationAggregationSourceOutputTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalOrganizationAggregationSourceOutputTypeDef = TypedDict(
    "_OptionalOrganizationAggregationSourceOutputTypeDef",
    {
        "AwsRegions": List[str],
        "AllAwsRegions": bool,
    },
    total=False,
)


class OrganizationAggregationSourceOutputTypeDef(
    _RequiredOrganizationAggregationSourceOutputTypeDef,
    _OptionalOrganizationAggregationSourceOutputTypeDef,
):
    pass


RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)

ConfigurationRecorderStatusTypeDef = TypedDict(
    "ConfigurationRecorderStatusTypeDef",
    {
        "name": str,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "recording": bool,
        "lastStatus": RecorderStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConformancePackComplianceFiltersTypeDef = TypedDict(
    "ConformancePackComplianceFiltersTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "ComplianceType": ConformancePackComplianceTypeType,
    },
    total=False,
)

ConformancePackComplianceScoreTypeDef = TypedDict(
    "ConformancePackComplianceScoreTypeDef",
    {
        "Score": str,
        "ConformancePackName": str,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ConformancePackComplianceScoresFiltersTypeDef = TypedDict(
    "ConformancePackComplianceScoresFiltersTypeDef",
    {
        "ConformancePackNames": Sequence[str],
    },
)

ConformancePackComplianceSummaryTypeDef = TypedDict(
    "ConformancePackComplianceSummaryTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": ConformancePackComplianceTypeType,
    },
)

ConformancePackInputParameterTypeDef = TypedDict(
    "ConformancePackInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
)

_RequiredTemplateSSMDocumentDetailsTypeDef = TypedDict(
    "_RequiredTemplateSSMDocumentDetailsTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalTemplateSSMDocumentDetailsTypeDef = TypedDict(
    "_OptionalTemplateSSMDocumentDetailsTypeDef",
    {
        "DocumentVersion": str,
    },
    total=False,
)


class TemplateSSMDocumentDetailsTypeDef(
    _RequiredTemplateSSMDocumentDetailsTypeDef, _OptionalTemplateSSMDocumentDetailsTypeDef
):
    pass


ConformancePackEvaluationFiltersTypeDef = TypedDict(
    "ConformancePackEvaluationFiltersTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "ComplianceType": ConformancePackComplianceTypeType,
        "ResourceType": str,
        "ResourceIds": Sequence[str],
    },
    total=False,
)

ConformancePackRuleComplianceTypeDef = TypedDict(
    "ConformancePackRuleComplianceTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": ConformancePackComplianceTypeType,
        "Controls": List[str],
    },
    total=False,
)

_RequiredConformancePackStatusDetailTypeDef = TypedDict(
    "_RequiredConformancePackStatusDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": ConformancePackStateType,
        "StackArn": str,
        "LastUpdateRequestedTime": datetime,
    },
)
_OptionalConformancePackStatusDetailTypeDef = TypedDict(
    "_OptionalConformancePackStatusDetailTypeDef",
    {
        "ConformancePackStatusReason": str,
        "LastUpdateCompletedTime": datetime,
    },
    total=False,
)


class ConformancePackStatusDetailTypeDef(
    _RequiredConformancePackStatusDetailTypeDef, _OptionalConformancePackStatusDetailTypeDef
):
    pass


_RequiredCustomPolicyDetailsTypeDef = TypedDict(
    "_RequiredCustomPolicyDetailsTypeDef",
    {
        "PolicyRuntime": str,
        "PolicyText": str,
    },
)
_OptionalCustomPolicyDetailsTypeDef = TypedDict(
    "_OptionalCustomPolicyDetailsTypeDef",
    {
        "EnableDebugLogDelivery": bool,
    },
    total=False,
)


class CustomPolicyDetailsTypeDef(
    _RequiredCustomPolicyDetailsTypeDef, _OptionalCustomPolicyDetailsTypeDef
):
    pass


DeleteAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)

DeleteConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)

DeleteConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

DeleteConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)

DeleteDeliveryChannelRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannelName": str,
    },
)

DeleteEvaluationResultsRequestRequestTypeDef = TypedDict(
    "DeleteEvaluationResultsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)

DeleteOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)

DeletePendingAggregationRequestRequestRequestTypeDef = TypedDict(
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
)

_RequiredDeleteRemediationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRemediationConfigurationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDeleteRemediationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRemediationConfigurationRequestRequestTypeDef",
    {
        "ResourceType": str,
    },
    total=False,
)


class DeleteRemediationConfigurationRequestRequestTypeDef(
    _RequiredDeleteRemediationConfigurationRequestRequestTypeDef,
    _OptionalDeleteRemediationConfigurationRequestRequestTypeDef,
):
    pass


RemediationExceptionResourceKeyTypeDef = TypedDict(
    "RemediationExceptionResourceKeyTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
    total=False,
)

DeleteResourceConfigRequestRequestTypeDef = TypedDict(
    "DeleteResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)

DeleteRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionConfigurationName": str,
    },
)

DeleteStoredQueryRequestRequestTypeDef = TypedDict(
    "DeleteStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)

DeliverConfigSnapshotRequestRequestTypeDef = TypedDict(
    "DeliverConfigSnapshotRequestRequestTypeDef",
    {
        "deliveryChannelName": str,
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

DescribeAggregationAuthorizationsRequestRequestTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeComplianceByConfigRuleRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "NextToken": str,
    },
    total=False,
)

DescribeComplianceByResourceRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConfigRuleEvaluationStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeConfigRulesFiltersTypeDef = TypedDict(
    "DescribeConfigRulesFiltersTypeDef",
    {
        "EvaluationMode": EvaluationModeType,
    },
    total=False,
)

_RequiredDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    {
        "UpdateStatus": Sequence[AggregatedSourceStatusTypeType],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef(
    _RequiredDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef,
    _OptionalDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef,
):
    pass


DescribeConfigurationAggregatorsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorNames": Sequence[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeConfigurationRecorderStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": Sequence[str],
    },
    total=False,
)

DescribeConfigurationRecordersRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": Sequence[str],
    },
    total=False,
)

DescribeConformancePackStatusRequestRequestTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestRequestTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeConformancePacksRequestRequestTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDeliveryChannelStatusRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    {
        "DeliveryChannelNames": Sequence[str],
    },
    total=False,
)

DescribeDeliveryChannelsRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    {
        "DeliveryChannelNames": Sequence[str],
    },
    total=False,
)

DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": Sequence[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleStatusTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": OrganizationRuleStatusType,
    },
)
_OptionalOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConfigRuleStatusTypeDef(
    _RequiredOrganizationConfigRuleStatusTypeDef, _OptionalOrganizationConfigRuleStatusTypeDef
):
    pass


DescribeOrganizationConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": Sequence[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConformancePackStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": Sequence[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredOrganizationConformancePackStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackStatusTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": OrganizationResourceStatusType,
    },
)
_OptionalOrganizationConformancePackStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConformancePackStatusTypeDef(
    _RequiredOrganizationConformancePackStatusTypeDef,
    _OptionalOrganizationConformancePackStatusTypeDef,
):
    pass


DescribeOrganizationConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": Sequence[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribePendingAggregationRequestsRequestRequestTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

PendingAggregationRequestTypeDef = TypedDict(
    "PendingAggregationRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
    total=False,
)

DescribeRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
    },
)

_RequiredRemediationExceptionTypeDef = TypedDict(
    "_RequiredRemediationExceptionTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
    },
)
_OptionalRemediationExceptionTypeDef = TypedDict(
    "_OptionalRemediationExceptionTypeDef",
    {
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)


class RemediationExceptionTypeDef(
    _RequiredRemediationExceptionTypeDef, _OptionalRemediationExceptionTypeDef
):
    pass


DescribeRetentionConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    {
        "RetentionConfigurationNames": Sequence[str],
        "NextToken": str,
    },
    total=False,
)

RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef",
    {
        "Name": str,
        "RetentionPeriodInDays": int,
    },
)

EvaluationContextTypeDef = TypedDict(
    "EvaluationContextTypeDef",
    {
        "EvaluationContextIdentifier": str,
    },
    total=False,
)

_RequiredEvaluationOutputTypeDef = TypedDict(
    "_RequiredEvaluationOutputTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": datetime,
    },
)
_OptionalEvaluationOutputTypeDef = TypedDict(
    "_OptionalEvaluationOutputTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class EvaluationOutputTypeDef(_RequiredEvaluationOutputTypeDef, _OptionalEvaluationOutputTypeDef):
    pass


EvaluationResultQualifierTypeDef = TypedDict(
    "EvaluationResultQualifierTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "EvaluationMode": EvaluationModeType,
    },
    total=False,
)

_RequiredEvaluationStatusTypeDef = TypedDict(
    "_RequiredEvaluationStatusTypeDef",
    {
        "Status": ResourceEvaluationStatusType,
    },
)
_OptionalEvaluationStatusTypeDef = TypedDict(
    "_OptionalEvaluationStatusTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class EvaluationStatusTypeDef(_RequiredEvaluationStatusTypeDef, _OptionalEvaluationStatusTypeDef):
    pass


_RequiredEvaluationTypeDef = TypedDict(
    "_RequiredEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
    },
)
_OptionalEvaluationTypeDef = TypedDict(
    "_OptionalEvaluationTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class EvaluationTypeDef(_RequiredEvaluationTypeDef, _OptionalEvaluationTypeDef):
    pass


ExclusionByResourceTypesOutputTypeDef = TypedDict(
    "ExclusionByResourceTypesOutputTypeDef",
    {
        "resourceTypes": List[ResourceTypeType],
    },
    total=False,
)

ExclusionByResourceTypesTypeDef = TypedDict(
    "ExclusionByResourceTypesTypeDef",
    {
        "resourceTypes": Sequence[ResourceTypeType],
    },
    total=False,
)

SsmControlsTypeDef = TypedDict(
    "SsmControlsTypeDef",
    {
        "ConcurrentExecutionRatePercentage": int,
        "ErrorPercentage": int,
    },
    total=False,
)

_RequiredExternalEvaluationTypeDef = TypedDict(
    "_RequiredExternalEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
    },
)
_OptionalExternalEvaluationTypeDef = TypedDict(
    "_OptionalExternalEvaluationTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class ExternalEvaluationTypeDef(
    _RequiredExternalEvaluationTypeDef, _OptionalExternalEvaluationTypeDef
):
    pass


FieldInfoTypeDef = TypedDict(
    "FieldInfoTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
    },
)
_OptionalGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef(
    _RequiredGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef,
    _OptionalGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef,
):
    pass


ResourceCountFiltersTypeDef = TypedDict(
    "ResourceCountFiltersTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "AccountId": str,
        "Region": str,
    },
    total=False,
)

GroupedResourceCountTypeDef = TypedDict(
    "GroupedResourceCountTypeDef",
    {
        "GroupName": str,
        "ResourceCount": int,
    },
)

_RequiredGetComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredGetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalGetComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalGetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetComplianceDetailsByConfigRuleRequestRequestTypeDef(
    _RequiredGetComplianceDetailsByConfigRuleRequestRequestTypeDef,
    _OptionalGetComplianceDetailsByConfigRuleRequestRequestTypeDef,
):
    pass


GetComplianceDetailsByResourceRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "NextToken": str,
        "ResourceEvaluationId": str,
    },
    total=False,
)

GetComplianceSummaryByResourceTypeRequestRequestTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    {
        "ResourceTypes": Sequence[str],
    },
    total=False,
)

_RequiredGetConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConformancePackNames": Sequence[str],
    },
)
_OptionalGetConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetConformancePackComplianceSummaryRequestRequestTypeDef(
    _RequiredGetConformancePackComplianceSummaryRequestRequestTypeDef,
    _OptionalGetConformancePackComplianceSummaryRequestRequestTypeDef,
):
    pass


GetCustomRulePolicyRequestRequestTypeDef = TypedDict(
    "GetCustomRulePolicyRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
    total=False,
)

GetDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "resourceTypes": Sequence[str],
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "resourceType": ResourceTypeType,
        "count": int,
    },
    total=False,
)

StatusDetailFiltersTypeDef = TypedDict(
    "StatusDetailFiltersTypeDef",
    {
        "AccountId": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
    },
    total=False,
)

_RequiredMemberAccountStatusTypeDef = TypedDict(
    "_RequiredMemberAccountStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
    },
)
_OptionalMemberAccountStatusTypeDef = TypedDict(
    "_OptionalMemberAccountStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class MemberAccountStatusTypeDef(
    _RequiredMemberAccountStatusTypeDef, _OptionalMemberAccountStatusTypeDef
):
    pass


OrganizationResourceDetailedStatusFiltersTypeDef = TypedDict(
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    {
        "AccountId": str,
        "Status": OrganizationResourceDetailedStatusType,
    },
    total=False,
)

_RequiredOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": OrganizationResourceDetailedStatusType,
    },
)
_OptionalOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackDetailedStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConformancePackDetailedStatusTypeDef(
    _RequiredOrganizationConformancePackDetailedStatusTypeDef,
    _OptionalOrganizationConformancePackDetailedStatusTypeDef,
):
    pass


GetOrganizationCustomRulePolicyRequestRequestTypeDef = TypedDict(
    "GetOrganizationCustomRulePolicyRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)

_RequiredGetResourceConfigHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceConfigHistoryRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)
_OptionalGetResourceConfigHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceConfigHistoryRequestRequestTypeDef",
    {
        "laterTime": Union[datetime, str],
        "earlierTime": Union[datetime, str],
        "chronologicalOrder": ChronologicalOrderType,
        "limit": int,
        "nextToken": str,
    },
    total=False,
)


class GetResourceConfigHistoryRequestRequestTypeDef(
    _RequiredGetResourceConfigHistoryRequestRequestTypeDef,
    _OptionalGetResourceConfigHistoryRequestRequestTypeDef,
):
    pass


GetResourceEvaluationSummaryRequestRequestTypeDef = TypedDict(
    "GetResourceEvaluationSummaryRequestRequestTypeDef",
    {
        "ResourceEvaluationId": str,
    },
)

_RequiredResourceDetailsTypeDef = TypedDict(
    "_RequiredResourceDetailsTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ResourceConfiguration": str,
    },
)
_OptionalResourceDetailsTypeDef = TypedDict(
    "_OptionalResourceDetailsTypeDef",
    {
        "ResourceConfigurationSchemaType": Literal["CFN_RESOURCE_SCHEMA"],
    },
    total=False,
)


class ResourceDetailsTypeDef(_RequiredResourceDetailsTypeDef, _OptionalResourceDetailsTypeDef):
    pass


GetStoredQueryRequestRequestTypeDef = TypedDict(
    "GetStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)

_RequiredStoredQueryTypeDef = TypedDict(
    "_RequiredStoredQueryTypeDef",
    {
        "QueryName": str,
    },
)
_OptionalStoredQueryTypeDef = TypedDict(
    "_OptionalStoredQueryTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "Description": str,
        "Expression": str,
    },
    total=False,
)


class StoredQueryTypeDef(_RequiredStoredQueryTypeDef, _OptionalStoredQueryTypeDef):
    pass


ResourceFiltersTypeDef = TypedDict(
    "ResourceFiltersTypeDef",
    {
        "AccountId": str,
        "ResourceId": str,
        "ResourceName": str,
        "Region": str,
    },
    total=False,
)

_RequiredListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
    },
)
_OptionalListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestRequestTypeDef",
    {
        "resourceIds": Sequence[str],
        "resourceName": str,
        "limit": int,
        "includeDeletedResources": bool,
        "nextToken": str,
    },
    total=False,
)


class ListDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListDiscoveredResourcesRequestRequestTypeDef,
):
    pass


ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)

ResourceEvaluationTypeDef = TypedDict(
    "ResourceEvaluationTypeDef",
    {
        "ResourceEvaluationId": str,
        "EvaluationMode": EvaluationModeType,
        "EvaluationStartTimestamp": datetime,
    },
    total=False,
)

ListStoredQueriesRequestRequestTypeDef = TypedDict(
    "ListStoredQueriesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredStoredQueryMetadataTypeDef = TypedDict(
    "_RequiredStoredQueryMetadataTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "QueryName": str,
    },
)
_OptionalStoredQueryMetadataTypeDef = TypedDict(
    "_OptionalStoredQueryMetadataTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class StoredQueryMetadataTypeDef(
    _RequiredStoredQueryMetadataTypeDef, _OptionalStoredQueryMetadataTypeDef
):
    pass


_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredOrganizationAggregationSourceTypeDef = TypedDict(
    "_RequiredOrganizationAggregationSourceTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalOrganizationAggregationSourceTypeDef = TypedDict(
    "_OptionalOrganizationAggregationSourceTypeDef",
    {
        "AwsRegions": Sequence[str],
        "AllAwsRegions": bool,
    },
    total=False,
)


class OrganizationAggregationSourceTypeDef(
    _RequiredOrganizationAggregationSourceTypeDef, _OptionalOrganizationAggregationSourceTypeDef
):
    pass


OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef = TypedDict(
    "OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef",
    {
        "Description": str,
        "OrganizationConfigRuleTriggerTypes": List[OrganizationConfigRuleTriggerTypeNoSNType],
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
        "PolicyRuntime": str,
        "DebugLogDeliveryAccounts": List[str],
    },
    total=False,
)

_RequiredOrganizationCustomRuleMetadataOutputTypeDef = TypedDict(
    "_RequiredOrganizationCustomRuleMetadataOutputTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[OrganizationConfigRuleTriggerTypeType],
    },
)
_OptionalOrganizationCustomRuleMetadataOutputTypeDef = TypedDict(
    "_OptionalOrganizationCustomRuleMetadataOutputTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationCustomRuleMetadataOutputTypeDef(
    _RequiredOrganizationCustomRuleMetadataOutputTypeDef,
    _OptionalOrganizationCustomRuleMetadataOutputTypeDef,
):
    pass


_RequiredOrganizationManagedRuleMetadataOutputTypeDef = TypedDict(
    "_RequiredOrganizationManagedRuleMetadataOutputTypeDef",
    {
        "RuleIdentifier": str,
    },
)
_OptionalOrganizationManagedRuleMetadataOutputTypeDef = TypedDict(
    "_OptionalOrganizationManagedRuleMetadataOutputTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationManagedRuleMetadataOutputTypeDef(
    _RequiredOrganizationManagedRuleMetadataOutputTypeDef,
    _OptionalOrganizationManagedRuleMetadataOutputTypeDef,
):
    pass


_RequiredOrganizationCustomPolicyRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationCustomPolicyRuleMetadataTypeDef",
    {
        "PolicyRuntime": str,
        "PolicyText": str,
    },
)
_OptionalOrganizationCustomPolicyRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationCustomPolicyRuleMetadataTypeDef",
    {
        "Description": str,
        "OrganizationConfigRuleTriggerTypes": Sequence[OrganizationConfigRuleTriggerTypeNoSNType],
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": Sequence[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
        "DebugLogDeliveryAccounts": Sequence[str],
    },
    total=False,
)


class OrganizationCustomPolicyRuleMetadataTypeDef(
    _RequiredOrganizationCustomPolicyRuleMetadataTypeDef,
    _OptionalOrganizationCustomPolicyRuleMetadataTypeDef,
):
    pass


_RequiredOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationCustomRuleMetadataTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": Sequence[OrganizationConfigRuleTriggerTypeType],
    },
)
_OptionalOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": Sequence[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationCustomRuleMetadataTypeDef(
    _RequiredOrganizationCustomRuleMetadataTypeDef, _OptionalOrganizationCustomRuleMetadataTypeDef
):
    pass


_RequiredOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationManagedRuleMetadataTypeDef",
    {
        "RuleIdentifier": str,
    },
)
_OptionalOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": Sequence[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationManagedRuleMetadataTypeDef(
    _RequiredOrganizationManagedRuleMetadataTypeDef, _OptionalOrganizationManagedRuleMetadataTypeDef
):
    pass


_RequiredPutResourceConfigRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "SchemaVersionId": str,
        "ResourceId": str,
        "Configuration": str,
    },
)
_OptionalPutResourceConfigRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourceConfigRequestRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class PutResourceConfigRequestRequestTypeDef(
    _RequiredPutResourceConfigRequestRequestTypeDef, _OptionalPutResourceConfigRequestRequestTypeDef
):
    pass


PutRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "PutRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionPeriodInDays": int,
    },
)

RecordingStrategyTypeDef = TypedDict(
    "RecordingStrategyTypeDef",
    {
        "useOnly": RecordingStrategyTypeType,
    },
    total=False,
)

RemediationExecutionStepTypeDef = TypedDict(
    "RemediationExecutionStepTypeDef",
    {
        "Name": str,
        "State": RemediationExecutionStepStateType,
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

ResourceValueTypeDef = TypedDict(
    "ResourceValueTypeDef",
    {
        "Value": Literal["RESOURCE_ID"],
    },
)

StaticValueOutputTypeDef = TypedDict(
    "StaticValueOutputTypeDef",
    {
        "Values": List[str],
    },
)

StaticValueTypeDef = TypedDict(
    "StaticValueTypeDef",
    {
        "Values": Sequence[str],
    },
)

TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

_RequiredSelectAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "_RequiredSelectAggregateResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
        "ConfigurationAggregatorName": str,
    },
)
_OptionalSelectAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "_OptionalSelectAggregateResourceConfigRequestRequestTypeDef",
    {
        "Limit": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class SelectAggregateResourceConfigRequestRequestTypeDef(
    _RequiredSelectAggregateResourceConfigRequestRequestTypeDef,
    _OptionalSelectAggregateResourceConfigRequestRequestTypeDef,
):
    pass


_RequiredSelectResourceConfigRequestRequestTypeDef = TypedDict(
    "_RequiredSelectResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
    },
)
_OptionalSelectResourceConfigRequestRequestTypeDef = TypedDict(
    "_OptionalSelectResourceConfigRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class SelectResourceConfigRequestRequestTypeDef(
    _RequiredSelectResourceConfigRequestRequestTypeDef,
    _OptionalSelectResourceConfigRequestRequestTypeDef,
):
    pass


SourceDetailTypeDef = TypedDict(
    "SourceDetailTypeDef",
    {
        "EventSource": Literal["aws.config"],
        "MessageType": MessageTypeType,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
    },
    total=False,
)

StartConfigRulesEvaluationRequestRequestTypeDef = TypedDict(
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
    },
    total=False,
)

StartConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StartConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

StopConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StopConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

AggregateComplianceByConformancePackTypeDef = TypedDict(
    "AggregateComplianceByConformancePackTypeDef",
    {
        "ConformancePackName": str,
        "Compliance": AggregateConformancePackComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateConformancePackComplianceSummaryTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryTypeDef",
    {
        "ComplianceSummary": AggregateConformancePackComplianceCountTypeDef,
        "GroupName": str,
    },
    total=False,
)

_RequiredDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    {
        "Filters": AggregateConformancePackComplianceFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef(
    _RequiredDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef,
    _OptionalDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef,
):
    pass


_RequiredGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "Filters": AggregateConformancePackComplianceSummaryFiltersTypeDef,
        "GroupByKey": AggregateConformancePackComplianceSummaryGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef(
    _RequiredGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef,
    _OptionalGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef,
):
    pass


BatchGetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifiers": Sequence[AggregateResourceIdentifierTypeDef],
    },
)

GetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "GetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifier": AggregateResourceIdentifierTypeDef,
    },
)

BatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List[BaseConfigurationItemTypeDef],
        "UnprocessedResourceIdentifiers": List[AggregateResourceIdentifierTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeliverConfigSnapshotResponseTypeDef = TypedDict(
    "DeliverConfigSnapshotResponseTypeDef",
    {
        "configSnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List[AggregationAuthorizationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[AggregatedSourceStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetCustomRulePolicyResponseTypeDef = TypedDict(
    "GetCustomRulePolicyResponseTypeDef",
    {
        "PolicyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetOrganizationCustomRulePolicyResponseTypeDef = TypedDict(
    "GetOrganizationCustomRulePolicyResponseTypeDef",
    {
        "PolicyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[AggregateResourceIdentifierTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutAggregationAuthorizationResponseTypeDef = TypedDict(
    "PutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": AggregationAuthorizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutConformancePackResponseTypeDef = TypedDict(
    "PutConformancePackResponseTypeDef",
    {
        "ConformancePackArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "PutOrganizationConfigRuleResponseTypeDef",
    {
        "OrganizationConfigRuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutOrganizationConformancePackResponseTypeDef = TypedDict(
    "PutOrganizationConformancePackResponseTypeDef",
    {
        "OrganizationConformancePackArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutStoredQueryResponseTypeDef = TypedDict(
    "PutStoredQueryResponseTypeDef",
    {
        "QueryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartResourceEvaluationResponseTypeDef = TypedDict(
    "StartResourceEvaluationResponseTypeDef",
    {
        "ResourceEvaluationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchGetResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetResourceConfigRequestRequestTypeDef",
    {
        "resourceKeys": Sequence[ResourceKeyTypeDef],
    },
)

BatchGetResourceConfigResponseTypeDef = TypedDict(
    "BatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List[BaseConfigurationItemTypeDef],
        "unprocessedResourceKeys": List[ResourceKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDescribeRemediationExecutionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRemediationExecutionStatusRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExecutionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRemediationExecutionStatusRequestRequestTypeDef",
    {
        "ResourceKeys": Sequence[ResourceKeyTypeDef],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeRemediationExecutionStatusRequestRequestTypeDef(
    _RequiredDescribeRemediationExecutionStatusRequestRequestTypeDef,
    _OptionalDescribeRemediationExecutionStatusRequestRequestTypeDef,
):
    pass


StartRemediationExecutionRequestRequestTypeDef = TypedDict(
    "StartRemediationExecutionRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence[ResourceKeyTypeDef],
    },
)

StartRemediationExecutionResponseTypeDef = TypedDict(
    "StartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ResourceKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ComplianceSummaryTypeDef = TypedDict(
    "ComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": ComplianceContributorCountTypeDef,
        "NonCompliantResourceCount": ComplianceContributorCountTypeDef,
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "ComplianceContributorCount": ComplianceContributorCountTypeDef,
    },
    total=False,
)

_RequiredDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    {
        "Filters": ConfigRuleComplianceFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef(
    _RequiredDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef,
    _OptionalDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef,
):
    pass


_RequiredGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    {
        "Filters": ConfigRuleComplianceSummaryFiltersTypeDef,
        "GroupByKey": ConfigRuleComplianceSummaryGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef(
    _RequiredGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef,
    _OptionalGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef,
):
    pass


DescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[ConfigRuleEvaluationStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeliveryChannelTypeDef = TypedDict(
    "DeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "s3KmsKeyArn": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": ConfigSnapshotDeliveryPropertiesTypeDef,
    },
    total=False,
)

DeliveryChannelStatusTypeDef = TypedDict(
    "DeliveryChannelStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": ConfigExportDeliveryInfoTypeDef,
        "configHistoryDeliveryInfo": ConfigExportDeliveryInfoTypeDef,
        "configStreamDeliveryInfo": ConfigStreamDeliveryInfoTypeDef,
    },
    total=False,
)

ConfigurationAggregatorTypeDef = TypedDict(
    "ConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List[AccountAggregationSourceOutputTypeDef],
        "OrganizationAggregationSource": OrganizationAggregationSourceOutputTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)

ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": ConfigurationItemStatusType,
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List[RelationshipTypeDef],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

DescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List[ConfigurationRecorderStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDescribeConformancePackComplianceRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConformancePackComplianceRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalDescribeConformancePackComplianceRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConformancePackComplianceRequestRequestTypeDef",
    {
        "Filters": ConformancePackComplianceFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeConformancePackComplianceRequestRequestTypeDef(
    _RequiredDescribeConformancePackComplianceRequestRequestTypeDef,
    _OptionalDescribeConformancePackComplianceRequestRequestTypeDef,
):
    pass


ListConformancePackComplianceScoresResponseTypeDef = TypedDict(
    "ListConformancePackComplianceScoresResponseTypeDef",
    {
        "NextToken": str,
        "ConformancePackComplianceScores": List[ConformancePackComplianceScoreTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConformancePackComplianceScoresRequestRequestTypeDef = TypedDict(
    "ListConformancePackComplianceScoresRequestRequestTypeDef",
    {
        "Filters": ConformancePackComplianceScoresFiltersTypeDef,
        "SortOrder": SortOrderType,
        "SortBy": Literal["SCORE"],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

GetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List[ConformancePackComplianceSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredOrganizationConformancePackTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "LastUpdateTime": datetime,
    },
)
_OptionalOrganizationConformancePackTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackTypeDef",
    {
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List[ConformancePackInputParameterTypeDef],
        "ExcludedAccounts": List[str],
    },
    total=False,
)


class OrganizationConformancePackTypeDef(
    _RequiredOrganizationConformancePackTypeDef, _OptionalOrganizationConformancePackTypeDef
):
    pass


_RequiredPutOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "_RequiredPutOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalPutOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "_OptionalPutOrganizationConformancePackRequestRequestTypeDef",
    {
        "TemplateS3Uri": str,
        "TemplateBody": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": Sequence[ConformancePackInputParameterTypeDef],
        "ExcludedAccounts": Sequence[str],
    },
    total=False,
)


class PutOrganizationConformancePackRequestRequestTypeDef(
    _RequiredPutOrganizationConformancePackRequestRequestTypeDef,
    _OptionalPutOrganizationConformancePackRequestRequestTypeDef,
):
    pass


_RequiredConformancePackDetailTypeDef = TypedDict(
    "_RequiredConformancePackDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
    },
)
_OptionalConformancePackDetailTypeDef = TypedDict(
    "_OptionalConformancePackDetailTypeDef",
    {
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List[ConformancePackInputParameterTypeDef],
        "LastUpdateRequestedTime": datetime,
        "CreatedBy": str,
        "TemplateSSMDocumentDetails": TemplateSSMDocumentDetailsTypeDef,
    },
    total=False,
)


class ConformancePackDetailTypeDef(
    _RequiredConformancePackDetailTypeDef, _OptionalConformancePackDetailTypeDef
):
    pass


_RequiredPutConformancePackRequestRequestTypeDef = TypedDict(
    "_RequiredPutConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalPutConformancePackRequestRequestTypeDef = TypedDict(
    "_OptionalPutConformancePackRequestRequestTypeDef",
    {
        "TemplateS3Uri": str,
        "TemplateBody": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": Sequence[ConformancePackInputParameterTypeDef],
        "TemplateSSMDocumentDetails": TemplateSSMDocumentDetailsTypeDef,
    },
    total=False,
)


class PutConformancePackRequestRequestTypeDef(
    _RequiredPutConformancePackRequestRequestTypeDef,
    _OptionalPutConformancePackRequestRequestTypeDef,
):
    pass


_RequiredGetConformancePackComplianceDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceDetailsRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalGetConformancePackComplianceDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceDetailsRequestRequestTypeDef",
    {
        "Filters": ConformancePackEvaluationFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetConformancePackComplianceDetailsRequestRequestTypeDef(
    _RequiredGetConformancePackComplianceDetailsRequestRequestTypeDef,
    _OptionalGetConformancePackComplianceDetailsRequestRequestTypeDef,
):
    pass


DescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "DescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List[ConformancePackRuleComplianceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConformancePackStatusResponseTypeDef = TypedDict(
    "DescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List[ConformancePackStatusDetailTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence[RemediationExceptionResourceKeyTypeDef],
    },
)

_RequiredDescribeRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRemediationExceptionsRequestRequestTypeDef",
    {
        "ResourceKeys": Sequence[RemediationExceptionResourceKeyTypeDef],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeRemediationExceptionsRequestRequestTypeDef(
    _RequiredDescribeRemediationExceptionsRequestRequestTypeDef,
    _OptionalDescribeRemediationExceptionsRequestRequestTypeDef,
):
    pass


FailedDeleteRemediationExceptionsBatchTypeDef = TypedDict(
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[RemediationExceptionResourceKeyTypeDef],
    },
    total=False,
)

_RequiredPutRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence[RemediationExceptionResourceKeyTypeDef],
    },
)
_OptionalPutRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutRemediationExceptionsRequestRequestTypeDef",
    {
        "Message": str,
        "ExpirationTime": Union[datetime, str],
    },
    total=False,
)


class PutRemediationExceptionsRequestRequestTypeDef(
    _RequiredPutRemediationExceptionsRequestRequestTypeDef,
    _OptionalPutRemediationExceptionsRequestRequestTypeDef,
):
    pass


_RequiredDescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef",
    {
        "Filters": ConfigRuleComplianceFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef(
    _RequiredDescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef,
    _OptionalDescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef,
):
    pass


_RequiredDescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef",
    {
        "Filters": AggregateConformancePackComplianceFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef(
    _RequiredDescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef,
    _OptionalDescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef,
):
    pass


DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateTypeDef = (
    TypedDict(
        "DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateTypeDef",
        {
            "PaginationConfig": PaginatorConfigTypeDef,
        },
        total=False,
    )
)

DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredDescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef = TypedDict(
    "_RequiredDescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef = TypedDict(
    "_OptionalDescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef",
    {
        "UpdateStatus": Sequence[AggregatedSourceStatusTypeType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef(
    _RequiredDescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef,
    _OptionalDescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef,
):
    pass


DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef",
    {
        "ConfigurationAggregatorNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef = TypedDict(
    "DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef",
    {
        "OrganizationConfigRuleNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef",
    {
        "OrganizationConfigRuleNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef",
    {
        "OrganizationConformancePackNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef",
    {
        "OrganizationConformancePackNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredDescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef = TypedDict(
    "_RequiredDescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef = TypedDict(
    "_OptionalDescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef",
    {
        "ResourceKeys": Sequence[ResourceKeyTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef(
    _RequiredDescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef,
    _OptionalDescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef,
):
    pass


DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef",
    {
        "RetentionConfigurationNames": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredGetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef = TypedDict(
    "_RequiredGetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
    },
)
_OptionalGetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef = TypedDict(
    "_OptionalGetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef(
    _RequiredGetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef,
    _OptionalGetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef,
):
    pass


_RequiredGetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef = TypedDict(
    "_RequiredGetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalGetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef = TypedDict(
    "_OptionalGetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef",
    {
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef(
    _RequiredGetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef,
    _OptionalGetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef,
):
    pass


GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef = TypedDict(
    "GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": Sequence[ComplianceTypeType],
        "ResourceEvaluationId": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredGetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef",
    {
        "ConformancePackNames": Sequence[str],
    },
)
_OptionalGetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef(
    _RequiredGetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef,
    _OptionalGetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef,
):
    pass


_RequiredGetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef = TypedDict(
    "_RequiredGetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)
_OptionalGetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef = TypedDict(
    "_OptionalGetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef",
    {
        "laterTime": Union[datetime, str],
        "earlierTime": Union[datetime, str],
        "chronologicalOrder": ChronologicalOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef(
    _RequiredGetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef,
    _OptionalGetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef,
):
    pass


_RequiredListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    {
        "resourceType": ResourceTypeType,
    },
)
_OptionalListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    {
        "resourceIds": Sequence[str],
        "resourceName": str,
        "includeDeletedResources": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef(
    _RequiredListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef,
    _OptionalListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef,
):
    pass


_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(
    _RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
    _OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
):
    pass


_RequiredSelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef = (
    TypedDict(
        "_RequiredSelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef",
        {
            "Expression": str,
            "ConfigurationAggregatorName": str,
        },
    )
)
_OptionalSelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef = (
    TypedDict(
        "_OptionalSelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef",
        {
            "MaxResults": int,
            "PaginationConfig": PaginatorConfigTypeDef,
        },
        total=False,
    )
)


class SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef(
    _RequiredSelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef,
    _OptionalSelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef,
):
    pass


_RequiredSelectResourceConfigRequestSelectResourceConfigPaginateTypeDef = TypedDict(
    "_RequiredSelectResourceConfigRequestSelectResourceConfigPaginateTypeDef",
    {
        "Expression": str,
    },
)
_OptionalSelectResourceConfigRequestSelectResourceConfigPaginateTypeDef = TypedDict(
    "_OptionalSelectResourceConfigRequestSelectResourceConfigPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef(
    _RequiredSelectResourceConfigRequestSelectResourceConfigPaginateTypeDef,
    _OptionalSelectResourceConfigRequestSelectResourceConfigPaginateTypeDef,
):
    pass


DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef = TypedDict(
    "DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "Filters": DescribeConfigRulesFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeConfigRulesRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
        "NextToken": str,
        "Filters": DescribeConfigRulesFiltersTypeDef,
    },
    total=False,
)

DescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List[OrganizationConfigRuleStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List[OrganizationConformancePackStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List[PendingAggregationRequestTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "DescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List[RemediationExceptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FailedRemediationExceptionBatchTypeDef = TypedDict(
    "FailedRemediationExceptionBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[RemediationExceptionTypeDef],
    },
    total=False,
)

DescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List[RetentionConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutRetentionConfigurationResponseTypeDef = TypedDict(
    "PutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": RetentionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutEvaluationsResponseTypeDef = TypedDict(
    "PutEvaluationsResponseTypeDef",
    {
        "FailedEvaluations": List[EvaluationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EvaluationResultIdentifierTypeDef = TypedDict(
    "EvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": EvaluationResultQualifierTypeDef,
        "OrderingTimestamp": datetime,
        "ResourceEvaluationId": str,
    },
    total=False,
)

_RequiredPutEvaluationsRequestRequestTypeDef = TypedDict(
    "_RequiredPutEvaluationsRequestRequestTypeDef",
    {
        "ResultToken": str,
    },
)
_OptionalPutEvaluationsRequestRequestTypeDef = TypedDict(
    "_OptionalPutEvaluationsRequestRequestTypeDef",
    {
        "Evaluations": Sequence[Union[EvaluationTypeDef, EvaluationOutputTypeDef]],
        "TestMode": bool,
    },
    total=False,
)


class PutEvaluationsRequestRequestTypeDef(
    _RequiredPutEvaluationsRequestRequestTypeDef, _OptionalPutEvaluationsRequestRequestTypeDef
):
    pass


ExecutionControlsTypeDef = TypedDict(
    "ExecutionControlsTypeDef",
    {
        "SsmControls": SsmControlsTypeDef,
    },
    total=False,
)

PutExternalEvaluationRequestRequestTypeDef = TypedDict(
    "PutExternalEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ExternalEvaluation": ExternalEvaluationTypeDef,
    },
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "SelectFields": List[FieldInfoTypeDef],
    },
    total=False,
)

_RequiredGetAggregateDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "Filters": ResourceCountFiltersTypeDef,
        "GroupByKey": ResourceCountGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetAggregateDiscoveredResourceCountsRequestRequestTypeDef(
    _RequiredGetAggregateDiscoveredResourceCountsRequestRequestTypeDef,
    _OptionalGetAggregateDiscoveredResourceCountsRequestRequestTypeDef,
):
    pass


GetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List[GroupedResourceCountTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List[ResourceCountTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef = TypedDict(
    "_RequiredGetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalGetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef = TypedDict(
    "_OptionalGetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef",
    {
        "Filters": StatusDetailFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef(
    _RequiredGetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef,
    _OptionalGetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef,
):
    pass


_RequiredGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    {
        "Filters": StatusDetailFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef(
    _RequiredGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef,
    _OptionalGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef,
):
    pass


GetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List[MemberAccountStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef = TypedDict(
    "_RequiredGetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalGetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef = TypedDict(
    "_OptionalGetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef",
    {
        "Filters": OrganizationResourceDetailedStatusFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef(
    _RequiredGetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef,
    _OptionalGetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef,
):
    pass


_RequiredGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    {
        "Filters": OrganizationResourceDetailedStatusFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef(
    _RequiredGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef,
    _OptionalGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef,
):
    pass


GetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            OrganizationConformancePackDetailedStatusTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetResourceEvaluationSummaryResponseTypeDef = TypedDict(
    "GetResourceEvaluationSummaryResponseTypeDef",
    {
        "ResourceEvaluationId": str,
        "EvaluationMode": EvaluationModeType,
        "EvaluationStatus": EvaluationStatusTypeDef,
        "EvaluationStartTimestamp": datetime,
        "Compliance": ComplianceTypeType,
        "EvaluationContext": EvaluationContextTypeDef,
        "ResourceDetails": ResourceDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStartResourceEvaluationRequestRequestTypeDef = TypedDict(
    "_RequiredStartResourceEvaluationRequestRequestTypeDef",
    {
        "ResourceDetails": ResourceDetailsTypeDef,
        "EvaluationMode": EvaluationModeType,
    },
)
_OptionalStartResourceEvaluationRequestRequestTypeDef = TypedDict(
    "_OptionalStartResourceEvaluationRequestRequestTypeDef",
    {
        "EvaluationContext": EvaluationContextTypeDef,
        "EvaluationTimeout": int,
        "ClientToken": str,
    },
    total=False,
)


class StartResourceEvaluationRequestRequestTypeDef(
    _RequiredStartResourceEvaluationRequestRequestTypeDef,
    _OptionalStartResourceEvaluationRequestRequestTypeDef,
):
    pass


GetStoredQueryResponseTypeDef = TypedDict(
    "GetStoredQueryResponseTypeDef",
    {
        "StoredQuery": StoredQueryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef = TypedDict(
    "_RequiredListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef = TypedDict(
    "_OptionalListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef",
    {
        "Filters": ResourceFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef(
    _RequiredListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef,
    _OptionalListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef,
):
    pass


_RequiredListAggregateDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAggregateDiscoveredResourcesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListAggregateDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAggregateDiscoveredResourcesRequestRequestTypeDef",
    {
        "Filters": ResourceFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListAggregateDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListAggregateDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListAggregateDiscoveredResourcesRequestRequestTypeDef,
):
    pass


ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List[ResourceIdentifierTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourceEvaluationsResponseTypeDef = TypedDict(
    "ListResourceEvaluationsResponseTypeDef",
    {
        "ResourceEvaluations": List[ResourceEvaluationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStoredQueriesResponseTypeDef = TypedDict(
    "ListStoredQueriesResponseTypeDef",
    {
        "StoredQueryMetadata": List[StoredQueryMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPutAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredPutAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)
_OptionalPutAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalPutAggregationAuthorizationRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutAggregationAuthorizationRequestRequestTypeDef(
    _RequiredPutAggregationAuthorizationRequestRequestTypeDef,
    _OptionalPutAggregationAuthorizationRequestRequestTypeDef,
):
    pass


_RequiredPutStoredQueryRequestRequestTypeDef = TypedDict(
    "_RequiredPutStoredQueryRequestRequestTypeDef",
    {
        "StoredQuery": StoredQueryTypeDef,
    },
)
_OptionalPutStoredQueryRequestRequestTypeDef = TypedDict(
    "_OptionalPutStoredQueryRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutStoredQueryRequestRequestTypeDef(
    _RequiredPutStoredQueryRequestRequestTypeDef, _OptionalPutStoredQueryRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredPutConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalPutConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationAggregatorRequestRequestTypeDef",
    {
        "AccountAggregationSources": Sequence[
            Union[AccountAggregationSourceTypeDef, AccountAggregationSourceOutputTypeDef]
        ],
        "OrganizationAggregationSource": OrganizationAggregationSourceTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutConfigurationAggregatorRequestRequestTypeDef(
    _RequiredPutConfigurationAggregatorRequestRequestTypeDef,
    _OptionalPutConfigurationAggregatorRequestRequestTypeDef,
):
    pass


_RequiredOrganizationConfigRuleTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
    },
)
_OptionalOrganizationConfigRuleTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleTypeDef",
    {
        "OrganizationManagedRuleMetadata": OrganizationManagedRuleMetadataOutputTypeDef,
        "OrganizationCustomRuleMetadata": OrganizationCustomRuleMetadataOutputTypeDef,
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
        "OrganizationCustomPolicyRuleMetadata": OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef,
    },
    total=False,
)


class OrganizationConfigRuleTypeDef(
    _RequiredOrganizationConfigRuleTypeDef, _OptionalOrganizationConfigRuleTypeDef
):
    pass


_RequiredPutOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalPutOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationManagedRuleMetadata": OrganizationManagedRuleMetadataTypeDef,
        "OrganizationCustomRuleMetadata": OrganizationCustomRuleMetadataTypeDef,
        "ExcludedAccounts": Sequence[str],
        "OrganizationCustomPolicyRuleMetadata": OrganizationCustomPolicyRuleMetadataTypeDef,
    },
    total=False,
)


class PutOrganizationConfigRuleRequestRequestTypeDef(
    _RequiredPutOrganizationConfigRuleRequestRequestTypeDef,
    _OptionalPutOrganizationConfigRuleRequestRequestTypeDef,
):
    pass


RecordingGroupOutputTypeDef = TypedDict(
    "RecordingGroupOutputTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[ResourceTypeType],
        "exclusionByResourceTypes": ExclusionByResourceTypesOutputTypeDef,
        "recordingStrategy": RecordingStrategyTypeDef,
    },
    total=False,
)

RecordingGroupTypeDef = TypedDict(
    "RecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": Sequence[ResourceTypeType],
        "exclusionByResourceTypes": ExclusionByResourceTypesTypeDef,
        "recordingStrategy": RecordingStrategyTypeDef,
    },
    total=False,
)

RemediationExecutionStatusTypeDef = TypedDict(
    "RemediationExecutionStatusTypeDef",
    {
        "ResourceKey": ResourceKeyTypeDef,
        "State": RemediationExecutionStateType,
        "StepDetails": List[RemediationExecutionStepTypeDef],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

RemediationParameterValueOutputTypeDef = TypedDict(
    "RemediationParameterValueOutputTypeDef",
    {
        "ResourceValue": ResourceValueTypeDef,
        "StaticValue": StaticValueOutputTypeDef,
    },
    total=False,
)

RemediationParameterValueTypeDef = TypedDict(
    "RemediationParameterValueTypeDef",
    {
        "ResourceValue": ResourceValueTypeDef,
        "StaticValue": StaticValueTypeDef,
    },
    total=False,
)

ResourceEvaluationFiltersTypeDef = TypedDict(
    "ResourceEvaluationFiltersTypeDef",
    {
        "EvaluationMode": EvaluationModeType,
        "TimeWindow": TimeWindowTypeDef,
        "EvaluationContextIdentifier": str,
    },
    total=False,
)

_RequiredSourceOutputTypeDef = TypedDict(
    "_RequiredSourceOutputTypeDef",
    {
        "Owner": OwnerType,
    },
)
_OptionalSourceOutputTypeDef = TypedDict(
    "_OptionalSourceOutputTypeDef",
    {
        "SourceIdentifier": str,
        "SourceDetails": List[SourceDetailTypeDef],
        "CustomPolicyDetails": CustomPolicyDetailsTypeDef,
    },
    total=False,
)


class SourceOutputTypeDef(_RequiredSourceOutputTypeDef, _OptionalSourceOutputTypeDef):
    pass


_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef",
    {
        "Owner": OwnerType,
    },
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "SourceIdentifier": str,
        "SourceDetails": Sequence[SourceDetailTypeDef],
        "CustomPolicyDetails": CustomPolicyDetailsTypeDef,
    },
    total=False,
)


class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass


DescribeAggregateComplianceByConformancePacksResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    {
        "AggregateComplianceByConformancePacks": List[AggregateComplianceByConformancePackTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAggregateConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    {
        "AggregateConformancePackComplianceSummaries": List[
            AggregateConformancePackComplianceSummaryTypeDef
        ],
        "GroupByKey": str,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AggregateComplianceCountTypeDef = TypedDict(
    "AggregateComplianceCountTypeDef",
    {
        "GroupName": str,
        "ComplianceSummary": ComplianceSummaryTypeDef,
    },
    total=False,
)

ComplianceSummaryByResourceTypeTypeDef = TypedDict(
    "ComplianceSummaryByResourceTypeTypeDef",
    {
        "ResourceType": str,
        "ComplianceSummary": ComplianceSummaryTypeDef,
    },
    total=False,
)

GetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    {
        "ComplianceSummary": ComplianceSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AggregateComplianceByConfigRuleTypeDef = TypedDict(
    "AggregateComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ComplianceTypeDef,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ComplianceByConfigRuleTypeDef = TypedDict(
    "ComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": ComplianceTypeDef,
    },
    total=False,
)

ComplianceByResourceTypeDef = TypedDict(
    "ComplianceByResourceTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": ComplianceTypeDef,
    },
    total=False,
)

DescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelsResponseTypeDef",
    {
        "DeliveryChannels": List[DeliveryChannelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutDeliveryChannelRequestRequestTypeDef = TypedDict(
    "PutDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannel": DeliveryChannelTypeDef,
    },
)

DescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List[DeliveryChannelStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List[ConfigurationAggregatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutConfigurationAggregatorResponseTypeDef = TypedDict(
    "PutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": ConfigurationAggregatorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAggregateResourceConfigResponseTypeDef = TypedDict(
    "GetAggregateResourceConfigResponseTypeDef",
    {
        "ConfigurationItem": ConfigurationItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetResourceConfigHistoryResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List[ConfigurationItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List[OrganizationConformancePackTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConformancePacksResponseTypeDef = TypedDict(
    "DescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List[ConformancePackDetailTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "DeleteRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List[FailedDeleteRemediationExceptionsBatchTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutRemediationExceptionsResponseTypeDef = TypedDict(
    "PutRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List[FailedRemediationExceptionBatchTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AggregateEvaluationResultTypeDef = TypedDict(
    "AggregateEvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": EvaluationResultIdentifierTypeDef,
        "ComplianceType": ComplianceTypeType,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

_RequiredConformancePackEvaluationResultTypeDef = TypedDict(
    "_RequiredConformancePackEvaluationResultTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "EvaluationResultIdentifier": EvaluationResultIdentifierTypeDef,
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
    },
)
_OptionalConformancePackEvaluationResultTypeDef = TypedDict(
    "_OptionalConformancePackEvaluationResultTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)


class ConformancePackEvaluationResultTypeDef(
    _RequiredConformancePackEvaluationResultTypeDef, _OptionalConformancePackEvaluationResultTypeDef
):
    pass


EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": EvaluationResultIdentifierTypeDef,
        "ComplianceType": ComplianceTypeType,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)

SelectAggregateResourceConfigResponseTypeDef = TypedDict(
    "SelectAggregateResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": QueryInfoTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SelectResourceConfigResponseTypeDef = TypedDict(
    "SelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": QueryInfoTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List[OrganizationConfigRuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConfigurationRecorderOutputTypeDef = TypedDict(
    "ConfigurationRecorderOutputTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": RecordingGroupOutputTypeDef,
    },
    total=False,
)

ConfigurationRecorderTypeDef = TypedDict(
    "ConfigurationRecorderTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": RecordingGroupTypeDef,
    },
    total=False,
)

DescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[RemediationExecutionStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredRemediationConfigurationOutputTypeDef = TypedDict(
    "_RequiredRemediationConfigurationOutputTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
    },
)
_OptionalRemediationConfigurationOutputTypeDef = TypedDict(
    "_OptionalRemediationConfigurationOutputTypeDef",
    {
        "TargetVersion": str,
        "Parameters": Dict[str, RemediationParameterValueOutputTypeDef],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class RemediationConfigurationOutputTypeDef(
    _RequiredRemediationConfigurationOutputTypeDef, _OptionalRemediationConfigurationOutputTypeDef
):
    pass


_RequiredRemediationConfigurationTypeDef = TypedDict(
    "_RequiredRemediationConfigurationTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
    },
)
_OptionalRemediationConfigurationTypeDef = TypedDict(
    "_OptionalRemediationConfigurationTypeDef",
    {
        "TargetVersion": str,
        "Parameters": Mapping[str, RemediationParameterValueTypeDef],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": ExecutionControlsTypeDef,
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class RemediationConfigurationTypeDef(
    _RequiredRemediationConfigurationTypeDef, _OptionalRemediationConfigurationTypeDef
):
    pass


ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef = TypedDict(
    "ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef",
    {
        "Filters": ResourceEvaluationFiltersTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListResourceEvaluationsRequestRequestTypeDef = TypedDict(
    "ListResourceEvaluationsRequestRequestTypeDef",
    {
        "Filters": ResourceEvaluationFiltersTypeDef,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredConfigRuleOutputTypeDef = TypedDict(
    "_RequiredConfigRuleOutputTypeDef",
    {
        "Source": SourceOutputTypeDef,
    },
)
_OptionalConfigRuleOutputTypeDef = TypedDict(
    "_OptionalConfigRuleOutputTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": ScopeOutputTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ConfigRuleState": ConfigRuleStateType,
        "CreatedBy": str,
        "EvaluationModes": List[EvaluationModeConfigurationTypeDef],
    },
    total=False,
)


class ConfigRuleOutputTypeDef(_RequiredConfigRuleOutputTypeDef, _OptionalConfigRuleOutputTypeDef):
    pass


_RequiredConfigRuleTypeDef = TypedDict(
    "_RequiredConfigRuleTypeDef",
    {
        "Source": SourceTypeDef,
    },
)
_OptionalConfigRuleTypeDef = TypedDict(
    "_OptionalConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": ScopeTypeDef,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ConfigRuleState": ConfigRuleStateType,
        "CreatedBy": str,
        "EvaluationModes": Sequence[EvaluationModeConfigurationTypeDef],
    },
    total=False,
)


class ConfigRuleTypeDef(_RequiredConfigRuleTypeDef, _OptionalConfigRuleTypeDef):
    pass


GetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List[AggregateComplianceCountTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List[ComplianceSummaryByResourceTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[AggregateComplianceByConfigRuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List[ComplianceByConfigRuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeComplianceByResourceResponseTypeDef = TypedDict(
    "DescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List[ComplianceByResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List[AggregateEvaluationResultTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List[ConformancePackEvaluationResultTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List[EvaluationResultTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List[EvaluationResultTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "DescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List[ConfigurationRecorderOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "PutConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorder": ConfigurationRecorderTypeDef,
    },
)

DescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "DescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List[RemediationConfigurationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FailedRemediationBatchTypeDef = TypedDict(
    "FailedRemediationBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[RemediationConfigurationOutputTypeDef],
    },
    total=False,
)

PutRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "PutRemediationConfigurationsRequestRequestTypeDef",
    {
        "RemediationConfigurations": Sequence[
            Union[RemediationConfigurationTypeDef, RemediationConfigurationOutputTypeDef]
        ],
    },
)

DescribeConfigRulesResponseTypeDef = TypedDict(
    "DescribeConfigRulesResponseTypeDef",
    {
        "ConfigRules": List[ConfigRuleOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPutConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigRuleRequestRequestTypeDef",
    {
        "ConfigRule": ConfigRuleTypeDef,
    },
)
_OptionalPutConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigRuleRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutConfigRuleRequestRequestTypeDef(
    _RequiredPutConfigRuleRequestRequestTypeDef, _OptionalPutConfigRuleRequestRequestTypeDef
):
    pass


PutRemediationConfigurationsResponseTypeDef = TypedDict(
    "PutRemediationConfigurationsResponseTypeDef",
    {
        "FailedBatches": List[FailedRemediationBatchTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
