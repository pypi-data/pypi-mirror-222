"""
Type annotations for panorama service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_panorama/type_defs/)

Usage::

    ```python
    from mypy_boto3_panorama.type_defs import AlternateSoftwareMetadataTypeDef

    data: AlternateSoftwareMetadataTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ApplicationInstanceHealthStatusType,
    ApplicationInstanceStatusType,
    ConnectionTypeType,
    DesiredStateType,
    DeviceAggregatedStatusType,
    DeviceBrandType,
    DeviceConnectionStatusType,
    DeviceReportedStatusType,
    DeviceStatusType,
    DeviceTypeType,
    JobTypeType,
    ListDevicesSortByType,
    NetworkConnectionStatusType,
    NodeCategoryType,
    NodeFromTemplateJobStatusType,
    NodeInstanceStatusType,
    NodeSignalValueType,
    PackageImportJobStatusType,
    PackageImportJobTypeType,
    PackageVersionStatusType,
    PortTypeType,
    SortOrderType,
    StatusFilterType,
    UpdateProgressType,
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
    "AlternateSoftwareMetadataTypeDef",
    "ReportedRuntimeContextStateTypeDef",
    "ManifestOverridesPayloadTypeDef",
    "ManifestPayloadTypeDef",
    "ResponseMetadataTypeDef",
    "JobTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "StorageLocationTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeregisterPackageVersionRequestRequestTypeDef",
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    "DescribeApplicationInstanceRequestRequestTypeDef",
    "DescribeDeviceJobRequestRequestTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "LatestDeviceJobTypeDef",
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    "JobResourceTagsOutputTypeDef",
    "DescribeNodeRequestRequestTypeDef",
    "DescribePackageImportJobRequestRequestTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "OTAJobConfigTypeDef",
    "DeviceJobTypeDef",
    "StaticIpConnectionInfoOutputTypeDef",
    "StaticIpConnectionInfoTypeDef",
    "EthernetStatusTypeDef",
    "JobResourceTagsTypeDef",
    "ListApplicationInstanceDependenciesRequestRequestTypeDef",
    "PackageObjectTypeDef",
    "ListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    "NodeInstanceTypeDef",
    "ListApplicationInstancesRequestRequestTypeDef",
    "ListDevicesJobsRequestRequestTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    "NodeFromTemplateJobTypeDef",
    "ListNodesRequestRequestTypeDef",
    "NodeTypeDef",
    "ListPackageImportJobsRequestRequestTypeDef",
    "PackageImportJobTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "PackageListItemTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NtpPayloadOutputTypeDef",
    "NtpPayloadTypeDef",
    "NtpStatusTypeDef",
    "NodeInputPortTypeDef",
    "NodeOutputPortTypeDef",
    "NodeSignalTypeDef",
    "OutPutS3LocationTypeDef",
    "PackageVersionOutputConfigTypeDef",
    "S3LocationTypeDef",
    "RegisterPackageVersionRequestRequestTypeDef",
    "RemoveApplicationInstanceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceMetadataRequestRequestTypeDef",
    "ApplicationInstanceTypeDef",
    "CreateApplicationInstanceRequestRequestTypeDef",
    "CreateApplicationInstanceResponseTypeDef",
    "CreateNodeFromTemplateJobResponseTypeDef",
    "CreatePackageImportJobResponseTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    "DescribeApplicationInstanceResponseTypeDef",
    "DescribeDeviceJobResponseTypeDef",
    "DescribePackageVersionResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ProvisionDeviceResponseTypeDef",
    "SignalApplicationInstanceNodeInstancesResponseTypeDef",
    "UpdateDeviceMetadataResponseTypeDef",
    "CreateJobForDevicesResponseTypeDef",
    "CreatePackageResponseTypeDef",
    "DescribePackageResponseTypeDef",
    "DeviceTypeDef",
    "DescribeNodeFromTemplateJobResponseTypeDef",
    "DeviceJobConfigTypeDef",
    "ListDevicesJobsResponseTypeDef",
    "EthernetPayloadOutputTypeDef",
    "EthernetPayloadTypeDef",
    "JobResourceTagsUnionTypeDef",
    "ListApplicationInstanceDependenciesResponseTypeDef",
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    "ListNodeFromTemplateJobsResponseTypeDef",
    "ListNodesResponseTypeDef",
    "ListPackageImportJobsResponseTypeDef",
    "ListPackagesResponseTypeDef",
    "NetworkStatusTypeDef",
    "NodeInterfaceTypeDef",
    "SignalApplicationInstanceNodeInstancesRequestRequestTypeDef",
    "PackageImportJobOutputTypeDef",
    "PackageImportJobOutputConfigTypeDef",
    "PackageVersionInputConfigTypeDef",
    "ListApplicationInstancesResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "CreateJobForDevicesRequestRequestTypeDef",
    "NetworkPayloadOutputTypeDef",
    "NetworkPayloadTypeDef",
    "CreateNodeFromTemplateJobRequestRequestTypeDef",
    "DescribeNodeResponseTypeDef",
    "PackageImportJobInputConfigTypeDef",
    "DescribeDeviceResponseTypeDef",
    "NetworkPayloadUnionTypeDef",
    "ProvisionDeviceRequestRequestTypeDef",
    "CreatePackageImportJobRequestRequestTypeDef",
    "DescribePackageImportJobResponseTypeDef",
)

AlternateSoftwareMetadataTypeDef = TypedDict(
    "AlternateSoftwareMetadataTypeDef",
    {
        "Version": str,
    },
    total=False,
)

ReportedRuntimeContextStateTypeDef = TypedDict(
    "ReportedRuntimeContextStateTypeDef",
    {
        "DesiredState": DesiredStateType,
        "DeviceReportedStatus": DeviceReportedStatusType,
        "DeviceReportedTime": datetime,
        "RuntimeContextName": str,
    },
)

ManifestOverridesPayloadTypeDef = TypedDict(
    "ManifestOverridesPayloadTypeDef",
    {
        "PayloadData": str,
    },
    total=False,
)

ManifestPayloadTypeDef = TypedDict(
    "ManifestPayloadTypeDef",
    {
        "PayloadData": str,
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

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "DeviceId": str,
        "JobId": str,
    },
    total=False,
)

_RequiredCreatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
    },
)
_OptionalCreatePackageRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageRequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreatePackageRequestRequestTypeDef(
    _RequiredCreatePackageRequestRequestTypeDef, _OptionalCreatePackageRequestRequestTypeDef
):
    pass


StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "BinaryPrefixLocation": str,
        "Bucket": str,
        "GeneratedPrefixLocation": str,
        "ManifestPrefixLocation": str,
        "RepoPrefixLocation": str,
    },
)

DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

_RequiredDeletePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageRequestRequestTypeDef",
    {
        "PackageId": str,
    },
)
_OptionalDeletePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageRequestRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)


class DeletePackageRequestRequestTypeDef(
    _RequiredDeletePackageRequestRequestTypeDef, _OptionalDeletePackageRequestRequestTypeDef
):
    pass


_RequiredDeregisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
_OptionalDeregisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterPackageVersionRequestRequestTypeDef",
    {
        "OwnerAccount": str,
        "UpdatedLatestPatchVersion": str,
    },
    total=False,
)


class DeregisterPackageVersionRequestRequestTypeDef(
    _RequiredDeregisterPackageVersionRequestRequestTypeDef,
    _OptionalDeregisterPackageVersionRequestRequestTypeDef,
):
    pass


DescribeApplicationInstanceDetailsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

DescribeApplicationInstanceRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

DescribeDeviceJobRequestRequestTypeDef = TypedDict(
    "DescribeDeviceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

LatestDeviceJobTypeDef = TypedDict(
    "LatestDeviceJobTypeDef",
    {
        "ImageVersion": str,
        "JobType": JobTypeType,
        "Status": UpdateProgressType,
    },
    total=False,
)

DescribeNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

JobResourceTagsOutputTypeDef = TypedDict(
    "JobResourceTagsOutputTypeDef",
    {
        "ResourceType": Literal["PACKAGE"],
        "Tags": Dict[str, str],
    },
)

_RequiredDescribeNodeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeNodeRequestRequestTypeDef",
    {
        "NodeId": str,
    },
)
_OptionalDescribeNodeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeNodeRequestRequestTypeDef",
    {
        "OwnerAccount": str,
    },
    total=False,
)


class DescribeNodeRequestRequestTypeDef(
    _RequiredDescribeNodeRequestRequestTypeDef, _OptionalDescribeNodeRequestRequestTypeDef
):
    pass


DescribePackageImportJobRequestRequestTypeDef = TypedDict(
    "DescribePackageImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePackageRequestRequestTypeDef = TypedDict(
    "DescribePackageRequestRequestTypeDef",
    {
        "PackageId": str,
    },
)

_RequiredDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
    },
)
_OptionalDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageVersionRequestRequestTypeDef",
    {
        "OwnerAccount": str,
        "PatchVersion": str,
    },
    total=False,
)


class DescribePackageVersionRequestRequestTypeDef(
    _RequiredDescribePackageVersionRequestRequestTypeDef,
    _OptionalDescribePackageVersionRequestRequestTypeDef,
):
    pass


_RequiredOTAJobConfigTypeDef = TypedDict(
    "_RequiredOTAJobConfigTypeDef",
    {
        "ImageVersion": str,
    },
)
_OptionalOTAJobConfigTypeDef = TypedDict(
    "_OptionalOTAJobConfigTypeDef",
    {
        "AllowMajorVersionUpdate": bool,
    },
    total=False,
)


class OTAJobConfigTypeDef(_RequiredOTAJobConfigTypeDef, _OptionalOTAJobConfigTypeDef):
    pass


DeviceJobTypeDef = TypedDict(
    "DeviceJobTypeDef",
    {
        "CreatedTime": datetime,
        "DeviceId": str,
        "DeviceName": str,
        "JobId": str,
        "JobType": JobTypeType,
    },
    total=False,
)

StaticIpConnectionInfoOutputTypeDef = TypedDict(
    "StaticIpConnectionInfoOutputTypeDef",
    {
        "DefaultGateway": str,
        "Dns": List[str],
        "IpAddress": str,
        "Mask": str,
    },
)

StaticIpConnectionInfoTypeDef = TypedDict(
    "StaticIpConnectionInfoTypeDef",
    {
        "DefaultGateway": str,
        "Dns": Sequence[str],
        "IpAddress": str,
        "Mask": str,
    },
)

EthernetStatusTypeDef = TypedDict(
    "EthernetStatusTypeDef",
    {
        "ConnectionStatus": NetworkConnectionStatusType,
        "HwAddress": str,
        "IpAddress": str,
    },
    total=False,
)

JobResourceTagsTypeDef = TypedDict(
    "JobResourceTagsTypeDef",
    {
        "ResourceType": Literal["PACKAGE"],
        "Tags": Mapping[str, str],
    },
)

_RequiredListApplicationInstanceDependenciesRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationInstanceDependenciesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)
_OptionalListApplicationInstanceDependenciesRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationInstanceDependenciesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListApplicationInstanceDependenciesRequestRequestTypeDef(
    _RequiredListApplicationInstanceDependenciesRequestRequestTypeDef,
    _OptionalListApplicationInstanceDependenciesRequestRequestTypeDef,
):
    pass


PackageObjectTypeDef = TypedDict(
    "PackageObjectTypeDef",
    {
        "Name": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)

_RequiredListApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)
_OptionalListApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListApplicationInstanceNodeInstancesRequestRequestTypeDef(
    _RequiredListApplicationInstanceNodeInstancesRequestRequestTypeDef,
    _OptionalListApplicationInstanceNodeInstancesRequestRequestTypeDef,
):
    pass


_RequiredNodeInstanceTypeDef = TypedDict(
    "_RequiredNodeInstanceTypeDef",
    {
        "CurrentStatus": NodeInstanceStatusType,
        "NodeInstanceId": str,
    },
)
_OptionalNodeInstanceTypeDef = TypedDict(
    "_OptionalNodeInstanceTypeDef",
    {
        "NodeId": str,
        "NodeName": str,
        "PackageName": str,
        "PackagePatchVersion": str,
        "PackageVersion": str,
    },
    total=False,
)


class NodeInstanceTypeDef(_RequiredNodeInstanceTypeDef, _OptionalNodeInstanceTypeDef):
    pass


ListApplicationInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstancesRequestRequestTypeDef",
    {
        "DeviceId": str,
        "MaxResults": int,
        "NextToken": str,
        "StatusFilter": StatusFilterType,
    },
    total=False,
)

ListDevicesJobsRequestRequestTypeDef = TypedDict(
    "ListDevicesJobsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceAggregatedStatusFilter": DeviceAggregatedStatusType,
        "MaxResults": int,
        "NameFilter": str,
        "NextToken": str,
        "SortBy": ListDevicesSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListNodeFromTemplateJobsRequestRequestTypeDef = TypedDict(
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

NodeFromTemplateJobTypeDef = TypedDict(
    "NodeFromTemplateJobTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "NodeName": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
    },
    total=False,
)

ListNodesRequestRequestTypeDef = TypedDict(
    "ListNodesRequestRequestTypeDef",
    {
        "Category": NodeCategoryType,
        "MaxResults": int,
        "NextToken": str,
        "OwnerAccount": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
    total=False,
)

_RequiredNodeTypeDef = TypedDict(
    "_RequiredNodeTypeDef",
    {
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
_OptionalNodeTypeDef = TypedDict(
    "_OptionalNodeTypeDef",
    {
        "Description": str,
        "OwnerAccount": str,
        "PackageArn": str,
    },
    total=False,
)


class NodeTypeDef(_RequiredNodeTypeDef, _OptionalNodeTypeDef):
    pass


ListPackageImportJobsRequestRequestTypeDef = TypedDict(
    "ListPackageImportJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

PackageImportJobTypeDef = TypedDict(
    "PackageImportJobTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "JobType": PackageImportJobTypeType,
        "LastUpdatedTime": datetime,
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
    },
    total=False,
)

ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

PackageListItemTypeDef = TypedDict(
    "PackageListItemTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "PackageId": str,
        "PackageName": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

NtpPayloadOutputTypeDef = TypedDict(
    "NtpPayloadOutputTypeDef",
    {
        "NtpServers": List[str],
    },
)

NtpPayloadTypeDef = TypedDict(
    "NtpPayloadTypeDef",
    {
        "NtpServers": Sequence[str],
    },
)

NtpStatusTypeDef = TypedDict(
    "NtpStatusTypeDef",
    {
        "ConnectionStatus": NetworkConnectionStatusType,
        "IpAddress": str,
        "NtpServerName": str,
    },
    total=False,
)

NodeInputPortTypeDef = TypedDict(
    "NodeInputPortTypeDef",
    {
        "DefaultValue": str,
        "Description": str,
        "MaxConnections": int,
        "Name": str,
        "Type": PortTypeType,
    },
    total=False,
)

NodeOutputPortTypeDef = TypedDict(
    "NodeOutputPortTypeDef",
    {
        "Description": str,
        "Name": str,
        "Type": PortTypeType,
    },
    total=False,
)

NodeSignalTypeDef = TypedDict(
    "NodeSignalTypeDef",
    {
        "NodeInstanceId": str,
        "Signal": NodeSignalValueType,
    },
)

OutPutS3LocationTypeDef = TypedDict(
    "OutPutS3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)

_RequiredPackageVersionOutputConfigTypeDef = TypedDict(
    "_RequiredPackageVersionOutputConfigTypeDef",
    {
        "PackageName": str,
        "PackageVersion": str,
    },
)
_OptionalPackageVersionOutputConfigTypeDef = TypedDict(
    "_OptionalPackageVersionOutputConfigTypeDef",
    {
        "MarkLatest": bool,
    },
    total=False,
)


class PackageVersionOutputConfigTypeDef(
    _RequiredPackageVersionOutputConfigTypeDef, _OptionalPackageVersionOutputConfigTypeDef
):
    pass


_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Region": str,
    },
    total=False,
)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


_RequiredRegisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
_OptionalRegisterPackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterPackageVersionRequestRequestTypeDef",
    {
        "MarkLatest": bool,
        "OwnerAccount": str,
    },
    total=False,
)


class RegisterPackageVersionRequestRequestTypeDef(
    _RequiredRegisterPackageVersionRequestRequestTypeDef,
    _OptionalRegisterPackageVersionRequestRequestTypeDef,
):
    pass


RemoveApplicationInstanceRequestRequestTypeDef = TypedDict(
    "RemoveApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)

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

_RequiredUpdateDeviceMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceMetadataRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceMetadataRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateDeviceMetadataRequestRequestTypeDef(
    _RequiredUpdateDeviceMetadataRequestRequestTypeDef,
    _OptionalUpdateDeviceMetadataRequestRequestTypeDef,
):
    pass


ApplicationInstanceTypeDef = TypedDict(
    "ApplicationInstanceTypeDef",
    {
        "ApplicationInstanceId": str,
        "Arn": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "Name": str,
        "RuntimeContextStates": List[ReportedRuntimeContextStateTypeDef],
        "Status": ApplicationInstanceStatusType,
        "StatusDescription": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationInstanceRequestRequestTypeDef",
    {
        "DefaultRuntimeContextDevice": str,
        "ManifestPayload": ManifestPayloadTypeDef,
    },
)
_OptionalCreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceIdToReplace": str,
        "Description": str,
        "ManifestOverridesPayload": ManifestOverridesPayloadTypeDef,
        "Name": str,
        "RuntimeRoleArn": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateApplicationInstanceRequestRequestTypeDef(
    _RequiredCreateApplicationInstanceRequestRequestTypeDef,
    _OptionalCreateApplicationInstanceRequestRequestTypeDef,
):
    pass


CreateApplicationInstanceResponseTypeDef = TypedDict(
    "CreateApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateNodeFromTemplateJobResponseTypeDef = TypedDict(
    "CreateNodeFromTemplateJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePackageImportJobResponseTypeDef = TypedDict(
    "CreatePackageImportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeApplicationInstanceDetailsResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "Description": str,
        "ManifestOverridesPayload": ManifestOverridesPayloadTypeDef,
        "ManifestPayload": ManifestPayloadTypeDef,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeApplicationInstanceResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "Arn": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "LastUpdatedTime": datetime,
        "Name": str,
        "RuntimeContextStates": List[ReportedRuntimeContextStateTypeDef],
        "RuntimeRoleArn": str,
        "Status": ApplicationInstanceStatusType,
        "StatusDescription": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDeviceJobResponseTypeDef = TypedDict(
    "DescribeDeviceJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "DeviceArn": str,
        "DeviceId": str,
        "DeviceName": str,
        "DeviceType": DeviceTypeType,
        "ImageVersion": str,
        "JobId": str,
        "JobType": JobTypeType,
        "Status": UpdateProgressType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePackageVersionResponseTypeDef = TypedDict(
    "DescribePackageVersionResponseTypeDef",
    {
        "IsLatestPatch": bool,
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "RegisteredTime": datetime,
        "Status": PackageVersionStatusType,
        "StatusDescription": str,
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

ProvisionDeviceResponseTypeDef = TypedDict(
    "ProvisionDeviceResponseTypeDef",
    {
        "Arn": str,
        "Certificates": bytes,
        "DeviceId": str,
        "IotThingName": str,
        "Status": DeviceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SignalApplicationInstanceNodeInstancesResponseTypeDef = TypedDict(
    "SignalApplicationInstanceNodeInstancesResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDeviceMetadataResponseTypeDef = TypedDict(
    "UpdateDeviceMetadataResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateJobForDevicesResponseTypeDef = TypedDict(
    "CreateJobForDevicesResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef",
    {
        "Arn": str,
        "PackageId": str,
        "StorageLocation": StorageLocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePackageResponseTypeDef = TypedDict(
    "DescribePackageResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "PackageId": str,
        "PackageName": str,
        "ReadAccessPrincipalArns": List[str],
        "StorageLocation": StorageLocationTypeDef,
        "Tags": Dict[str, str],
        "WriteAccessPrincipalArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Brand": DeviceBrandType,
        "CreatedTime": datetime,
        "CurrentSoftware": str,
        "Description": str,
        "DeviceAggregatedStatus": DeviceAggregatedStatusType,
        "DeviceId": str,
        "LastUpdatedTime": datetime,
        "LatestDeviceJob": LatestDeviceJobTypeDef,
        "LeaseExpirationTime": datetime,
        "Name": str,
        "ProvisioningStatus": DeviceStatusType,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
    },
    total=False,
)

DescribeNodeFromTemplateJobResponseTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "JobTags": List[JobResourceTagsOutputTypeDef],
        "LastUpdatedTime": datetime,
        "NodeDescription": str,
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "TemplateParameters": Dict[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeviceJobConfigTypeDef = TypedDict(
    "DeviceJobConfigTypeDef",
    {
        "OTAJobConfig": OTAJobConfigTypeDef,
    },
    total=False,
)

ListDevicesJobsResponseTypeDef = TypedDict(
    "ListDevicesJobsResponseTypeDef",
    {
        "DeviceJobs": List[DeviceJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredEthernetPayloadOutputTypeDef = TypedDict(
    "_RequiredEthernetPayloadOutputTypeDef",
    {
        "ConnectionType": ConnectionTypeType,
    },
)
_OptionalEthernetPayloadOutputTypeDef = TypedDict(
    "_OptionalEthernetPayloadOutputTypeDef",
    {
        "StaticIpConnectionInfo": StaticIpConnectionInfoOutputTypeDef,
    },
    total=False,
)


class EthernetPayloadOutputTypeDef(
    _RequiredEthernetPayloadOutputTypeDef, _OptionalEthernetPayloadOutputTypeDef
):
    pass


_RequiredEthernetPayloadTypeDef = TypedDict(
    "_RequiredEthernetPayloadTypeDef",
    {
        "ConnectionType": ConnectionTypeType,
    },
)
_OptionalEthernetPayloadTypeDef = TypedDict(
    "_OptionalEthernetPayloadTypeDef",
    {
        "StaticIpConnectionInfo": StaticIpConnectionInfoTypeDef,
    },
    total=False,
)


class EthernetPayloadTypeDef(_RequiredEthernetPayloadTypeDef, _OptionalEthernetPayloadTypeDef):
    pass


JobResourceTagsUnionTypeDef = Union[JobResourceTagsTypeDef, JobResourceTagsOutputTypeDef]
ListApplicationInstanceDependenciesResponseTypeDef = TypedDict(
    "ListApplicationInstanceDependenciesResponseTypeDef",
    {
        "NextToken": str,
        "PackageObjects": List[PackageObjectTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListApplicationInstanceNodeInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInstances": List[NodeInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNodeFromTemplateJobsResponseTypeDef = TypedDict(
    "ListNodeFromTemplateJobsResponseTypeDef",
    {
        "NextToken": str,
        "NodeFromTemplateJobs": List[NodeFromTemplateJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "Nodes": List[NodeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPackageImportJobsResponseTypeDef = TypedDict(
    "ListPackageImportJobsResponseTypeDef",
    {
        "NextToken": str,
        "PackageImportJobs": List[PackageImportJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPackagesResponseTypeDef = TypedDict(
    "ListPackagesResponseTypeDef",
    {
        "NextToken": str,
        "Packages": List[PackageListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkStatusTypeDef = TypedDict(
    "NetworkStatusTypeDef",
    {
        "Ethernet0Status": EthernetStatusTypeDef,
        "Ethernet1Status": EthernetStatusTypeDef,
        "LastUpdatedTime": datetime,
        "NtpStatus": NtpStatusTypeDef,
    },
    total=False,
)

NodeInterfaceTypeDef = TypedDict(
    "NodeInterfaceTypeDef",
    {
        "Inputs": List[NodeInputPortTypeDef],
        "Outputs": List[NodeOutputPortTypeDef],
    },
)

SignalApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "SignalApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
        "NodeSignals": Sequence[NodeSignalTypeDef],
    },
)

PackageImportJobOutputTypeDef = TypedDict(
    "PackageImportJobOutputTypeDef",
    {
        "OutputS3Location": OutPutS3LocationTypeDef,
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)

PackageImportJobOutputConfigTypeDef = TypedDict(
    "PackageImportJobOutputConfigTypeDef",
    {
        "PackageVersionOutputConfig": PackageVersionOutputConfigTypeDef,
    },
    total=False,
)

PackageVersionInputConfigTypeDef = TypedDict(
    "PackageVersionInputConfigTypeDef",
    {
        "S3Location": S3LocationTypeDef,
    },
)

ListApplicationInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstancesResponseTypeDef",
    {
        "ApplicationInstances": List[ApplicationInstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateJobForDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobForDevicesRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "JobType": JobTypeType,
    },
)
_OptionalCreateJobForDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobForDevicesRequestRequestTypeDef",
    {
        "DeviceJobConfig": DeviceJobConfigTypeDef,
    },
    total=False,
)


class CreateJobForDevicesRequestRequestTypeDef(
    _RequiredCreateJobForDevicesRequestRequestTypeDef,
    _OptionalCreateJobForDevicesRequestRequestTypeDef,
):
    pass


NetworkPayloadOutputTypeDef = TypedDict(
    "NetworkPayloadOutputTypeDef",
    {
        "Ethernet0": EthernetPayloadOutputTypeDef,
        "Ethernet1": EthernetPayloadOutputTypeDef,
        "Ntp": NtpPayloadOutputTypeDef,
    },
    total=False,
)

NetworkPayloadTypeDef = TypedDict(
    "NetworkPayloadTypeDef",
    {
        "Ethernet0": EthernetPayloadTypeDef,
        "Ethernet1": EthernetPayloadTypeDef,
        "Ntp": NtpPayloadTypeDef,
    },
    total=False,
)

_RequiredCreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "TemplateParameters": Mapping[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
    },
)
_OptionalCreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "JobTags": Sequence[JobResourceTagsUnionTypeDef],
        "NodeDescription": str,
    },
    total=False,
)


class CreateNodeFromTemplateJobRequestRequestTypeDef(
    _RequiredCreateNodeFromTemplateJobRequestRequestTypeDef,
    _OptionalCreateNodeFromTemplateJobRequestRequestTypeDef,
):
    pass


DescribeNodeResponseTypeDef = TypedDict(
    "DescribeNodeResponseTypeDef",
    {
        "AssetName": str,
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Description": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "NodeInterface": NodeInterfaceTypeDef,
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PackageImportJobInputConfigTypeDef = TypedDict(
    "PackageImportJobInputConfigTypeDef",
    {
        "PackageVersionInputConfig": PackageVersionInputConfigTypeDef,
    },
    total=False,
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "AlternateSoftwares": List[AlternateSoftwareMetadataTypeDef],
        "Arn": str,
        "Brand": DeviceBrandType,
        "CreatedTime": datetime,
        "CurrentNetworkingStatus": NetworkStatusTypeDef,
        "CurrentSoftware": str,
        "Description": str,
        "DeviceAggregatedStatus": DeviceAggregatedStatusType,
        "DeviceConnectionStatus": DeviceConnectionStatusType,
        "DeviceId": str,
        "LatestAlternateSoftware": str,
        "LatestDeviceJob": LatestDeviceJobTypeDef,
        "LatestSoftware": str,
        "LeaseExpirationTime": datetime,
        "Name": str,
        "NetworkingConfiguration": NetworkPayloadOutputTypeDef,
        "ProvisioningStatus": DeviceStatusType,
        "SerialNumber": str,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkPayloadUnionTypeDef = Union[NetworkPayloadTypeDef, NetworkPayloadOutputTypeDef]
_RequiredProvisionDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionDeviceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalProvisionDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionDeviceRequestRequestTypeDef",
    {
        "Description": str,
        "NetworkingConfiguration": NetworkPayloadTypeDef,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class ProvisionDeviceRequestRequestTypeDef(
    _RequiredProvisionDeviceRequestRequestTypeDef, _OptionalProvisionDeviceRequestRequestTypeDef
):
    pass


_RequiredCreatePackageImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageImportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InputConfig": PackageImportJobInputConfigTypeDef,
        "JobType": PackageImportJobTypeType,
        "OutputConfig": PackageImportJobOutputConfigTypeDef,
    },
)
_OptionalCreatePackageImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageImportJobRequestRequestTypeDef",
    {
        "JobTags": Sequence[JobResourceTagsUnionTypeDef],
    },
    total=False,
)


class CreatePackageImportJobRequestRequestTypeDef(
    _RequiredCreatePackageImportJobRequestRequestTypeDef,
    _OptionalCreatePackageImportJobRequestRequestTypeDef,
):
    pass


DescribePackageImportJobResponseTypeDef = TypedDict(
    "DescribePackageImportJobResponseTypeDef",
    {
        "ClientToken": str,
        "CreatedTime": datetime,
        "InputConfig": PackageImportJobInputConfigTypeDef,
        "JobId": str,
        "JobTags": List[JobResourceTagsOutputTypeDef],
        "JobType": PackageImportJobTypeType,
        "LastUpdatedTime": datetime,
        "Output": PackageImportJobOutputTypeDef,
        "OutputConfig": PackageImportJobOutputConfigTypeDef,
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
