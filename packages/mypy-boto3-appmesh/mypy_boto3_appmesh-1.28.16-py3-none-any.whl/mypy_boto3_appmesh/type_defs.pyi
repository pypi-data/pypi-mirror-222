"""
Type annotations for appmesh service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs/)

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AwsCloudMapInstanceAttributeTypeDef

    data: AwsCloudMapInstanceAttributeTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    DefaultGatewayRouteRewriteType,
    DnsResponseTypeType,
    DurationUnitType,
    EgressFilterTypeType,
    GatewayRouteStatusCodeType,
    GrpcRetryPolicyEventType,
    HttpMethodType,
    HttpSchemeType,
    IpPreferenceType,
    ListenerTlsModeType,
    MeshStatusCodeType,
    PortProtocolType,
    RouteStatusCodeType,
    VirtualGatewayListenerTlsModeType,
    VirtualGatewayPortProtocolType,
    VirtualGatewayStatusCodeType,
    VirtualNodeStatusCodeType,
    VirtualRouterStatusCodeType,
    VirtualServiceStatusCodeType,
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
    "AwsCloudMapInstanceAttributeTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "TagRefTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteGatewayRouteInputRequestTypeDef",
    "DeleteMeshInputRequestTypeDef",
    "DeleteRouteInputRequestTypeDef",
    "DeleteVirtualGatewayInputRequestTypeDef",
    "DeleteVirtualNodeInputRequestTypeDef",
    "DeleteVirtualRouterInputRequestTypeDef",
    "DeleteVirtualServiceInputRequestTypeDef",
    "DescribeGatewayRouteInputRequestTypeDef",
    "DescribeMeshInputRequestTypeDef",
    "DescribeRouteInputRequestTypeDef",
    "DescribeVirtualGatewayInputRequestTypeDef",
    "DescribeVirtualNodeInputRequestTypeDef",
    "DescribeVirtualRouterInputRequestTypeDef",
    "DescribeVirtualServiceInputRequestTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "GatewayRouteStatusTypeDef",
    "ResourceMetadataTypeDef",
    "GatewayRouteHostnameMatchTypeDef",
    "GatewayRouteHostnameRewriteTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "MatchRangeTypeDef",
    "WeightedTargetTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpPathMatchTypeDef",
    "HttpGatewayRoutePathRewriteTypeDef",
    "HttpGatewayRoutePrefixRewriteTypeDef",
    "QueryParameterMatchTypeDef",
    "JsonFormatRefTypeDef",
    "PaginatorConfigTypeDef",
    "ListGatewayRoutesInputRequestTypeDef",
    "ListMeshesInputRequestTypeDef",
    "MeshRefTypeDef",
    "ListRoutesInputRequestTypeDef",
    "RouteRefTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListVirtualGatewaysInputRequestTypeDef",
    "VirtualGatewayRefTypeDef",
    "ListVirtualNodesInputRequestTypeDef",
    "VirtualNodeRefTypeDef",
    "ListVirtualRoutersInputRequestTypeDef",
    "VirtualRouterRefTypeDef",
    "ListVirtualServicesInputRequestTypeDef",
    "VirtualServiceRefTypeDef",
    "PortMappingTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "MeshStatusTypeDef",
    "MeshServiceDiscoveryTypeDef",
    "RouteStatusTypeDef",
    "SubjectAlternativeNameMatchersOutputTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "TcpRouteMatchTypeDef",
    "TlsValidationContextAcmTrustOutputTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "UntagResourceInputRequestTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualServiceStatusTypeDef",
    "AwsCloudMapServiceDiscoveryOutputTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "ClientTlsCertificateTypeDef",
    "TagResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "GrpcRetryPolicyOutputTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcTimeoutTypeDef",
    "HttpRetryPolicyOutputTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpTimeoutTypeDef",
    "OutlierDetectionTypeDef",
    "TcpTimeoutTypeDef",
    "GrpcGatewayRouteRewriteTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "GatewayRouteTargetTypeDef",
    "GrpcMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "HeaderMatchMethodTypeDef",
    "GrpcRouteActionOutputTypeDef",
    "GrpcRouteActionTypeDef",
    "HttpRouteActionOutputTypeDef",
    "HttpRouteActionTypeDef",
    "TcpRouteActionOutputTypeDef",
    "TcpRouteActionTypeDef",
    "HttpGatewayRouteRewriteTypeDef",
    "HttpQueryParameterTypeDef",
    "LoggingFormatOutputTypeDef",
    "LoggingFormatTypeDef",
    "ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef",
    "ListMeshesInputListMeshesPaginateTypeDef",
    "ListRoutesInputListRoutesPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef",
    "ListVirtualNodesInputListVirtualNodesPaginateTypeDef",
    "ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef",
    "ListVirtualServicesInputListVirtualServicesPaginateTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesOutputTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "VirtualRouterListenerTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "MeshSpecTypeDef",
    "SubjectAlternativeNamesOutputTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TlsValidationContextTrustOutputTypeDef",
    "TlsValidationContextTrustTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustOutputTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualServiceProviderTypeDef",
    "ServiceDiscoveryOutputTypeDef",
    "ServiceDiscoveryTypeDef",
    "ListenerTimeoutTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMetadataTypeDef",
    "GrpcRouteMetadataTypeDef",
    "HttpGatewayRouteHeaderTypeDef",
    "HttpRouteHeaderTypeDef",
    "TcpRouteOutputTypeDef",
    "TcpRouteTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "FileAccessLogOutputTypeDef",
    "VirtualGatewayFileAccessLogOutputTypeDef",
    "FileAccessLogTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualRouterSpecOutputTypeDef",
    "VirtualRouterSpecTypeDef",
    "CreateMeshInputRequestTypeDef",
    "MeshDataTypeDef",
    "UpdateMeshInputRequestTypeDef",
    "ListenerTlsValidationContextOutputTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "TlsValidationContextOutputTypeDef",
    "TlsValidationContextTypeDef",
    "VirtualGatewayListenerTlsValidationContextOutputTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "VirtualGatewayTlsValidationContextOutputTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "VirtualServiceSpecTypeDef",
    "GrpcGatewayRouteMatchOutputTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcRouteMatchOutputTypeDef",
    "GrpcRouteMatchTypeDef",
    "HttpGatewayRouteMatchOutputTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpRouteMatchOutputTypeDef",
    "HttpRouteMatchTypeDef",
    "AccessLogOutputTypeDef",
    "VirtualGatewayAccessLogOutputTypeDef",
    "AccessLogTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualRouterDataTypeDef",
    "CreateVirtualRouterInputRequestTypeDef",
    "UpdateVirtualRouterInputRequestTypeDef",
    "VirtualRouterSpecUnionTypeDef",
    "CreateMeshOutputTypeDef",
    "DeleteMeshOutputTypeDef",
    "DescribeMeshOutputTypeDef",
    "UpdateMeshOutputTypeDef",
    "ListenerTlsOutputTypeDef",
    "ListenerTlsTypeDef",
    "ClientPolicyTlsOutputTypeDef",
    "ClientPolicyTlsTypeDef",
    "VirtualGatewayListenerTlsOutputTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayClientPolicyTlsOutputTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "CreateVirtualServiceInputRequestTypeDef",
    "UpdateVirtualServiceInputRequestTypeDef",
    "VirtualServiceDataTypeDef",
    "GrpcGatewayRouteOutputTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcRouteOutputTypeDef",
    "GrpcRouteTypeDef",
    "HttpGatewayRouteOutputTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpRouteOutputTypeDef",
    "HttpRouteTypeDef",
    "LoggingOutputTypeDef",
    "VirtualGatewayLoggingOutputTypeDef",
    "LoggingTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "ListenerOutputTypeDef",
    "ListenerTypeDef",
    "ClientPolicyOutputTypeDef",
    "ClientPolicyTypeDef",
    "VirtualGatewayListenerOutputTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayClientPolicyOutputTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
    "GatewayRouteSpecOutputTypeDef",
    "GatewayRouteSpecTypeDef",
    "RouteSpecOutputTypeDef",
    "RouteSpecTypeDef",
    "BackendDefaultsOutputTypeDef",
    "VirtualServiceBackendOutputTypeDef",
    "BackendDefaultsTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualGatewayBackendDefaultsOutputTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "GatewayRouteDataTypeDef",
    "CreateGatewayRouteInputRequestTypeDef",
    "GatewayRouteSpecUnionTypeDef",
    "UpdateGatewayRouteInputRequestTypeDef",
    "RouteDataTypeDef",
    "CreateRouteInputRequestTypeDef",
    "RouteSpecUnionTypeDef",
    "UpdateRouteInputRequestTypeDef",
    "BackendOutputTypeDef",
    "BackendTypeDef",
    "VirtualGatewaySpecOutputTypeDef",
    "VirtualGatewaySpecTypeDef",
    "CreateGatewayRouteOutputTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "CreateRouteOutputTypeDef",
    "DeleteRouteOutputTypeDef",
    "DescribeRouteOutputTypeDef",
    "UpdateRouteOutputTypeDef",
    "VirtualNodeSpecOutputTypeDef",
    "VirtualNodeSpecTypeDef",
    "VirtualGatewayDataTypeDef",
    "CreateVirtualGatewayInputRequestTypeDef",
    "UpdateVirtualGatewayInputRequestTypeDef",
    "VirtualGatewaySpecUnionTypeDef",
    "VirtualNodeDataTypeDef",
    "CreateVirtualNodeInputRequestTypeDef",
    "UpdateVirtualNodeInputRequestTypeDef",
    "VirtualNodeSpecUnionTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
)

AwsCloudMapInstanceAttributeTypeDef = TypedDict(
    "AwsCloudMapInstanceAttributeTypeDef",
    {
        "key": str,
        "value": str,
    },
)

ListenerTlsFileCertificateTypeDef = TypedDict(
    "ListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

ListenerTlsSdsCertificateTypeDef = TypedDict(
    "ListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

TagRefTypeDef = TypedDict(
    "TagRefTypeDef",
    {
        "key": str,
        "value": str,
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

_RequiredDeleteGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredDeleteGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDeleteGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalDeleteGatewayRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteGatewayRouteInputRequestTypeDef(
    _RequiredDeleteGatewayRouteInputRequestTypeDef, _OptionalDeleteGatewayRouteInputRequestTypeDef
):
    pass

DeleteMeshInputRequestTypeDef = TypedDict(
    "DeleteMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)

_RequiredDeleteRouteInputRequestTypeDef = TypedDict(
    "_RequiredDeleteRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
    },
)
_OptionalDeleteRouteInputRequestTypeDef = TypedDict(
    "_OptionalDeleteRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteRouteInputRequestTypeDef(
    _RequiredDeleteRouteInputRequestTypeDef, _OptionalDeleteRouteInputRequestTypeDef
):
    pass

_RequiredDeleteVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDeleteVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualGatewayInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualGatewayInputRequestTypeDef(
    _RequiredDeleteVirtualGatewayInputRequestTypeDef,
    _OptionalDeleteVirtualGatewayInputRequestTypeDef,
):
    pass

_RequiredDeleteVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
    },
)
_OptionalDeleteVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualNodeInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualNodeInputRequestTypeDef(
    _RequiredDeleteVirtualNodeInputRequestTypeDef, _OptionalDeleteVirtualNodeInputRequestTypeDef
):
    pass

_RequiredDeleteVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalDeleteVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualRouterInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualRouterInputRequestTypeDef(
    _RequiredDeleteVirtualRouterInputRequestTypeDef, _OptionalDeleteVirtualRouterInputRequestTypeDef
):
    pass

_RequiredDeleteVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
    },
)
_OptionalDeleteVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualServiceInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualServiceInputRequestTypeDef(
    _RequiredDeleteVirtualServiceInputRequestTypeDef,
    _OptionalDeleteVirtualServiceInputRequestTypeDef,
):
    pass

_RequiredDescribeGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredDescribeGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDescribeGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalDescribeGatewayRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeGatewayRouteInputRequestTypeDef(
    _RequiredDescribeGatewayRouteInputRequestTypeDef,
    _OptionalDescribeGatewayRouteInputRequestTypeDef,
):
    pass

_RequiredDescribeMeshInputRequestTypeDef = TypedDict(
    "_RequiredDescribeMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalDescribeMeshInputRequestTypeDef = TypedDict(
    "_OptionalDescribeMeshInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeMeshInputRequestTypeDef(
    _RequiredDescribeMeshInputRequestTypeDef, _OptionalDescribeMeshInputRequestTypeDef
):
    pass

_RequiredDescribeRouteInputRequestTypeDef = TypedDict(
    "_RequiredDescribeRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
    },
)
_OptionalDescribeRouteInputRequestTypeDef = TypedDict(
    "_OptionalDescribeRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeRouteInputRequestTypeDef(
    _RequiredDescribeRouteInputRequestTypeDef, _OptionalDescribeRouteInputRequestTypeDef
):
    pass

_RequiredDescribeVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDescribeVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualGatewayInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualGatewayInputRequestTypeDef(
    _RequiredDescribeVirtualGatewayInputRequestTypeDef,
    _OptionalDescribeVirtualGatewayInputRequestTypeDef,
):
    pass

_RequiredDescribeVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
    },
)
_OptionalDescribeVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualNodeInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualNodeInputRequestTypeDef(
    _RequiredDescribeVirtualNodeInputRequestTypeDef, _OptionalDescribeVirtualNodeInputRequestTypeDef
):
    pass

_RequiredDescribeVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalDescribeVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualRouterInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualRouterInputRequestTypeDef(
    _RequiredDescribeVirtualRouterInputRequestTypeDef,
    _OptionalDescribeVirtualRouterInputRequestTypeDef,
):
    pass

_RequiredDescribeVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
    },
)
_OptionalDescribeVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualServiceInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualServiceInputRequestTypeDef(
    _RequiredDescribeVirtualServiceInputRequestTypeDef,
    _OptionalDescribeVirtualServiceInputRequestTypeDef,
):
    pass

_RequiredDnsServiceDiscoveryTypeDef = TypedDict(
    "_RequiredDnsServiceDiscoveryTypeDef",
    {
        "hostname": str,
    },
)
_OptionalDnsServiceDiscoveryTypeDef = TypedDict(
    "_OptionalDnsServiceDiscoveryTypeDef",
    {
        "ipPreference": IpPreferenceType,
        "responseType": DnsResponseTypeType,
    },
    total=False,
)

class DnsServiceDiscoveryTypeDef(
    _RequiredDnsServiceDiscoveryTypeDef, _OptionalDnsServiceDiscoveryTypeDef
):
    pass

DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "unit": DurationUnitType,
        "value": int,
    },
    total=False,
)

EgressFilterTypeDef = TypedDict(
    "EgressFilterTypeDef",
    {
        "type": EgressFilterTypeType,
    },
)

GatewayRouteStatusTypeDef = TypedDict(
    "GatewayRouteStatusTypeDef",
    {
        "status": GatewayRouteStatusCodeType,
    },
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshOwner": str,
        "resourceOwner": str,
        "uid": str,
        "version": int,
    },
)

GatewayRouteHostnameMatchTypeDef = TypedDict(
    "GatewayRouteHostnameMatchTypeDef",
    {
        "exact": str,
        "suffix": str,
    },
    total=False,
)

GatewayRouteHostnameRewriteTypeDef = TypedDict(
    "GatewayRouteHostnameRewriteTypeDef",
    {
        "defaultTargetHostname": DefaultGatewayRouteRewriteType,
    },
    total=False,
)

GatewayRouteRefTypeDef = TypedDict(
    "GatewayRouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "gatewayRouteName": str,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

GatewayRouteVirtualServiceTypeDef = TypedDict(
    "GatewayRouteVirtualServiceTypeDef",
    {
        "virtualServiceName": str,
    },
)

MatchRangeTypeDef = TypedDict(
    "MatchRangeTypeDef",
    {
        "end": int,
        "start": int,
    },
)

_RequiredWeightedTargetTypeDef = TypedDict(
    "_RequiredWeightedTargetTypeDef",
    {
        "virtualNode": str,
        "weight": int,
    },
)
_OptionalWeightedTargetTypeDef = TypedDict(
    "_OptionalWeightedTargetTypeDef",
    {
        "port": int,
    },
    total=False,
)

class WeightedTargetTypeDef(_RequiredWeightedTargetTypeDef, _OptionalWeightedTargetTypeDef):
    pass

_RequiredHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": PortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalHealthCheckPolicyTypeDef",
    {
        "path": str,
        "port": int,
    },
    total=False,
)

class HealthCheckPolicyTypeDef(
    _RequiredHealthCheckPolicyTypeDef, _OptionalHealthCheckPolicyTypeDef
):
    pass

HttpPathMatchTypeDef = TypedDict(
    "HttpPathMatchTypeDef",
    {
        "exact": str,
        "regex": str,
    },
    total=False,
)

HttpGatewayRoutePathRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePathRewriteTypeDef",
    {
        "exact": str,
    },
    total=False,
)

HttpGatewayRoutePrefixRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePrefixRewriteTypeDef",
    {
        "defaultPrefix": DefaultGatewayRouteRewriteType,
        "value": str,
    },
    total=False,
)

QueryParameterMatchTypeDef = TypedDict(
    "QueryParameterMatchTypeDef",
    {
        "exact": str,
    },
    total=False,
)

JsonFormatRefTypeDef = TypedDict(
    "JsonFormatRefTypeDef",
    {
        "key": str,
        "value": str,
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

_RequiredListGatewayRoutesInputRequestTypeDef = TypedDict(
    "_RequiredListGatewayRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalListGatewayRoutesInputRequestTypeDef = TypedDict(
    "_OptionalListGatewayRoutesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListGatewayRoutesInputRequestTypeDef(
    _RequiredListGatewayRoutesInputRequestTypeDef, _OptionalListGatewayRoutesInputRequestTypeDef
):
    pass

ListMeshesInputRequestTypeDef = TypedDict(
    "ListMeshesInputRequestTypeDef",
    {
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

MeshRefTypeDef = TypedDict(
    "MeshRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
    },
)

_RequiredListRoutesInputRequestTypeDef = TypedDict(
    "_RequiredListRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalListRoutesInputRequestTypeDef = TypedDict(
    "_OptionalListRoutesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListRoutesInputRequestTypeDef(
    _RequiredListRoutesInputRequestTypeDef, _OptionalListRoutesInputRequestTypeDef
):
    pass

RouteRefTypeDef = TypedDict(
    "RouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "routeName": str,
        "version": int,
        "virtualRouterName": str,
    },
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
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

_RequiredListVirtualGatewaysInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualGatewaysInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualGatewaysInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualGatewaysInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualGatewaysInputRequestTypeDef(
    _RequiredListVirtualGatewaysInputRequestTypeDef, _OptionalListVirtualGatewaysInputRequestTypeDef
):
    pass

VirtualGatewayRefTypeDef = TypedDict(
    "VirtualGatewayRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

_RequiredListVirtualNodesInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualNodesInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualNodesInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualNodesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualNodesInputRequestTypeDef(
    _RequiredListVirtualNodesInputRequestTypeDef, _OptionalListVirtualNodesInputRequestTypeDef
):
    pass

VirtualNodeRefTypeDef = TypedDict(
    "VirtualNodeRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualNodeName": str,
    },
)

_RequiredListVirtualRoutersInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualRoutersInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualRoutersInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualRoutersInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualRoutersInputRequestTypeDef(
    _RequiredListVirtualRoutersInputRequestTypeDef, _OptionalListVirtualRoutersInputRequestTypeDef
):
    pass

VirtualRouterRefTypeDef = TypedDict(
    "VirtualRouterRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualRouterName": str,
    },
)

_RequiredListVirtualServicesInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualServicesInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualServicesInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualServicesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualServicesInputRequestTypeDef(
    _RequiredListVirtualServicesInputRequestTypeDef, _OptionalListVirtualServicesInputRequestTypeDef
):
    pass

VirtualServiceRefTypeDef = TypedDict(
    "VirtualServiceRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualServiceName": str,
    },
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "port": int,
        "protocol": PortProtocolType,
    },
)

ListenerTlsAcmCertificateTypeDef = TypedDict(
    "ListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

TlsValidationContextFileTrustTypeDef = TypedDict(
    "TlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

TlsValidationContextSdsTrustTypeDef = TypedDict(
    "TlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

MeshStatusTypeDef = TypedDict(
    "MeshStatusTypeDef",
    {
        "status": MeshStatusCodeType,
    },
    total=False,
)

MeshServiceDiscoveryTypeDef = TypedDict(
    "MeshServiceDiscoveryTypeDef",
    {
        "ipPreference": IpPreferenceType,
    },
    total=False,
)

RouteStatusTypeDef = TypedDict(
    "RouteStatusTypeDef",
    {
        "status": RouteStatusCodeType,
    },
)

SubjectAlternativeNameMatchersOutputTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersOutputTypeDef",
    {
        "exact": List[str],
    },
)

SubjectAlternativeNameMatchersTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersTypeDef",
    {
        "exact": Sequence[str],
    },
)

TcpRouteMatchTypeDef = TypedDict(
    "TcpRouteMatchTypeDef",
    {
        "port": int,
    },
    total=False,
)

TlsValidationContextAcmTrustOutputTypeDef = TypedDict(
    "TlsValidationContextAcmTrustOutputTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)

TlsValidationContextAcmTrustTypeDef = TypedDict(
    "TlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": Sequence[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

VirtualGatewayListenerTlsFileCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

VirtualGatewayListenerTlsSdsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

VirtualGatewayGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualGatewayHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
_OptionalVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxPendingRequests": int,
    },
    total=False,
)

class VirtualGatewayHttpConnectionPoolTypeDef(
    _RequiredVirtualGatewayHttpConnectionPoolTypeDef,
    _OptionalVirtualGatewayHttpConnectionPoolTypeDef,
):
    pass

VirtualGatewayStatusTypeDef = TypedDict(
    "VirtualGatewayStatusTypeDef",
    {
        "status": VirtualGatewayStatusCodeType,
    },
)

_RequiredVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": VirtualGatewayPortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "path": str,
        "port": int,
    },
    total=False,
)

class VirtualGatewayHealthCheckPolicyTypeDef(
    _RequiredVirtualGatewayHealthCheckPolicyTypeDef, _OptionalVirtualGatewayHealthCheckPolicyTypeDef
):
    pass

VirtualGatewayPortMappingTypeDef = TypedDict(
    "VirtualGatewayPortMappingTypeDef",
    {
        "port": int,
        "protocol": VirtualGatewayPortProtocolType,
    },
)

VirtualGatewayListenerTlsAcmCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

VirtualGatewayTlsValidationContextFileTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

VirtualGatewayTlsValidationContextSdsTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)

VirtualGatewayTlsValidationContextAcmTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": Sequence[str],
    },
)

VirtualNodeGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualNodeGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualNodeHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
_OptionalVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxPendingRequests": int,
    },
    total=False,
)

class VirtualNodeHttpConnectionPoolTypeDef(
    _RequiredVirtualNodeHttpConnectionPoolTypeDef, _OptionalVirtualNodeHttpConnectionPoolTypeDef
):
    pass

VirtualNodeTcpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeTcpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)

VirtualNodeStatusTypeDef = TypedDict(
    "VirtualNodeStatusTypeDef",
    {
        "status": VirtualNodeStatusCodeType,
    },
)

VirtualNodeServiceProviderTypeDef = TypedDict(
    "VirtualNodeServiceProviderTypeDef",
    {
        "virtualNodeName": str,
    },
)

VirtualRouterStatusTypeDef = TypedDict(
    "VirtualRouterStatusTypeDef",
    {
        "status": VirtualRouterStatusCodeType,
    },
)

VirtualRouterServiceProviderTypeDef = TypedDict(
    "VirtualRouterServiceProviderTypeDef",
    {
        "virtualRouterName": str,
    },
)

VirtualServiceStatusTypeDef = TypedDict(
    "VirtualServiceStatusTypeDef",
    {
        "status": VirtualServiceStatusCodeType,
    },
)

_RequiredAwsCloudMapServiceDiscoveryOutputTypeDef = TypedDict(
    "_RequiredAwsCloudMapServiceDiscoveryOutputTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
    },
)
_OptionalAwsCloudMapServiceDiscoveryOutputTypeDef = TypedDict(
    "_OptionalAwsCloudMapServiceDiscoveryOutputTypeDef",
    {
        "attributes": List[AwsCloudMapInstanceAttributeTypeDef],
        "ipPreference": IpPreferenceType,
    },
    total=False,
)

class AwsCloudMapServiceDiscoveryOutputTypeDef(
    _RequiredAwsCloudMapServiceDiscoveryOutputTypeDef,
    _OptionalAwsCloudMapServiceDiscoveryOutputTypeDef,
):
    pass

_RequiredAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_RequiredAwsCloudMapServiceDiscoveryTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
    },
)
_OptionalAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_OptionalAwsCloudMapServiceDiscoveryTypeDef",
    {
        "attributes": Sequence[AwsCloudMapInstanceAttributeTypeDef],
        "ipPreference": IpPreferenceType,
    },
    total=False,
)

class AwsCloudMapServiceDiscoveryTypeDef(
    _RequiredAwsCloudMapServiceDiscoveryTypeDef, _OptionalAwsCloudMapServiceDiscoveryTypeDef
):
    pass

ClientTlsCertificateTypeDef = TypedDict(
    "ClientTlsCertificateTypeDef",
    {
        "file": ListenerTlsFileCertificateTypeDef,
        "sds": ListenerTlsSdsCertificateTypeDef,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagRefTypeDef],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List[TagRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGrpcRetryPolicyOutputTypeDef = TypedDict(
    "_RequiredGrpcRetryPolicyOutputTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
    },
)
_OptionalGrpcRetryPolicyOutputTypeDef = TypedDict(
    "_OptionalGrpcRetryPolicyOutputTypeDef",
    {
        "grpcRetryEvents": List[GrpcRetryPolicyEventType],
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)

class GrpcRetryPolicyOutputTypeDef(
    _RequiredGrpcRetryPolicyOutputTypeDef, _OptionalGrpcRetryPolicyOutputTypeDef
):
    pass

_RequiredGrpcRetryPolicyTypeDef = TypedDict(
    "_RequiredGrpcRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
    },
)
_OptionalGrpcRetryPolicyTypeDef = TypedDict(
    "_OptionalGrpcRetryPolicyTypeDef",
    {
        "grpcRetryEvents": Sequence[GrpcRetryPolicyEventType],
        "httpRetryEvents": Sequence[str],
        "tcpRetryEvents": Sequence[Literal["connection-error"]],
    },
    total=False,
)

class GrpcRetryPolicyTypeDef(_RequiredGrpcRetryPolicyTypeDef, _OptionalGrpcRetryPolicyTypeDef):
    pass

GrpcTimeoutTypeDef = TypedDict(
    "GrpcTimeoutTypeDef",
    {
        "idle": DurationTypeDef,
        "perRequest": DurationTypeDef,
    },
    total=False,
)

_RequiredHttpRetryPolicyOutputTypeDef = TypedDict(
    "_RequiredHttpRetryPolicyOutputTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
    },
)
_OptionalHttpRetryPolicyOutputTypeDef = TypedDict(
    "_OptionalHttpRetryPolicyOutputTypeDef",
    {
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)

class HttpRetryPolicyOutputTypeDef(
    _RequiredHttpRetryPolicyOutputTypeDef, _OptionalHttpRetryPolicyOutputTypeDef
):
    pass

_RequiredHttpRetryPolicyTypeDef = TypedDict(
    "_RequiredHttpRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": DurationTypeDef,
    },
)
_OptionalHttpRetryPolicyTypeDef = TypedDict(
    "_OptionalHttpRetryPolicyTypeDef",
    {
        "httpRetryEvents": Sequence[str],
        "tcpRetryEvents": Sequence[Literal["connection-error"]],
    },
    total=False,
)

class HttpRetryPolicyTypeDef(_RequiredHttpRetryPolicyTypeDef, _OptionalHttpRetryPolicyTypeDef):
    pass

HttpTimeoutTypeDef = TypedDict(
    "HttpTimeoutTypeDef",
    {
        "idle": DurationTypeDef,
        "perRequest": DurationTypeDef,
    },
    total=False,
)

OutlierDetectionTypeDef = TypedDict(
    "OutlierDetectionTypeDef",
    {
        "baseEjectionDuration": DurationTypeDef,
        "interval": DurationTypeDef,
        "maxEjectionPercent": int,
        "maxServerErrors": int,
    },
)

TcpTimeoutTypeDef = TypedDict(
    "TcpTimeoutTypeDef",
    {
        "idle": DurationTypeDef,
    },
    total=False,
)

GrpcGatewayRouteRewriteTypeDef = TypedDict(
    "GrpcGatewayRouteRewriteTypeDef",
    {
        "hostname": GatewayRouteHostnameRewriteTypeDef,
    },
    total=False,
)

ListGatewayRoutesOutputTypeDef = TypedDict(
    "ListGatewayRoutesOutputTypeDef",
    {
        "gatewayRoutes": List[GatewayRouteRefTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGatewayRouteTargetTypeDef = TypedDict(
    "_RequiredGatewayRouteTargetTypeDef",
    {
        "virtualService": GatewayRouteVirtualServiceTypeDef,
    },
)
_OptionalGatewayRouteTargetTypeDef = TypedDict(
    "_OptionalGatewayRouteTargetTypeDef",
    {
        "port": int,
    },
    total=False,
)

class GatewayRouteTargetTypeDef(
    _RequiredGatewayRouteTargetTypeDef, _OptionalGatewayRouteTargetTypeDef
):
    pass

GrpcMetadataMatchMethodTypeDef = TypedDict(
    "GrpcMetadataMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": MatchRangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": MatchRangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": MatchRangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

GrpcRouteActionOutputTypeDef = TypedDict(
    "GrpcRouteActionOutputTypeDef",
    {
        "weightedTargets": List[WeightedTargetTypeDef],
    },
)

GrpcRouteActionTypeDef = TypedDict(
    "GrpcRouteActionTypeDef",
    {
        "weightedTargets": Sequence[WeightedTargetTypeDef],
    },
)

HttpRouteActionOutputTypeDef = TypedDict(
    "HttpRouteActionOutputTypeDef",
    {
        "weightedTargets": List[WeightedTargetTypeDef],
    },
)

HttpRouteActionTypeDef = TypedDict(
    "HttpRouteActionTypeDef",
    {
        "weightedTargets": Sequence[WeightedTargetTypeDef],
    },
)

TcpRouteActionOutputTypeDef = TypedDict(
    "TcpRouteActionOutputTypeDef",
    {
        "weightedTargets": List[WeightedTargetTypeDef],
    },
)

TcpRouteActionTypeDef = TypedDict(
    "TcpRouteActionTypeDef",
    {
        "weightedTargets": Sequence[WeightedTargetTypeDef],
    },
)

HttpGatewayRouteRewriteTypeDef = TypedDict(
    "HttpGatewayRouteRewriteTypeDef",
    {
        "hostname": GatewayRouteHostnameRewriteTypeDef,
        "path": HttpGatewayRoutePathRewriteTypeDef,
        "prefix": HttpGatewayRoutePrefixRewriteTypeDef,
    },
    total=False,
)

_RequiredHttpQueryParameterTypeDef = TypedDict(
    "_RequiredHttpQueryParameterTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpQueryParameterTypeDef = TypedDict(
    "_OptionalHttpQueryParameterTypeDef",
    {
        "match": QueryParameterMatchTypeDef,
    },
    total=False,
)

class HttpQueryParameterTypeDef(
    _RequiredHttpQueryParameterTypeDef, _OptionalHttpQueryParameterTypeDef
):
    pass

LoggingFormatOutputTypeDef = TypedDict(
    "LoggingFormatOutputTypeDef",
    {
        "json": List[JsonFormatRefTypeDef],
        "text": str,
    },
    total=False,
)

LoggingFormatTypeDef = TypedDict(
    "LoggingFormatTypeDef",
    {
        "json": Sequence[JsonFormatRefTypeDef],
        "text": str,
    },
    total=False,
)

_RequiredListGatewayRoutesInputListGatewayRoutesPaginateTypeDef = TypedDict(
    "_RequiredListGatewayRoutesInputListGatewayRoutesPaginateTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalListGatewayRoutesInputListGatewayRoutesPaginateTypeDef = TypedDict(
    "_OptionalListGatewayRoutesInputListGatewayRoutesPaginateTypeDef",
    {
        "meshOwner": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef(
    _RequiredListGatewayRoutesInputListGatewayRoutesPaginateTypeDef,
    _OptionalListGatewayRoutesInputListGatewayRoutesPaginateTypeDef,
):
    pass

ListMeshesInputListMeshesPaginateTypeDef = TypedDict(
    "ListMeshesInputListMeshesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListRoutesInputListRoutesPaginateTypeDef = TypedDict(
    "_RequiredListRoutesInputListRoutesPaginateTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalListRoutesInputListRoutesPaginateTypeDef = TypedDict(
    "_OptionalListRoutesInputListRoutesPaginateTypeDef",
    {
        "meshOwner": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListRoutesInputListRoutesPaginateTypeDef(
    _RequiredListRoutesInputListRoutesPaginateTypeDef,
    _OptionalListRoutesInputListRoutesPaginateTypeDef,
):
    pass

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

_RequiredListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef = TypedDict(
    "_RequiredListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef = TypedDict(
    "_OptionalListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef",
    {
        "meshOwner": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef(
    _RequiredListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef,
    _OptionalListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef,
):
    pass

_RequiredListVirtualNodesInputListVirtualNodesPaginateTypeDef = TypedDict(
    "_RequiredListVirtualNodesInputListVirtualNodesPaginateTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualNodesInputListVirtualNodesPaginateTypeDef = TypedDict(
    "_OptionalListVirtualNodesInputListVirtualNodesPaginateTypeDef",
    {
        "meshOwner": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListVirtualNodesInputListVirtualNodesPaginateTypeDef(
    _RequiredListVirtualNodesInputListVirtualNodesPaginateTypeDef,
    _OptionalListVirtualNodesInputListVirtualNodesPaginateTypeDef,
):
    pass

_RequiredListVirtualRoutersInputListVirtualRoutersPaginateTypeDef = TypedDict(
    "_RequiredListVirtualRoutersInputListVirtualRoutersPaginateTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualRoutersInputListVirtualRoutersPaginateTypeDef = TypedDict(
    "_OptionalListVirtualRoutersInputListVirtualRoutersPaginateTypeDef",
    {
        "meshOwner": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef(
    _RequiredListVirtualRoutersInputListVirtualRoutersPaginateTypeDef,
    _OptionalListVirtualRoutersInputListVirtualRoutersPaginateTypeDef,
):
    pass

_RequiredListVirtualServicesInputListVirtualServicesPaginateTypeDef = TypedDict(
    "_RequiredListVirtualServicesInputListVirtualServicesPaginateTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualServicesInputListVirtualServicesPaginateTypeDef = TypedDict(
    "_OptionalListVirtualServicesInputListVirtualServicesPaginateTypeDef",
    {
        "meshOwner": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListVirtualServicesInputListVirtualServicesPaginateTypeDef(
    _RequiredListVirtualServicesInputListVirtualServicesPaginateTypeDef,
    _OptionalListVirtualServicesInputListVirtualServicesPaginateTypeDef,
):
    pass

ListMeshesOutputTypeDef = TypedDict(
    "ListMeshesOutputTypeDef",
    {
        "meshes": List[MeshRefTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRoutesOutputTypeDef = TypedDict(
    "ListRoutesOutputTypeDef",
    {
        "nextToken": str,
        "routes": List[RouteRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVirtualGatewaysOutputTypeDef = TypedDict(
    "ListVirtualGatewaysOutputTypeDef",
    {
        "nextToken": str,
        "virtualGateways": List[VirtualGatewayRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVirtualNodesOutputTypeDef = TypedDict(
    "ListVirtualNodesOutputTypeDef",
    {
        "nextToken": str,
        "virtualNodes": List[VirtualNodeRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVirtualRoutersOutputTypeDef = TypedDict(
    "ListVirtualRoutersOutputTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List[VirtualRouterRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVirtualServicesOutputTypeDef = TypedDict(
    "ListVirtualServicesOutputTypeDef",
    {
        "nextToken": str,
        "virtualServices": List[VirtualServiceRefTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

VirtualRouterListenerTypeDef = TypedDict(
    "VirtualRouterListenerTypeDef",
    {
        "portMapping": PortMappingTypeDef,
    },
)

ListenerTlsCertificateTypeDef = TypedDict(
    "ListenerTlsCertificateTypeDef",
    {
        "acm": ListenerTlsAcmCertificateTypeDef,
        "file": ListenerTlsFileCertificateTypeDef,
        "sds": ListenerTlsSdsCertificateTypeDef,
    },
    total=False,
)

ListenerTlsValidationContextTrustTypeDef = TypedDict(
    "ListenerTlsValidationContextTrustTypeDef",
    {
        "file": TlsValidationContextFileTrustTypeDef,
        "sds": TlsValidationContextSdsTrustTypeDef,
    },
    total=False,
)

MeshSpecTypeDef = TypedDict(
    "MeshSpecTypeDef",
    {
        "egressFilter": EgressFilterTypeDef,
        "serviceDiscovery": MeshServiceDiscoveryTypeDef,
    },
    total=False,
)

SubjectAlternativeNamesOutputTypeDef = TypedDict(
    "SubjectAlternativeNamesOutputTypeDef",
    {
        "match": SubjectAlternativeNameMatchersOutputTypeDef,
    },
)

SubjectAlternativeNamesTypeDef = TypedDict(
    "SubjectAlternativeNamesTypeDef",
    {
        "match": SubjectAlternativeNameMatchersTypeDef,
    },
)

TlsValidationContextTrustOutputTypeDef = TypedDict(
    "TlsValidationContextTrustOutputTypeDef",
    {
        "acm": TlsValidationContextAcmTrustOutputTypeDef,
        "file": TlsValidationContextFileTrustTypeDef,
        "sds": TlsValidationContextSdsTrustTypeDef,
    },
    total=False,
)

TlsValidationContextTrustTypeDef = TypedDict(
    "TlsValidationContextTrustTypeDef",
    {
        "acm": TlsValidationContextAcmTrustTypeDef,
        "file": TlsValidationContextFileTrustTypeDef,
        "sds": TlsValidationContextSdsTrustTypeDef,
    },
    total=False,
)

VirtualGatewayClientTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayClientTlsCertificateTypeDef",
    {
        "file": VirtualGatewayListenerTlsFileCertificateTypeDef,
        "sds": VirtualGatewayListenerTlsSdsCertificateTypeDef,
    },
    total=False,
)

VirtualGatewayConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayConnectionPoolTypeDef",
    {
        "grpc": VirtualGatewayGrpcConnectionPoolTypeDef,
        "http": VirtualGatewayHttpConnectionPoolTypeDef,
        "http2": VirtualGatewayHttp2ConnectionPoolTypeDef,
    },
    total=False,
)

VirtualGatewayListenerTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsCertificateTypeDef",
    {
        "acm": VirtualGatewayListenerTlsAcmCertificateTypeDef,
        "file": VirtualGatewayListenerTlsFileCertificateTypeDef,
        "sds": VirtualGatewayListenerTlsSdsCertificateTypeDef,
    },
    total=False,
)

VirtualGatewayListenerTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    {
        "file": VirtualGatewayTlsValidationContextFileTrustTypeDef,
        "sds": VirtualGatewayTlsValidationContextSdsTrustTypeDef,
    },
    total=False,
)

VirtualGatewayTlsValidationContextTrustOutputTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustOutputTypeDef",
    {
        "acm": VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef,
        "file": VirtualGatewayTlsValidationContextFileTrustTypeDef,
        "sds": VirtualGatewayTlsValidationContextSdsTrustTypeDef,
    },
    total=False,
)

VirtualGatewayTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    {
        "acm": VirtualGatewayTlsValidationContextAcmTrustTypeDef,
        "file": VirtualGatewayTlsValidationContextFileTrustTypeDef,
        "sds": VirtualGatewayTlsValidationContextSdsTrustTypeDef,
    },
    total=False,
)

VirtualNodeConnectionPoolTypeDef = TypedDict(
    "VirtualNodeConnectionPoolTypeDef",
    {
        "grpc": VirtualNodeGrpcConnectionPoolTypeDef,
        "http": VirtualNodeHttpConnectionPoolTypeDef,
        "http2": VirtualNodeHttp2ConnectionPoolTypeDef,
        "tcp": VirtualNodeTcpConnectionPoolTypeDef,
    },
    total=False,
)

VirtualServiceProviderTypeDef = TypedDict(
    "VirtualServiceProviderTypeDef",
    {
        "virtualNode": VirtualNodeServiceProviderTypeDef,
        "virtualRouter": VirtualRouterServiceProviderTypeDef,
    },
    total=False,
)

ServiceDiscoveryOutputTypeDef = TypedDict(
    "ServiceDiscoveryOutputTypeDef",
    {
        "awsCloudMap": AwsCloudMapServiceDiscoveryOutputTypeDef,
        "dns": DnsServiceDiscoveryTypeDef,
    },
    total=False,
)

ServiceDiscoveryTypeDef = TypedDict(
    "ServiceDiscoveryTypeDef",
    {
        "awsCloudMap": AwsCloudMapServiceDiscoveryTypeDef,
        "dns": DnsServiceDiscoveryTypeDef,
    },
    total=False,
)

ListenerTimeoutTypeDef = TypedDict(
    "ListenerTimeoutTypeDef",
    {
        "grpc": GrpcTimeoutTypeDef,
        "http": HttpTimeoutTypeDef,
        "http2": HttpTimeoutTypeDef,
        "tcp": TcpTimeoutTypeDef,
    },
    total=False,
)

_RequiredGrpcGatewayRouteActionTypeDef = TypedDict(
    "_RequiredGrpcGatewayRouteActionTypeDef",
    {
        "target": GatewayRouteTargetTypeDef,
    },
)
_OptionalGrpcGatewayRouteActionTypeDef = TypedDict(
    "_OptionalGrpcGatewayRouteActionTypeDef",
    {
        "rewrite": GrpcGatewayRouteRewriteTypeDef,
    },
    total=False,
)

class GrpcGatewayRouteActionTypeDef(
    _RequiredGrpcGatewayRouteActionTypeDef, _OptionalGrpcGatewayRouteActionTypeDef
):
    pass

_RequiredGrpcGatewayRouteMetadataTypeDef = TypedDict(
    "_RequiredGrpcGatewayRouteMetadataTypeDef",
    {
        "name": str,
    },
)
_OptionalGrpcGatewayRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcGatewayRouteMetadataTypeDef",
    {
        "invert": bool,
        "match": GrpcMetadataMatchMethodTypeDef,
    },
    total=False,
)

class GrpcGatewayRouteMetadataTypeDef(
    _RequiredGrpcGatewayRouteMetadataTypeDef, _OptionalGrpcGatewayRouteMetadataTypeDef
):
    pass

_RequiredGrpcRouteMetadataTypeDef = TypedDict(
    "_RequiredGrpcRouteMetadataTypeDef",
    {
        "name": str,
    },
)
_OptionalGrpcRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcRouteMetadataTypeDef",
    {
        "invert": bool,
        "match": GrpcRouteMetadataMatchMethodTypeDef,
    },
    total=False,
)

class GrpcRouteMetadataTypeDef(
    _RequiredGrpcRouteMetadataTypeDef, _OptionalGrpcRouteMetadataTypeDef
):
    pass

_RequiredHttpGatewayRouteHeaderTypeDef = TypedDict(
    "_RequiredHttpGatewayRouteHeaderTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpGatewayRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpGatewayRouteHeaderTypeDef",
    {
        "invert": bool,
        "match": HeaderMatchMethodTypeDef,
    },
    total=False,
)

class HttpGatewayRouteHeaderTypeDef(
    _RequiredHttpGatewayRouteHeaderTypeDef, _OptionalHttpGatewayRouteHeaderTypeDef
):
    pass

_RequiredHttpRouteHeaderTypeDef = TypedDict(
    "_RequiredHttpRouteHeaderTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpRouteHeaderTypeDef",
    {
        "invert": bool,
        "match": HeaderMatchMethodTypeDef,
    },
    total=False,
)

class HttpRouteHeaderTypeDef(_RequiredHttpRouteHeaderTypeDef, _OptionalHttpRouteHeaderTypeDef):
    pass

_RequiredTcpRouteOutputTypeDef = TypedDict(
    "_RequiredTcpRouteOutputTypeDef",
    {
        "action": TcpRouteActionOutputTypeDef,
    },
)
_OptionalTcpRouteOutputTypeDef = TypedDict(
    "_OptionalTcpRouteOutputTypeDef",
    {
        "match": TcpRouteMatchTypeDef,
        "timeout": TcpTimeoutTypeDef,
    },
    total=False,
)

class TcpRouteOutputTypeDef(_RequiredTcpRouteOutputTypeDef, _OptionalTcpRouteOutputTypeDef):
    pass

_RequiredTcpRouteTypeDef = TypedDict(
    "_RequiredTcpRouteTypeDef",
    {
        "action": TcpRouteActionTypeDef,
    },
)
_OptionalTcpRouteTypeDef = TypedDict(
    "_OptionalTcpRouteTypeDef",
    {
        "match": TcpRouteMatchTypeDef,
        "timeout": TcpTimeoutTypeDef,
    },
    total=False,
)

class TcpRouteTypeDef(_RequiredTcpRouteTypeDef, _OptionalTcpRouteTypeDef):
    pass

_RequiredHttpGatewayRouteActionTypeDef = TypedDict(
    "_RequiredHttpGatewayRouteActionTypeDef",
    {
        "target": GatewayRouteTargetTypeDef,
    },
)
_OptionalHttpGatewayRouteActionTypeDef = TypedDict(
    "_OptionalHttpGatewayRouteActionTypeDef",
    {
        "rewrite": HttpGatewayRouteRewriteTypeDef,
    },
    total=False,
)

class HttpGatewayRouteActionTypeDef(
    _RequiredHttpGatewayRouteActionTypeDef, _OptionalHttpGatewayRouteActionTypeDef
):
    pass

_RequiredFileAccessLogOutputTypeDef = TypedDict(
    "_RequiredFileAccessLogOutputTypeDef",
    {
        "path": str,
    },
)
_OptionalFileAccessLogOutputTypeDef = TypedDict(
    "_OptionalFileAccessLogOutputTypeDef",
    {
        "format": LoggingFormatOutputTypeDef,
    },
    total=False,
)

class FileAccessLogOutputTypeDef(
    _RequiredFileAccessLogOutputTypeDef, _OptionalFileAccessLogOutputTypeDef
):
    pass

_RequiredVirtualGatewayFileAccessLogOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewayFileAccessLogOutputTypeDef",
    {
        "path": str,
    },
)
_OptionalVirtualGatewayFileAccessLogOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewayFileAccessLogOutputTypeDef",
    {
        "format": LoggingFormatOutputTypeDef,
    },
    total=False,
)

class VirtualGatewayFileAccessLogOutputTypeDef(
    _RequiredVirtualGatewayFileAccessLogOutputTypeDef,
    _OptionalVirtualGatewayFileAccessLogOutputTypeDef,
):
    pass

_RequiredFileAccessLogTypeDef = TypedDict(
    "_RequiredFileAccessLogTypeDef",
    {
        "path": str,
    },
)
_OptionalFileAccessLogTypeDef = TypedDict(
    "_OptionalFileAccessLogTypeDef",
    {
        "format": LoggingFormatTypeDef,
    },
    total=False,
)

class FileAccessLogTypeDef(_RequiredFileAccessLogTypeDef, _OptionalFileAccessLogTypeDef):
    pass

_RequiredVirtualGatewayFileAccessLogTypeDef = TypedDict(
    "_RequiredVirtualGatewayFileAccessLogTypeDef",
    {
        "path": str,
    },
)
_OptionalVirtualGatewayFileAccessLogTypeDef = TypedDict(
    "_OptionalVirtualGatewayFileAccessLogTypeDef",
    {
        "format": LoggingFormatTypeDef,
    },
    total=False,
)

class VirtualGatewayFileAccessLogTypeDef(
    _RequiredVirtualGatewayFileAccessLogTypeDef, _OptionalVirtualGatewayFileAccessLogTypeDef
):
    pass

VirtualRouterSpecOutputTypeDef = TypedDict(
    "VirtualRouterSpecOutputTypeDef",
    {
        "listeners": List[VirtualRouterListenerTypeDef],
    },
    total=False,
)

VirtualRouterSpecTypeDef = TypedDict(
    "VirtualRouterSpecTypeDef",
    {
        "listeners": Sequence[VirtualRouterListenerTypeDef],
    },
    total=False,
)

_RequiredCreateMeshInputRequestTypeDef = TypedDict(
    "_RequiredCreateMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalCreateMeshInputRequestTypeDef = TypedDict(
    "_OptionalCreateMeshInputRequestTypeDef",
    {
        "clientToken": str,
        "spec": MeshSpecTypeDef,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateMeshInputRequestTypeDef(
    _RequiredCreateMeshInputRequestTypeDef, _OptionalCreateMeshInputRequestTypeDef
):
    pass

MeshDataTypeDef = TypedDict(
    "MeshDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": MeshSpecTypeDef,
        "status": MeshStatusTypeDef,
    },
)

_RequiredUpdateMeshInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalUpdateMeshInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMeshInputRequestTypeDef",
    {
        "clientToken": str,
        "spec": MeshSpecTypeDef,
    },
    total=False,
)

class UpdateMeshInputRequestTypeDef(
    _RequiredUpdateMeshInputRequestTypeDef, _OptionalUpdateMeshInputRequestTypeDef
):
    pass

_RequiredListenerTlsValidationContextOutputTypeDef = TypedDict(
    "_RequiredListenerTlsValidationContextOutputTypeDef",
    {
        "trust": ListenerTlsValidationContextTrustTypeDef,
    },
)
_OptionalListenerTlsValidationContextOutputTypeDef = TypedDict(
    "_OptionalListenerTlsValidationContextOutputTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesOutputTypeDef,
    },
    total=False,
)

class ListenerTlsValidationContextOutputTypeDef(
    _RequiredListenerTlsValidationContextOutputTypeDef,
    _OptionalListenerTlsValidationContextOutputTypeDef,
):
    pass

_RequiredListenerTlsValidationContextTypeDef = TypedDict(
    "_RequiredListenerTlsValidationContextTypeDef",
    {
        "trust": ListenerTlsValidationContextTrustTypeDef,
    },
)
_OptionalListenerTlsValidationContextTypeDef = TypedDict(
    "_OptionalListenerTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesTypeDef,
    },
    total=False,
)

class ListenerTlsValidationContextTypeDef(
    _RequiredListenerTlsValidationContextTypeDef, _OptionalListenerTlsValidationContextTypeDef
):
    pass

_RequiredTlsValidationContextOutputTypeDef = TypedDict(
    "_RequiredTlsValidationContextOutputTypeDef",
    {
        "trust": TlsValidationContextTrustOutputTypeDef,
    },
)
_OptionalTlsValidationContextOutputTypeDef = TypedDict(
    "_OptionalTlsValidationContextOutputTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesOutputTypeDef,
    },
    total=False,
)

class TlsValidationContextOutputTypeDef(
    _RequiredTlsValidationContextOutputTypeDef, _OptionalTlsValidationContextOutputTypeDef
):
    pass

_RequiredTlsValidationContextTypeDef = TypedDict(
    "_RequiredTlsValidationContextTypeDef",
    {
        "trust": TlsValidationContextTrustTypeDef,
    },
)
_OptionalTlsValidationContextTypeDef = TypedDict(
    "_OptionalTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesTypeDef,
    },
    total=False,
)

class TlsValidationContextTypeDef(
    _RequiredTlsValidationContextTypeDef, _OptionalTlsValidationContextTypeDef
):
    pass

_RequiredVirtualGatewayListenerTlsValidationContextOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsValidationContextOutputTypeDef",
    {
        "trust": VirtualGatewayListenerTlsValidationContextTrustTypeDef,
    },
)
_OptionalVirtualGatewayListenerTlsValidationContextOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsValidationContextOutputTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesOutputTypeDef,
    },
    total=False,
)

class VirtualGatewayListenerTlsValidationContextOutputTypeDef(
    _RequiredVirtualGatewayListenerTlsValidationContextOutputTypeDef,
    _OptionalVirtualGatewayListenerTlsValidationContextOutputTypeDef,
):
    pass

_RequiredVirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "trust": VirtualGatewayListenerTlsValidationContextTrustTypeDef,
    },
)
_OptionalVirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesTypeDef,
    },
    total=False,
)

class VirtualGatewayListenerTlsValidationContextTypeDef(
    _RequiredVirtualGatewayListenerTlsValidationContextTypeDef,
    _OptionalVirtualGatewayListenerTlsValidationContextTypeDef,
):
    pass

_RequiredVirtualGatewayTlsValidationContextOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewayTlsValidationContextOutputTypeDef",
    {
        "trust": VirtualGatewayTlsValidationContextTrustOutputTypeDef,
    },
)
_OptionalVirtualGatewayTlsValidationContextOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewayTlsValidationContextOutputTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesOutputTypeDef,
    },
    total=False,
)

class VirtualGatewayTlsValidationContextOutputTypeDef(
    _RequiredVirtualGatewayTlsValidationContextOutputTypeDef,
    _OptionalVirtualGatewayTlsValidationContextOutputTypeDef,
):
    pass

_RequiredVirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "_RequiredVirtualGatewayTlsValidationContextTypeDef",
    {
        "trust": VirtualGatewayTlsValidationContextTrustTypeDef,
    },
)
_OptionalVirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "_OptionalVirtualGatewayTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": SubjectAlternativeNamesTypeDef,
    },
    total=False,
)

class VirtualGatewayTlsValidationContextTypeDef(
    _RequiredVirtualGatewayTlsValidationContextTypeDef,
    _OptionalVirtualGatewayTlsValidationContextTypeDef,
):
    pass

VirtualServiceSpecTypeDef = TypedDict(
    "VirtualServiceSpecTypeDef",
    {
        "provider": VirtualServiceProviderTypeDef,
    },
    total=False,
)

GrpcGatewayRouteMatchOutputTypeDef = TypedDict(
    "GrpcGatewayRouteMatchOutputTypeDef",
    {
        "hostname": GatewayRouteHostnameMatchTypeDef,
        "metadata": List[GrpcGatewayRouteMetadataTypeDef],
        "port": int,
        "serviceName": str,
    },
    total=False,
)

GrpcGatewayRouteMatchTypeDef = TypedDict(
    "GrpcGatewayRouteMatchTypeDef",
    {
        "hostname": GatewayRouteHostnameMatchTypeDef,
        "metadata": Sequence[GrpcGatewayRouteMetadataTypeDef],
        "port": int,
        "serviceName": str,
    },
    total=False,
)

GrpcRouteMatchOutputTypeDef = TypedDict(
    "GrpcRouteMatchOutputTypeDef",
    {
        "metadata": List[GrpcRouteMetadataTypeDef],
        "methodName": str,
        "port": int,
        "serviceName": str,
    },
    total=False,
)

GrpcRouteMatchTypeDef = TypedDict(
    "GrpcRouteMatchTypeDef",
    {
        "metadata": Sequence[GrpcRouteMetadataTypeDef],
        "methodName": str,
        "port": int,
        "serviceName": str,
    },
    total=False,
)

HttpGatewayRouteMatchOutputTypeDef = TypedDict(
    "HttpGatewayRouteMatchOutputTypeDef",
    {
        "headers": List[HttpGatewayRouteHeaderTypeDef],
        "hostname": GatewayRouteHostnameMatchTypeDef,
        "method": HttpMethodType,
        "path": HttpPathMatchTypeDef,
        "port": int,
        "prefix": str,
        "queryParameters": List[HttpQueryParameterTypeDef],
    },
    total=False,
)

HttpGatewayRouteMatchTypeDef = TypedDict(
    "HttpGatewayRouteMatchTypeDef",
    {
        "headers": Sequence[HttpGatewayRouteHeaderTypeDef],
        "hostname": GatewayRouteHostnameMatchTypeDef,
        "method": HttpMethodType,
        "path": HttpPathMatchTypeDef,
        "port": int,
        "prefix": str,
        "queryParameters": Sequence[HttpQueryParameterTypeDef],
    },
    total=False,
)

HttpRouteMatchOutputTypeDef = TypedDict(
    "HttpRouteMatchOutputTypeDef",
    {
        "headers": List[HttpRouteHeaderTypeDef],
        "method": HttpMethodType,
        "path": HttpPathMatchTypeDef,
        "port": int,
        "prefix": str,
        "queryParameters": List[HttpQueryParameterTypeDef],
        "scheme": HttpSchemeType,
    },
    total=False,
)

HttpRouteMatchTypeDef = TypedDict(
    "HttpRouteMatchTypeDef",
    {
        "headers": Sequence[HttpRouteHeaderTypeDef],
        "method": HttpMethodType,
        "path": HttpPathMatchTypeDef,
        "port": int,
        "prefix": str,
        "queryParameters": Sequence[HttpQueryParameterTypeDef],
        "scheme": HttpSchemeType,
    },
    total=False,
)

AccessLogOutputTypeDef = TypedDict(
    "AccessLogOutputTypeDef",
    {
        "file": FileAccessLogOutputTypeDef,
    },
    total=False,
)

VirtualGatewayAccessLogOutputTypeDef = TypedDict(
    "VirtualGatewayAccessLogOutputTypeDef",
    {
        "file": VirtualGatewayFileAccessLogOutputTypeDef,
    },
    total=False,
)

AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "file": FileAccessLogTypeDef,
    },
    total=False,
)

VirtualGatewayAccessLogTypeDef = TypedDict(
    "VirtualGatewayAccessLogTypeDef",
    {
        "file": VirtualGatewayFileAccessLogTypeDef,
    },
    total=False,
)

VirtualRouterDataTypeDef = TypedDict(
    "VirtualRouterDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualRouterSpecOutputTypeDef,
        "status": VirtualRouterStatusTypeDef,
        "virtualRouterName": str,
    },
)

_RequiredCreateVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualRouterSpecTypeDef,
        "virtualRouterName": str,
    },
)
_OptionalCreateVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualRouterInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateVirtualRouterInputRequestTypeDef(
    _RequiredCreateVirtualRouterInputRequestTypeDef, _OptionalCreateVirtualRouterInputRequestTypeDef
):
    pass

_RequiredUpdateVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualRouterSpecTypeDef,
        "virtualRouterName": str,
    },
)
_OptionalUpdateVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualRouterInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualRouterInputRequestTypeDef(
    _RequiredUpdateVirtualRouterInputRequestTypeDef, _OptionalUpdateVirtualRouterInputRequestTypeDef
):
    pass

VirtualRouterSpecUnionTypeDef = Union[VirtualRouterSpecTypeDef, VirtualRouterSpecOutputTypeDef]
CreateMeshOutputTypeDef = TypedDict(
    "CreateMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteMeshOutputTypeDef = TypedDict(
    "DeleteMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeMeshOutputTypeDef = TypedDict(
    "DescribeMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateMeshOutputTypeDef = TypedDict(
    "UpdateMeshOutputTypeDef",
    {
        "mesh": MeshDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListenerTlsOutputTypeDef = TypedDict(
    "_RequiredListenerTlsOutputTypeDef",
    {
        "certificate": ListenerTlsCertificateTypeDef,
        "mode": ListenerTlsModeType,
    },
)
_OptionalListenerTlsOutputTypeDef = TypedDict(
    "_OptionalListenerTlsOutputTypeDef",
    {
        "validation": ListenerTlsValidationContextOutputTypeDef,
    },
    total=False,
)

class ListenerTlsOutputTypeDef(
    _RequiredListenerTlsOutputTypeDef, _OptionalListenerTlsOutputTypeDef
):
    pass

_RequiredListenerTlsTypeDef = TypedDict(
    "_RequiredListenerTlsTypeDef",
    {
        "certificate": ListenerTlsCertificateTypeDef,
        "mode": ListenerTlsModeType,
    },
)
_OptionalListenerTlsTypeDef = TypedDict(
    "_OptionalListenerTlsTypeDef",
    {
        "validation": ListenerTlsValidationContextTypeDef,
    },
    total=False,
)

class ListenerTlsTypeDef(_RequiredListenerTlsTypeDef, _OptionalListenerTlsTypeDef):
    pass

_RequiredClientPolicyTlsOutputTypeDef = TypedDict(
    "_RequiredClientPolicyTlsOutputTypeDef",
    {
        "validation": TlsValidationContextOutputTypeDef,
    },
)
_OptionalClientPolicyTlsOutputTypeDef = TypedDict(
    "_OptionalClientPolicyTlsOutputTypeDef",
    {
        "certificate": ClientTlsCertificateTypeDef,
        "enforce": bool,
        "ports": List[int],
    },
    total=False,
)

class ClientPolicyTlsOutputTypeDef(
    _RequiredClientPolicyTlsOutputTypeDef, _OptionalClientPolicyTlsOutputTypeDef
):
    pass

_RequiredClientPolicyTlsTypeDef = TypedDict(
    "_RequiredClientPolicyTlsTypeDef",
    {
        "validation": TlsValidationContextTypeDef,
    },
)
_OptionalClientPolicyTlsTypeDef = TypedDict(
    "_OptionalClientPolicyTlsTypeDef",
    {
        "certificate": ClientTlsCertificateTypeDef,
        "enforce": bool,
        "ports": Sequence[int],
    },
    total=False,
)

class ClientPolicyTlsTypeDef(_RequiredClientPolicyTlsTypeDef, _OptionalClientPolicyTlsTypeDef):
    pass

_RequiredVirtualGatewayListenerTlsOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsOutputTypeDef",
    {
        "certificate": VirtualGatewayListenerTlsCertificateTypeDef,
        "mode": VirtualGatewayListenerTlsModeType,
    },
)
_OptionalVirtualGatewayListenerTlsOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsOutputTypeDef",
    {
        "validation": VirtualGatewayListenerTlsValidationContextOutputTypeDef,
    },
    total=False,
)

class VirtualGatewayListenerTlsOutputTypeDef(
    _RequiredVirtualGatewayListenerTlsOutputTypeDef, _OptionalVirtualGatewayListenerTlsOutputTypeDef
):
    pass

_RequiredVirtualGatewayListenerTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsTypeDef",
    {
        "certificate": VirtualGatewayListenerTlsCertificateTypeDef,
        "mode": VirtualGatewayListenerTlsModeType,
    },
)
_OptionalVirtualGatewayListenerTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsTypeDef",
    {
        "validation": VirtualGatewayListenerTlsValidationContextTypeDef,
    },
    total=False,
)

class VirtualGatewayListenerTlsTypeDef(
    _RequiredVirtualGatewayListenerTlsTypeDef, _OptionalVirtualGatewayListenerTlsTypeDef
):
    pass

_RequiredVirtualGatewayClientPolicyTlsOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewayClientPolicyTlsOutputTypeDef",
    {
        "validation": VirtualGatewayTlsValidationContextOutputTypeDef,
    },
)
_OptionalVirtualGatewayClientPolicyTlsOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewayClientPolicyTlsOutputTypeDef",
    {
        "certificate": VirtualGatewayClientTlsCertificateTypeDef,
        "enforce": bool,
        "ports": List[int],
    },
    total=False,
)

class VirtualGatewayClientPolicyTlsOutputTypeDef(
    _RequiredVirtualGatewayClientPolicyTlsOutputTypeDef,
    _OptionalVirtualGatewayClientPolicyTlsOutputTypeDef,
):
    pass

_RequiredVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayClientPolicyTlsTypeDef",
    {
        "validation": VirtualGatewayTlsValidationContextTypeDef,
    },
)
_OptionalVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayClientPolicyTlsTypeDef",
    {
        "certificate": VirtualGatewayClientTlsCertificateTypeDef,
        "enforce": bool,
        "ports": Sequence[int],
    },
    total=False,
)

class VirtualGatewayClientPolicyTlsTypeDef(
    _RequiredVirtualGatewayClientPolicyTlsTypeDef, _OptionalVirtualGatewayClientPolicyTlsTypeDef
):
    pass

_RequiredCreateVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualServiceSpecTypeDef,
        "virtualServiceName": str,
    },
)
_OptionalCreateVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualServiceInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateVirtualServiceInputRequestTypeDef(
    _RequiredCreateVirtualServiceInputRequestTypeDef,
    _OptionalCreateVirtualServiceInputRequestTypeDef,
):
    pass

_RequiredUpdateVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualServiceSpecTypeDef,
        "virtualServiceName": str,
    },
)
_OptionalUpdateVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualServiceInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualServiceInputRequestTypeDef(
    _RequiredUpdateVirtualServiceInputRequestTypeDef,
    _OptionalUpdateVirtualServiceInputRequestTypeDef,
):
    pass

VirtualServiceDataTypeDef = TypedDict(
    "VirtualServiceDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualServiceSpecTypeDef,
        "status": VirtualServiceStatusTypeDef,
        "virtualServiceName": str,
    },
)

GrpcGatewayRouteOutputTypeDef = TypedDict(
    "GrpcGatewayRouteOutputTypeDef",
    {
        "action": GrpcGatewayRouteActionTypeDef,
        "match": GrpcGatewayRouteMatchOutputTypeDef,
    },
)

GrpcGatewayRouteTypeDef = TypedDict(
    "GrpcGatewayRouteTypeDef",
    {
        "action": GrpcGatewayRouteActionTypeDef,
        "match": GrpcGatewayRouteMatchTypeDef,
    },
)

_RequiredGrpcRouteOutputTypeDef = TypedDict(
    "_RequiredGrpcRouteOutputTypeDef",
    {
        "action": GrpcRouteActionOutputTypeDef,
        "match": GrpcRouteMatchOutputTypeDef,
    },
)
_OptionalGrpcRouteOutputTypeDef = TypedDict(
    "_OptionalGrpcRouteOutputTypeDef",
    {
        "retryPolicy": GrpcRetryPolicyOutputTypeDef,
        "timeout": GrpcTimeoutTypeDef,
    },
    total=False,
)

class GrpcRouteOutputTypeDef(_RequiredGrpcRouteOutputTypeDef, _OptionalGrpcRouteOutputTypeDef):
    pass

_RequiredGrpcRouteTypeDef = TypedDict(
    "_RequiredGrpcRouteTypeDef",
    {
        "action": GrpcRouteActionTypeDef,
        "match": GrpcRouteMatchTypeDef,
    },
)
_OptionalGrpcRouteTypeDef = TypedDict(
    "_OptionalGrpcRouteTypeDef",
    {
        "retryPolicy": GrpcRetryPolicyTypeDef,
        "timeout": GrpcTimeoutTypeDef,
    },
    total=False,
)

class GrpcRouteTypeDef(_RequiredGrpcRouteTypeDef, _OptionalGrpcRouteTypeDef):
    pass

HttpGatewayRouteOutputTypeDef = TypedDict(
    "HttpGatewayRouteOutputTypeDef",
    {
        "action": HttpGatewayRouteActionTypeDef,
        "match": HttpGatewayRouteMatchOutputTypeDef,
    },
)

HttpGatewayRouteTypeDef = TypedDict(
    "HttpGatewayRouteTypeDef",
    {
        "action": HttpGatewayRouteActionTypeDef,
        "match": HttpGatewayRouteMatchTypeDef,
    },
)

_RequiredHttpRouteOutputTypeDef = TypedDict(
    "_RequiredHttpRouteOutputTypeDef",
    {
        "action": HttpRouteActionOutputTypeDef,
        "match": HttpRouteMatchOutputTypeDef,
    },
)
_OptionalHttpRouteOutputTypeDef = TypedDict(
    "_OptionalHttpRouteOutputTypeDef",
    {
        "retryPolicy": HttpRetryPolicyOutputTypeDef,
        "timeout": HttpTimeoutTypeDef,
    },
    total=False,
)

class HttpRouteOutputTypeDef(_RequiredHttpRouteOutputTypeDef, _OptionalHttpRouteOutputTypeDef):
    pass

_RequiredHttpRouteTypeDef = TypedDict(
    "_RequiredHttpRouteTypeDef",
    {
        "action": HttpRouteActionTypeDef,
        "match": HttpRouteMatchTypeDef,
    },
)
_OptionalHttpRouteTypeDef = TypedDict(
    "_OptionalHttpRouteTypeDef",
    {
        "retryPolicy": HttpRetryPolicyTypeDef,
        "timeout": HttpTimeoutTypeDef,
    },
    total=False,
)

class HttpRouteTypeDef(_RequiredHttpRouteTypeDef, _OptionalHttpRouteTypeDef):
    pass

LoggingOutputTypeDef = TypedDict(
    "LoggingOutputTypeDef",
    {
        "accessLog": AccessLogOutputTypeDef,
    },
    total=False,
)

VirtualGatewayLoggingOutputTypeDef = TypedDict(
    "VirtualGatewayLoggingOutputTypeDef",
    {
        "accessLog": VirtualGatewayAccessLogOutputTypeDef,
    },
    total=False,
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "accessLog": AccessLogTypeDef,
    },
    total=False,
)

VirtualGatewayLoggingTypeDef = TypedDict(
    "VirtualGatewayLoggingTypeDef",
    {
        "accessLog": VirtualGatewayAccessLogTypeDef,
    },
    total=False,
)

CreateVirtualRouterOutputTypeDef = TypedDict(
    "CreateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVirtualRouterOutputTypeDef = TypedDict(
    "DeleteVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeVirtualRouterOutputTypeDef = TypedDict(
    "DescribeVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateVirtualRouterOutputTypeDef = TypedDict(
    "UpdateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": VirtualRouterDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListenerOutputTypeDef = TypedDict(
    "_RequiredListenerOutputTypeDef",
    {
        "portMapping": PortMappingTypeDef,
    },
)
_OptionalListenerOutputTypeDef = TypedDict(
    "_OptionalListenerOutputTypeDef",
    {
        "connectionPool": VirtualNodeConnectionPoolTypeDef,
        "healthCheck": HealthCheckPolicyTypeDef,
        "outlierDetection": OutlierDetectionTypeDef,
        "timeout": ListenerTimeoutTypeDef,
        "tls": ListenerTlsOutputTypeDef,
    },
    total=False,
)

class ListenerOutputTypeDef(_RequiredListenerOutputTypeDef, _OptionalListenerOutputTypeDef):
    pass

_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef",
    {
        "portMapping": PortMappingTypeDef,
    },
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef",
    {
        "connectionPool": VirtualNodeConnectionPoolTypeDef,
        "healthCheck": HealthCheckPolicyTypeDef,
        "outlierDetection": OutlierDetectionTypeDef,
        "timeout": ListenerTimeoutTypeDef,
        "tls": ListenerTlsTypeDef,
    },
    total=False,
)

class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass

ClientPolicyOutputTypeDef = TypedDict(
    "ClientPolicyOutputTypeDef",
    {
        "tls": ClientPolicyTlsOutputTypeDef,
    },
    total=False,
)

ClientPolicyTypeDef = TypedDict(
    "ClientPolicyTypeDef",
    {
        "tls": ClientPolicyTlsTypeDef,
    },
    total=False,
)

_RequiredVirtualGatewayListenerOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerOutputTypeDef",
    {
        "portMapping": VirtualGatewayPortMappingTypeDef,
    },
)
_OptionalVirtualGatewayListenerOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerOutputTypeDef",
    {
        "connectionPool": VirtualGatewayConnectionPoolTypeDef,
        "healthCheck": VirtualGatewayHealthCheckPolicyTypeDef,
        "tls": VirtualGatewayListenerTlsOutputTypeDef,
    },
    total=False,
)

class VirtualGatewayListenerOutputTypeDef(
    _RequiredVirtualGatewayListenerOutputTypeDef, _OptionalVirtualGatewayListenerOutputTypeDef
):
    pass

_RequiredVirtualGatewayListenerTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTypeDef",
    {
        "portMapping": VirtualGatewayPortMappingTypeDef,
    },
)
_OptionalVirtualGatewayListenerTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTypeDef",
    {
        "connectionPool": VirtualGatewayConnectionPoolTypeDef,
        "healthCheck": VirtualGatewayHealthCheckPolicyTypeDef,
        "tls": VirtualGatewayListenerTlsTypeDef,
    },
    total=False,
)

class VirtualGatewayListenerTypeDef(
    _RequiredVirtualGatewayListenerTypeDef, _OptionalVirtualGatewayListenerTypeDef
):
    pass

VirtualGatewayClientPolicyOutputTypeDef = TypedDict(
    "VirtualGatewayClientPolicyOutputTypeDef",
    {
        "tls": VirtualGatewayClientPolicyTlsOutputTypeDef,
    },
    total=False,
)

VirtualGatewayClientPolicyTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTypeDef",
    {
        "tls": VirtualGatewayClientPolicyTlsTypeDef,
    },
    total=False,
)

CreateVirtualServiceOutputTypeDef = TypedDict(
    "CreateVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVirtualServiceOutputTypeDef = TypedDict(
    "DeleteVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeVirtualServiceOutputTypeDef = TypedDict(
    "DescribeVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateVirtualServiceOutputTypeDef = TypedDict(
    "UpdateVirtualServiceOutputTypeDef",
    {
        "virtualService": VirtualServiceDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GatewayRouteSpecOutputTypeDef = TypedDict(
    "GatewayRouteSpecOutputTypeDef",
    {
        "grpcRoute": GrpcGatewayRouteOutputTypeDef,
        "http2Route": HttpGatewayRouteOutputTypeDef,
        "httpRoute": HttpGatewayRouteOutputTypeDef,
        "priority": int,
    },
    total=False,
)

GatewayRouteSpecTypeDef = TypedDict(
    "GatewayRouteSpecTypeDef",
    {
        "grpcRoute": GrpcGatewayRouteTypeDef,
        "http2Route": HttpGatewayRouteTypeDef,
        "httpRoute": HttpGatewayRouteTypeDef,
        "priority": int,
    },
    total=False,
)

RouteSpecOutputTypeDef = TypedDict(
    "RouteSpecOutputTypeDef",
    {
        "grpcRoute": GrpcRouteOutputTypeDef,
        "http2Route": HttpRouteOutputTypeDef,
        "httpRoute": HttpRouteOutputTypeDef,
        "priority": int,
        "tcpRoute": TcpRouteOutputTypeDef,
    },
    total=False,
)

RouteSpecTypeDef = TypedDict(
    "RouteSpecTypeDef",
    {
        "grpcRoute": GrpcRouteTypeDef,
        "http2Route": HttpRouteTypeDef,
        "httpRoute": HttpRouteTypeDef,
        "priority": int,
        "tcpRoute": TcpRouteTypeDef,
    },
    total=False,
)

BackendDefaultsOutputTypeDef = TypedDict(
    "BackendDefaultsOutputTypeDef",
    {
        "clientPolicy": ClientPolicyOutputTypeDef,
    },
    total=False,
)

_RequiredVirtualServiceBackendOutputTypeDef = TypedDict(
    "_RequiredVirtualServiceBackendOutputTypeDef",
    {
        "virtualServiceName": str,
    },
)
_OptionalVirtualServiceBackendOutputTypeDef = TypedDict(
    "_OptionalVirtualServiceBackendOutputTypeDef",
    {
        "clientPolicy": ClientPolicyOutputTypeDef,
    },
    total=False,
)

class VirtualServiceBackendOutputTypeDef(
    _RequiredVirtualServiceBackendOutputTypeDef, _OptionalVirtualServiceBackendOutputTypeDef
):
    pass

BackendDefaultsTypeDef = TypedDict(
    "BackendDefaultsTypeDef",
    {
        "clientPolicy": ClientPolicyTypeDef,
    },
    total=False,
)

_RequiredVirtualServiceBackendTypeDef = TypedDict(
    "_RequiredVirtualServiceBackendTypeDef",
    {
        "virtualServiceName": str,
    },
)
_OptionalVirtualServiceBackendTypeDef = TypedDict(
    "_OptionalVirtualServiceBackendTypeDef",
    {
        "clientPolicy": ClientPolicyTypeDef,
    },
    total=False,
)

class VirtualServiceBackendTypeDef(
    _RequiredVirtualServiceBackendTypeDef, _OptionalVirtualServiceBackendTypeDef
):
    pass

VirtualGatewayBackendDefaultsOutputTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsOutputTypeDef",
    {
        "clientPolicy": VirtualGatewayClientPolicyOutputTypeDef,
    },
    total=False,
)

VirtualGatewayBackendDefaultsTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsTypeDef",
    {
        "clientPolicy": VirtualGatewayClientPolicyTypeDef,
    },
    total=False,
)

GatewayRouteDataTypeDef = TypedDict(
    "GatewayRouteDataTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": GatewayRouteSpecOutputTypeDef,
        "status": GatewayRouteStatusTypeDef,
        "virtualGatewayName": str,
    },
)

_RequiredCreateGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredCreateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": GatewayRouteSpecTypeDef,
        "virtualGatewayName": str,
    },
)
_OptionalCreateGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalCreateGatewayRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateGatewayRouteInputRequestTypeDef(
    _RequiredCreateGatewayRouteInputRequestTypeDef, _OptionalCreateGatewayRouteInputRequestTypeDef
):
    pass

GatewayRouteSpecUnionTypeDef = Union[GatewayRouteSpecTypeDef, GatewayRouteSpecOutputTypeDef]
_RequiredUpdateGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": GatewayRouteSpecTypeDef,
        "virtualGatewayName": str,
    },
)
_OptionalUpdateGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateGatewayRouteInputRequestTypeDef(
    _RequiredUpdateGatewayRouteInputRequestTypeDef, _OptionalUpdateGatewayRouteInputRequestTypeDef
):
    pass

RouteDataTypeDef = TypedDict(
    "RouteDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "routeName": str,
        "spec": RouteSpecOutputTypeDef,
        "status": RouteStatusTypeDef,
        "virtualRouterName": str,
    },
)

_RequiredCreateRouteInputRequestTypeDef = TypedDict(
    "_RequiredCreateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": RouteSpecTypeDef,
        "virtualRouterName": str,
    },
)
_OptionalCreateRouteInputRequestTypeDef = TypedDict(
    "_OptionalCreateRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateRouteInputRequestTypeDef(
    _RequiredCreateRouteInputRequestTypeDef, _OptionalCreateRouteInputRequestTypeDef
):
    pass

RouteSpecUnionTypeDef = Union[RouteSpecTypeDef, RouteSpecOutputTypeDef]
_RequiredUpdateRouteInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": RouteSpecTypeDef,
        "virtualRouterName": str,
    },
)
_OptionalUpdateRouteInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateRouteInputRequestTypeDef(
    _RequiredUpdateRouteInputRequestTypeDef, _OptionalUpdateRouteInputRequestTypeDef
):
    pass

BackendOutputTypeDef = TypedDict(
    "BackendOutputTypeDef",
    {
        "virtualService": VirtualServiceBackendOutputTypeDef,
    },
    total=False,
)

BackendTypeDef = TypedDict(
    "BackendTypeDef",
    {
        "virtualService": VirtualServiceBackendTypeDef,
    },
    total=False,
)

_RequiredVirtualGatewaySpecOutputTypeDef = TypedDict(
    "_RequiredVirtualGatewaySpecOutputTypeDef",
    {
        "listeners": List[VirtualGatewayListenerOutputTypeDef],
    },
)
_OptionalVirtualGatewaySpecOutputTypeDef = TypedDict(
    "_OptionalVirtualGatewaySpecOutputTypeDef",
    {
        "backendDefaults": VirtualGatewayBackendDefaultsOutputTypeDef,
        "logging": VirtualGatewayLoggingOutputTypeDef,
    },
    total=False,
)

class VirtualGatewaySpecOutputTypeDef(
    _RequiredVirtualGatewaySpecOutputTypeDef, _OptionalVirtualGatewaySpecOutputTypeDef
):
    pass

_RequiredVirtualGatewaySpecTypeDef = TypedDict(
    "_RequiredVirtualGatewaySpecTypeDef",
    {
        "listeners": Sequence[VirtualGatewayListenerTypeDef],
    },
)
_OptionalVirtualGatewaySpecTypeDef = TypedDict(
    "_OptionalVirtualGatewaySpecTypeDef",
    {
        "backendDefaults": VirtualGatewayBackendDefaultsTypeDef,
        "logging": VirtualGatewayLoggingTypeDef,
    },
    total=False,
)

class VirtualGatewaySpecTypeDef(
    _RequiredVirtualGatewaySpecTypeDef, _OptionalVirtualGatewaySpecTypeDef
):
    pass

CreateGatewayRouteOutputTypeDef = TypedDict(
    "CreateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteGatewayRouteOutputTypeDef = TypedDict(
    "DeleteGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeGatewayRouteOutputTypeDef = TypedDict(
    "DescribeGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateGatewayRouteOutputTypeDef = TypedDict(
    "UpdateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": GatewayRouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRouteOutputTypeDef = TypedDict(
    "CreateRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRouteOutputTypeDef = TypedDict(
    "DeleteRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeRouteOutputTypeDef = TypedDict(
    "DescribeRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRouteOutputTypeDef = TypedDict(
    "UpdateRouteOutputTypeDef",
    {
        "route": RouteDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

VirtualNodeSpecOutputTypeDef = TypedDict(
    "VirtualNodeSpecOutputTypeDef",
    {
        "backendDefaults": BackendDefaultsOutputTypeDef,
        "backends": List[BackendOutputTypeDef],
        "listeners": List[ListenerOutputTypeDef],
        "logging": LoggingOutputTypeDef,
        "serviceDiscovery": ServiceDiscoveryOutputTypeDef,
    },
    total=False,
)

VirtualNodeSpecTypeDef = TypedDict(
    "VirtualNodeSpecTypeDef",
    {
        "backendDefaults": BackendDefaultsTypeDef,
        "backends": Sequence[BackendTypeDef],
        "listeners": Sequence[ListenerTypeDef],
        "logging": LoggingTypeDef,
        "serviceDiscovery": ServiceDiscoveryTypeDef,
    },
    total=False,
)

VirtualGatewayDataTypeDef = TypedDict(
    "VirtualGatewayDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualGatewaySpecOutputTypeDef,
        "status": VirtualGatewayStatusTypeDef,
        "virtualGatewayName": str,
    },
)

_RequiredCreateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualGatewaySpecTypeDef,
        "virtualGatewayName": str,
    },
)
_OptionalCreateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualGatewayInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateVirtualGatewayInputRequestTypeDef(
    _RequiredCreateVirtualGatewayInputRequestTypeDef,
    _OptionalCreateVirtualGatewayInputRequestTypeDef,
):
    pass

_RequiredUpdateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualGatewaySpecTypeDef,
        "virtualGatewayName": str,
    },
)
_OptionalUpdateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualGatewayInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualGatewayInputRequestTypeDef(
    _RequiredUpdateVirtualGatewayInputRequestTypeDef,
    _OptionalUpdateVirtualGatewayInputRequestTypeDef,
):
    pass

VirtualGatewaySpecUnionTypeDef = Union[VirtualGatewaySpecTypeDef, VirtualGatewaySpecOutputTypeDef]
VirtualNodeDataTypeDef = TypedDict(
    "VirtualNodeDataTypeDef",
    {
        "meshName": str,
        "metadata": ResourceMetadataTypeDef,
        "spec": VirtualNodeSpecOutputTypeDef,
        "status": VirtualNodeStatusTypeDef,
        "virtualNodeName": str,
    },
)

_RequiredCreateVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualNodeSpecTypeDef,
        "virtualNodeName": str,
    },
)
_OptionalCreateVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualNodeInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": Sequence[TagRefTypeDef],
    },
    total=False,
)

class CreateVirtualNodeInputRequestTypeDef(
    _RequiredCreateVirtualNodeInputRequestTypeDef, _OptionalCreateVirtualNodeInputRequestTypeDef
):
    pass

_RequiredUpdateVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": VirtualNodeSpecTypeDef,
        "virtualNodeName": str,
    },
)
_OptionalUpdateVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualNodeInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualNodeInputRequestTypeDef(
    _RequiredUpdateVirtualNodeInputRequestTypeDef, _OptionalUpdateVirtualNodeInputRequestTypeDef
):
    pass

VirtualNodeSpecUnionTypeDef = Union[VirtualNodeSpecTypeDef, VirtualNodeSpecOutputTypeDef]
CreateVirtualGatewayOutputTypeDef = TypedDict(
    "CreateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVirtualGatewayOutputTypeDef = TypedDict(
    "DeleteVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeVirtualGatewayOutputTypeDef = TypedDict(
    "DescribeVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateVirtualGatewayOutputTypeDef = TypedDict(
    "UpdateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": VirtualGatewayDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateVirtualNodeOutputTypeDef = TypedDict(
    "CreateVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVirtualNodeOutputTypeDef = TypedDict(
    "DeleteVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeVirtualNodeOutputTypeDef = TypedDict(
    "DescribeVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateVirtualNodeOutputTypeDef = TypedDict(
    "UpdateVirtualNodeOutputTypeDef",
    {
        "virtualNode": VirtualNodeDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
