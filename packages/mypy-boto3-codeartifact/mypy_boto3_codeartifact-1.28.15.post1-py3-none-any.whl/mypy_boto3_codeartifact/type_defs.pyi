"""
Type annotations for codeartifact service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/type_defs/)

Usage::

    ```python
    from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AllowPublishType,
    AllowUpstreamType,
    DomainStatusType,
    HashAlgorithmType,
    PackageFormatType,
    PackageVersionErrorCodeType,
    PackageVersionOriginTypeType,
    PackageVersionStatusType,
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
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CopyPackageVersionsRequestRequestTypeDef",
    "PackageVersionErrorTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagTypeDef",
    "DomainDescriptionTypeDef",
    "UpstreamRepositoryTypeDef",
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    "ResourcePolicyTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageVersionsRequestRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribeRepositoryRequestRequestTypeDef",
    "DisassociateExternalConnectionRequestRequestTypeDef",
    "DisposePackageVersionsRequestRequestTypeDef",
    "DomainEntryPointTypeDef",
    "DomainSummaryTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetDomainPermissionsPolicyRequestRequestTypeDef",
    "GetPackageVersionAssetRequestRequestTypeDef",
    "GetPackageVersionReadmeRequestRequestTypeDef",
    "GetRepositoryEndpointRequestRequestTypeDef",
    "GetRepositoryPermissionsPolicyRequestRequestTypeDef",
    "LicenseInfoTypeDef",
    "PaginatorConfigTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListPackageVersionAssetsRequestRequestTypeDef",
    "ListPackageVersionDependenciesRequestRequestTypeDef",
    "PackageDependencyTypeDef",
    "ListPackageVersionsRequestRequestTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "ListRepositoriesInDomainRequestRequestTypeDef",
    "RepositorySummaryTypeDef",
    "ListRepositoriesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PackageOriginRestrictionsTypeDef",
    "PublishPackageVersionRequestRequestTypeDef",
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    "PutRepositoryPermissionsPolicyRequestRequestTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackageVersionsStatusRequestRequestTypeDef",
    "GetAuthorizationTokenResultTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "PublishPackageVersionResultTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "DeleteDomainResultTypeDef",
    "DescribeDomainResultTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "UpdateRepositoryRequestRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "PackageVersionOriginTypeDef",
    "ListDomainsResultTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef",
    "ListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    "ListPackagesRequestListPackagesPaginateTypeDef",
    "ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef",
    "ListRepositoriesRequestListRepositoriesPaginateTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesResultTypeDef",
    "PackageOriginConfigurationTypeDef",
    "PutPackageOriginConfigurationRequestRequestTypeDef",
    "RepositoryDescriptionTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionSummaryTypeDef",
    "PackageDescriptionTypeDef",
    "PackageSummaryTypeDef",
    "PutPackageOriginConfigurationResultTypeDef",
    "AssociateExternalConnectionResultTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "UpdateRepositoryResultTypeDef",
    "DescribePackageVersionResultTypeDef",
    "ListPackageVersionsResultTypeDef",
    "DescribePackageResultTypeDef",
    "DeletePackageResultTypeDef",
    "ListPackagesResultTypeDef",
)

_RequiredAssetSummaryTypeDef = TypedDict(
    "_RequiredAssetSummaryTypeDef",
    {
        "name": str,
    },
)
_OptionalAssetSummaryTypeDef = TypedDict(
    "_OptionalAssetSummaryTypeDef",
    {
        "size": int,
        "hashes": Dict[HashAlgorithmType, str],
    },
    total=False,
)

class AssetSummaryTypeDef(_RequiredAssetSummaryTypeDef, _OptionalAssetSummaryTypeDef):
    pass

_RequiredAssociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
    },
)
_OptionalAssociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateExternalConnectionRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class AssociateExternalConnectionRequestRequestTypeDef(
    _RequiredAssociateExternalConnectionRequestRequestTypeDef,
    _OptionalAssociateExternalConnectionRequestRequestTypeDef,
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

_RequiredCopyPackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredCopyPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "sourceRepository": str,
        "destinationRepository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalCopyPackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalCopyPackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versions": Sequence[str],
        "versionRevisions": Mapping[str, str],
        "allowOverwrite": bool,
        "includeFromUpstream": bool,
    },
    total=False,
)

class CopyPackageVersionsRequestRequestTypeDef(
    _RequiredCopyPackageVersionsRequestRequestTypeDef,
    _OptionalCopyPackageVersionsRequestRequestTypeDef,
):
    pass

PackageVersionErrorTypeDef = TypedDict(
    "PackageVersionErrorTypeDef",
    {
        "errorCode": PackageVersionErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

SuccessfulPackageVersionInfoTypeDef = TypedDict(
    "SuccessfulPackageVersionInfoTypeDef",
    {
        "revision": str,
        "status": PackageVersionStatusType,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

DomainDescriptionTypeDef = TypedDict(
    "DomainDescriptionTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatusType,
        "createdTime": datetime,
        "encryptionKey": str,
        "repositoryCount": int,
        "assetSizeBytes": int,
        "s3BucketArn": str,
    },
    total=False,
)

UpstreamRepositoryTypeDef = TypedDict(
    "UpstreamRepositoryTypeDef",
    {
        "repositoryName": str,
    },
)

_RequiredDeleteDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDeleteDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class DeleteDomainPermissionsPolicyRequestRequestTypeDef(
    _RequiredDeleteDomainPermissionsPolicyRequestRequestTypeDef,
    _OptionalDeleteDomainPermissionsPolicyRequestRequestTypeDef,
):
    pass

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "resourceArn": str,
        "revision": str,
        "document": str,
    },
    total=False,
)

_RequiredDeleteDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDeleteDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DeleteDomainRequestRequestTypeDef(
    _RequiredDeleteDomainRequestRequestTypeDef, _OptionalDeleteDomainRequestRequestTypeDef
):
    pass

_RequiredDeletePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalDeletePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class DeletePackageRequestRequestTypeDef(
    _RequiredDeletePackageRequestRequestTypeDef, _OptionalDeletePackageRequestRequestTypeDef
):
    pass

_RequiredDeletePackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
    },
)
_OptionalDeletePackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)

class DeletePackageVersionsRequestRequestTypeDef(
    _RequiredDeletePackageVersionsRequestRequestTypeDef,
    _OptionalDeletePackageVersionsRequestRequestTypeDef,
):
    pass

_RequiredDeleteRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDeleteRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class DeleteRepositoryPermissionsPolicyRequestRequestTypeDef(
    _RequiredDeleteRepositoryPermissionsPolicyRequestRequestTypeDef,
    _OptionalDeleteRepositoryPermissionsPolicyRequestRequestTypeDef,
):
    pass

_RequiredDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DeleteRepositoryRequestRequestTypeDef(
    _RequiredDeleteRepositoryRequestRequestTypeDef, _OptionalDeleteRepositoryRequestRequestTypeDef
):
    pass

_RequiredDescribeDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDescribeDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DescribeDomainRequestRequestTypeDef(
    _RequiredDescribeDomainRequestRequestTypeDef, _OptionalDescribeDomainRequestRequestTypeDef
):
    pass

_RequiredDescribePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalDescribePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class DescribePackageRequestRequestTypeDef(
    _RequiredDescribePackageRequestRequestTypeDef, _OptionalDescribePackageRequestRequestTypeDef
):
    pass

_RequiredDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageVersionRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class DescribePackageVersionRequestRequestTypeDef(
    _RequiredDescribePackageVersionRequestRequestTypeDef,
    _OptionalDescribePackageVersionRequestRequestTypeDef,
):
    pass

_RequiredDescribeRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDescribeRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DescribeRepositoryRequestRequestTypeDef(
    _RequiredDescribeRepositoryRequestRequestTypeDef,
    _OptionalDescribeRepositoryRequestRequestTypeDef,
):
    pass

_RequiredDisassociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
    },
)
_OptionalDisassociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateExternalConnectionRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DisassociateExternalConnectionRequestRequestTypeDef(
    _RequiredDisassociateExternalConnectionRequestRequestTypeDef,
    _OptionalDisassociateExternalConnectionRequestRequestTypeDef,
):
    pass

_RequiredDisposePackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDisposePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
    },
)
_OptionalDisposePackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDisposePackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versionRevisions": Mapping[str, str],
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)

class DisposePackageVersionsRequestRequestTypeDef(
    _RequiredDisposePackageVersionsRequestRequestTypeDef,
    _OptionalDisposePackageVersionsRequestRequestTypeDef,
):
    pass

DomainEntryPointTypeDef = TypedDict(
    "DomainEntryPointTypeDef",
    {
        "repositoryName": str,
        "externalConnectionName": str,
    },
    total=False,
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatusType,
        "createdTime": datetime,
        "encryptionKey": str,
    },
    total=False,
)

_RequiredGetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizationTokenRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalGetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizationTokenRequestRequestTypeDef",
    {
        "domainOwner": str,
        "durationSeconds": int,
    },
    total=False,
)

class GetAuthorizationTokenRequestRequestTypeDef(
    _RequiredGetAuthorizationTokenRequestRequestTypeDef,
    _OptionalGetAuthorizationTokenRequestRequestTypeDef,
):
    pass

_RequiredGetDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalGetDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class GetDomainPermissionsPolicyRequestRequestTypeDef(
    _RequiredGetDomainPermissionsPolicyRequestRequestTypeDef,
    _OptionalGetDomainPermissionsPolicyRequestRequestTypeDef,
):
    pass

_RequiredGetPackageVersionAssetRequestRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionAssetRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "asset": str,
    },
)
_OptionalGetPackageVersionAssetRequestRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionAssetRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "packageVersionRevision": str,
    },
    total=False,
)

class GetPackageVersionAssetRequestRequestTypeDef(
    _RequiredGetPackageVersionAssetRequestRequestTypeDef,
    _OptionalGetPackageVersionAssetRequestRequestTypeDef,
):
    pass

_RequiredGetPackageVersionReadmeRequestRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionReadmeRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalGetPackageVersionReadmeRequestRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionReadmeRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class GetPackageVersionReadmeRequestRequestTypeDef(
    _RequiredGetPackageVersionReadmeRequestRequestTypeDef,
    _OptionalGetPackageVersionReadmeRequestRequestTypeDef,
):
    pass

_RequiredGetRepositoryEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryEndpointRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
    },
)
_OptionalGetRepositoryEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryEndpointRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class GetRepositoryEndpointRequestRequestTypeDef(
    _RequiredGetRepositoryEndpointRequestRequestTypeDef,
    _OptionalGetRepositoryEndpointRequestRequestTypeDef,
):
    pass

_RequiredGetRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalGetRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class GetRepositoryPermissionsPolicyRequestRequestTypeDef(
    _RequiredGetRepositoryPermissionsPolicyRequestRequestTypeDef,
    _OptionalGetRepositoryPermissionsPolicyRequestRequestTypeDef,
):
    pass

LicenseInfoTypeDef = TypedDict(
    "LicenseInfoTypeDef",
    {
        "name": str,
        "url": str,
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

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListPackageVersionAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionAssetsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionAssetsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPackageVersionAssetsRequestRequestTypeDef(
    _RequiredListPackageVersionAssetsRequestRequestTypeDef,
    _OptionalListPackageVersionAssetsRequestRequestTypeDef,
):
    pass

_RequiredListPackageVersionDependenciesRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionDependenciesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionDependenciesRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionDependenciesRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "nextToken": str,
    },
    total=False,
)

class ListPackageVersionDependenciesRequestRequestTypeDef(
    _RequiredListPackageVersionDependenciesRequestRequestTypeDef,
    _OptionalListPackageVersionDependenciesRequestRequestTypeDef,
):
    pass

PackageDependencyTypeDef = TypedDict(
    "PackageDependencyTypeDef",
    {
        "namespace": str,
        "package": str,
        "dependencyType": str,
        "versionRequirement": str,
    },
    total=False,
)

_RequiredListPackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalListPackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "status": PackageVersionStatusType,
        "sortBy": Literal["PUBLISHED_TIME"],
        "maxResults": int,
        "nextToken": str,
        "originType": PackageVersionOriginTypeType,
    },
    total=False,
)

class ListPackageVersionsRequestRequestTypeDef(
    _RequiredListPackageVersionsRequestRequestTypeDef,
    _OptionalListPackageVersionsRequestRequestTypeDef,
):
    pass

_RequiredListPackagesRequestRequestTypeDef = TypedDict(
    "_RequiredListPackagesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalListPackagesRequestRequestTypeDef = TypedDict(
    "_OptionalListPackagesRequestRequestTypeDef",
    {
        "domainOwner": str,
        "format": PackageFormatType,
        "namespace": str,
        "packagePrefix": str,
        "maxResults": int,
        "nextToken": str,
        "publish": AllowPublishType,
        "upstream": AllowUpstreamType,
    },
    total=False,
)

class ListPackagesRequestRequestTypeDef(
    _RequiredListPackagesRequestRequestTypeDef, _OptionalListPackagesRequestRequestTypeDef
):
    pass

_RequiredListRepositoriesInDomainRequestRequestTypeDef = TypedDict(
    "_RequiredListRepositoriesInDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalListRepositoriesInDomainRequestRequestTypeDef = TypedDict(
    "_OptionalListRepositoriesInDomainRequestRequestTypeDef",
    {
        "domainOwner": str,
        "administratorAccount": str,
        "repositoryPrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListRepositoriesInDomainRequestRequestTypeDef(
    _RequiredListRepositoriesInDomainRequestRequestTypeDef,
    _OptionalListRepositoriesInDomainRequestRequestTypeDef,
):
    pass

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
        "createdTime": datetime,
    },
    total=False,
)

ListRepositoriesRequestRequestTypeDef = TypedDict(
    "ListRepositoriesRequestRequestTypeDef",
    {
        "repositoryPrefix": str,
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

PackageOriginRestrictionsTypeDef = TypedDict(
    "PackageOriginRestrictionsTypeDef",
    {
        "publish": AllowPublishType,
        "upstream": AllowUpstreamType,
    },
)

_RequiredPublishPackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredPublishPackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "assetContent": Union[str, bytes, IO[Any], StreamingBody],
        "assetName": str,
        "assetSHA256": str,
    },
)
_OptionalPublishPackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalPublishPackageVersionRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "unfinished": bool,
    },
    total=False,
)

class PublishPackageVersionRequestRequestTypeDef(
    _RequiredPublishPackageVersionRequestRequestTypeDef,
    _OptionalPublishPackageVersionRequestRequestTypeDef,
):
    pass

_RequiredPutDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "policyDocument": str,
    },
)
_OptionalPutDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class PutDomainPermissionsPolicyRequestRequestTypeDef(
    _RequiredPutDomainPermissionsPolicyRequestRequestTypeDef,
    _OptionalPutDomainPermissionsPolicyRequestRequestTypeDef,
):
    pass

_RequiredPutRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "policyDocument": str,
    },
)
_OptionalPutRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class PutRepositoryPermissionsPolicyRequestRequestTypeDef(
    _RequiredPutRepositoryPermissionsPolicyRequestRequestTypeDef,
    _OptionalPutRepositoryPermissionsPolicyRequestRequestTypeDef,
):
    pass

RepositoryExternalConnectionInfoTypeDef = TypedDict(
    "RepositoryExternalConnectionInfoTypeDef",
    {
        "externalConnectionName": str,
        "packageFormat": PackageFormatType,
        "status": Literal["Available"],
    },
    total=False,
)

UpstreamRepositoryInfoTypeDef = TypedDict(
    "UpstreamRepositoryInfoTypeDef",
    {
        "repositoryName": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdatePackageVersionsStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageVersionsStatusRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "targetStatus": PackageVersionStatusType,
    },
)
_OptionalUpdatePackageVersionsStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageVersionsStatusRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versionRevisions": Mapping[str, str],
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)

class UpdatePackageVersionsStatusRequestRequestTypeDef(
    _RequiredUpdatePackageVersionsStatusRequestRequestTypeDef,
    _OptionalUpdatePackageVersionsStatusRequestRequestTypeDef,
):
    pass

GetAuthorizationTokenResultTypeDef = TypedDict(
    "GetAuthorizationTokenResultTypeDef",
    {
        "authorizationToken": str,
        "expiration": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPackageVersionAssetResultTypeDef = TypedDict(
    "GetPackageVersionAssetResultTypeDef",
    {
        "asset": StreamingBody,
        "assetName": str,
        "packageVersion": str,
        "packageVersionRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPackageVersionReadmeResultTypeDef = TypedDict(
    "GetPackageVersionReadmeResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRepositoryEndpointResultTypeDef = TypedDict(
    "GetRepositoryEndpointResultTypeDef",
    {
        "repositoryEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPackageVersionAssetsResultTypeDef = TypedDict(
    "ListPackageVersionAssetsResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "assets": List[AssetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PublishPackageVersionResultTypeDef = TypedDict(
    "PublishPackageVersionResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "status": PackageVersionStatusType,
        "asset": AssetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CopyPackageVersionsResultTypeDef = TypedDict(
    "CopyPackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePackageVersionsResultTypeDef = TypedDict(
    "DeletePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisposePackageVersionsResultTypeDef = TypedDict(
    "DisposePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePackageVersionsStatusResultTypeDef = TypedDict(
    "UpdatePackageVersionsStatusResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "encryptionKey": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "domain": DomainDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "domain": DomainDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDomainResultTypeDef = TypedDict(
    "DescribeDomainResultTypeDef",
    {
        "domain": DomainDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
        "description": str,
        "upstreams": Sequence[UpstreamRepositoryTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateRepositoryRequestRequestTypeDef(
    _RequiredCreateRepositoryRequestRequestTypeDef, _OptionalCreateRepositoryRequestRequestTypeDef
):
    pass

_RequiredUpdateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalUpdateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
        "description": str,
        "upstreams": Sequence[UpstreamRepositoryTypeDef],
    },
    total=False,
)

class UpdateRepositoryRequestRequestTypeDef(
    _RequiredUpdateRepositoryRequestRequestTypeDef, _OptionalUpdateRepositoryRequestRequestTypeDef
):
    pass

DeleteDomainPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDomainPermissionsPolicyResultTypeDef = TypedDict(
    "GetDomainPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutDomainPermissionsPolicyResultTypeDef = TypedDict(
    "PutDomainPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PackageVersionOriginTypeDef = TypedDict(
    "PackageVersionOriginTypeDef",
    {
        "domainEntryPoint": DomainEntryPointTypeDef,
        "originType": PackageVersionOriginTypeType,
    },
    total=False,
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "domains": List[DomainSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef = TypedDict(
    "_RequiredListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef = TypedDict(
    "_OptionalListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef(
    _RequiredListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef,
    _OptionalListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef,
):
    pass

_RequiredListPackageVersionsRequestListPackageVersionsPaginateTypeDef = TypedDict(
    "_RequiredListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalListPackageVersionsRequestListPackageVersionsPaginateTypeDef = TypedDict(
    "_OptionalListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "status": PackageVersionStatusType,
        "sortBy": Literal["PUBLISHED_TIME"],
        "originType": PackageVersionOriginTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPackageVersionsRequestListPackageVersionsPaginateTypeDef(
    _RequiredListPackageVersionsRequestListPackageVersionsPaginateTypeDef,
    _OptionalListPackageVersionsRequestListPackageVersionsPaginateTypeDef,
):
    pass

_RequiredListPackagesRequestListPackagesPaginateTypeDef = TypedDict(
    "_RequiredListPackagesRequestListPackagesPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalListPackagesRequestListPackagesPaginateTypeDef = TypedDict(
    "_OptionalListPackagesRequestListPackagesPaginateTypeDef",
    {
        "domainOwner": str,
        "format": PackageFormatType,
        "namespace": str,
        "packagePrefix": str,
        "publish": AllowPublishType,
        "upstream": AllowUpstreamType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPackagesRequestListPackagesPaginateTypeDef(
    _RequiredListPackagesRequestListPackagesPaginateTypeDef,
    _OptionalListPackagesRequestListPackagesPaginateTypeDef,
):
    pass

_RequiredListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef = TypedDict(
    "_RequiredListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef",
    {
        "domain": str,
    },
)
_OptionalListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef = TypedDict(
    "_OptionalListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef",
    {
        "domainOwner": str,
        "administratorAccount": str,
        "repositoryPrefix": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef(
    _RequiredListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef,
    _OptionalListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef,
):
    pass

ListRepositoriesRequestListRepositoriesPaginateTypeDef = TypedDict(
    "ListRepositoriesRequestListRepositoriesPaginateTypeDef",
    {
        "repositoryPrefix": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPackageVersionDependenciesResultTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "dependencies": List[PackageDependencyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRepositoriesInDomainResultTypeDef = TypedDict(
    "ListRepositoriesInDomainResultTypeDef",
    {
        "repositories": List[RepositorySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRepositoriesResultTypeDef = TypedDict(
    "ListRepositoriesResultTypeDef",
    {
        "repositories": List[RepositorySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PackageOriginConfigurationTypeDef = TypedDict(
    "PackageOriginConfigurationTypeDef",
    {
        "restrictions": PackageOriginRestrictionsTypeDef,
    },
    total=False,
)

_RequiredPutPackageOriginConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutPackageOriginConfigurationRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "restrictions": PackageOriginRestrictionsTypeDef,
    },
)
_OptionalPutPackageOriginConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutPackageOriginConfigurationRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class PutPackageOriginConfigurationRequestRequestTypeDef(
    _RequiredPutPackageOriginConfigurationRequestRequestTypeDef,
    _OptionalPutPackageOriginConfigurationRequestRequestTypeDef,
):
    pass

RepositoryDescriptionTypeDef = TypedDict(
    "RepositoryDescriptionTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
        "upstreams": List[UpstreamRepositoryInfoTypeDef],
        "externalConnections": List[RepositoryExternalConnectionInfoTypeDef],
        "createdTime": datetime,
    },
    total=False,
)

PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "packageName": str,
        "displayName": str,
        "version": str,
        "summary": str,
        "homePage": str,
        "sourceCodeRepository": str,
        "publishedTime": datetime,
        "licenses": List[LicenseInfoTypeDef],
        "revision": str,
        "status": PackageVersionStatusType,
        "origin": PackageVersionOriginTypeDef,
    },
    total=False,
)

_RequiredPackageVersionSummaryTypeDef = TypedDict(
    "_RequiredPackageVersionSummaryTypeDef",
    {
        "version": str,
        "status": PackageVersionStatusType,
    },
)
_OptionalPackageVersionSummaryTypeDef = TypedDict(
    "_OptionalPackageVersionSummaryTypeDef",
    {
        "revision": str,
        "origin": PackageVersionOriginTypeDef,
    },
    total=False,
)

class PackageVersionSummaryTypeDef(
    _RequiredPackageVersionSummaryTypeDef, _OptionalPackageVersionSummaryTypeDef
):
    pass

PackageDescriptionTypeDef = TypedDict(
    "PackageDescriptionTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "name": str,
        "originConfiguration": PackageOriginConfigurationTypeDef,
    },
    total=False,
)

PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "originConfiguration": PackageOriginConfigurationTypeDef,
    },
    total=False,
)

PutPackageOriginConfigurationResultTypeDef = TypedDict(
    "PutPackageOriginConfigurationResultTypeDef",
    {
        "originConfiguration": PackageOriginConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateExternalConnectionResultTypeDef = TypedDict(
    "AssociateExternalConnectionResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRepositoryResultTypeDef = TypedDict(
    "CreateRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRepositoryResultTypeDef = TypedDict(
    "DeleteRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeRepositoryResultTypeDef = TypedDict(
    "DescribeRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociateExternalConnectionResultTypeDef = TypedDict(
    "DisassociateExternalConnectionResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRepositoryResultTypeDef = TypedDict(
    "UpdateRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePackageVersionResultTypeDef = TypedDict(
    "DescribePackageVersionResultTypeDef",
    {
        "packageVersion": PackageVersionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPackageVersionsResultTypeDef = TypedDict(
    "ListPackageVersionsResultTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "versions": List[PackageVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePackageResultTypeDef = TypedDict(
    "DescribePackageResultTypeDef",
    {
        "package": PackageDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePackageResultTypeDef = TypedDict(
    "DeletePackageResultTypeDef",
    {
        "deletedPackage": PackageSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPackagesResultTypeDef = TypedDict(
    "ListPackagesResultTypeDef",
    {
        "packages": List[PackageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
