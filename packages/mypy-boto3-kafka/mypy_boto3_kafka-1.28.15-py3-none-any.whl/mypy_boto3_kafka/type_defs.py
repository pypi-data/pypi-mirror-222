"""
Type annotations for kafka service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/type_defs/)

Usage::

    ```python
    from mypy_boto3_kafka.type_defs import BatchAssociateScramSecretRequestRequestTypeDef

    data: BatchAssociateScramSecretRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ClientBrokerType,
    ClusterStateType,
    ClusterTypeType,
    ConfigurationStateType,
    EnhancedMonitoringType,
    KafkaVersionStatusType,
    StorageModeType,
    UserIdentityTypeType,
    VpcConnectionStateType,
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
    "BatchAssociateScramSecretRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedScramSecretTypeDef",
    "BatchDisassociateScramSecretRequestRequestTypeDef",
    "ProvisionedThroughputTypeDef",
    "CloudWatchLogsTypeDef",
    "FirehoseTypeDef",
    "S3TypeDef",
    "BrokerSoftwareInfoTypeDef",
    "TlsOutputTypeDef",
    "UnauthenticatedTypeDef",
    "TlsTypeDef",
    "ClientVpcConnectionTypeDef",
    "StateInfoTypeDef",
    "ErrorInfoTypeDef",
    "ClusterOperationStepInfoTypeDef",
    "ClusterOperationV2SummaryTypeDef",
    "CompatibleKafkaVersionTypeDef",
    "ConfigurationInfoTypeDef",
    "ConfigurationRevisionTypeDef",
    "PublicAccessTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateVpcConnectionRequestRequestTypeDef",
    "DeleteClusterPolicyRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteConfigurationRequestRequestTypeDef",
    "DeleteVpcConnectionRequestRequestTypeDef",
    "DescribeClusterOperationRequestRequestTypeDef",
    "DescribeClusterOperationV2RequestRequestTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterV2RequestRequestTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeVpcConnectionRequestRequestTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "GetBootstrapBrokersRequestRequestTypeDef",
    "GetClusterPolicyRequestRequestTypeDef",
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    "IamTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaVersionTypeDef",
    "PaginatorConfigTypeDef",
    "ListClientVpcConnectionsRequestRequestTypeDef",
    "ListClusterOperationsRequestRequestTypeDef",
    "ListClusterOperationsV2RequestRequestTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersV2RequestRequestTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListKafkaVersionsRequestRequestTypeDef",
    "ListNodesRequestRequestTypeDef",
    "ListScramSecretsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVpcConnectionsRequestRequestTypeDef",
    "VpcConnectionTypeDef",
    "NodeExporterInfoTypeDef",
    "NodeExporterTypeDef",
    "ZookeeperNodeInfoTypeDef",
    "PutClusterPolicyRequestRequestTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "RejectClientVpcConnectionRequestRequestTypeDef",
    "ScramTypeDef",
    "VpcConfigTypeDef",
    "VpcConfigOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrokerCountRequestRequestTypeDef",
    "UpdateBrokerTypeRequestRequestTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UserIdentityTypeDef",
    "VpcConnectivityTlsTypeDef",
    "VpcConnectivityIamTypeDef",
    "VpcConnectivityScramTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateClusterV2ResponseTypeDef",
    "CreateVpcConnectionResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteConfigurationResponseTypeDef",
    "DeleteVpcConnectionResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeVpcConnectionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "GetClusterPolicyResponseTypeDef",
    "ListScramSecretsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutClusterPolicyResponseTypeDef",
    "RebootBrokerResponseTypeDef",
    "UpdateBrokerCountResponseTypeDef",
    "UpdateBrokerStorageResponseTypeDef",
    "UpdateBrokerTypeResponseTypeDef",
    "UpdateClusterConfigurationResponseTypeDef",
    "UpdateClusterKafkaVersionResponseTypeDef",
    "UpdateConnectivityResponseTypeDef",
    "UpdateMonitoringResponseTypeDef",
    "UpdateSecurityResponseTypeDef",
    "UpdateStorageResponseTypeDef",
    "BatchAssociateScramSecretResponseTypeDef",
    "BatchDisassociateScramSecretResponseTypeDef",
    "BrokerEBSVolumeInfoTypeDef",
    "EBSStorageInfoTypeDef",
    "UpdateStorageRequestRequestTypeDef",
    "BrokerLogsTypeDef",
    "BrokerNodeInfoTypeDef",
    "ListClientVpcConnectionsResponseTypeDef",
    "ClusterOperationStepTypeDef",
    "ListClusterOperationsV2ResponseTypeDef",
    "GetCompatibleKafkaVersionsResponseTypeDef",
    "UpdateClusterConfigurationRequestRequestTypeDef",
    "UpdateClusterKafkaVersionRequestRequestTypeDef",
    "ConfigurationTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "EncryptionInfoTypeDef",
    "ServerlessSaslTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "ListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef",
    "ListClusterOperationsRequestListClusterOperationsPaginateTypeDef",
    "ListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListClustersV2RequestListClustersV2PaginateTypeDef",
    "ListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef",
    "ListConfigurationsRequestListConfigurationsPaginateTypeDef",
    "ListKafkaVersionsRequestListKafkaVersionsPaginateTypeDef",
    "ListNodesRequestListNodesPaginateTypeDef",
    "ListScramSecretsRequestListScramSecretsPaginateTypeDef",
    "ListVpcConnectionsRequestListVpcConnectionsPaginateTypeDef",
    "ListVpcConnectionsResponseTypeDef",
    "PrometheusInfoTypeDef",
    "PrometheusTypeDef",
    "SaslTypeDef",
    "VpcConnectionInfoServerlessTypeDef",
    "VpcConnectionInfoTypeDef",
    "VpcConnectivitySaslTypeDef",
    "UpdateBrokerStorageRequestRequestTypeDef",
    "StorageInfoTypeDef",
    "LoggingInfoTypeDef",
    "NodeInfoTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ServerlessClientAuthenticationTypeDef",
    "OpenMonitoringInfoTypeDef",
    "OpenMonitoringTypeDef",
    "ClientAuthenticationOutputTypeDef",
    "ClientAuthenticationTypeDef",
    "ClusterOperationV2ServerlessTypeDef",
    "VpcConnectivityClientAuthenticationTypeDef",
    "ListNodesResponseTypeDef",
    "ServerlessRequestTypeDef",
    "ServerlessTypeDef",
    "UpdateMonitoringRequestRequestTypeDef",
    "UpdateSecurityRequestRequestTypeDef",
    "VpcConnectivityTypeDef",
    "ConnectivityInfoTypeDef",
    "BrokerNodeGroupInfoOutputTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "MutableClusterInfoTypeDef",
    "UpdateConnectivityRequestRequestTypeDef",
    "ClusterInfoTypeDef",
    "ProvisionedTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "ProvisionedRequestTypeDef",
    "ClusterOperationInfoTypeDef",
    "ClusterOperationV2ProvisionedTypeDef",
    "DescribeClusterResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ClusterTypeDef",
    "CreateClusterV2RequestRequestTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ClusterOperationV2TypeDef",
    "DescribeClusterV2ResponseTypeDef",
    "ListClustersV2ResponseTypeDef",
    "DescribeClusterOperationV2ResponseTypeDef",
)

BatchAssociateScramSecretRequestRequestTypeDef = TypedDict(
    "BatchAssociateScramSecretRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": Sequence[str],
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

UnprocessedScramSecretTypeDef = TypedDict(
    "UnprocessedScramSecretTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "SecretArn": str,
    },
    total=False,
)

BatchDisassociateScramSecretRequestRequestTypeDef = TypedDict(
    "BatchDisassociateScramSecretRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": Sequence[str],
    },
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "Enabled": bool,
        "VolumeThroughput": int,
    },
    total=False,
)

_RequiredCloudWatchLogsTypeDef = TypedDict(
    "_RequiredCloudWatchLogsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCloudWatchLogsTypeDef = TypedDict(
    "_OptionalCloudWatchLogsTypeDef",
    {
        "LogGroup": str,
    },
    total=False,
)


class CloudWatchLogsTypeDef(_RequiredCloudWatchLogsTypeDef, _OptionalCloudWatchLogsTypeDef):
    pass


_RequiredFirehoseTypeDef = TypedDict(
    "_RequiredFirehoseTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalFirehoseTypeDef = TypedDict(
    "_OptionalFirehoseTypeDef",
    {
        "DeliveryStream": str,
    },
    total=False,
)


class FirehoseTypeDef(_RequiredFirehoseTypeDef, _OptionalFirehoseTypeDef):
    pass


_RequiredS3TypeDef = TypedDict(
    "_RequiredS3TypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalS3TypeDef = TypedDict(
    "_OptionalS3TypeDef",
    {
        "Bucket": str,
        "Prefix": str,
    },
    total=False,
)


class S3TypeDef(_RequiredS3TypeDef, _OptionalS3TypeDef):
    pass


BrokerSoftwareInfoTypeDef = TypedDict(
    "BrokerSoftwareInfoTypeDef",
    {
        "ConfigurationArn": str,
        "ConfigurationRevision": int,
        "KafkaVersion": str,
    },
    total=False,
)

TlsOutputTypeDef = TypedDict(
    "TlsOutputTypeDef",
    {
        "CertificateAuthorityArnList": List[str],
        "Enabled": bool,
    },
    total=False,
)

UnauthenticatedTypeDef = TypedDict(
    "UnauthenticatedTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

TlsTypeDef = TypedDict(
    "TlsTypeDef",
    {
        "CertificateAuthorityArnList": Sequence[str],
        "Enabled": bool,
    },
    total=False,
)

_RequiredClientVpcConnectionTypeDef = TypedDict(
    "_RequiredClientVpcConnectionTypeDef",
    {
        "VpcConnectionArn": str,
    },
)
_OptionalClientVpcConnectionTypeDef = TypedDict(
    "_OptionalClientVpcConnectionTypeDef",
    {
        "Authentication": str,
        "CreationTime": datetime,
        "State": VpcConnectionStateType,
        "Owner": str,
    },
    total=False,
)


class ClientVpcConnectionTypeDef(
    _RequiredClientVpcConnectionTypeDef, _OptionalClientVpcConnectionTypeDef
):
    pass


StateInfoTypeDef = TypedDict(
    "StateInfoTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "ErrorCode": str,
        "ErrorString": str,
    },
    total=False,
)

ClusterOperationStepInfoTypeDef = TypedDict(
    "ClusterOperationStepInfoTypeDef",
    {
        "StepStatus": str,
    },
    total=False,
)

ClusterOperationV2SummaryTypeDef = TypedDict(
    "ClusterOperationV2SummaryTypeDef",
    {
        "ClusterArn": str,
        "ClusterType": ClusterTypeType,
        "StartTime": datetime,
        "EndTime": datetime,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
    },
    total=False,
)

CompatibleKafkaVersionTypeDef = TypedDict(
    "CompatibleKafkaVersionTypeDef",
    {
        "SourceVersion": str,
        "TargetVersions": List[str],
    },
    total=False,
)

ConfigurationInfoTypeDef = TypedDict(
    "ConfigurationInfoTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef",
    {
        "CreationTime": datetime,
        "Revision": int,
    },
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class ConfigurationRevisionTypeDef(
    _RequiredConfigurationRevisionTypeDef, _OptionalConfigurationRevisionTypeDef
):
    pass


PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "Type": str,
    },
    total=False,
)

_RequiredCreateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "ServerProperties": Union[str, bytes, IO[Any], StreamingBody],
    },
)
_OptionalCreateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "KafkaVersions": Sequence[str],
    },
    total=False,
)


class CreateConfigurationRequestRequestTypeDef(
    _RequiredCreateConfigurationRequestRequestTypeDef,
    _OptionalCreateConfigurationRequestRequestTypeDef,
):
    pass


_RequiredCreateVpcConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcConnectionRequestRequestTypeDef",
    {
        "TargetClusterArn": str,
        "Authentication": str,
        "VpcId": str,
        "ClientSubnets": Sequence[str],
        "SecurityGroups": Sequence[str],
    },
)
_OptionalCreateVpcConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcConnectionRequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateVpcConnectionRequestRequestTypeDef(
    _RequiredCreateVpcConnectionRequestRequestTypeDef,
    _OptionalCreateVpcConnectionRequestRequestTypeDef,
):
    pass


DeleteClusterPolicyRequestRequestTypeDef = TypedDict(
    "DeleteClusterPolicyRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

_RequiredDeleteClusterRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalDeleteClusterRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteClusterRequestRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)


class DeleteClusterRequestRequestTypeDef(
    _RequiredDeleteClusterRequestRequestTypeDef, _OptionalDeleteClusterRequestRequestTypeDef
):
    pass


DeleteConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteVpcConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcConnectionRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeClusterOperationRequestRequestTypeDef = TypedDict(
    "DescribeClusterOperationRequestRequestTypeDef",
    {
        "ClusterOperationArn": str,
    },
)

DescribeClusterOperationV2RequestRequestTypeDef = TypedDict(
    "DescribeClusterOperationV2RequestRequestTypeDef",
    {
        "ClusterOperationArn": str,
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterV2RequestRequestTypeDef = TypedDict(
    "DescribeClusterV2RequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

DescribeVpcConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVpcConnectionRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

EncryptionAtRestTypeDef = TypedDict(
    "EncryptionAtRestTypeDef",
    {
        "DataVolumeKMSKeyId": str,
    },
)

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {
        "ClientBroker": ClientBrokerType,
        "InCluster": bool,
    },
    total=False,
)

GetBootstrapBrokersRequestRequestTypeDef = TypedDict(
    "GetBootstrapBrokersRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

GetClusterPolicyRequestRequestTypeDef = TypedDict(
    "GetClusterPolicyRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

GetCompatibleKafkaVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
    total=False,
)

IamTypeDef = TypedDict(
    "IamTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

JmxExporterInfoTypeDef = TypedDict(
    "JmxExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

JmxExporterTypeDef = TypedDict(
    "JmxExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

KafkaVersionTypeDef = TypedDict(
    "KafkaVersionTypeDef",
    {
        "Version": str,
        "Status": KafkaVersionStatusType,
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

_RequiredListClientVpcConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredListClientVpcConnectionsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClientVpcConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalListClientVpcConnectionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListClientVpcConnectionsRequestRequestTypeDef(
    _RequiredListClientVpcConnectionsRequestRequestTypeDef,
    _OptionalListClientVpcConnectionsRequestRequestTypeDef,
):
    pass


_RequiredListClusterOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListClusterOperationsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListClusterOperationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListClusterOperationsRequestRequestTypeDef(
    _RequiredListClusterOperationsRequestRequestTypeDef,
    _OptionalListClusterOperationsRequestRequestTypeDef,
):
    pass


_RequiredListClusterOperationsV2RequestRequestTypeDef = TypedDict(
    "_RequiredListClusterOperationsV2RequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsV2RequestRequestTypeDef = TypedDict(
    "_OptionalListClusterOperationsV2RequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListClusterOperationsV2RequestRequestTypeDef(
    _RequiredListClusterOperationsV2RequestRequestTypeDef,
    _OptionalListClusterOperationsV2RequestRequestTypeDef,
):
    pass


ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "ClusterNameFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersV2RequestRequestTypeDef = TypedDict(
    "ListClustersV2RequestRequestTypeDef",
    {
        "ClusterNameFilter": str,
        "ClusterTypeFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_OptionalListConfigurationRevisionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListConfigurationRevisionsRequestRequestTypeDef(
    _RequiredListConfigurationRevisionsRequestRequestTypeDef,
    _OptionalListConfigurationRevisionsRequestRequestTypeDef,
):
    pass


ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListKafkaVersionsRequestRequestTypeDef = TypedDict(
    "ListKafkaVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListNodesRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListNodesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListNodesRequestRequestTypeDef(
    _RequiredListNodesRequestRequestTypeDef, _OptionalListNodesRequestRequestTypeDef
):
    pass


_RequiredListScramSecretsRequestRequestTypeDef = TypedDict(
    "_RequiredListScramSecretsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListScramSecretsRequestRequestTypeDef = TypedDict(
    "_OptionalListScramSecretsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListScramSecretsRequestRequestTypeDef(
    _RequiredListScramSecretsRequestRequestTypeDef, _OptionalListScramSecretsRequestRequestTypeDef
):
    pass


ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListVpcConnectionsRequestRequestTypeDef = TypedDict(
    "ListVpcConnectionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredVpcConnectionTypeDef = TypedDict(
    "_RequiredVpcConnectionTypeDef",
    {
        "VpcConnectionArn": str,
        "TargetClusterArn": str,
    },
)
_OptionalVpcConnectionTypeDef = TypedDict(
    "_OptionalVpcConnectionTypeDef",
    {
        "CreationTime": datetime,
        "Authentication": str,
        "VpcId": str,
        "State": VpcConnectionStateType,
    },
    total=False,
)


class VpcConnectionTypeDef(_RequiredVpcConnectionTypeDef, _OptionalVpcConnectionTypeDef):
    pass


NodeExporterInfoTypeDef = TypedDict(
    "NodeExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeExporterTypeDef = TypedDict(
    "NodeExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

ZookeeperNodeInfoTypeDef = TypedDict(
    "ZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)

_RequiredPutClusterPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutClusterPolicyRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "Policy": str,
    },
)
_OptionalPutClusterPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutClusterPolicyRequestRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)


class PutClusterPolicyRequestRequestTypeDef(
    _RequiredPutClusterPolicyRequestRequestTypeDef, _OptionalPutClusterPolicyRequestRequestTypeDef
):
    pass


RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerIds": Sequence[str],
        "ClusterArn": str,
    },
)

RejectClientVpcConnectionRequestRequestTypeDef = TypedDict(
    "RejectClientVpcConnectionRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "VpcConnectionArn": str,
    },
)

ScramTypeDef = TypedDict(
    "ScramTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredVpcConfigTypeDef = TypedDict(
    "_RequiredVpcConfigTypeDef",
    {
        "SubnetIds": Sequence[str],
    },
)
_OptionalVpcConfigTypeDef = TypedDict(
    "_OptionalVpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
    },
    total=False,
)


class VpcConfigTypeDef(_RequiredVpcConfigTypeDef, _OptionalVpcConfigTypeDef):
    pass


_RequiredVpcConfigOutputTypeDef = TypedDict(
    "_RequiredVpcConfigOutputTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalVpcConfigOutputTypeDef = TypedDict(
    "_OptionalVpcConfigOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class VpcConfigOutputTypeDef(_RequiredVpcConfigOutputTypeDef, _OptionalVpcConfigOutputTypeDef):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateBrokerCountRequestRequestTypeDef = TypedDict(
    "UpdateBrokerCountRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetNumberOfBrokerNodes": int,
    },
)

UpdateBrokerTypeRequestRequestTypeDef = TypedDict(
    "UpdateBrokerTypeRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetInstanceType": str,
    },
)

_RequiredUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
        "ServerProperties": Union[str, bytes, IO[Any], StreamingBody],
    },
)
_OptionalUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateConfigurationRequestRequestTypeDef(
    _RequiredUpdateConfigurationRequestRequestTypeDef,
    _OptionalUpdateConfigurationRequestRequestTypeDef,
):
    pass


UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "Type": UserIdentityTypeType,
        "PrincipalId": str,
    },
    total=False,
)

VpcConnectivityTlsTypeDef = TypedDict(
    "VpcConnectivityTlsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

VpcConnectivityIamTypeDef = TypedDict(
    "VpcConnectivityIamTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

VpcConnectivityScramTypeDef = TypedDict(
    "VpcConnectivityScramTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateClusterV2ResponseTypeDef = TypedDict(
    "CreateClusterV2ResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ClusterType": ClusterTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateVpcConnectionResponseTypeDef = TypedDict(
    "CreateVpcConnectionResponseTypeDef",
    {
        "VpcConnectionArn": str,
        "State": VpcConnectionStateType,
        "Authentication": str,
        "VpcId": str,
        "ClientSubnets": List[str],
        "SecurityGroups": List[str],
        "CreationTime": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "State": ClusterStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteConfigurationResponseTypeDef = TypedDict(
    "DeleteConfigurationResponseTypeDef",
    {
        "Arn": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVpcConnectionResponseTypeDef = TypedDict(
    "DeleteVpcConnectionResponseTypeDef",
    {
        "VpcConnectionArn": str,
        "State": VpcConnectionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeVpcConnectionResponseTypeDef = TypedDict(
    "DescribeVpcConnectionResponseTypeDef",
    {
        "VpcConnectionArn": str,
        "TargetClusterArn": str,
        "State": VpcConnectionStateType,
        "Authentication": str,
        "VpcId": str,
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "CreationTime": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBootstrapBrokersResponseTypeDef = TypedDict(
    "GetBootstrapBrokersResponseTypeDef",
    {
        "BootstrapBrokerString": str,
        "BootstrapBrokerStringTls": str,
        "BootstrapBrokerStringSaslScram": str,
        "BootstrapBrokerStringSaslIam": str,
        "BootstrapBrokerStringPublicTls": str,
        "BootstrapBrokerStringPublicSaslScram": str,
        "BootstrapBrokerStringPublicSaslIam": str,
        "BootstrapBrokerStringVpcConnectivityTls": str,
        "BootstrapBrokerStringVpcConnectivitySaslScram": str,
        "BootstrapBrokerStringVpcConnectivitySaslIam": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetClusterPolicyResponseTypeDef = TypedDict(
    "GetClusterPolicyResponseTypeDef",
    {
        "CurrentVersion": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListScramSecretsResponseTypeDef = TypedDict(
    "ListScramSecretsResponseTypeDef",
    {
        "NextToken": str,
        "SecretArnList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutClusterPolicyResponseTypeDef = TypedDict(
    "PutClusterPolicyResponseTypeDef",
    {
        "CurrentVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RebootBrokerResponseTypeDef = TypedDict(
    "RebootBrokerResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateBrokerCountResponseTypeDef = TypedDict(
    "UpdateBrokerCountResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateBrokerStorageResponseTypeDef = TypedDict(
    "UpdateBrokerStorageResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateBrokerTypeResponseTypeDef = TypedDict(
    "UpdateBrokerTypeResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateClusterConfigurationResponseTypeDef = TypedDict(
    "UpdateClusterConfigurationResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateClusterKafkaVersionResponseTypeDef = TypedDict(
    "UpdateClusterKafkaVersionResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateConnectivityResponseTypeDef = TypedDict(
    "UpdateConnectivityResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateMonitoringResponseTypeDef = TypedDict(
    "UpdateMonitoringResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSecurityResponseTypeDef = TypedDict(
    "UpdateSecurityResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateStorageResponseTypeDef = TypedDict(
    "UpdateStorageResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchAssociateScramSecretResponseTypeDef = TypedDict(
    "BatchAssociateScramSecretResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List[UnprocessedScramSecretTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDisassociateScramSecretResponseTypeDef = TypedDict(
    "BatchDisassociateScramSecretResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List[UnprocessedScramSecretTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_RequiredBrokerEBSVolumeInfoTypeDef",
    {
        "KafkaBrokerNodeId": str,
    },
)
_OptionalBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_OptionalBrokerEBSVolumeInfoTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "VolumeSizeGB": int,
    },
    total=False,
)


class BrokerEBSVolumeInfoTypeDef(
    _RequiredBrokerEBSVolumeInfoTypeDef, _OptionalBrokerEBSVolumeInfoTypeDef
):
    pass


EBSStorageInfoTypeDef = TypedDict(
    "EBSStorageInfoTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "VolumeSize": int,
    },
    total=False,
)

_RequiredUpdateStorageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateStorageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageRequestRequestTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "StorageMode": StorageModeType,
        "VolumeSizeGB": int,
    },
    total=False,
)


class UpdateStorageRequestRequestTypeDef(
    _RequiredUpdateStorageRequestRequestTypeDef, _OptionalUpdateStorageRequestRequestTypeDef
):
    pass


BrokerLogsTypeDef = TypedDict(
    "BrokerLogsTypeDef",
    {
        "CloudWatchLogs": CloudWatchLogsTypeDef,
        "Firehose": FirehoseTypeDef,
        "S3": S3TypeDef,
    },
    total=False,
)

BrokerNodeInfoTypeDef = TypedDict(
    "BrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)

ListClientVpcConnectionsResponseTypeDef = TypedDict(
    "ListClientVpcConnectionsResponseTypeDef",
    {
        "ClientVpcConnections": List[ClientVpcConnectionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ClusterOperationStepTypeDef = TypedDict(
    "ClusterOperationStepTypeDef",
    {
        "StepInfo": ClusterOperationStepInfoTypeDef,
        "StepName": str,
    },
    total=False,
)

ListClusterOperationsV2ResponseTypeDef = TypedDict(
    "ListClusterOperationsV2ResponseTypeDef",
    {
        "ClusterOperationInfoList": List[ClusterOperationV2SummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetCompatibleKafkaVersionsResponseTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsResponseTypeDef",
    {
        "CompatibleKafkaVersions": List[CompatibleKafkaVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateClusterConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateClusterConfigurationRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ConfigurationInfo": ConfigurationInfoTypeDef,
        "CurrentVersion": str,
    },
)

_RequiredUpdateClusterKafkaVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterKafkaVersionRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetKafkaVersion": str,
    },
)
_OptionalUpdateClusterKafkaVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterKafkaVersionRequestRequestTypeDef",
    {
        "ConfigurationInfo": ConfigurationInfoTypeDef,
    },
    total=False,
)


class UpdateClusterKafkaVersionRequestRequestTypeDef(
    _RequiredUpdateClusterKafkaVersionRequestRequestTypeDef,
    _OptionalUpdateClusterKafkaVersionRequestRequestTypeDef,
):
    pass


ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "State": ConfigurationStateType,
    },
)

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List[ConfigurationRevisionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EncryptionInfoTypeDef = TypedDict(
    "EncryptionInfoTypeDef",
    {
        "EncryptionAtRest": EncryptionAtRestTypeDef,
        "EncryptionInTransit": EncryptionInTransitTypeDef,
    },
    total=False,
)

ServerlessSaslTypeDef = TypedDict(
    "ServerlessSaslTypeDef",
    {
        "Iam": IamTypeDef,
    },
    total=False,
)

ListKafkaVersionsResponseTypeDef = TypedDict(
    "ListKafkaVersionsResponseTypeDef",
    {
        "KafkaVersions": List[KafkaVersionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef = TypedDict(
    "_RequiredListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef = TypedDict(
    "_OptionalListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef(
    _RequiredListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef,
    _OptionalListClientVpcConnectionsRequestListClientVpcConnectionsPaginateTypeDef,
):
    pass


_RequiredListClusterOperationsRequestListClusterOperationsPaginateTypeDef = TypedDict(
    "_RequiredListClusterOperationsRequestListClusterOperationsPaginateTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsRequestListClusterOperationsPaginateTypeDef = TypedDict(
    "_OptionalListClusterOperationsRequestListClusterOperationsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListClusterOperationsRequestListClusterOperationsPaginateTypeDef(
    _RequiredListClusterOperationsRequestListClusterOperationsPaginateTypeDef,
    _OptionalListClusterOperationsRequestListClusterOperationsPaginateTypeDef,
):
    pass


_RequiredListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef = TypedDict(
    "_RequiredListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef = TypedDict(
    "_OptionalListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef(
    _RequiredListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef,
    _OptionalListClusterOperationsV2RequestListClusterOperationsV2PaginateTypeDef,
):
    pass


ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "ClusterNameFilter": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListClustersV2RequestListClustersV2PaginateTypeDef = TypedDict(
    "ListClustersV2RequestListClustersV2PaginateTypeDef",
    {
        "ClusterNameFilter": str,
        "ClusterTypeFilter": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef = TypedDict(
    "_OptionalListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef(
    _RequiredListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef,
    _OptionalListConfigurationRevisionsRequestListConfigurationRevisionsPaginateTypeDef,
):
    pass


ListConfigurationsRequestListConfigurationsPaginateTypeDef = TypedDict(
    "ListConfigurationsRequestListConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListKafkaVersionsRequestListKafkaVersionsPaginateTypeDef = TypedDict(
    "ListKafkaVersionsRequestListKafkaVersionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListNodesRequestListNodesPaginateTypeDef = TypedDict(
    "_RequiredListNodesRequestListNodesPaginateTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListNodesRequestListNodesPaginateTypeDef = TypedDict(
    "_OptionalListNodesRequestListNodesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListNodesRequestListNodesPaginateTypeDef(
    _RequiredListNodesRequestListNodesPaginateTypeDef,
    _OptionalListNodesRequestListNodesPaginateTypeDef,
):
    pass


_RequiredListScramSecretsRequestListScramSecretsPaginateTypeDef = TypedDict(
    "_RequiredListScramSecretsRequestListScramSecretsPaginateTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListScramSecretsRequestListScramSecretsPaginateTypeDef = TypedDict(
    "_OptionalListScramSecretsRequestListScramSecretsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListScramSecretsRequestListScramSecretsPaginateTypeDef(
    _RequiredListScramSecretsRequestListScramSecretsPaginateTypeDef,
    _OptionalListScramSecretsRequestListScramSecretsPaginateTypeDef,
):
    pass


ListVpcConnectionsRequestListVpcConnectionsPaginateTypeDef = TypedDict(
    "ListVpcConnectionsRequestListVpcConnectionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListVpcConnectionsResponseTypeDef = TypedDict(
    "ListVpcConnectionsResponseTypeDef",
    {
        "VpcConnections": List[VpcConnectionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PrometheusInfoTypeDef = TypedDict(
    "PrometheusInfoTypeDef",
    {
        "JmxExporter": JmxExporterInfoTypeDef,
        "NodeExporter": NodeExporterInfoTypeDef,
    },
    total=False,
)

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {
        "JmxExporter": JmxExporterTypeDef,
        "NodeExporter": NodeExporterTypeDef,
    },
    total=False,
)

SaslTypeDef = TypedDict(
    "SaslTypeDef",
    {
        "Scram": ScramTypeDef,
        "Iam": IamTypeDef,
    },
    total=False,
)

VpcConnectionInfoServerlessTypeDef = TypedDict(
    "VpcConnectionInfoServerlessTypeDef",
    {
        "CreationTime": datetime,
        "Owner": str,
        "UserIdentity": UserIdentityTypeDef,
        "VpcConnectionArn": str,
    },
    total=False,
)

VpcConnectionInfoTypeDef = TypedDict(
    "VpcConnectionInfoTypeDef",
    {
        "VpcConnectionArn": str,
        "Owner": str,
        "UserIdentity": UserIdentityTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

VpcConnectivitySaslTypeDef = TypedDict(
    "VpcConnectivitySaslTypeDef",
    {
        "Scram": VpcConnectivityScramTypeDef,
        "Iam": VpcConnectivityIamTypeDef,
    },
    total=False,
)

UpdateBrokerStorageRequestRequestTypeDef = TypedDict(
    "UpdateBrokerStorageRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetBrokerEBSVolumeInfo": Sequence[BrokerEBSVolumeInfoTypeDef],
    },
)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef",
    {
        "EbsStorageInfo": EBSStorageInfoTypeDef,
    },
    total=False,
)

LoggingInfoTypeDef = TypedDict(
    "LoggingInfoTypeDef",
    {
        "BrokerLogs": BrokerLogsTypeDef,
    },
)

NodeInfoTypeDef = TypedDict(
    "NodeInfoTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": BrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": Literal["BROKER"],
        "ZookeeperNodeInfo": ZookeeperNodeInfoTypeDef,
    },
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ServerlessClientAuthenticationTypeDef = TypedDict(
    "ServerlessClientAuthenticationTypeDef",
    {
        "Sasl": ServerlessSaslTypeDef,
    },
    total=False,
)

OpenMonitoringInfoTypeDef = TypedDict(
    "OpenMonitoringInfoTypeDef",
    {
        "Prometheus": PrometheusInfoTypeDef,
    },
)

OpenMonitoringTypeDef = TypedDict(
    "OpenMonitoringTypeDef",
    {
        "Prometheus": PrometheusTypeDef,
    },
)

ClientAuthenticationOutputTypeDef = TypedDict(
    "ClientAuthenticationOutputTypeDef",
    {
        "Sasl": SaslTypeDef,
        "Tls": TlsOutputTypeDef,
        "Unauthenticated": UnauthenticatedTypeDef,
    },
    total=False,
)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef",
    {
        "Sasl": SaslTypeDef,
        "Tls": TlsTypeDef,
        "Unauthenticated": UnauthenticatedTypeDef,
    },
    total=False,
)

ClusterOperationV2ServerlessTypeDef = TypedDict(
    "ClusterOperationV2ServerlessTypeDef",
    {
        "VpcConnectionInfo": VpcConnectionInfoServerlessTypeDef,
    },
    total=False,
)

VpcConnectivityClientAuthenticationTypeDef = TypedDict(
    "VpcConnectivityClientAuthenticationTypeDef",
    {
        "Sasl": VpcConnectivitySaslTypeDef,
        "Tls": VpcConnectivityTlsTypeDef,
    },
    total=False,
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInfoList": List[NodeInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredServerlessRequestTypeDef = TypedDict(
    "_RequiredServerlessRequestTypeDef",
    {
        "VpcConfigs": Sequence[VpcConfigTypeDef],
    },
)
_OptionalServerlessRequestTypeDef = TypedDict(
    "_OptionalServerlessRequestTypeDef",
    {
        "ClientAuthentication": ServerlessClientAuthenticationTypeDef,
    },
    total=False,
)


class ServerlessRequestTypeDef(
    _RequiredServerlessRequestTypeDef, _OptionalServerlessRequestTypeDef
):
    pass


_RequiredServerlessTypeDef = TypedDict(
    "_RequiredServerlessTypeDef",
    {
        "VpcConfigs": List[VpcConfigOutputTypeDef],
    },
)
_OptionalServerlessTypeDef = TypedDict(
    "_OptionalServerlessTypeDef",
    {
        "ClientAuthentication": ServerlessClientAuthenticationTypeDef,
    },
    total=False,
)


class ServerlessTypeDef(_RequiredServerlessTypeDef, _OptionalServerlessTypeDef):
    pass


_RequiredUpdateMonitoringRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMonitoringRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateMonitoringRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMonitoringRequestRequestTypeDef",
    {
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": OpenMonitoringInfoTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
    },
    total=False,
)


class UpdateMonitoringRequestRequestTypeDef(
    _RequiredUpdateMonitoringRequestRequestTypeDef, _OptionalUpdateMonitoringRequestRequestTypeDef
):
    pass


_RequiredUpdateSecurityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateSecurityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityRequestRequestTypeDef",
    {
        "ClientAuthentication": ClientAuthenticationTypeDef,
        "EncryptionInfo": EncryptionInfoTypeDef,
    },
    total=False,
)


class UpdateSecurityRequestRequestTypeDef(
    _RequiredUpdateSecurityRequestRequestTypeDef, _OptionalUpdateSecurityRequestRequestTypeDef
):
    pass


VpcConnectivityTypeDef = TypedDict(
    "VpcConnectivityTypeDef",
    {
        "ClientAuthentication": VpcConnectivityClientAuthenticationTypeDef,
    },
    total=False,
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "PublicAccess": PublicAccessTypeDef,
        "VpcConnectivity": VpcConnectivityTypeDef,
    },
    total=False,
)

_RequiredBrokerNodeGroupInfoOutputTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoOutputTypeDef",
    {
        "ClientSubnets": List[str],
        "InstanceType": str,
    },
)
_OptionalBrokerNodeGroupInfoOutputTypeDef = TypedDict(
    "_OptionalBrokerNodeGroupInfoOutputTypeDef",
    {
        "BrokerAZDistribution": Literal["DEFAULT"],
        "SecurityGroups": List[str],
        "StorageInfo": StorageInfoTypeDef,
        "ConnectivityInfo": ConnectivityInfoTypeDef,
        "ZoneIds": List[str],
    },
    total=False,
)


class BrokerNodeGroupInfoOutputTypeDef(
    _RequiredBrokerNodeGroupInfoOutputTypeDef, _OptionalBrokerNodeGroupInfoOutputTypeDef
):
    pass


_RequiredBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoTypeDef",
    {
        "ClientSubnets": Sequence[str],
        "InstanceType": str,
    },
)
_OptionalBrokerNodeGroupInfoTypeDef = TypedDict(
    "_OptionalBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": Literal["DEFAULT"],
        "SecurityGroups": Sequence[str],
        "StorageInfo": StorageInfoTypeDef,
        "ConnectivityInfo": ConnectivityInfoTypeDef,
        "ZoneIds": Sequence[str],
    },
    total=False,
)


class BrokerNodeGroupInfoTypeDef(
    _RequiredBrokerNodeGroupInfoTypeDef, _OptionalBrokerNodeGroupInfoTypeDef
):
    pass


MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[BrokerEBSVolumeInfoTypeDef],
        "ConfigurationInfo": ConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": OpenMonitoringTypeDef,
        "KafkaVersion": str,
        "LoggingInfo": LoggingInfoTypeDef,
        "InstanceType": str,
        "ClientAuthentication": ClientAuthenticationOutputTypeDef,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "ConnectivityInfo": ConnectivityInfoTypeDef,
        "StorageMode": StorageModeType,
    },
    total=False,
)

UpdateConnectivityRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ConnectivityInfo": ConnectivityInfoTypeDef,
        "CurrentVersion": str,
    },
)

ClusterInfoTypeDef = TypedDict(
    "ClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": BrokerNodeGroupInfoOutputTypeDef,
        "ClientAuthentication": ClientAuthenticationOutputTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": OpenMonitoringTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "State": ClusterStateType,
        "StateInfo": StateInfoTypeDef,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
        "ZookeeperConnectStringTls": str,
        "StorageMode": StorageModeType,
    },
    total=False,
)

_RequiredProvisionedTypeDef = TypedDict(
    "_RequiredProvisionedTypeDef",
    {
        "BrokerNodeGroupInfo": BrokerNodeGroupInfoOutputTypeDef,
        "NumberOfBrokerNodes": int,
    },
)
_OptionalProvisionedTypeDef = TypedDict(
    "_OptionalProvisionedTypeDef",
    {
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "ClientAuthentication": ClientAuthenticationOutputTypeDef,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": OpenMonitoringInfoTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
        "ZookeeperConnectString": str,
        "ZookeeperConnectStringTls": str,
        "StorageMode": StorageModeType,
    },
    total=False,
)


class ProvisionedTypeDef(_RequiredProvisionedTypeDef, _OptionalProvisionedTypeDef):
    pass


_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "BrokerNodeGroupInfo": BrokerNodeGroupInfoTypeDef,
        "ClusterName": str,
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "ClientAuthentication": ClientAuthenticationTypeDef,
        "ConfigurationInfo": ConfigurationInfoTypeDef,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": OpenMonitoringInfoTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
        "Tags": Mapping[str, str],
        "StorageMode": StorageModeType,
    },
    total=False,
)


class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass


_RequiredProvisionedRequestTypeDef = TypedDict(
    "_RequiredProvisionedRequestTypeDef",
    {
        "BrokerNodeGroupInfo": BrokerNodeGroupInfoTypeDef,
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
    },
)
_OptionalProvisionedRequestTypeDef = TypedDict(
    "_OptionalProvisionedRequestTypeDef",
    {
        "ClientAuthentication": ClientAuthenticationTypeDef,
        "ConfigurationInfo": ConfigurationInfoTypeDef,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": OpenMonitoringInfoTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
        "StorageMode": StorageModeType,
    },
    total=False,
)


class ProvisionedRequestTypeDef(
    _RequiredProvisionedRequestTypeDef, _OptionalProvisionedRequestTypeDef
):
    pass


ClusterOperationInfoTypeDef = TypedDict(
    "ClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationSteps": List[ClusterOperationStepTypeDef],
        "OperationType": str,
        "SourceClusterInfo": MutableClusterInfoTypeDef,
        "TargetClusterInfo": MutableClusterInfoTypeDef,
        "VpcConnectionInfo": VpcConnectionInfoTypeDef,
    },
    total=False,
)

ClusterOperationV2ProvisionedTypeDef = TypedDict(
    "ClusterOperationV2ProvisionedTypeDef",
    {
        "OperationSteps": List[ClusterOperationStepTypeDef],
        "SourceClusterInfo": MutableClusterInfoTypeDef,
        "TargetClusterInfo": MutableClusterInfoTypeDef,
        "VpcConnectionInfo": VpcConnectionInfoTypeDef,
    },
    total=False,
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "ClusterInfo": ClusterInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "ClusterInfoList": List[ClusterInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ActiveOperationArn": str,
        "ClusterType": ClusterTypeType,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentVersion": str,
        "State": ClusterStateType,
        "StateInfo": StateInfoTypeDef,
        "Tags": Dict[str, str],
        "Provisioned": ProvisionedTypeDef,
        "Serverless": ServerlessTypeDef,
    },
    total=False,
)

_RequiredCreateClusterV2RequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterV2RequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
_OptionalCreateClusterV2RequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterV2RequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
        "Provisioned": ProvisionedRequestTypeDef,
        "Serverless": ServerlessRequestTypeDef,
    },
    total=False,
)


class CreateClusterV2RequestRequestTypeDef(
    _RequiredCreateClusterV2RequestRequestTypeDef, _OptionalCreateClusterV2RequestRequestTypeDef
):
    pass


DescribeClusterOperationResponseTypeDef = TypedDict(
    "DescribeClusterOperationResponseTypeDef",
    {
        "ClusterOperationInfo": ClusterOperationInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListClusterOperationsResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List[ClusterOperationInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ClusterOperationV2TypeDef = TypedDict(
    "ClusterOperationV2TypeDef",
    {
        "ClusterArn": str,
        "ClusterType": ClusterTypeType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "Provisioned": ClusterOperationV2ProvisionedTypeDef,
        "Serverless": ClusterOperationV2ServerlessTypeDef,
    },
    total=False,
)

DescribeClusterV2ResponseTypeDef = TypedDict(
    "DescribeClusterV2ResponseTypeDef",
    {
        "ClusterInfo": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListClustersV2ResponseTypeDef = TypedDict(
    "ListClustersV2ResponseTypeDef",
    {
        "ClusterInfoList": List[ClusterTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeClusterOperationV2ResponseTypeDef = TypedDict(
    "DescribeClusterOperationV2ResponseTypeDef",
    {
        "ClusterOperationInfo": ClusterOperationV2TypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
