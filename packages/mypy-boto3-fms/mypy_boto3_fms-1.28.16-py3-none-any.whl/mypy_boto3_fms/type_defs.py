"""
Type annotations for fms service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/type_defs/)

Usage::

    ```python
    from mypy_boto3_fms.type_defs import AccountScopeOutputTypeDef

    data: AccountScopeOutputTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccountRoleStatusType,
    CustomerPolicyScopeIdTypeType,
    CustomerPolicyStatusType,
    DependentServiceNameType,
    DestinationTypeType,
    FailedItemReasonType,
    FirewallDeploymentModelType,
    MarketplaceSubscriptionOnboardingStatusType,
    OrganizationStatusType,
    PolicyComplianceStatusTypeType,
    RemediationActionTypeType,
    ResourceSetStatusType,
    RuleOrderType,
    SecurityServiceTypeType,
    TargetTypeType,
    ThirdPartyFirewallAssociationStatusType,
    ThirdPartyFirewallType,
    ViolationReasonType,
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
    "AccountScopeOutputTypeDef",
    "AccountScopeTypeDef",
    "ActionTargetTypeDef",
    "AdminAccountSummaryTypeDef",
    "OrganizationalUnitScopeOutputTypeDef",
    "PolicyTypeScopeOutputTypeDef",
    "RegionScopeOutputTypeDef",
    "OrganizationalUnitScopeTypeDef",
    "PolicyTypeScopeTypeDef",
    "RegionScopeTypeDef",
    "AppTypeDef",
    "TimestampTypeDef",
    "AssociateAdminAccountRequestRequestTypeDef",
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "PartialMatchTypeDef",
    "BatchAssociateResourceRequestRequestTypeDef",
    "FailedItemTypeDef",
    "BatchDisassociateResourceRequestRequestTypeDef",
    "ComplianceViolatorTypeDef",
    "DeleteAppsListRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeleteProtocolsListRequestRequestTypeDef",
    "DeleteResourceSetRequestRequestTypeDef",
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    "DiscoveredResourceTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EvaluationResultTypeDef",
    "ExpectedRouteTypeDef",
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    "GetAdminScopeRequestRequestTypeDef",
    "GetAppsListRequestRequestTypeDef",
    "GetComplianceDetailRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetProtocolsListRequestRequestTypeDef",
    "ProtocolsListDataOutputTypeDef",
    "GetResourceSetRequestRequestTypeDef",
    "ResourceSetOutputTypeDef",
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    "GetViolationDetailsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    "ListAdminsManagingAccountRequestRequestTypeDef",
    "ListAppsListsRequestRequestTypeDef",
    "ListComplianceStatusRequestRequestTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "PolicySummaryTypeDef",
    "ListProtocolsListsRequestRequestTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ListResourceSetResourcesRequestRequestTypeDef",
    "ResourceTypeDef",
    "ListResourceSetsRequestRequestTypeDef",
    "ResourceSetSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    "RouteTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatelessRuleGroupTypeDef",
    "NetworkFirewallPolicyTypeDef",
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    "ThirdPartyFirewallPolicyTypeDef",
    "ResourceTagTypeDef",
    "PutNotificationChannelRequestRequestTypeDef",
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "EC2AssociateRouteTableActionTypeDef",
    "EC2CopyRouteTableActionTypeDef",
    "EC2CreateRouteActionTypeDef",
    "EC2CreateRouteTableActionTypeDef",
    "EC2DeleteRouteActionTypeDef",
    "EC2ReplaceRouteActionTypeDef",
    "EC2ReplaceRouteTableAssociationActionTypeDef",
    "AdminScopeOutputTypeDef",
    "AdminScopeTypeDef",
    "AppsListDataOutputTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "GetProtectionStatusRequestRequestTypeDef",
    "ProtocolsListDataTypeDef",
    "ResourceSetTypeDef",
    "AssociateThirdPartyFirewallResponseTypeDef",
    "DisassociateThirdPartyFirewallResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    "ListAdminAccountsForOrganizationResponseTypeDef",
    "ListAdminsManagingAccountResponseTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "BatchAssociateResourceResponseTypeDef",
    "BatchDisassociateResourceResponseTypeDef",
    "PolicyComplianceDetailTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "PolicyComplianceStatusTypeDef",
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    "GetProtocolsListResponseTypeDef",
    "PutProtocolsListResponseTypeDef",
    "GetResourceSetResponseTypeDef",
    "PutResourceSetResponseTypeDef",
    "ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef",
    "ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef",
    "ListAppsListsRequestListAppsListsPaginateTypeDef",
    "ListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    "ListMemberAccountsRequestListMemberAccountsPaginateTypeDef",
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    "ListProtocolsListsRequestListProtocolsListsPaginateTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListResourceSetResourcesResponseTypeDef",
    "ListResourceSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    "StatefulRuleGroupTypeDef",
    "PolicyOptionTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "RemediationActionTypeDef",
    "GetAdminScopeResponseTypeDef",
    "AdminScopeUnionTypeDef",
    "PutAdminAccountRequestRequestTypeDef",
    "GetAppsListResponseTypeDef",
    "PutAppsListResponseTypeDef",
    "ListAppsListsResponseTypeDef",
    "AppsListDataUnionTypeDef",
    "PutAppsListRequestRequestTypeDef",
    "ProtocolsListDataUnionTypeDef",
    "PutProtocolsListRequestRequestTypeDef",
    "PutResourceSetRequestRequestTypeDef",
    "ResourceSetUnionTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "RemediationActionWithOrderTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "PolicyOutputTypeDef",
    "PolicyTypeDef",
    "PossibleRemediationActionTypeDef",
    "GetPolicyResponseTypeDef",
    "PutPolicyResponseTypeDef",
    "PolicyUnionTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "PossibleRemediationActionsTypeDef",
    "ResourceViolationTypeDef",
    "ViolationDetailTypeDef",
    "GetViolationDetailsResponseTypeDef",
)

AccountScopeOutputTypeDef = TypedDict(
    "AccountScopeOutputTypeDef",
    {
        "Accounts": List[str],
        "AllAccountsEnabled": bool,
        "ExcludeSpecifiedAccounts": bool,
    },
    total=False,
)

AccountScopeTypeDef = TypedDict(
    "AccountScopeTypeDef",
    {
        "Accounts": Sequence[str],
        "AllAccountsEnabled": bool,
        "ExcludeSpecifiedAccounts": bool,
    },
    total=False,
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ResourceId": str,
        "Description": str,
    },
    total=False,
)

AdminAccountSummaryTypeDef = TypedDict(
    "AdminAccountSummaryTypeDef",
    {
        "AdminAccount": str,
        "DefaultAdmin": bool,
        "Status": OrganizationStatusType,
    },
    total=False,
)

OrganizationalUnitScopeOutputTypeDef = TypedDict(
    "OrganizationalUnitScopeOutputTypeDef",
    {
        "OrganizationalUnits": List[str],
        "AllOrganizationalUnitsEnabled": bool,
        "ExcludeSpecifiedOrganizationalUnits": bool,
    },
    total=False,
)

PolicyTypeScopeOutputTypeDef = TypedDict(
    "PolicyTypeScopeOutputTypeDef",
    {
        "PolicyTypes": List[SecurityServiceTypeType],
        "AllPolicyTypesEnabled": bool,
    },
    total=False,
)

RegionScopeOutputTypeDef = TypedDict(
    "RegionScopeOutputTypeDef",
    {
        "Regions": List[str],
        "AllRegionsEnabled": bool,
    },
    total=False,
)

OrganizationalUnitScopeTypeDef = TypedDict(
    "OrganizationalUnitScopeTypeDef",
    {
        "OrganizationalUnits": Sequence[str],
        "AllOrganizationalUnitsEnabled": bool,
        "ExcludeSpecifiedOrganizationalUnits": bool,
    },
    total=False,
)

PolicyTypeScopeTypeDef = TypedDict(
    "PolicyTypeScopeTypeDef",
    {
        "PolicyTypes": Sequence[SecurityServiceTypeType],
        "AllPolicyTypesEnabled": bool,
    },
    total=False,
)

RegionScopeTypeDef = TypedDict(
    "RegionScopeTypeDef",
    {
        "Regions": Sequence[str],
        "AllRegionsEnabled": bool,
    },
    total=False,
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppName": str,
        "Protocol": str,
        "Port": int,
    },
)

TimestampTypeDef = Union[datetime, str]
AssociateAdminAccountRequestRequestTypeDef = TypedDict(
    "AssociateAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)

AssociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "AssociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
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

AwsEc2NetworkInterfaceViolationTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolatingSecurityGroups": List[str],
    },
    total=False,
)

PartialMatchTypeDef = TypedDict(
    "PartialMatchTypeDef",
    {
        "Reference": str,
        "TargetViolationReasons": List[str],
    },
    total=False,
)

BatchAssociateResourceRequestRequestTypeDef = TypedDict(
    "BatchAssociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": Sequence[str],
    },
)

FailedItemTypeDef = TypedDict(
    "FailedItemTypeDef",
    {
        "URI": str,
        "Reason": FailedItemReasonType,
    },
    total=False,
)

BatchDisassociateResourceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateResourceRequestRequestTypeDef",
    {
        "ResourceSetIdentifier": str,
        "Items": Sequence[str],
    },
)

ComplianceViolatorTypeDef = TypedDict(
    "ComplianceViolatorTypeDef",
    {
        "ResourceId": str,
        "ViolationReason": ViolationReasonType,
        "ResourceType": str,
        "Metadata": Dict[str, str],
    },
    total=False,
)

DeleteAppsListRequestRequestTypeDef = TypedDict(
    "DeleteAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

_RequiredDeletePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalDeletePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePolicyRequestRequestTypeDef",
    {
        "DeleteAllPolicyResources": bool,
    },
    total=False,
)


class DeletePolicyRequestRequestTypeDef(
    _RequiredDeletePolicyRequestRequestTypeDef, _OptionalDeletePolicyRequestRequestTypeDef
):
    pass


DeleteProtocolsListRequestRequestTypeDef = TypedDict(
    "DeleteProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)

DeleteResourceSetRequestRequestTypeDef = TypedDict(
    "DeleteResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DisassociateThirdPartyFirewallRequestRequestTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)

DiscoveredResourceTypeDef = TypedDict(
    "DiscoveredResourceTypeDef",
    {
        "URI": str,
        "AccountId": str,
        "Type": str,
        "Name": str,
    },
    total=False,
)

DnsDuplicateRuleGroupViolationTypeDef = TypedDict(
    "DnsDuplicateRuleGroupViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
    },
    total=False,
)

DnsRuleGroupLimitExceededViolationTypeDef = TypedDict(
    "DnsRuleGroupLimitExceededViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "NumberOfRuleGroupsAlreadyAssociated": int,
    },
    total=False,
)

DnsRuleGroupPriorityConflictViolationTypeDef = TypedDict(
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "ConflictingPriority": int,
        "ConflictingPolicyId": str,
        "UnavailablePriorities": List[int],
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "ComplianceStatus": PolicyComplianceStatusTypeType,
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

ExpectedRouteTypeDef = TypedDict(
    "ExpectedRouteTypeDef",
    {
        "IpV4Cidr": str,
        "PrefixListId": str,
        "IpV6Cidr": str,
        "ContributingSubnets": List[str],
        "AllowedTargets": List[str],
        "RouteTableId": str,
    },
    total=False,
)

FMSPolicyUpdateFirewallCreationConfigActionTypeDef = TypedDict(
    "FMSPolicyUpdateFirewallCreationConfigActionTypeDef",
    {
        "Description": str,
        "FirewallCreationConfig": str,
    },
    total=False,
)

FirewallSubnetIsOutOfScopeViolationTypeDef = TypedDict(
    "FirewallSubnetIsOutOfScopeViolationTypeDef",
    {
        "FirewallSubnetId": str,
        "VpcId": str,
        "SubnetAvailabilityZone": str,
        "SubnetAvailabilityZoneId": str,
        "VpcEndpointId": str,
    },
    total=False,
)

FirewallSubnetMissingVPCEndpointViolationTypeDef = TypedDict(
    "FirewallSubnetMissingVPCEndpointViolationTypeDef",
    {
        "FirewallSubnetId": str,
        "VpcId": str,
        "SubnetAvailabilityZone": str,
        "SubnetAvailabilityZoneId": str,
    },
    total=False,
)

GetAdminScopeRequestRequestTypeDef = TypedDict(
    "GetAdminScopeRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)

_RequiredGetAppsListRequestRequestTypeDef = TypedDict(
    "_RequiredGetAppsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetAppsListRequestRequestTypeDef = TypedDict(
    "_OptionalGetAppsListRequestRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)


class GetAppsListRequestRequestTypeDef(
    _RequiredGetAppsListRequestRequestTypeDef, _OptionalGetAppsListRequestRequestTypeDef
):
    pass


GetComplianceDetailRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

_RequiredGetProtocolsListRequestRequestTypeDef = TypedDict(
    "_RequiredGetProtocolsListRequestRequestTypeDef",
    {
        "ListId": str,
    },
)
_OptionalGetProtocolsListRequestRequestTypeDef = TypedDict(
    "_OptionalGetProtocolsListRequestRequestTypeDef",
    {
        "DefaultList": bool,
    },
    total=False,
)


class GetProtocolsListRequestRequestTypeDef(
    _RequiredGetProtocolsListRequestRequestTypeDef, _OptionalGetProtocolsListRequestRequestTypeDef
):
    pass


_RequiredProtocolsListDataOutputTypeDef = TypedDict(
    "_RequiredProtocolsListDataOutputTypeDef",
    {
        "ListName": str,
        "ProtocolsList": List[str],
    },
)
_OptionalProtocolsListDataOutputTypeDef = TypedDict(
    "_OptionalProtocolsListDataOutputTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
        "PreviousProtocolsList": Dict[str, List[str]],
    },
    total=False,
)


class ProtocolsListDataOutputTypeDef(
    _RequiredProtocolsListDataOutputTypeDef, _OptionalProtocolsListDataOutputTypeDef
):
    pass


GetResourceSetRequestRequestTypeDef = TypedDict(
    "GetResourceSetRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

_RequiredResourceSetOutputTypeDef = TypedDict(
    "_RequiredResourceSetOutputTypeDef",
    {
        "Name": str,
        "ResourceTypeList": List[str],
    },
)
_OptionalResourceSetOutputTypeDef = TypedDict(
    "_OptionalResourceSetOutputTypeDef",
    {
        "Id": str,
        "Description": str,
        "UpdateToken": str,
        "LastUpdateTime": datetime,
        "ResourceSetStatus": ResourceSetStatusType,
    },
    total=False,
)


class ResourceSetOutputTypeDef(
    _RequiredResourceSetOutputTypeDef, _OptionalResourceSetOutputTypeDef
):
    pass


GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)

GetViolationDetailsRequestRequestTypeDef = TypedDict(
    "GetViolationDetailsRequestRequestTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
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

ListAdminAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAdminsManagingAccountRequestRequestTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListAppsListsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListAppsListsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppsListsRequestRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAppsListsRequestRequestTypeDef(
    _RequiredListAppsListsRequestRequestTypeDef, _OptionalListAppsListsRequestRequestTypeDef
):
    pass


_RequiredListComplianceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListComplianceStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalListComplianceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListComplianceStatusRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListComplianceStatusRequestRequestTypeDef(
    _RequiredListComplianceStatusRequestRequestTypeDef,
    _OptionalListComplianceStatusRequestRequestTypeDef,
):
    pass


_RequiredListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestRequestTypeDef",
    {
        "MemberAccountIds": Sequence[str],
        "ResourceType": str,
    },
)
_OptionalListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListDiscoveredResourcesRequestRequestTypeDef,
):
    pass


ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": SecurityServiceTypeType,
        "RemediationEnabled": bool,
        "DeleteUnusedFMManagedResources": bool,
        "PolicyStatus": CustomerPolicyStatusType,
    },
    total=False,
)

_RequiredListProtocolsListsRequestRequestTypeDef = TypedDict(
    "_RequiredListProtocolsListsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListProtocolsListsRequestRequestTypeDef = TypedDict(
    "_OptionalListProtocolsListsRequestRequestTypeDef",
    {
        "DefaultLists": bool,
        "NextToken": str,
    },
    total=False,
)


class ListProtocolsListsRequestRequestTypeDef(
    _RequiredListProtocolsListsRequestRequestTypeDef,
    _OptionalListProtocolsListsRequestRequestTypeDef,
):
    pass


ProtocolsListDataSummaryTypeDef = TypedDict(
    "ProtocolsListDataSummaryTypeDef",
    {
        "ListArn": str,
        "ListId": str,
        "ListName": str,
        "ProtocolsList": List[str],
    },
    total=False,
)

_RequiredListResourceSetResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceSetResourcesRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalListResourceSetResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceSetResourcesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListResourceSetResourcesRequestRequestTypeDef(
    _RequiredListResourceSetResourcesRequestRequestTypeDef,
    _OptionalListResourceSetResourcesRequestRequestTypeDef,
):
    pass


_RequiredResourceTypeDef = TypedDict(
    "_RequiredResourceTypeDef",
    {
        "URI": str,
    },
)
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)


class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass


ListResourceSetsRequestRequestTypeDef = TypedDict(
    "ListResourceSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ResourceSetSummaryTypeDef = TypedDict(
    "ResourceSetSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "LastUpdateTime": datetime,
        "ResourceSetStatus": ResourceSetStatusType,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
        "MaxResults": int,
    },
)
_OptionalListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef(
    _RequiredListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef,
    _OptionalListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef,
):
    pass


ThirdPartyFirewallFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallFirewallPolicyTypeDef",
    {
        "FirewallPolicyId": str,
        "FirewallPolicyName": str,
    },
    total=False,
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationType": DestinationTypeType,
        "TargetType": TargetTypeType,
        "Destination": str,
        "Target": str,
    },
    total=False,
)

NetworkFirewallMissingExpectedRTViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "CurrentRouteTable": str,
        "ExpectedRouteTable": str,
    },
    total=False,
)

NetworkFirewallMissingFirewallViolationTypeDef = TypedDict(
    "NetworkFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

NetworkFirewallMissingSubnetViolationTypeDef = TypedDict(
    "NetworkFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": RuleOrderType,
    },
    total=False,
)

StatelessRuleGroupTypeDef = TypedDict(
    "StatelessRuleGroupTypeDef",
    {
        "RuleGroupName": str,
        "ResourceId": str,
        "Priority": int,
    },
    total=False,
)

NetworkFirewallPolicyTypeDef = TypedDict(
    "NetworkFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": FirewallDeploymentModelType,
    },
    total=False,
)

NetworkFirewallStatefulRuleGroupOverrideTypeDef = TypedDict(
    "NetworkFirewallStatefulRuleGroupOverrideTypeDef",
    {
        "Action": Literal["DROP_TO_ALERT"],
    },
    total=False,
)

ThirdPartyFirewallPolicyTypeDef = TypedDict(
    "ThirdPartyFirewallPolicyTypeDef",
    {
        "FirewallDeploymentModel": FirewallDeploymentModelType,
    },
    total=False,
)

_RequiredResourceTagTypeDef = TypedDict(
    "_RequiredResourceTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalResourceTagTypeDef = TypedDict(
    "_OptionalResourceTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
    pass


PutNotificationChannelRequestRequestTypeDef = TypedDict(
    "PutNotificationChannelRequestRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
    },
)

ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "CurrentRouteTable": str,
        "ExpectedRouteTable": str,
    },
    total=False,
)

ThirdPartyFirewallMissingFirewallViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingFirewallViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

ThirdPartyFirewallMissingSubnetViolationTypeDef = TypedDict(
    "ThirdPartyFirewallMissingSubnetViolationTypeDef",
    {
        "ViolationTarget": str,
        "VPC": str,
        "AvailabilityZone": str,
        "TargetViolationReason": str,
    },
    total=False,
)

SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": str,
        "IPV6Range": str,
        "PrefixListId": str,
        "Protocol": str,
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredEC2AssociateRouteTableActionTypeDef = TypedDict(
    "_RequiredEC2AssociateRouteTableActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
    },
)
_OptionalEC2AssociateRouteTableActionTypeDef = TypedDict(
    "_OptionalEC2AssociateRouteTableActionTypeDef",
    {
        "Description": str,
        "SubnetId": ActionTargetTypeDef,
        "GatewayId": ActionTargetTypeDef,
    },
    total=False,
)


class EC2AssociateRouteTableActionTypeDef(
    _RequiredEC2AssociateRouteTableActionTypeDef, _OptionalEC2AssociateRouteTableActionTypeDef
):
    pass


_RequiredEC2CopyRouteTableActionTypeDef = TypedDict(
    "_RequiredEC2CopyRouteTableActionTypeDef",
    {
        "VpcId": ActionTargetTypeDef,
        "RouteTableId": ActionTargetTypeDef,
    },
)
_OptionalEC2CopyRouteTableActionTypeDef = TypedDict(
    "_OptionalEC2CopyRouteTableActionTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class EC2CopyRouteTableActionTypeDef(
    _RequiredEC2CopyRouteTableActionTypeDef, _OptionalEC2CopyRouteTableActionTypeDef
):
    pass


_RequiredEC2CreateRouteActionTypeDef = TypedDict(
    "_RequiredEC2CreateRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
    },
)
_OptionalEC2CreateRouteActionTypeDef = TypedDict(
    "_OptionalEC2CreateRouteActionTypeDef",
    {
        "Description": str,
        "DestinationCidrBlock": str,
        "DestinationPrefixListId": str,
        "DestinationIpv6CidrBlock": str,
        "VpcEndpointId": ActionTargetTypeDef,
        "GatewayId": ActionTargetTypeDef,
    },
    total=False,
)


class EC2CreateRouteActionTypeDef(
    _RequiredEC2CreateRouteActionTypeDef, _OptionalEC2CreateRouteActionTypeDef
):
    pass


_RequiredEC2CreateRouteTableActionTypeDef = TypedDict(
    "_RequiredEC2CreateRouteTableActionTypeDef",
    {
        "VpcId": ActionTargetTypeDef,
    },
)
_OptionalEC2CreateRouteTableActionTypeDef = TypedDict(
    "_OptionalEC2CreateRouteTableActionTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class EC2CreateRouteTableActionTypeDef(
    _RequiredEC2CreateRouteTableActionTypeDef, _OptionalEC2CreateRouteTableActionTypeDef
):
    pass


_RequiredEC2DeleteRouteActionTypeDef = TypedDict(
    "_RequiredEC2DeleteRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
    },
)
_OptionalEC2DeleteRouteActionTypeDef = TypedDict(
    "_OptionalEC2DeleteRouteActionTypeDef",
    {
        "Description": str,
        "DestinationCidrBlock": str,
        "DestinationPrefixListId": str,
        "DestinationIpv6CidrBlock": str,
    },
    total=False,
)


class EC2DeleteRouteActionTypeDef(
    _RequiredEC2DeleteRouteActionTypeDef, _OptionalEC2DeleteRouteActionTypeDef
):
    pass


_RequiredEC2ReplaceRouteActionTypeDef = TypedDict(
    "_RequiredEC2ReplaceRouteActionTypeDef",
    {
        "RouteTableId": ActionTargetTypeDef,
    },
)
_OptionalEC2ReplaceRouteActionTypeDef = TypedDict(
    "_OptionalEC2ReplaceRouteActionTypeDef",
    {
        "Description": str,
        "DestinationCidrBlock": str,
        "DestinationPrefixListId": str,
        "DestinationIpv6CidrBlock": str,
        "GatewayId": ActionTargetTypeDef,
    },
    total=False,
)


class EC2ReplaceRouteActionTypeDef(
    _RequiredEC2ReplaceRouteActionTypeDef, _OptionalEC2ReplaceRouteActionTypeDef
):
    pass


_RequiredEC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "_RequiredEC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "AssociationId": ActionTargetTypeDef,
        "RouteTableId": ActionTargetTypeDef,
    },
)
_OptionalEC2ReplaceRouteTableAssociationActionTypeDef = TypedDict(
    "_OptionalEC2ReplaceRouteTableAssociationActionTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class EC2ReplaceRouteTableAssociationActionTypeDef(
    _RequiredEC2ReplaceRouteTableAssociationActionTypeDef,
    _OptionalEC2ReplaceRouteTableAssociationActionTypeDef,
):
    pass


AdminScopeOutputTypeDef = TypedDict(
    "AdminScopeOutputTypeDef",
    {
        "AccountScope": AccountScopeOutputTypeDef,
        "OrganizationalUnitScope": OrganizationalUnitScopeOutputTypeDef,
        "RegionScope": RegionScopeOutputTypeDef,
        "PolicyTypeScope": PolicyTypeScopeOutputTypeDef,
    },
    total=False,
)

AdminScopeTypeDef = TypedDict(
    "AdminScopeTypeDef",
    {
        "AccountScope": AccountScopeTypeDef,
        "OrganizationalUnitScope": OrganizationalUnitScopeTypeDef,
        "RegionScope": RegionScopeTypeDef,
        "PolicyTypeScope": PolicyTypeScopeTypeDef,
    },
    total=False,
)

_RequiredAppsListDataOutputTypeDef = TypedDict(
    "_RequiredAppsListDataOutputTypeDef",
    {
        "ListName": str,
        "AppsList": List[AppTypeDef],
    },
)
_OptionalAppsListDataOutputTypeDef = TypedDict(
    "_OptionalAppsListDataOutputTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": datetime,
        "LastUpdateTime": datetime,
        "PreviousAppsList": Dict[str, List[AppTypeDef]],
    },
    total=False,
)


class AppsListDataOutputTypeDef(
    _RequiredAppsListDataOutputTypeDef, _OptionalAppsListDataOutputTypeDef
):
    pass


AppsListDataSummaryTypeDef = TypedDict(
    "AppsListDataSummaryTypeDef",
    {
        "ListArn": str,
        "ListId": str,
        "ListName": str,
        "AppsList": List[AppTypeDef],
    },
    total=False,
)

_RequiredAppsListDataTypeDef = TypedDict(
    "_RequiredAppsListDataTypeDef",
    {
        "ListName": str,
        "AppsList": Sequence[AppTypeDef],
    },
)
_OptionalAppsListDataTypeDef = TypedDict(
    "_OptionalAppsListDataTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": TimestampTypeDef,
        "LastUpdateTime": TimestampTypeDef,
        "PreviousAppsList": Mapping[str, Sequence[AppTypeDef]],
    },
    total=False,
)


class AppsListDataTypeDef(_RequiredAppsListDataTypeDef, _OptionalAppsListDataTypeDef):
    pass


_RequiredGetProtectionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetProtectionStatusRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalGetProtectionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetProtectionStatusRequestRequestTypeDef",
    {
        "MemberAccountId": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetProtectionStatusRequestRequestTypeDef(
    _RequiredGetProtectionStatusRequestRequestTypeDef,
    _OptionalGetProtectionStatusRequestRequestTypeDef,
):
    pass


_RequiredProtocolsListDataTypeDef = TypedDict(
    "_RequiredProtocolsListDataTypeDef",
    {
        "ListName": str,
        "ProtocolsList": Sequence[str],
    },
)
_OptionalProtocolsListDataTypeDef = TypedDict(
    "_OptionalProtocolsListDataTypeDef",
    {
        "ListId": str,
        "ListUpdateToken": str,
        "CreateTime": TimestampTypeDef,
        "LastUpdateTime": TimestampTypeDef,
        "PreviousProtocolsList": Mapping[str, Sequence[str]],
    },
    total=False,
)


class ProtocolsListDataTypeDef(
    _RequiredProtocolsListDataTypeDef, _OptionalProtocolsListDataTypeDef
):
    pass


_RequiredResourceSetTypeDef = TypedDict(
    "_RequiredResourceSetTypeDef",
    {
        "Name": str,
        "ResourceTypeList": Sequence[str],
    },
)
_OptionalResourceSetTypeDef = TypedDict(
    "_OptionalResourceSetTypeDef",
    {
        "Id": str,
        "Description": str,
        "UpdateToken": str,
        "LastUpdateTime": TimestampTypeDef,
        "ResourceSetStatus": ResourceSetStatusType,
    },
    total=False,
)


class ResourceSetTypeDef(_RequiredResourceSetTypeDef, _OptionalResourceSetTypeDef):
    pass


AssociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "AssociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociateThirdPartyFirewallResponseTypeDef = TypedDict(
    "DisassociateThirdPartyFirewallResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAdminAccountResponseTypeDef = TypedDict(
    "GetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": AccountRoleStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetNotificationChannelResponseTypeDef = TypedDict(
    "GetNotificationChannelResponseTypeDef",
    {
        "SnsTopicArn": str,
        "SnsRoleName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetProtectionStatusResponseTypeDef = TypedDict(
    "GetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": SecurityServiceTypeType,
        "Data": str,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetThirdPartyFirewallAssociationStatusResponseTypeDef = TypedDict(
    "GetThirdPartyFirewallAssociationStatusResponseTypeDef",
    {
        "ThirdPartyFirewallStatus": ThirdPartyFirewallAssociationStatusType,
        "MarketplaceOnboardingStatus": MarketplaceSubscriptionOnboardingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAdminAccountsForOrganizationResponseTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationResponseTypeDef",
    {
        "AdminAccounts": List[AdminAccountSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAdminsManagingAccountResponseTypeDef = TypedDict(
    "ListAdminsManagingAccountResponseTypeDef",
    {
        "AdminAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMemberAccountsResponseTypeDef = TypedDict(
    "ListMemberAccountsResponseTypeDef",
    {
        "MemberAccounts": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AwsEc2InstanceViolationTypeDef = TypedDict(
    "AwsEc2InstanceViolationTypeDef",
    {
        "ViolationTarget": str,
        "AwsEc2NetworkInterfaceViolations": List[AwsEc2NetworkInterfaceViolationTypeDef],
    },
    total=False,
)

BatchAssociateResourceResponseTypeDef = TypedDict(
    "BatchAssociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List[FailedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDisassociateResourceResponseTypeDef = TypedDict(
    "BatchDisassociateResourceResponseTypeDef",
    {
        "ResourceSetIdentifier": str,
        "FailedItems": List[FailedItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PolicyComplianceDetailTypeDef = TypedDict(
    "PolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "MemberAccount": str,
        "Violators": List[ComplianceViolatorTypeDef],
        "EvaluationLimitExceeded": bool,
        "ExpiredAt": datetime,
        "IssueInfoMap": Dict[DependentServiceNameType, str],
    },
    total=False,
)

ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "Items": List[DiscoveredResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PolicyComplianceStatusTypeDef = TypedDict(
    "PolicyComplianceStatusTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[EvaluationResultTypeDef],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[DependentServiceNameType, str],
    },
    total=False,
)

NetworkFirewallMissingExpectedRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallMissingExpectedRoutesViolationTypeDef",
    {
        "ViolationTarget": str,
        "ExpectedRoutes": List[ExpectedRouteTypeDef],
        "VpcId": str,
    },
    total=False,
)

GetProtocolsListResponseTypeDef = TypedDict(
    "GetProtocolsListResponseTypeDef",
    {
        "ProtocolsList": ProtocolsListDataOutputTypeDef,
        "ProtocolsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutProtocolsListResponseTypeDef = TypedDict(
    "PutProtocolsListResponseTypeDef",
    {
        "ProtocolsList": ProtocolsListDataOutputTypeDef,
        "ProtocolsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetResourceSetResponseTypeDef = TypedDict(
    "GetResourceSetResponseTypeDef",
    {
        "ResourceSet": ResourceSetOutputTypeDef,
        "ResourceSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutResourceSetResponseTypeDef = TypedDict(
    "PutResourceSetResponseTypeDef",
    {
        "ResourceSet": ResourceSetOutputTypeDef,
        "ResourceSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef = TypedDict(
    "ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef = TypedDict(
    "ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAppsListsRequestListAppsListsPaginateTypeDef = TypedDict(
    "ListAppsListsRequestListAppsListsPaginateTypeDef",
    {
        "DefaultLists": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListComplianceStatusRequestListComplianceStatusPaginateTypeDef = TypedDict(
    "_RequiredListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalListComplianceStatusRequestListComplianceStatusPaginateTypeDef = TypedDict(
    "_OptionalListComplianceStatusRequestListComplianceStatusPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListComplianceStatusRequestListComplianceStatusPaginateTypeDef(
    _RequiredListComplianceStatusRequestListComplianceStatusPaginateTypeDef,
    _OptionalListComplianceStatusRequestListComplianceStatusPaginateTypeDef,
):
    pass


ListMemberAccountsRequestListMemberAccountsPaginateTypeDef = TypedDict(
    "ListMemberAccountsRequestListMemberAccountsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPoliciesRequestListPoliciesPaginateTypeDef = TypedDict(
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListProtocolsListsRequestListProtocolsListsPaginateTypeDef = TypedDict(
    "ListProtocolsListsRequestListProtocolsListsPaginateTypeDef",
    {
        "DefaultLists": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef = TypedDict(
    "_RequiredListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    {
        "ThirdPartyFirewall": ThirdPartyFirewallType,
    },
)
_OptionalListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef = TypedDict(
    "_OptionalListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef(
    _RequiredListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef,
    _OptionalListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef,
):
    pass


ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "PolicyList": List[PolicySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListProtocolsListsResponseTypeDef = TypedDict(
    "ListProtocolsListsResponseTypeDef",
    {
        "ProtocolsLists": List[ProtocolsListDataSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourceSetResourcesResponseTypeDef = TypedDict(
    "ListResourceSetResourcesResponseTypeDef",
    {
        "Items": List[ResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourceSetsResponseTypeDef = TypedDict(
    "ListResourceSetsResponseTypeDef",
    {
        "ResourceSets": List[ResourceSetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": Sequence[TagTypeDef],
    },
)

ListThirdPartyFirewallFirewallPoliciesResponseTypeDef = TypedDict(
    "ListThirdPartyFirewallFirewallPoliciesResponseTypeDef",
    {
        "ThirdPartyFirewallFirewallPolicies": List[ThirdPartyFirewallFirewallPolicyTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkFirewallBlackHoleRouteDetectedViolationTypeDef = TypedDict(
    "NetworkFirewallBlackHoleRouteDetectedViolationTypeDef",
    {
        "ViolationTarget": str,
        "RouteTableId": str,
        "VpcId": str,
        "ViolatingRoutes": List[RouteTypeDef],
    },
    total=False,
)

NetworkFirewallInternetTrafficNotInspectedViolationTypeDef = TypedDict(
    "NetworkFirewallInternetTrafficNotInspectedViolationTypeDef",
    {
        "SubnetId": str,
        "SubnetAvailabilityZone": str,
        "RouteTableId": str,
        "ViolatingRoutes": List[RouteTypeDef],
        "IsRouteTableUsedInDifferentAZ": bool,
        "CurrentFirewallSubnetRouteTable": str,
        "ExpectedFirewallEndpoint": str,
        "FirewallSubnetId": str,
        "ExpectedFirewallSubnetRoutes": List[ExpectedRouteTypeDef],
        "ActualFirewallSubnetRoutes": List[RouteTypeDef],
        "InternetGatewayId": str,
        "CurrentInternetGatewayRouteTable": str,
        "ExpectedInternetGatewayRoutes": List[ExpectedRouteTypeDef],
        "ActualInternetGatewayRoutes": List[RouteTypeDef],
        "VpcId": str,
    },
    total=False,
)

NetworkFirewallInvalidRouteConfigurationViolationTypeDef = TypedDict(
    "NetworkFirewallInvalidRouteConfigurationViolationTypeDef",
    {
        "AffectedSubnets": List[str],
        "RouteTableId": str,
        "IsRouteTableUsedInDifferentAZ": bool,
        "ViolatingRoute": RouteTypeDef,
        "CurrentFirewallSubnetRouteTable": str,
        "ExpectedFirewallEndpoint": str,
        "ActualFirewallEndpoint": str,
        "ExpectedFirewallSubnetId": str,
        "ActualFirewallSubnetId": str,
        "ExpectedFirewallSubnetRoutes": List[ExpectedRouteTypeDef],
        "ActualFirewallSubnetRoutes": List[RouteTypeDef],
        "InternetGatewayId": str,
        "CurrentInternetGatewayRouteTable": str,
        "ExpectedInternetGatewayRoutes": List[ExpectedRouteTypeDef],
        "ActualInternetGatewayRoutes": List[RouteTypeDef],
        "VpcId": str,
    },
    total=False,
)

NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef",
    {
        "FirewallSubnetId": str,
        "ViolatingRoutes": List[RouteTypeDef],
        "RouteTableId": str,
        "FirewallEndpoint": str,
        "VpcId": str,
    },
    total=False,
)

NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef = TypedDict(
    "NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef",
    {
        "GatewayId": str,
        "ViolatingRoutes": List[RouteTypeDef],
        "RouteTableId": str,
        "VpcId": str,
    },
    total=False,
)

RouteHasOutOfScopeEndpointViolationTypeDef = TypedDict(
    "RouteHasOutOfScopeEndpointViolationTypeDef",
    {
        "SubnetId": str,
        "VpcId": str,
        "RouteTableId": str,
        "ViolatingRoutes": List[RouteTypeDef],
        "SubnetAvailabilityZone": str,
        "SubnetAvailabilityZoneId": str,
        "CurrentFirewallSubnetRouteTable": str,
        "FirewallSubnetId": str,
        "FirewallSubnetRoutes": List[RouteTypeDef],
        "InternetGatewayId": str,
        "CurrentInternetGatewayRouteTable": str,
        "InternetGatewayRoutes": List[RouteTypeDef],
    },
    total=False,
)

StatefulRuleGroupTypeDef = TypedDict(
    "StatefulRuleGroupTypeDef",
    {
        "RuleGroupName": str,
        "ResourceId": str,
        "Priority": int,
        "Override": NetworkFirewallStatefulRuleGroupOverrideTypeDef,
    },
    total=False,
)

PolicyOptionTypeDef = TypedDict(
    "PolicyOptionTypeDef",
    {
        "NetworkFirewallPolicy": NetworkFirewallPolicyTypeDef,
        "ThirdPartyFirewallPolicy": ThirdPartyFirewallPolicyTypeDef,
    },
    total=False,
)

SecurityGroupRemediationActionTypeDef = TypedDict(
    "SecurityGroupRemediationActionTypeDef",
    {
        "RemediationActionType": RemediationActionTypeType,
        "Description": str,
        "RemediationResult": SecurityGroupRuleDescriptionTypeDef,
        "IsDefaultAction": bool,
    },
    total=False,
)

RemediationActionTypeDef = TypedDict(
    "RemediationActionTypeDef",
    {
        "Description": str,
        "EC2CreateRouteAction": EC2CreateRouteActionTypeDef,
        "EC2ReplaceRouteAction": EC2ReplaceRouteActionTypeDef,
        "EC2DeleteRouteAction": EC2DeleteRouteActionTypeDef,
        "EC2CopyRouteTableAction": EC2CopyRouteTableActionTypeDef,
        "EC2ReplaceRouteTableAssociationAction": EC2ReplaceRouteTableAssociationActionTypeDef,
        "EC2AssociateRouteTableAction": EC2AssociateRouteTableActionTypeDef,
        "EC2CreateRouteTableAction": EC2CreateRouteTableActionTypeDef,
        "FMSPolicyUpdateFirewallCreationConfigAction": (
            FMSPolicyUpdateFirewallCreationConfigActionTypeDef
        ),
    },
    total=False,
)

GetAdminScopeResponseTypeDef = TypedDict(
    "GetAdminScopeResponseTypeDef",
    {
        "AdminScope": AdminScopeOutputTypeDef,
        "Status": OrganizationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AdminScopeUnionTypeDef = Union[AdminScopeTypeDef, AdminScopeOutputTypeDef]
_RequiredPutAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredPutAdminAccountRequestRequestTypeDef",
    {
        "AdminAccount": str,
    },
)
_OptionalPutAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalPutAdminAccountRequestRequestTypeDef",
    {
        "AdminScope": AdminScopeTypeDef,
    },
    total=False,
)


class PutAdminAccountRequestRequestTypeDef(
    _RequiredPutAdminAccountRequestRequestTypeDef, _OptionalPutAdminAccountRequestRequestTypeDef
):
    pass


GetAppsListResponseTypeDef = TypedDict(
    "GetAppsListResponseTypeDef",
    {
        "AppsList": AppsListDataOutputTypeDef,
        "AppsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutAppsListResponseTypeDef = TypedDict(
    "PutAppsListResponseTypeDef",
    {
        "AppsList": AppsListDataOutputTypeDef,
        "AppsListArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAppsListsResponseTypeDef = TypedDict(
    "ListAppsListsResponseTypeDef",
    {
        "AppsLists": List[AppsListDataSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AppsListDataUnionTypeDef = Union[AppsListDataTypeDef, AppsListDataOutputTypeDef]
_RequiredPutAppsListRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppsListRequestRequestTypeDef",
    {
        "AppsList": AppsListDataTypeDef,
    },
)
_OptionalPutAppsListRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppsListRequestRequestTypeDef",
    {
        "TagList": Sequence[TagTypeDef],
    },
    total=False,
)


class PutAppsListRequestRequestTypeDef(
    _RequiredPutAppsListRequestRequestTypeDef, _OptionalPutAppsListRequestRequestTypeDef
):
    pass


ProtocolsListDataUnionTypeDef = Union[ProtocolsListDataTypeDef, ProtocolsListDataOutputTypeDef]
_RequiredPutProtocolsListRequestRequestTypeDef = TypedDict(
    "_RequiredPutProtocolsListRequestRequestTypeDef",
    {
        "ProtocolsList": ProtocolsListDataTypeDef,
    },
)
_OptionalPutProtocolsListRequestRequestTypeDef = TypedDict(
    "_OptionalPutProtocolsListRequestRequestTypeDef",
    {
        "TagList": Sequence[TagTypeDef],
    },
    total=False,
)


class PutProtocolsListRequestRequestTypeDef(
    _RequiredPutProtocolsListRequestRequestTypeDef, _OptionalPutProtocolsListRequestRequestTypeDef
):
    pass


_RequiredPutResourceSetRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourceSetRequestRequestTypeDef",
    {
        "ResourceSet": ResourceSetTypeDef,
    },
)
_OptionalPutResourceSetRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourceSetRequestRequestTypeDef",
    {
        "TagList": Sequence[TagTypeDef],
    },
    total=False,
)


class PutResourceSetRequestRequestTypeDef(
    _RequiredPutResourceSetRequestRequestTypeDef, _OptionalPutResourceSetRequestRequestTypeDef
):
    pass


ResourceSetUnionTypeDef = Union[ResourceSetTypeDef, ResourceSetOutputTypeDef]
GetComplianceDetailResponseTypeDef = TypedDict(
    "GetComplianceDetailResponseTypeDef",
    {
        "PolicyComplianceDetail": PolicyComplianceDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListComplianceStatusResponseTypeDef = TypedDict(
    "ListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[PolicyComplianceStatusTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkFirewallPolicyDescriptionTypeDef = TypedDict(
    "NetworkFirewallPolicyDescriptionTypeDef",
    {
        "StatelessRuleGroups": List[StatelessRuleGroupTypeDef],
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
        "StatelessCustomActions": List[str],
        "StatefulRuleGroups": List[StatefulRuleGroupTypeDef],
        "StatefulDefaultActions": List[str],
        "StatefulEngineOptions": StatefulEngineOptionsTypeDef,
    },
    total=False,
)

_RequiredSecurityServicePolicyDataTypeDef = TypedDict(
    "_RequiredSecurityServicePolicyDataTypeDef",
    {
        "Type": SecurityServiceTypeType,
    },
)
_OptionalSecurityServicePolicyDataTypeDef = TypedDict(
    "_OptionalSecurityServicePolicyDataTypeDef",
    {
        "ManagedServiceData": str,
        "PolicyOption": PolicyOptionTypeDef,
    },
    total=False,
)


class SecurityServicePolicyDataTypeDef(
    _RequiredSecurityServicePolicyDataTypeDef, _OptionalSecurityServicePolicyDataTypeDef
):
    pass


AwsVPCSecurityGroupViolationTypeDef = TypedDict(
    "AwsVPCSecurityGroupViolationTypeDef",
    {
        "ViolationTarget": str,
        "ViolationTargetDescription": str,
        "PartialMatches": List[PartialMatchTypeDef],
        "PossibleSecurityGroupRemediationActions": List[SecurityGroupRemediationActionTypeDef],
    },
    total=False,
)

RemediationActionWithOrderTypeDef = TypedDict(
    "RemediationActionWithOrderTypeDef",
    {
        "RemediationAction": RemediationActionTypeDef,
        "Order": int,
    },
    total=False,
)

NetworkFirewallPolicyModifiedViolationTypeDef = TypedDict(
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    {
        "ViolationTarget": str,
        "CurrentPolicyDescription": NetworkFirewallPolicyDescriptionTypeDef,
        "ExpectedPolicyDescription": NetworkFirewallPolicyDescriptionTypeDef,
    },
    total=False,
)

_RequiredPolicyOutputTypeDef = TypedDict(
    "_RequiredPolicyOutputTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": SecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
    },
)
_OptionalPolicyOutputTypeDef = TypedDict(
    "_OptionalPolicyOutputTypeDef",
    {
        "PolicyId": str,
        "PolicyUpdateToken": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ResourceTagTypeDef],
        "DeleteUnusedFMManagedResources": bool,
        "IncludeMap": Dict[CustomerPolicyScopeIdTypeType, List[str]],
        "ExcludeMap": Dict[CustomerPolicyScopeIdTypeType, List[str]],
        "ResourceSetIds": List[str],
        "PolicyDescription": str,
        "PolicyStatus": CustomerPolicyStatusType,
    },
    total=False,
)


class PolicyOutputTypeDef(_RequiredPolicyOutputTypeDef, _OptionalPolicyOutputTypeDef):
    pass


_RequiredPolicyTypeDef = TypedDict(
    "_RequiredPolicyTypeDef",
    {
        "PolicyName": str,
        "SecurityServicePolicyData": SecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
    },
)
_OptionalPolicyTypeDef = TypedDict(
    "_OptionalPolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyUpdateToken": str,
        "ResourceTypeList": Sequence[str],
        "ResourceTags": Sequence[ResourceTagTypeDef],
        "DeleteUnusedFMManagedResources": bool,
        "IncludeMap": Mapping[CustomerPolicyScopeIdTypeType, Sequence[str]],
        "ExcludeMap": Mapping[CustomerPolicyScopeIdTypeType, Sequence[str]],
        "ResourceSetIds": Sequence[str],
        "PolicyDescription": str,
        "PolicyStatus": CustomerPolicyStatusType,
    },
    total=False,
)


class PolicyTypeDef(_RequiredPolicyTypeDef, _OptionalPolicyTypeDef):
    pass


_RequiredPossibleRemediationActionTypeDef = TypedDict(
    "_RequiredPossibleRemediationActionTypeDef",
    {
        "OrderedRemediationActions": List[RemediationActionWithOrderTypeDef],
    },
)
_OptionalPossibleRemediationActionTypeDef = TypedDict(
    "_OptionalPossibleRemediationActionTypeDef",
    {
        "Description": str,
        "IsDefaultAction": bool,
    },
    total=False,
)


class PossibleRemediationActionTypeDef(
    _RequiredPossibleRemediationActionTypeDef, _OptionalPossibleRemediationActionTypeDef
):
    pass


GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": PolicyOutputTypeDef,
        "PolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutPolicyResponseTypeDef = TypedDict(
    "PutPolicyResponseTypeDef",
    {
        "Policy": PolicyOutputTypeDef,
        "PolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PolicyUnionTypeDef = Union[PolicyTypeDef, PolicyOutputTypeDef]
_RequiredPutPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutPolicyRequestRequestTypeDef",
    {
        "Policy": PolicyTypeDef,
    },
)
_OptionalPutPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutPolicyRequestRequestTypeDef",
    {
        "TagList": Sequence[TagTypeDef],
    },
    total=False,
)


class PutPolicyRequestRequestTypeDef(
    _RequiredPutPolicyRequestRequestTypeDef, _OptionalPutPolicyRequestRequestTypeDef
):
    pass


PossibleRemediationActionsTypeDef = TypedDict(
    "PossibleRemediationActionsTypeDef",
    {
        "Description": str,
        "Actions": List[PossibleRemediationActionTypeDef],
    },
    total=False,
)

ResourceViolationTypeDef = TypedDict(
    "ResourceViolationTypeDef",
    {
        "AwsVPCSecurityGroupViolation": AwsVPCSecurityGroupViolationTypeDef,
        "AwsEc2NetworkInterfaceViolation": AwsEc2NetworkInterfaceViolationTypeDef,
        "AwsEc2InstanceViolation": AwsEc2InstanceViolationTypeDef,
        "NetworkFirewallMissingFirewallViolation": NetworkFirewallMissingFirewallViolationTypeDef,
        "NetworkFirewallMissingSubnetViolation": NetworkFirewallMissingSubnetViolationTypeDef,
        "NetworkFirewallMissingExpectedRTViolation": (
            NetworkFirewallMissingExpectedRTViolationTypeDef
        ),
        "NetworkFirewallPolicyModifiedViolation": NetworkFirewallPolicyModifiedViolationTypeDef,
        "NetworkFirewallInternetTrafficNotInspectedViolation": (
            NetworkFirewallInternetTrafficNotInspectedViolationTypeDef
        ),
        "NetworkFirewallInvalidRouteConfigurationViolation": (
            NetworkFirewallInvalidRouteConfigurationViolationTypeDef
        ),
        "NetworkFirewallBlackHoleRouteDetectedViolation": (
            NetworkFirewallBlackHoleRouteDetectedViolationTypeDef
        ),
        "NetworkFirewallUnexpectedFirewallRoutesViolation": (
            NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef
        ),
        "NetworkFirewallUnexpectedGatewayRoutesViolation": (
            NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef
        ),
        "NetworkFirewallMissingExpectedRoutesViolation": (
            NetworkFirewallMissingExpectedRoutesViolationTypeDef
        ),
        "DnsRuleGroupPriorityConflictViolation": DnsRuleGroupPriorityConflictViolationTypeDef,
        "DnsDuplicateRuleGroupViolation": DnsDuplicateRuleGroupViolationTypeDef,
        "DnsRuleGroupLimitExceededViolation": DnsRuleGroupLimitExceededViolationTypeDef,
        "PossibleRemediationActions": PossibleRemediationActionsTypeDef,
        "FirewallSubnetIsOutOfScopeViolation": FirewallSubnetIsOutOfScopeViolationTypeDef,
        "RouteHasOutOfScopeEndpointViolation": RouteHasOutOfScopeEndpointViolationTypeDef,
        "ThirdPartyFirewallMissingFirewallViolation": (
            ThirdPartyFirewallMissingFirewallViolationTypeDef
        ),
        "ThirdPartyFirewallMissingSubnetViolation": ThirdPartyFirewallMissingSubnetViolationTypeDef,
        "ThirdPartyFirewallMissingExpectedRouteTableViolation": (
            ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef
        ),
        "FirewallSubnetMissingVPCEndpointViolation": (
            FirewallSubnetMissingVPCEndpointViolationTypeDef
        ),
    },
    total=False,
)

_RequiredViolationDetailTypeDef = TypedDict(
    "_RequiredViolationDetailTypeDef",
    {
        "PolicyId": str,
        "MemberAccount": str,
        "ResourceId": str,
        "ResourceType": str,
        "ResourceViolations": List[ResourceViolationTypeDef],
    },
)
_OptionalViolationDetailTypeDef = TypedDict(
    "_OptionalViolationDetailTypeDef",
    {
        "ResourceTags": List[TagTypeDef],
        "ResourceDescription": str,
    },
    total=False,
)


class ViolationDetailTypeDef(_RequiredViolationDetailTypeDef, _OptionalViolationDetailTypeDef):
    pass


GetViolationDetailsResponseTypeDef = TypedDict(
    "GetViolationDetailsResponseTypeDef",
    {
        "ViolationDetail": ViolationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
