"""
Type annotations for workspaces-web service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/type_defs/)

Usage::

    ```python
    from mypy_boto3_workspaces_web.type_defs import AssociateBrowserSettingsRequestRequestTypeDef

    data: AssociateBrowserSettingsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AuthenticationTypeType,
    EnabledTypeType,
    IdentityProviderTypeType,
    PortalStatusType,
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
    "AssociateBrowserSettingsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateIpAccessSettingsRequestRequestTypeDef",
    "AssociateNetworkSettingsRequestRequestTypeDef",
    "AssociateTrustStoreRequestRequestTypeDef",
    "AssociateUserAccessLoggingSettingsRequestRequestTypeDef",
    "AssociateUserSettingsRequestRequestTypeDef",
    "BrowserSettingsSummaryTypeDef",
    "BrowserSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "TagTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "IpRuleTypeDef",
    "DeleteBrowserSettingsRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteIpAccessSettingsRequestRequestTypeDef",
    "DeleteNetworkSettingsRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeleteTrustStoreRequestRequestTypeDef",
    "DeleteUserAccessLoggingSettingsRequestRequestTypeDef",
    "DeleteUserSettingsRequestRequestTypeDef",
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    "DisassociateIpAccessSettingsRequestRequestTypeDef",
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    "DisassociateTrustStoreRequestRequestTypeDef",
    "DisassociateUserAccessLoggingSettingsRequestRequestTypeDef",
    "DisassociateUserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsRequestRequestTypeDef",
    "GetIdentityProviderRequestRequestTypeDef",
    "IdentityProviderTypeDef",
    "GetIpAccessSettingsRequestRequestTypeDef",
    "GetNetworkSettingsRequestRequestTypeDef",
    "NetworkSettingsTypeDef",
    "GetPortalRequestRequestTypeDef",
    "PortalTypeDef",
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    "GetTrustStoreCertificateRequestRequestTypeDef",
    "GetTrustStoreRequestRequestTypeDef",
    "TrustStoreTypeDef",
    "GetUserAccessLoggingSettingsRequestRequestTypeDef",
    "UserAccessLoggingSettingsTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "UserSettingsTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IpAccessSettingsSummaryTypeDef",
    "ListBrowserSettingsRequestRequestTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIpAccessSettingsRequestRequestTypeDef",
    "ListNetworkSettingsRequestRequestTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "PortalSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    "ListTrustStoresRequestRequestTypeDef",
    "TrustStoreSummaryTypeDef",
    "ListUserAccessLoggingSettingsRequestRequestTypeDef",
    "UserAccessLoggingSettingsSummaryTypeDef",
    "ListUserSettingsRequestRequestTypeDef",
    "UserSettingsSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrowserSettingsRequestRequestTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateNetworkSettingsRequestRequestTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdateTrustStoreRequestRequestTypeDef",
    "UpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "AssociateBrowserSettingsResponseTypeDef",
    "AssociateIpAccessSettingsResponseTypeDef",
    "AssociateNetworkSettingsResponseTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "CreateBrowserSettingsResponseTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateIpAccessSettingsResponseTypeDef",
    "CreateNetworkSettingsResponseTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateTrustStoreResponseTypeDef",
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    "CreateUserSettingsResponseTypeDef",
    "GetPortalServiceProviderMetadataResponseTypeDef",
    "UpdateTrustStoreResponseTypeDef",
    "ListBrowserSettingsResponseTypeDef",
    "GetBrowserSettingsResponseTypeDef",
    "UpdateBrowserSettingsResponseTypeDef",
    "ListTrustStoreCertificatesResponseTypeDef",
    "GetTrustStoreCertificateResponseTypeDef",
    "CreateBrowserSettingsRequestRequestTypeDef",
    "CreateNetworkSettingsRequestRequestTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreateTrustStoreRequestRequestTypeDef",
    "CreateUserAccessLoggingSettingsRequestRequestTypeDef",
    "CreateUserSettingsRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIpAccessSettingsRequestRequestTypeDef",
    "IpAccessSettingsTypeDef",
    "UpdateIpAccessSettingsRequestRequestTypeDef",
    "GetIdentityProviderResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "GetNetworkSettingsResponseTypeDef",
    "UpdateNetworkSettingsResponseTypeDef",
    "GetPortalResponseTypeDef",
    "UpdatePortalResponseTypeDef",
    "GetTrustStoreResponseTypeDef",
    "GetUserAccessLoggingSettingsResponseTypeDef",
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    "GetUserSettingsResponseTypeDef",
    "UpdateUserSettingsResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListIpAccessSettingsResponseTypeDef",
    "ListNetworkSettingsResponseTypeDef",
    "ListPortalsResponseTypeDef",
    "ListTrustStoresResponseTypeDef",
    "ListUserAccessLoggingSettingsResponseTypeDef",
    "ListUserSettingsResponseTypeDef",
    "GetIpAccessSettingsResponseTypeDef",
    "UpdateIpAccessSettingsResponseTypeDef",
)

AssociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
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

AssociateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "AssociateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
        "portalArn": str,
    },
)

AssociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "AssociateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
    },
)

AssociateTrustStoreRequestRequestTypeDef = TypedDict(
    "AssociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
    },
)

AssociateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userAccessLoggingSettingsArn": str,
    },
)

AssociateUserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
    },
)

BrowserSettingsSummaryTypeDef = TypedDict(
    "BrowserSettingsSummaryTypeDef",
    {
        "browserSettingsArn": str,
    },
    total=False,
)

_RequiredBrowserSettingsTypeDef = TypedDict(
    "_RequiredBrowserSettingsTypeDef",
    {
        "browserSettingsArn": str,
    },
)
_OptionalBrowserSettingsTypeDef = TypedDict(
    "_OptionalBrowserSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "browserPolicy": str,
    },
    total=False,
)


class BrowserSettingsTypeDef(_RequiredBrowserSettingsTypeDef, _OptionalBrowserSettingsTypeDef):
    pass


CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "issuer": str,
        "notValidAfter": datetime,
        "notValidBefore": datetime,
        "subject": str,
        "thumbprint": str,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "body": bytes,
        "issuer": str,
        "notValidAfter": datetime,
        "notValidBefore": datetime,
        "subject": str,
        "thumbprint": str,
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

_RequiredCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderDetails": Mapping[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
        "portalArn": str,
    },
)
_OptionalCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityProviderRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class CreateIdentityProviderRequestRequestTypeDef(
    _RequiredCreateIdentityProviderRequestRequestTypeDef,
    _OptionalCreateIdentityProviderRequestRequestTypeDef,
):
    pass


_RequiredIpRuleTypeDef = TypedDict(
    "_RequiredIpRuleTypeDef",
    {
        "ipRange": str,
    },
)
_OptionalIpRuleTypeDef = TypedDict(
    "_OptionalIpRuleTypeDef",
    {
        "description": str,
    },
    total=False,
)


class IpRuleTypeDef(_RequiredIpRuleTypeDef, _OptionalIpRuleTypeDef):
    pass


DeleteBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

DeleteIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "DeleteIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)

DeleteNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DeleteNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DeleteTrustStoreRequestRequestTypeDef = TypedDict(
    "DeleteTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

DeleteUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)

DeleteUserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

DisassociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateIpAccessSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateTrustStoreRequestRequestTypeDef = TypedDict(
    "DisassociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateUserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetBrowserSettingsRequestRequestTypeDef = TypedDict(
    "GetBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

GetIdentityProviderRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

_RequiredIdentityProviderTypeDef = TypedDict(
    "_RequiredIdentityProviderTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalIdentityProviderTypeDef = TypedDict(
    "_OptionalIdentityProviderTypeDef",
    {
        "identityProviderDetails": Dict[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)


class IdentityProviderTypeDef(_RequiredIdentityProviderTypeDef, _OptionalIdentityProviderTypeDef):
    pass


GetIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "GetIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)

GetNetworkSettingsRequestRequestTypeDef = TypedDict(
    "GetNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

_RequiredNetworkSettingsTypeDef = TypedDict(
    "_RequiredNetworkSettingsTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalNetworkSettingsTypeDef = TypedDict(
    "_OptionalNetworkSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
    total=False,
)


class NetworkSettingsTypeDef(_RequiredNetworkSettingsTypeDef, _OptionalNetworkSettingsTypeDef):
    pass


GetPortalRequestRequestTypeDef = TypedDict(
    "GetPortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

PortalTypeDef = TypedDict(
    "PortalTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "browserSettingsArn": str,
        "browserType": Literal["Chrome"],
        "creationDate": datetime,
        "displayName": str,
        "ipAccessSettingsArn": str,
        "networkSettingsArn": str,
        "portalArn": str,
        "portalEndpoint": str,
        "portalStatus": PortalStatusType,
        "rendererType": Literal["AppStream"],
        "statusReason": str,
        "trustStoreArn": str,
        "userAccessLoggingSettingsArn": str,
        "userSettingsArn": str,
    },
    total=False,
)

GetPortalServiceProviderMetadataRequestRequestTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetTrustStoreCertificateRequestRequestTypeDef = TypedDict(
    "GetTrustStoreCertificateRequestRequestTypeDef",
    {
        "thumbprint": str,
        "trustStoreArn": str,
    },
)

GetTrustStoreRequestRequestTypeDef = TypedDict(
    "GetTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

TrustStoreTypeDef = TypedDict(
    "TrustStoreTypeDef",
    {
        "associatedPortalArns": List[str],
        "trustStoreArn": str,
    },
    total=False,
)

GetUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "GetUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)

_RequiredUserAccessLoggingSettingsTypeDef = TypedDict(
    "_RequiredUserAccessLoggingSettingsTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
_OptionalUserAccessLoggingSettingsTypeDef = TypedDict(
    "_OptionalUserAccessLoggingSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "kinesisStreamArn": str,
    },
    total=False,
)


class UserAccessLoggingSettingsTypeDef(
    _RequiredUserAccessLoggingSettingsTypeDef, _OptionalUserAccessLoggingSettingsTypeDef
):
    pass


GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

_RequiredUserSettingsTypeDef = TypedDict(
    "_RequiredUserSettingsTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUserSettingsTypeDef = TypedDict(
    "_OptionalUserSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "copyAllowed": EnabledTypeType,
        "disconnectTimeoutInMinutes": int,
        "downloadAllowed": EnabledTypeType,
        "idleDisconnectTimeoutInMinutes": int,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)


class UserSettingsTypeDef(_RequiredUserSettingsTypeDef, _OptionalUserSettingsTypeDef):
    pass


IdentityProviderSummaryTypeDef = TypedDict(
    "IdentityProviderSummaryTypeDef",
    {
        "identityProviderArn": str,
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)

IpAccessSettingsSummaryTypeDef = TypedDict(
    "IpAccessSettingsSummaryTypeDef",
    {
        "creationDate": datetime,
        "description": str,
        "displayName": str,
        "ipAccessSettingsArn": str,
    },
    total=False,
)

ListBrowserSettingsRequestRequestTypeDef = TypedDict(
    "ListBrowserSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIdentityProvidersRequestRequestTypeDef(
    _RequiredListIdentityProvidersRequestRequestTypeDef,
    _OptionalListIdentityProvidersRequestRequestTypeDef,
):
    pass


ListIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "ListIpAccessSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListNetworkSettingsRequestRequestTypeDef = TypedDict(
    "ListNetworkSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

NetworkSettingsSummaryTypeDef = TypedDict(
    "NetworkSettingsSummaryTypeDef",
    {
        "networkSettingsArn": str,
        "vpcId": str,
    },
    total=False,
)

ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

PortalSummaryTypeDef = TypedDict(
    "PortalSummaryTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "browserSettingsArn": str,
        "browserType": Literal["Chrome"],
        "creationDate": datetime,
        "displayName": str,
        "ipAccessSettingsArn": str,
        "networkSettingsArn": str,
        "portalArn": str,
        "portalEndpoint": str,
        "portalStatus": PortalStatusType,
        "rendererType": Literal["AppStream"],
        "trustStoreArn": str,
        "userAccessLoggingSettingsArn": str,
        "userSettingsArn": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

_RequiredListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTrustStoreCertificatesRequestRequestTypeDef(
    _RequiredListTrustStoreCertificatesRequestRequestTypeDef,
    _OptionalListTrustStoreCertificatesRequestRequestTypeDef,
):
    pass


ListTrustStoresRequestRequestTypeDef = TypedDict(
    "ListTrustStoresRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

TrustStoreSummaryTypeDef = TypedDict(
    "TrustStoreSummaryTypeDef",
    {
        "trustStoreArn": str,
    },
    total=False,
)

ListUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "ListUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

UserAccessLoggingSettingsSummaryTypeDef = TypedDict(
    "UserAccessLoggingSettingsSummaryTypeDef",
    {
        "kinesisStreamArn": str,
        "userAccessLoggingSettingsArn": str,
    },
    total=False,
)

ListUserSettingsRequestRequestTypeDef = TypedDict(
    "ListUserSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

UserSettingsSummaryTypeDef = TypedDict(
    "UserSettingsSummaryTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "disconnectTimeoutInMinutes": int,
        "downloadAllowed": EnabledTypeType,
        "idleDisconnectTimeoutInMinutes": int,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
        "userSettingsArn": str,
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

_RequiredUpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)
_OptionalUpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
        "clientToken": str,
    },
    total=False,
)


class UpdateBrowserSettingsRequestRequestTypeDef(
    _RequiredUpdateBrowserSettingsRequestRequestTypeDef,
    _OptionalUpdateBrowserSettingsRequestRequestTypeDef,
):
    pass


_RequiredUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderRequestRequestTypeDef",
    {
        "clientToken": str,
        "identityProviderDetails": Mapping[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)


class UpdateIdentityProviderRequestRequestTypeDef(
    _RequiredUpdateIdentityProviderRequestRequestTypeDef,
    _OptionalUpdateIdentityProviderRequestRequestTypeDef,
):
    pass


_RequiredUpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalUpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
    total=False,
)


class UpdateNetworkSettingsRequestRequestTypeDef(
    _RequiredUpdateNetworkSettingsRequestRequestTypeDef,
    _OptionalUpdateNetworkSettingsRequestRequestTypeDef,
):
    pass


_RequiredUpdatePortalRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalUpdatePortalRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePortalRequestRequestTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "displayName": str,
    },
    total=False,
)


class UpdatePortalRequestRequestTypeDef(
    _RequiredUpdatePortalRequestRequestTypeDef, _OptionalUpdatePortalRequestRequestTypeDef
):
    pass


_RequiredUpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalUpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustStoreRequestRequestTypeDef",
    {
        "certificatesToAdd": Sequence[Union[str, bytes, IO[Any], StreamingBody]],
        "certificatesToDelete": Sequence[str],
        "clientToken": str,
    },
    total=False,
)


class UpdateTrustStoreRequestRequestTypeDef(
    _RequiredUpdateTrustStoreRequestRequestTypeDef, _OptionalUpdateTrustStoreRequestRequestTypeDef
):
    pass


_RequiredUpdateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
_OptionalUpdateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "kinesisStreamArn": str,
    },
    total=False,
)


class UpdateUserAccessLoggingSettingsRequestRequestTypeDef(
    _RequiredUpdateUserAccessLoggingSettingsRequestRequestTypeDef,
    _OptionalUpdateUserAccessLoggingSettingsRequestRequestTypeDef,
):
    pass


_RequiredUpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "copyAllowed": EnabledTypeType,
        "disconnectTimeoutInMinutes": int,
        "downloadAllowed": EnabledTypeType,
        "idleDisconnectTimeoutInMinutes": int,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)


class UpdateUserSettingsRequestRequestTypeDef(
    _RequiredUpdateUserSettingsRequestRequestTypeDef,
    _OptionalUpdateUserSettingsRequestRequestTypeDef,
):
    pass


AssociateBrowserSettingsResponseTypeDef = TypedDict(
    "AssociateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateIpAccessSettingsResponseTypeDef = TypedDict(
    "AssociateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateNetworkSettingsResponseTypeDef = TypedDict(
    "AssociateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateTrustStoreResponseTypeDef = TypedDict(
    "AssociateTrustStoreResponseTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userAccessLoggingSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateUserSettingsResponseTypeDef = TypedDict(
    "AssociateUserSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateBrowserSettingsResponseTypeDef = TypedDict(
    "CreateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "identityProviderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateIpAccessSettingsResponseTypeDef = TypedDict(
    "CreateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateNetworkSettingsResponseTypeDef = TypedDict(
    "CreateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalArn": str,
        "portalEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTrustStoreResponseTypeDef = TypedDict(
    "CreateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateUserSettingsResponseTypeDef = TypedDict(
    "CreateUserSettingsResponseTypeDef",
    {
        "userSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPortalServiceProviderMetadataResponseTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataResponseTypeDef",
    {
        "portalArn": str,
        "serviceProviderSamlMetadata": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTrustStoreResponseTypeDef = TypedDict(
    "UpdateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBrowserSettingsResponseTypeDef = TypedDict(
    "ListBrowserSettingsResponseTypeDef",
    {
        "browserSettings": List[BrowserSettingsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBrowserSettingsResponseTypeDef = TypedDict(
    "GetBrowserSettingsResponseTypeDef",
    {
        "browserSettings": BrowserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateBrowserSettingsResponseTypeDef = TypedDict(
    "UpdateBrowserSettingsResponseTypeDef",
    {
        "browserSettings": BrowserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTrustStoreCertificatesResponseTypeDef = TypedDict(
    "ListTrustStoreCertificatesResponseTypeDef",
    {
        "certificateList": List[CertificateSummaryTypeDef],
        "nextToken": str,
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetTrustStoreCertificateResponseTypeDef = TypedDict(
    "GetTrustStoreCertificateResponseTypeDef",
    {
        "certificate": CertificateTypeDef,
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
    },
)
_OptionalCreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBrowserSettingsRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Mapping[str, str],
        "clientToken": str,
        "customerManagedKey": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateBrowserSettingsRequestRequestTypeDef(
    _RequiredCreateBrowserSettingsRequestRequestTypeDef,
    _OptionalCreateBrowserSettingsRequestRequestTypeDef,
):
    pass


_RequiredCreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkSettingsRequestRequestTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)
_OptionalCreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateNetworkSettingsRequestRequestTypeDef(
    _RequiredCreateNetworkSettingsRequestRequestTypeDef,
    _OptionalCreateNetworkSettingsRequestRequestTypeDef,
):
    pass


CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Mapping[str, str],
        "authenticationType": AuthenticationTypeType,
        "clientToken": str,
        "customerManagedKey": str,
        "displayName": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

_RequiredCreateTrustStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustStoreRequestRequestTypeDef",
    {
        "certificateList": Sequence[Union[str, bytes, IO[Any], StreamingBody]],
    },
)
_OptionalCreateTrustStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustStoreRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateTrustStoreRequestRequestTypeDef(
    _RequiredCreateTrustStoreRequestRequestTypeDef, _OptionalCreateTrustStoreRequestRequestTypeDef
):
    pass


_RequiredCreateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "kinesisStreamArn": str,
    },
)
_OptionalCreateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateUserAccessLoggingSettingsRequestRequestTypeDef(
    _RequiredCreateUserAccessLoggingSettingsRequestRequestTypeDef,
    _OptionalCreateUserAccessLoggingSettingsRequestRequestTypeDef,
):
    pass


_RequiredCreateUserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserSettingsRequestRequestTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
)
_OptionalCreateUserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "disconnectTimeoutInMinutes": int,
        "idleDisconnectTimeoutInMinutes": int,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateUserSettingsRequestRequestTypeDef(
    _RequiredCreateUserSettingsRequestRequestTypeDef,
    _OptionalCreateUserSettingsRequestRequestTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass


_RequiredCreateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipRules": Sequence[IpRuleTypeDef],
    },
)
_OptionalCreateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIpAccessSettingsRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Mapping[str, str],
        "clientToken": str,
        "customerManagedKey": str,
        "description": str,
        "displayName": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateIpAccessSettingsRequestRequestTypeDef(
    _RequiredCreateIpAccessSettingsRequestRequestTypeDef,
    _OptionalCreateIpAccessSettingsRequestRequestTypeDef,
):
    pass


_RequiredIpAccessSettingsTypeDef = TypedDict(
    "_RequiredIpAccessSettingsTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
_OptionalIpAccessSettingsTypeDef = TypedDict(
    "_OptionalIpAccessSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "creationDate": datetime,
        "description": str,
        "displayName": str,
        "ipRules": List[IpRuleTypeDef],
    },
    total=False,
)


class IpAccessSettingsTypeDef(_RequiredIpAccessSettingsTypeDef, _OptionalIpAccessSettingsTypeDef):
    pass


_RequiredUpdateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
_OptionalUpdateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIpAccessSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "displayName": str,
        "ipRules": Sequence[IpRuleTypeDef],
    },
    total=False,
)


class UpdateIpAccessSettingsRequestRequestTypeDef(
    _RequiredUpdateIpAccessSettingsRequestRequestTypeDef,
    _OptionalUpdateIpAccessSettingsRequestRequestTypeDef,
):
    pass


GetIdentityProviderResponseTypeDef = TypedDict(
    "GetIdentityProviderResponseTypeDef",
    {
        "identityProvider": IdentityProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "identityProvider": IdentityProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetNetworkSettingsResponseTypeDef = TypedDict(
    "GetNetworkSettingsResponseTypeDef",
    {
        "networkSettings": NetworkSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateNetworkSettingsResponseTypeDef = TypedDict(
    "UpdateNetworkSettingsResponseTypeDef",
    {
        "networkSettings": NetworkSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPortalResponseTypeDef = TypedDict(
    "GetPortalResponseTypeDef",
    {
        "portal": PortalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portal": PortalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetTrustStoreResponseTypeDef = TypedDict(
    "GetTrustStoreResponseTypeDef",
    {
        "trustStore": TrustStoreTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "GetUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettings": UserAccessLoggingSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettings": UserAccessLoggingSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "userSettings": UserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateUserSettingsResponseTypeDef = TypedDict(
    "UpdateUserSettingsResponseTypeDef",
    {
        "userSettings": UserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "identityProviders": List[IdentityProviderSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIpAccessSettingsResponseTypeDef = TypedDict(
    "ListIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": List[IpAccessSettingsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNetworkSettingsResponseTypeDef = TypedDict(
    "ListNetworkSettingsResponseTypeDef",
    {
        "networkSettings": List[NetworkSettingsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "nextToken": str,
        "portals": List[PortalSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTrustStoresResponseTypeDef = TypedDict(
    "ListTrustStoresResponseTypeDef",
    {
        "nextToken": str,
        "trustStores": List[TrustStoreSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "ListUserAccessLoggingSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userAccessLoggingSettings": List[UserAccessLoggingSettingsSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUserSettingsResponseTypeDef = TypedDict(
    "ListUserSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userSettings": List[UserSettingsSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetIpAccessSettingsResponseTypeDef = TypedDict(
    "GetIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": IpAccessSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateIpAccessSettingsResponseTypeDef = TypedDict(
    "UpdateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": IpAccessSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
