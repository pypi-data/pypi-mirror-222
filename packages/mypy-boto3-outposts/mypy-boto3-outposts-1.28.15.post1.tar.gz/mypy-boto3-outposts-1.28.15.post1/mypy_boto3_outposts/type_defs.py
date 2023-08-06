"""
Type annotations for outposts service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs/)

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AddressTypeType,
    AssetStateType,
    CatalogItemClassType,
    CatalogItemStatusType,
    ComputeAssetStateType,
    FiberOpticCableTypeType,
    LineItemStatusType,
    MaximumSupportedWeightLbsType,
    OpticalStandardType,
    OrderStatusType,
    OrderTypeType,
    PaymentOptionType,
    PaymentTermType,
    PowerConnectorType,
    PowerDrawKvaType,
    PowerFeedDropType,
    PowerPhaseType,
    ShipmentCarrierType,
    SupportedHardwareTypeType,
    SupportedStorageEnumType,
    UplinkCountType,
    UplinkGbpsType,
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
    "AddressTypeDef",
    "AssetLocationTypeDef",
    "ComputeAttributesTypeDef",
    "CancelOrderInputRequestTypeDef",
    "EC2CapacityTypeDef",
    "ConnectionDetailsTypeDef",
    "LineItemRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateOutpostInputRequestTypeDef",
    "OutpostTypeDef",
    "RackPhysicalPropertiesTypeDef",
    "DeleteOutpostInputRequestTypeDef",
    "DeleteSiteInputRequestTypeDef",
    "GetCatalogItemInputRequestTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetOrderInputRequestTypeDef",
    "GetOutpostInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetOutpostInstanceTypesInputRequestTypeDef",
    "InstanceTypeItemTypeDef",
    "GetSiteAddressInputRequestTypeDef",
    "GetSiteInputRequestTypeDef",
    "LineItemAssetInformationTypeDef",
    "ShipmentInformationTypeDef",
    "ListAssetsInputRequestTypeDef",
    "ListCatalogItemsInputRequestTypeDef",
    "ListOrdersInputRequestTypeDef",
    "OrderSummaryTypeDef",
    "ListOutpostsInputRequestTypeDef",
    "ListSitesInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StartConnectionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOutpostInputRequestTypeDef",
    "UpdateSiteInputRequestTypeDef",
    "UpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    "UpdateSiteAddressInputRequestTypeDef",
    "AssetInfoTypeDef",
    "CatalogItemTypeDef",
    "CreateOrderInputRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetSiteAddressOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartConnectionResponseTypeDef",
    "UpdateSiteAddressOutputTypeDef",
    "CreateOutpostOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "ListOutpostsOutputTypeDef",
    "UpdateOutpostOutputTypeDef",
    "CreateSiteInputRequestTypeDef",
    "SiteTypeDef",
    "GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef",
    "ListAssetsInputListAssetsPaginateTypeDef",
    "ListCatalogItemsInputListCatalogItemsPaginateTypeDef",
    "ListOrdersInputListOrdersPaginateTypeDef",
    "ListOutpostsInputListOutpostsPaginateTypeDef",
    "ListSitesInputListSitesPaginateTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "LineItemTypeDef",
    "ListOrdersOutputTypeDef",
    "ListAssetsOutputTypeDef",
    "GetCatalogItemOutputTypeDef",
    "ListCatalogItemsOutputTypeDef",
    "CreateSiteOutputTypeDef",
    "GetSiteOutputTypeDef",
    "ListSitesOutputTypeDef",
    "UpdateSiteOutputTypeDef",
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    "OrderTypeDef",
    "CreateOrderOutputTypeDef",
    "GetOrderOutputTypeDef",
)

_RequiredAddressTypeDef = TypedDict(
    "_RequiredAddressTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "StateOrRegion": str,
        "PostalCode": str,
        "CountryCode": str,
    },
)
_OptionalAddressTypeDef = TypedDict(
    "_OptionalAddressTypeDef",
    {
        "ContactName": str,
        "ContactPhoneNumber": str,
        "AddressLine2": str,
        "AddressLine3": str,
        "DistrictOrCounty": str,
        "Municipality": str,
    },
    total=False,
)


class AddressTypeDef(_RequiredAddressTypeDef, _OptionalAddressTypeDef):
    pass


AssetLocationTypeDef = TypedDict(
    "AssetLocationTypeDef",
    {
        "RackElevation": float,
    },
    total=False,
)

ComputeAttributesTypeDef = TypedDict(
    "ComputeAttributesTypeDef",
    {
        "HostId": str,
        "State": ComputeAssetStateType,
    },
    total=False,
)

CancelOrderInputRequestTypeDef = TypedDict(
    "CancelOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)

EC2CapacityTypeDef = TypedDict(
    "EC2CapacityTypeDef",
    {
        "Family": str,
        "MaxSize": str,
        "Quantity": str,
    },
    total=False,
)

ConnectionDetailsTypeDef = TypedDict(
    "ConnectionDetailsTypeDef",
    {
        "ClientPublicKey": str,
        "ServerPublicKey": str,
        "ServerEndpoint": str,
        "ClientTunnelAddress": str,
        "ServerTunnelAddress": str,
        "AllowedIps": List[str],
    },
    total=False,
)

LineItemRequestTypeDef = TypedDict(
    "LineItemRequestTypeDef",
    {
        "CatalogItemId": str,
        "Quantity": int,
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

_RequiredCreateOutpostInputRequestTypeDef = TypedDict(
    "_RequiredCreateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "SiteId": str,
    },
)
_OptionalCreateOutpostInputRequestTypeDef = TypedDict(
    "_OptionalCreateOutpostInputRequestTypeDef",
    {
        "Description": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Mapping[str, str],
        "SupportedHardwareType": SupportedHardwareTypeType,
    },
    total=False,
)


class CreateOutpostInputRequestTypeDef(
    _RequiredCreateOutpostInputRequestTypeDef, _OptionalCreateOutpostInputRequestTypeDef
):
    pass


OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
        "SupportedHardwareType": SupportedHardwareTypeType,
    },
    total=False,
)

RackPhysicalPropertiesTypeDef = TypedDict(
    "RackPhysicalPropertiesTypeDef",
    {
        "PowerDrawKva": PowerDrawKvaType,
        "PowerPhase": PowerPhaseType,
        "PowerConnector": PowerConnectorType,
        "PowerFeedDrop": PowerFeedDropType,
        "UplinkGbps": UplinkGbpsType,
        "UplinkCount": UplinkCountType,
        "FiberOpticCableType": FiberOpticCableTypeType,
        "OpticalStandard": OpticalStandardType,
        "MaximumSupportedWeightLbs": MaximumSupportedWeightLbsType,
    },
    total=False,
)

DeleteOutpostInputRequestTypeDef = TypedDict(
    "DeleteOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

DeleteSiteInputRequestTypeDef = TypedDict(
    "DeleteSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

GetCatalogItemInputRequestTypeDef = TypedDict(
    "GetCatalogItemInputRequestTypeDef",
    {
        "CatalogItemId": str,
    },
)

GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

GetOrderInputRequestTypeDef = TypedDict(
    "GetOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)

GetOutpostInputRequestTypeDef = TypedDict(
    "GetOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
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

_RequiredGetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "_RequiredGetOutpostInstanceTypesInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalGetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "_OptionalGetOutpostInstanceTypesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetOutpostInstanceTypesInputRequestTypeDef(
    _RequiredGetOutpostInstanceTypesInputRequestTypeDef,
    _OptionalGetOutpostInstanceTypesInputRequestTypeDef,
):
    pass


InstanceTypeItemTypeDef = TypedDict(
    "InstanceTypeItemTypeDef",
    {
        "InstanceType": str,
    },
    total=False,
)

GetSiteAddressInputRequestTypeDef = TypedDict(
    "GetSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
    },
)

GetSiteInputRequestTypeDef = TypedDict(
    "GetSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

LineItemAssetInformationTypeDef = TypedDict(
    "LineItemAssetInformationTypeDef",
    {
        "AssetId": str,
        "MacAddressList": List[str],
    },
    total=False,
)

ShipmentInformationTypeDef = TypedDict(
    "ShipmentInformationTypeDef",
    {
        "ShipmentTrackingNumber": str,
        "ShipmentCarrier": ShipmentCarrierType,
    },
    total=False,
)

_RequiredListAssetsInputRequestTypeDef = TypedDict(
    "_RequiredListAssetsInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
    },
)
_OptionalListAssetsInputRequestTypeDef = TypedDict(
    "_OptionalListAssetsInputRequestTypeDef",
    {
        "HostIdFilter": Sequence[str],
        "MaxResults": int,
        "NextToken": str,
        "StatusFilter": Sequence[AssetStateType],
    },
    total=False,
)


class ListAssetsInputRequestTypeDef(
    _RequiredListAssetsInputRequestTypeDef, _OptionalListAssetsInputRequestTypeDef
):
    pass


ListCatalogItemsInputRequestTypeDef = TypedDict(
    "ListCatalogItemsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ItemClassFilter": Sequence[CatalogItemClassType],
        "SupportedStorageFilter": Sequence[SupportedStorageEnumType],
        "EC2FamilyFilter": Sequence[str],
    },
    total=False,
)

ListOrdersInputRequestTypeDef = TypedDict(
    "ListOrdersInputRequestTypeDef",
    {
        "OutpostIdentifierFilter": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

OrderSummaryTypeDef = TypedDict(
    "OrderSummaryTypeDef",
    {
        "OutpostId": str,
        "OrderId": str,
        "OrderType": OrderTypeType,
        "Status": OrderStatusType,
        "LineItemCountsByStatus": Dict[LineItemStatusType, int],
        "OrderSubmissionDate": datetime,
        "OrderFulfilledDate": datetime,
    },
    total=False,
)

ListOutpostsInputRequestTypeDef = TypedDict(
    "ListOutpostsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LifeCycleStatusFilter": Sequence[str],
        "AvailabilityZoneFilter": Sequence[str],
        "AvailabilityZoneIdFilter": Sequence[str],
    },
    total=False,
)

ListSitesInputRequestTypeDef = TypedDict(
    "ListSitesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "OperatingAddressCountryCodeFilter": Sequence[str],
        "OperatingAddressStateOrRegionFilter": Sequence[str],
        "OperatingAddressCityFilter": Sequence[str],
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

StartConnectionRequestRequestTypeDef = TypedDict(
    "StartConnectionRequestRequestTypeDef",
    {
        "DeviceSerialNumber": str,
        "AssetId": str,
        "ClientPublicKey": str,
        "NetworkInterfaceDeviceIndex": int,
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

_RequiredUpdateOutpostInputRequestTypeDef = TypedDict(
    "_RequiredUpdateOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalUpdateOutpostInputRequestTypeDef = TypedDict(
    "_OptionalUpdateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SupportedHardwareType": SupportedHardwareTypeType,
    },
    total=False,
)


class UpdateOutpostInputRequestTypeDef(
    _RequiredUpdateOutpostInputRequestTypeDef, _OptionalUpdateOutpostInputRequestTypeDef
):
    pass


_RequiredUpdateSiteInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)
_OptionalUpdateSiteInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Notes": str,
    },
    total=False,
)


class UpdateSiteInputRequestTypeDef(
    _RequiredUpdateSiteInputRequestTypeDef, _OptionalUpdateSiteInputRequestTypeDef
):
    pass


_RequiredUpdateSiteRackPhysicalPropertiesInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    {
        "SiteId": str,
    },
)
_OptionalUpdateSiteRackPhysicalPropertiesInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    {
        "PowerDrawKva": PowerDrawKvaType,
        "PowerPhase": PowerPhaseType,
        "PowerConnector": PowerConnectorType,
        "PowerFeedDrop": PowerFeedDropType,
        "UplinkGbps": UplinkGbpsType,
        "UplinkCount": UplinkCountType,
        "FiberOpticCableType": FiberOpticCableTypeType,
        "OpticalStandard": OpticalStandardType,
        "MaximumSupportedWeightLbs": MaximumSupportedWeightLbsType,
    },
    total=False,
)


class UpdateSiteRackPhysicalPropertiesInputRequestTypeDef(
    _RequiredUpdateSiteRackPhysicalPropertiesInputRequestTypeDef,
    _OptionalUpdateSiteRackPhysicalPropertiesInputRequestTypeDef,
):
    pass


UpdateSiteAddressInputRequestTypeDef = TypedDict(
    "UpdateSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": AddressTypeDef,
    },
)

AssetInfoTypeDef = TypedDict(
    "AssetInfoTypeDef",
    {
        "AssetId": str,
        "RackId": str,
        "AssetType": Literal["COMPUTE"],
        "ComputeAttributes": ComputeAttributesTypeDef,
        "AssetLocation": AssetLocationTypeDef,
    },
    total=False,
)

CatalogItemTypeDef = TypedDict(
    "CatalogItemTypeDef",
    {
        "CatalogItemId": str,
        "ItemStatus": CatalogItemStatusType,
        "EC2Capacities": List[EC2CapacityTypeDef],
        "PowerKva": float,
        "WeightLbs": int,
        "SupportedUplinkGbps": List[int],
        "SupportedStorage": List[SupportedStorageEnumType],
    },
    total=False,
)

_RequiredCreateOrderInputRequestTypeDef = TypedDict(
    "_RequiredCreateOrderInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "LineItems": Sequence[LineItemRequestTypeDef],
        "PaymentOption": PaymentOptionType,
    },
)
_OptionalCreateOrderInputRequestTypeDef = TypedDict(
    "_OptionalCreateOrderInputRequestTypeDef",
    {
        "PaymentTerm": PaymentTermType,
    },
    total=False,
)


class CreateOrderInputRequestTypeDef(
    _RequiredCreateOrderInputRequestTypeDef, _OptionalCreateOrderInputRequestTypeDef
):
    pass


GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "ConnectionId": str,
        "ConnectionDetails": ConnectionDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSiteAddressOutputTypeDef = TypedDict(
    "GetSiteAddressOutputTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": AddressTypeDef,
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

StartConnectionResponseTypeDef = TypedDict(
    "StartConnectionResponseTypeDef",
    {
        "ConnectionId": str,
        "UnderlayIpAddress": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSiteAddressOutputTypeDef = TypedDict(
    "UpdateSiteAddressOutputTypeDef",
    {
        "AddressType": AddressTypeType,
        "Address": AddressTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef",
    {
        "Outpost": OutpostTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef",
    {
        "Outpost": OutpostTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef",
    {
        "Outposts": List[OutpostTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateOutpostOutputTypeDef = TypedDict(
    "UpdateOutpostOutputTypeDef",
    {
        "Outpost": OutpostTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateSiteInputRequestTypeDef = TypedDict(
    "_RequiredCreateSiteInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateSiteInputRequestTypeDef = TypedDict(
    "_OptionalCreateSiteInputRequestTypeDef",
    {
        "Description": str,
        "Notes": str,
        "Tags": Mapping[str, str],
        "OperatingAddress": AddressTypeDef,
        "ShippingAddress": AddressTypeDef,
        "RackPhysicalProperties": RackPhysicalPropertiesTypeDef,
    },
    total=False,
)


class CreateSiteInputRequestTypeDef(
    _RequiredCreateSiteInputRequestTypeDef, _OptionalCreateSiteInputRequestTypeDef
):
    pass


SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "AccountId": str,
        "Name": str,
        "Description": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
        "Notes": str,
        "OperatingAddressCountryCode": str,
        "OperatingAddressStateOrRegion": str,
        "OperatingAddressCity": str,
        "RackPhysicalProperties": RackPhysicalPropertiesTypeDef,
    },
    total=False,
)

_RequiredGetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef = TypedDict(
    "_RequiredGetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalGetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef = TypedDict(
    "_OptionalGetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef(
    _RequiredGetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef,
    _OptionalGetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef,
):
    pass


_RequiredListAssetsInputListAssetsPaginateTypeDef = TypedDict(
    "_RequiredListAssetsInputListAssetsPaginateTypeDef",
    {
        "OutpostIdentifier": str,
    },
)
_OptionalListAssetsInputListAssetsPaginateTypeDef = TypedDict(
    "_OptionalListAssetsInputListAssetsPaginateTypeDef",
    {
        "HostIdFilter": Sequence[str],
        "StatusFilter": Sequence[AssetStateType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAssetsInputListAssetsPaginateTypeDef(
    _RequiredListAssetsInputListAssetsPaginateTypeDef,
    _OptionalListAssetsInputListAssetsPaginateTypeDef,
):
    pass


ListCatalogItemsInputListCatalogItemsPaginateTypeDef = TypedDict(
    "ListCatalogItemsInputListCatalogItemsPaginateTypeDef",
    {
        "ItemClassFilter": Sequence[CatalogItemClassType],
        "SupportedStorageFilter": Sequence[SupportedStorageEnumType],
        "EC2FamilyFilter": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListOrdersInputListOrdersPaginateTypeDef = TypedDict(
    "ListOrdersInputListOrdersPaginateTypeDef",
    {
        "OutpostIdentifierFilter": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListOutpostsInputListOutpostsPaginateTypeDef = TypedDict(
    "ListOutpostsInputListOutpostsPaginateTypeDef",
    {
        "LifeCycleStatusFilter": Sequence[str],
        "AvailabilityZoneFilter": Sequence[str],
        "AvailabilityZoneIdFilter": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSitesInputListSitesPaginateTypeDef = TypedDict(
    "ListSitesInputListSitesPaginateTypeDef",
    {
        "OperatingAddressCountryCodeFilter": Sequence[str],
        "OperatingAddressStateOrRegionFilter": Sequence[str],
        "OperatingAddressCityFilter": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List[InstanceTypeItemTypeDef],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LineItemTypeDef = TypedDict(
    "LineItemTypeDef",
    {
        "CatalogItemId": str,
        "LineItemId": str,
        "Quantity": int,
        "Status": LineItemStatusType,
        "ShipmentInformation": ShipmentInformationTypeDef,
        "AssetInformationList": List[LineItemAssetInformationTypeDef],
        "PreviousLineItemId": str,
        "PreviousOrderId": str,
    },
    total=False,
)

ListOrdersOutputTypeDef = TypedDict(
    "ListOrdersOutputTypeDef",
    {
        "Orders": List[OrderSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAssetsOutputTypeDef = TypedDict(
    "ListAssetsOutputTypeDef",
    {
        "Assets": List[AssetInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetCatalogItemOutputTypeDef = TypedDict(
    "GetCatalogItemOutputTypeDef",
    {
        "CatalogItem": CatalogItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCatalogItemsOutputTypeDef = TypedDict(
    "ListCatalogItemsOutputTypeDef",
    {
        "CatalogItems": List[CatalogItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateSiteOutputTypeDef = TypedDict(
    "CreateSiteOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSiteOutputTypeDef = TypedDict(
    "GetSiteOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef",
    {
        "Sites": List[SiteTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSiteOutputTypeDef = TypedDict(
    "UpdateSiteOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSiteRackPhysicalPropertiesOutputTypeDef = TypedDict(
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "OutpostId": str,
        "OrderId": str,
        "Status": OrderStatusType,
        "LineItems": List[LineItemTypeDef],
        "PaymentOption": PaymentOptionType,
        "OrderSubmissionDate": datetime,
        "OrderFulfilledDate": datetime,
        "PaymentTerm": PaymentTermType,
        "OrderType": OrderTypeType,
    },
    total=False,
)

CreateOrderOutputTypeDef = TypedDict(
    "CreateOrderOutputTypeDef",
    {
        "Order": OrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetOrderOutputTypeDef = TypedDict(
    "GetOrderOutputTypeDef",
    {
        "Order": OrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
