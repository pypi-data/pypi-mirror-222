"""
Type annotations for license-manager-linux-subscriptions service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/type_defs/)

Usage::

    ```python
    from mypy_boto3_license_manager_linux_subscriptions.type_defs import FilterTypeDef

    data: FilterTypeDef = ...
    ```
"""
import sys
from typing import Dict, List, Sequence, Union

from .literals import (
    LinuxSubscriptionsDiscoveryType,
    OperatorType,
    OrganizationIntegrationType,
    StatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "FilterTypeDef",
    "LinuxSubscriptionsDiscoverySettingsOutputTypeDef",
    "ResponseMetadataTypeDef",
    "InstanceTypeDef",
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    "PaginatorConfigTypeDef",
    "SubscriptionTypeDef",
    "ListLinuxSubscriptionInstancesRequestRequestTypeDef",
    "ListLinuxSubscriptionsRequestRequestTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "UpdateServiceSettingsResponseTypeDef",
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    "LinuxSubscriptionsDiscoverySettingsUnionTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
    "ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef",
    "ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef",
    "ListLinuxSubscriptionsResponseTypeDef",
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Operator": OperatorType,
        "Values": Sequence[str],
    },
    total=False,
)

LinuxSubscriptionsDiscoverySettingsOutputTypeDef = TypedDict(
    "LinuxSubscriptionsDiscoverySettingsOutputTypeDef",
    {
        "OrganizationIntegration": OrganizationIntegrationType,
        "SourceRegions": List[str],
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

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AccountID": str,
        "AmiId": str,
        "InstanceID": str,
        "InstanceType": str,
        "LastUpdatedTime": str,
        "ProductCode": List[str],
        "Region": str,
        "Status": str,
        "SubscriptionName": str,
        "UsageOperation": str,
    },
    total=False,
)

LinuxSubscriptionsDiscoverySettingsTypeDef = TypedDict(
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    {
        "OrganizationIntegration": OrganizationIntegrationType,
        "SourceRegions": Sequence[str],
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

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "InstanceCount": int,
        "Name": str,
        "Type": str,
    },
    total=False,
)

ListLinuxSubscriptionInstancesRequestRequestTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLinuxSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListLinuxSubscriptionsRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "HomeRegions": List[str],
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": LinuxSubscriptionsDiscoverySettingsOutputTypeDef,
        "Status": StatusType,
        "StatusMessage": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateServiceSettingsResponseTypeDef = TypedDict(
    "UpdateServiceSettingsResponseTypeDef",
    {
        "HomeRegions": List[str],
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": LinuxSubscriptionsDiscoverySettingsOutputTypeDef,
        "Status": StatusType,
        "StatusMessage": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLinuxSubscriptionInstancesResponseTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LinuxSubscriptionsDiscoverySettingsUnionTypeDef = Union[
    LinuxSubscriptionsDiscoverySettingsTypeDef, LinuxSubscriptionsDiscoverySettingsOutputTypeDef
]
_RequiredUpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceSettingsRequestRequestTypeDef",
    {
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": LinuxSubscriptionsDiscoverySettingsTypeDef,
    },
)
_OptionalUpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceSettingsRequestRequestTypeDef",
    {
        "AllowUpdate": bool,
    },
    total=False,
)


class UpdateServiceSettingsRequestRequestTypeDef(
    _RequiredUpdateServiceSettingsRequestRequestTypeDef,
    _OptionalUpdateServiceSettingsRequestRequestTypeDef,
):
    pass


ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef = TypedDict(
    "ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListLinuxSubscriptionsResponseTypeDef = TypedDict(
    "ListLinuxSubscriptionsResponseTypeDef",
    {
        "NextToken": str,
        "Subscriptions": List[SubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
