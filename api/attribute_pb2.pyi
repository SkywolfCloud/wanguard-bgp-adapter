from google.protobuf import any_pb2 as _any_pb2
import gobgp_pb2 as _gobgp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LsOspfRouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LS_OSPF_ROUTE_TYPE_UNKNOWN: _ClassVar[LsOspfRouteType]
    LS_OSPF_ROUTE_TYPE_INTRA_AREA: _ClassVar[LsOspfRouteType]
    LS_OSPF_ROUTE_TYPE_INTER_AREA: _ClassVar[LsOspfRouteType]
    LS_OSPF_ROUTE_TYPE_EXTERNAL1: _ClassVar[LsOspfRouteType]
    LS_OSPF_ROUTE_TYPE_EXTERNAL2: _ClassVar[LsOspfRouteType]
    LS_OSPF_ROUTE_TYPE_NSSA1: _ClassVar[LsOspfRouteType]
    LS_OSPF_ROUTE_TYPE_NSSA2: _ClassVar[LsOspfRouteType]

class LsNLRIType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LS_NLRI_UNKNOWN: _ClassVar[LsNLRIType]
    LS_NLRI_NODE: _ClassVar[LsNLRIType]
    LS_NLRI_LINK: _ClassVar[LsNLRIType]
    LS_NLRI_PREFIX_V4: _ClassVar[LsNLRIType]
    LS_NLRI_PREFIX_V6: _ClassVar[LsNLRIType]

class LsProtocolID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LS_PROTOCOL_UNKNOWN: _ClassVar[LsProtocolID]
    LS_PROTOCOL_ISIS_L1: _ClassVar[LsProtocolID]
    LS_PROTOCOL_ISIS_L2: _ClassVar[LsProtocolID]
    LS_PROTOCOL_OSPF_V2: _ClassVar[LsProtocolID]
    LS_PROTOCOL_DIRECT: _ClassVar[LsProtocolID]
    LS_PROTOCOL_STATIC: _ClassVar[LsProtocolID]
    LS_PROTOCOL_OSPF_V3: _ClassVar[LsProtocolID]

class SRv6Behavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESERVED: _ClassVar[SRv6Behavior]
    END: _ClassVar[SRv6Behavior]
    END_WITH_PSP: _ClassVar[SRv6Behavior]
    END_WITH_USP: _ClassVar[SRv6Behavior]
    END_WITH_PSP_USP: _ClassVar[SRv6Behavior]
    ENDX: _ClassVar[SRv6Behavior]
    ENDX_WITH_PSP: _ClassVar[SRv6Behavior]
    ENDX_WITH_USP: _ClassVar[SRv6Behavior]
    ENDX_WITH_PSP_USP: _ClassVar[SRv6Behavior]
    ENDT: _ClassVar[SRv6Behavior]
    ENDT_WITH_PSP: _ClassVar[SRv6Behavior]
    ENDT_WITH_USP: _ClassVar[SRv6Behavior]
    ENDT_WITH_PSP_USP: _ClassVar[SRv6Behavior]
    END_B6_ENCAPS: _ClassVar[SRv6Behavior]
    END_BM: _ClassVar[SRv6Behavior]
    END_DX6: _ClassVar[SRv6Behavior]
    END_DX4: _ClassVar[SRv6Behavior]
    END_DT6: _ClassVar[SRv6Behavior]
    END_DT4: _ClassVar[SRv6Behavior]
    END_DT46: _ClassVar[SRv6Behavior]
    END_DX2: _ClassVar[SRv6Behavior]
    END_DX2V: _ClassVar[SRv6Behavior]
    END_DT2U: _ClassVar[SRv6Behavior]
    END_DT2M: _ClassVar[SRv6Behavior]
    END_B6_ENCAPS_Red: _ClassVar[SRv6Behavior]
    END_WITH_USD: _ClassVar[SRv6Behavior]
    END_WITH_PSP_USD: _ClassVar[SRv6Behavior]
    END_WITH_USP_USD: _ClassVar[SRv6Behavior]
    END_WITH_PSP_USP_USD: _ClassVar[SRv6Behavior]
    ENDX_WITH_USD: _ClassVar[SRv6Behavior]
    ENDX_WITH_PSP_USD: _ClassVar[SRv6Behavior]
    ENDX_WITH_USP_USD: _ClassVar[SRv6Behavior]
    ENDX_WITH_PSP_USP_USD: _ClassVar[SRv6Behavior]
    ENDT_WITH_USD: _ClassVar[SRv6Behavior]
    ENDT_WITH_PSP_USD: _ClassVar[SRv6Behavior]
    ENDT_WITH_USP_USD: _ClassVar[SRv6Behavior]
    ENDT_WITH_PSP_USP_USD: _ClassVar[SRv6Behavior]
    ENDM_GTP6D: _ClassVar[SRv6Behavior]
    ENDM_GTP6DI: _ClassVar[SRv6Behavior]
    ENDM_GTP6E: _ClassVar[SRv6Behavior]
    ENDM_GTP4E: _ClassVar[SRv6Behavior]

class ENLPType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Reserved: _ClassVar[ENLPType]
    Type1: _ClassVar[ENLPType]
    Type2: _ClassVar[ENLPType]
    Type3: _ClassVar[ENLPType]
    Type4: _ClassVar[ENLPType]
LS_OSPF_ROUTE_TYPE_UNKNOWN: LsOspfRouteType
LS_OSPF_ROUTE_TYPE_INTRA_AREA: LsOspfRouteType
LS_OSPF_ROUTE_TYPE_INTER_AREA: LsOspfRouteType
LS_OSPF_ROUTE_TYPE_EXTERNAL1: LsOspfRouteType
LS_OSPF_ROUTE_TYPE_EXTERNAL2: LsOspfRouteType
LS_OSPF_ROUTE_TYPE_NSSA1: LsOspfRouteType
LS_OSPF_ROUTE_TYPE_NSSA2: LsOspfRouteType
LS_NLRI_UNKNOWN: LsNLRIType
LS_NLRI_NODE: LsNLRIType
LS_NLRI_LINK: LsNLRIType
LS_NLRI_PREFIX_V4: LsNLRIType
LS_NLRI_PREFIX_V6: LsNLRIType
LS_PROTOCOL_UNKNOWN: LsProtocolID
LS_PROTOCOL_ISIS_L1: LsProtocolID
LS_PROTOCOL_ISIS_L2: LsProtocolID
LS_PROTOCOL_OSPF_V2: LsProtocolID
LS_PROTOCOL_DIRECT: LsProtocolID
LS_PROTOCOL_STATIC: LsProtocolID
LS_PROTOCOL_OSPF_V3: LsProtocolID
RESERVED: SRv6Behavior
END: SRv6Behavior
END_WITH_PSP: SRv6Behavior
END_WITH_USP: SRv6Behavior
END_WITH_PSP_USP: SRv6Behavior
ENDX: SRv6Behavior
ENDX_WITH_PSP: SRv6Behavior
ENDX_WITH_USP: SRv6Behavior
ENDX_WITH_PSP_USP: SRv6Behavior
ENDT: SRv6Behavior
ENDT_WITH_PSP: SRv6Behavior
ENDT_WITH_USP: SRv6Behavior
ENDT_WITH_PSP_USP: SRv6Behavior
END_B6_ENCAPS: SRv6Behavior
END_BM: SRv6Behavior
END_DX6: SRv6Behavior
END_DX4: SRv6Behavior
END_DT6: SRv6Behavior
END_DT4: SRv6Behavior
END_DT46: SRv6Behavior
END_DX2: SRv6Behavior
END_DX2V: SRv6Behavior
END_DT2U: SRv6Behavior
END_DT2M: SRv6Behavior
END_B6_ENCAPS_Red: SRv6Behavior
END_WITH_USD: SRv6Behavior
END_WITH_PSP_USD: SRv6Behavior
END_WITH_USP_USD: SRv6Behavior
END_WITH_PSP_USP_USD: SRv6Behavior
ENDX_WITH_USD: SRv6Behavior
ENDX_WITH_PSP_USD: SRv6Behavior
ENDX_WITH_USP_USD: SRv6Behavior
ENDX_WITH_PSP_USP_USD: SRv6Behavior
ENDT_WITH_USD: SRv6Behavior
ENDT_WITH_PSP_USD: SRv6Behavior
ENDT_WITH_USP_USD: SRv6Behavior
ENDT_WITH_PSP_USP_USD: SRv6Behavior
ENDM_GTP6D: SRv6Behavior
ENDM_GTP6DI: SRv6Behavior
ENDM_GTP6E: SRv6Behavior
ENDM_GTP4E: SRv6Behavior
Reserved: ENLPType
Type1: ENLPType
Type2: ENLPType
Type3: ENLPType
Type4: ENLPType

class OriginAttribute(_message.Message):
    __slots__ = ("origin",)
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    origin: int
    def __init__(self, origin: _Optional[int] = ...) -> None: ...

class AsSegment(_message.Message):
    __slots__ = ("type", "numbers")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[AsSegment.Type]
        AS_SET: _ClassVar[AsSegment.Type]
        AS_SEQUENCE: _ClassVar[AsSegment.Type]
        AS_CONFED_SEQUENCE: _ClassVar[AsSegment.Type]
        AS_CONFED_SET: _ClassVar[AsSegment.Type]
    UNKNOWN: AsSegment.Type
    AS_SET: AsSegment.Type
    AS_SEQUENCE: AsSegment.Type
    AS_CONFED_SEQUENCE: AsSegment.Type
    AS_CONFED_SET: AsSegment.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    type: AsSegment.Type
    numbers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[_Union[AsSegment.Type, str]] = ..., numbers: _Optional[_Iterable[int]] = ...) -> None: ...

class AsPathAttribute(_message.Message):
    __slots__ = ("segments",)
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[AsSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[AsSegment, _Mapping]]] = ...) -> None: ...

class NextHopAttribute(_message.Message):
    __slots__ = ("next_hop",)
    NEXT_HOP_FIELD_NUMBER: _ClassVar[int]
    next_hop: str
    def __init__(self, next_hop: _Optional[str] = ...) -> None: ...

class MultiExitDiscAttribute(_message.Message):
    __slots__ = ("med",)
    MED_FIELD_NUMBER: _ClassVar[int]
    med: int
    def __init__(self, med: _Optional[int] = ...) -> None: ...

class LocalPrefAttribute(_message.Message):
    __slots__ = ("local_pref",)
    LOCAL_PREF_FIELD_NUMBER: _ClassVar[int]
    local_pref: int
    def __init__(self, local_pref: _Optional[int] = ...) -> None: ...

class AtomicAggregateAttribute(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AggregatorAttribute(_message.Message):
    __slots__ = ("asn", "address")
    ASN_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    asn: int
    address: str
    def __init__(self, asn: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class CommunitiesAttribute(_message.Message):
    __slots__ = ("communities",)
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    communities: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, communities: _Optional[_Iterable[int]] = ...) -> None: ...

class OriginatorIdAttribute(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ClusterListAttribute(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class IPAddressPrefix(_message.Message):
    __slots__ = ("prefix_len", "prefix")
    PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    prefix_len: int
    prefix: str
    def __init__(self, prefix_len: _Optional[int] = ..., prefix: _Optional[str] = ...) -> None: ...

class LabeledIPAddressPrefix(_message.Message):
    __slots__ = ("labels", "prefix_len", "prefix")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[int]
    prefix_len: int
    prefix: str
    def __init__(self, labels: _Optional[_Iterable[int]] = ..., prefix_len: _Optional[int] = ..., prefix: _Optional[str] = ...) -> None: ...

class EncapsulationNLRI(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class RouteDistinguisherTwoOctetASN(_message.Message):
    __slots__ = ("admin", "assigned")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    admin: int
    assigned: int
    def __init__(self, admin: _Optional[int] = ..., assigned: _Optional[int] = ...) -> None: ...

class RouteDistinguisherIPAddress(_message.Message):
    __slots__ = ("admin", "assigned")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    admin: str
    assigned: int
    def __init__(self, admin: _Optional[str] = ..., assigned: _Optional[int] = ...) -> None: ...

class RouteDistinguisherFourOctetASN(_message.Message):
    __slots__ = ("admin", "assigned")
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    admin: int
    assigned: int
    def __init__(self, admin: _Optional[int] = ..., assigned: _Optional[int] = ...) -> None: ...

class EthernetSegmentIdentifier(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: bytes
    def __init__(self, type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class VPLSNLRI(_message.Message):
    __slots__ = ("rd", "ve_id", "ve_block_offset", "ve_block_size", "label_block_base")
    RD_FIELD_NUMBER: _ClassVar[int]
    VE_ID_FIELD_NUMBER: _ClassVar[int]
    VE_BLOCK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    VE_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    LABEL_BLOCK_BASE_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    ve_id: int
    ve_block_offset: int
    ve_block_size: int
    label_block_base: int
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., ve_id: _Optional[int] = ..., ve_block_offset: _Optional[int] = ..., ve_block_size: _Optional[int] = ..., label_block_base: _Optional[int] = ...) -> None: ...

class EVPNEthernetAutoDiscoveryRoute(_message.Message):
    __slots__ = ("rd", "esi", "ethernet_tag", "label")
    RD_FIELD_NUMBER: _ClassVar[int]
    ESI_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_TAG_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    esi: EthernetSegmentIdentifier
    ethernet_tag: int
    label: int
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., esi: _Optional[_Union[EthernetSegmentIdentifier, _Mapping]] = ..., ethernet_tag: _Optional[int] = ..., label: _Optional[int] = ...) -> None: ...

class EVPNMACIPAdvertisementRoute(_message.Message):
    __slots__ = ("rd", "esi", "ethernet_tag", "mac_address", "ip_address", "labels")
    RD_FIELD_NUMBER: _ClassVar[int]
    ESI_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_TAG_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    esi: EthernetSegmentIdentifier
    ethernet_tag: int
    mac_address: str
    ip_address: str
    labels: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., esi: _Optional[_Union[EthernetSegmentIdentifier, _Mapping]] = ..., ethernet_tag: _Optional[int] = ..., mac_address: _Optional[str] = ..., ip_address: _Optional[str] = ..., labels: _Optional[_Iterable[int]] = ...) -> None: ...

class EVPNInclusiveMulticastEthernetTagRoute(_message.Message):
    __slots__ = ("rd", "ethernet_tag", "ip_address")
    RD_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_TAG_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    ethernet_tag: int
    ip_address: str
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., ethernet_tag: _Optional[int] = ..., ip_address: _Optional[str] = ...) -> None: ...

class EVPNEthernetSegmentRoute(_message.Message):
    __slots__ = ("rd", "esi", "ip_address")
    RD_FIELD_NUMBER: _ClassVar[int]
    ESI_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    esi: EthernetSegmentIdentifier
    ip_address: str
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., esi: _Optional[_Union[EthernetSegmentIdentifier, _Mapping]] = ..., ip_address: _Optional[str] = ...) -> None: ...

class EVPNIPPrefixRoute(_message.Message):
    __slots__ = ("rd", "esi", "ethernet_tag", "ip_prefix", "ip_prefix_len", "gw_address", "label")
    RD_FIELD_NUMBER: _ClassVar[int]
    ESI_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_TAG_FIELD_NUMBER: _ClassVar[int]
    IP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IP_PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    GW_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    esi: EthernetSegmentIdentifier
    ethernet_tag: int
    ip_prefix: str
    ip_prefix_len: int
    gw_address: str
    label: int
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., esi: _Optional[_Union[EthernetSegmentIdentifier, _Mapping]] = ..., ethernet_tag: _Optional[int] = ..., ip_prefix: _Optional[str] = ..., ip_prefix_len: _Optional[int] = ..., gw_address: _Optional[str] = ..., label: _Optional[int] = ...) -> None: ...

class EVPNIPMSIRoute(_message.Message):
    __slots__ = ("rd", "ethernet_tag", "rt")
    RD_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_TAG_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    ethernet_tag: int
    rt: _any_pb2.Any
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., ethernet_tag: _Optional[int] = ..., rt: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class SRPolicyNLRI(_message.Message):
    __slots__ = ("length", "distinguisher", "color", "endpoint")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHER_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    length: int
    distinguisher: int
    color: int
    endpoint: bytes
    def __init__(self, length: _Optional[int] = ..., distinguisher: _Optional[int] = ..., color: _Optional[int] = ..., endpoint: _Optional[bytes] = ...) -> None: ...

class LabeledVPNIPAddressPrefix(_message.Message):
    __slots__ = ("labels", "rd", "prefix_len", "prefix")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RD_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[int]
    rd: _any_pb2.Any
    prefix_len: int
    prefix: str
    def __init__(self, labels: _Optional[_Iterable[int]] = ..., rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., prefix_len: _Optional[int] = ..., prefix: _Optional[str] = ...) -> None: ...

class RouteTargetMembershipNLRI(_message.Message):
    __slots__ = ("asn", "rt")
    ASN_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    asn: int
    rt: _any_pb2.Any
    def __init__(self, asn: _Optional[int] = ..., rt: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class FlowSpecIPPrefix(_message.Message):
    __slots__ = ("type", "prefix_len", "prefix", "offset")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    type: int
    prefix_len: int
    prefix: str
    offset: int
    def __init__(self, type: _Optional[int] = ..., prefix_len: _Optional[int] = ..., prefix: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class FlowSpecMAC(_message.Message):
    __slots__ = ("type", "address")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    type: int
    address: str
    def __init__(self, type: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class FlowSpecComponentItem(_message.Message):
    __slots__ = ("op", "value")
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    op: int
    value: int
    def __init__(self, op: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class FlowSpecComponent(_message.Message):
    __slots__ = ("type", "items")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    type: int
    items: _containers.RepeatedCompositeFieldContainer[FlowSpecComponentItem]
    def __init__(self, type: _Optional[int] = ..., items: _Optional[_Iterable[_Union[FlowSpecComponentItem, _Mapping]]] = ...) -> None: ...

class FlowSpecNLRI(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, rules: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class VPNFlowSpecNLRI(_message.Message):
    __slots__ = ("rd", "rules")
    RD_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    rules: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., rules: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class OpaqueNLRI(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class LsNodeDescriptor(_message.Message):
    __slots__ = ("asn", "bgp_ls_id", "ospf_area_id", "pseudonode", "igp_router_id", "bgp_router_id", "bgp_confederation_member")
    ASN_FIELD_NUMBER: _ClassVar[int]
    BGP_LS_ID_FIELD_NUMBER: _ClassVar[int]
    OSPF_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    PSEUDONODE_FIELD_NUMBER: _ClassVar[int]
    IGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    BGP_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    BGP_CONFEDERATION_MEMBER_FIELD_NUMBER: _ClassVar[int]
    asn: int
    bgp_ls_id: int
    ospf_area_id: int
    pseudonode: bool
    igp_router_id: str
    bgp_router_id: str
    bgp_confederation_member: int
    def __init__(self, asn: _Optional[int] = ..., bgp_ls_id: _Optional[int] = ..., ospf_area_id: _Optional[int] = ..., pseudonode: bool = ..., igp_router_id: _Optional[str] = ..., bgp_router_id: _Optional[str] = ..., bgp_confederation_member: _Optional[int] = ...) -> None: ...

class LsLinkDescriptor(_message.Message):
    __slots__ = ("link_local_id", "link_remote_id", "interface_addr_ipv4", "neighbor_addr_ipv4", "interface_addr_ipv6", "neighbor_addr_ipv6")
    LINK_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_REMOTE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ADDR_IPV4_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_ADDR_IPV4_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ADDR_IPV6_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_ADDR_IPV6_FIELD_NUMBER: _ClassVar[int]
    link_local_id: int
    link_remote_id: int
    interface_addr_ipv4: str
    neighbor_addr_ipv4: str
    interface_addr_ipv6: str
    neighbor_addr_ipv6: str
    def __init__(self, link_local_id: _Optional[int] = ..., link_remote_id: _Optional[int] = ..., interface_addr_ipv4: _Optional[str] = ..., neighbor_addr_ipv4: _Optional[str] = ..., interface_addr_ipv6: _Optional[str] = ..., neighbor_addr_ipv6: _Optional[str] = ...) -> None: ...

class LsPrefixDescriptor(_message.Message):
    __slots__ = ("ip_reachability", "ospf_route_type")
    IP_REACHABILITY_FIELD_NUMBER: _ClassVar[int]
    OSPF_ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ip_reachability: _containers.RepeatedScalarFieldContainer[str]
    ospf_route_type: LsOspfRouteType
    def __init__(self, ip_reachability: _Optional[_Iterable[str]] = ..., ospf_route_type: _Optional[_Union[LsOspfRouteType, str]] = ...) -> None: ...

class LsNodeNLRI(_message.Message):
    __slots__ = ("local_node",)
    LOCAL_NODE_FIELD_NUMBER: _ClassVar[int]
    local_node: LsNodeDescriptor
    def __init__(self, local_node: _Optional[_Union[LsNodeDescriptor, _Mapping]] = ...) -> None: ...

class LsLinkNLRI(_message.Message):
    __slots__ = ("local_node", "remote_node", "link_descriptor")
    LOCAL_NODE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NODE_FIELD_NUMBER: _ClassVar[int]
    LINK_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    local_node: LsNodeDescriptor
    remote_node: LsNodeDescriptor
    link_descriptor: LsLinkDescriptor
    def __init__(self, local_node: _Optional[_Union[LsNodeDescriptor, _Mapping]] = ..., remote_node: _Optional[_Union[LsNodeDescriptor, _Mapping]] = ..., link_descriptor: _Optional[_Union[LsLinkDescriptor, _Mapping]] = ...) -> None: ...

class LsPrefixV4NLRI(_message.Message):
    __slots__ = ("local_node", "prefix_descriptor")
    LOCAL_NODE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    local_node: LsNodeDescriptor
    prefix_descriptor: LsPrefixDescriptor
    def __init__(self, local_node: _Optional[_Union[LsNodeDescriptor, _Mapping]] = ..., prefix_descriptor: _Optional[_Union[LsPrefixDescriptor, _Mapping]] = ...) -> None: ...

class LsPrefixV6NLRI(_message.Message):
    __slots__ = ("local_node", "prefix_descriptor")
    LOCAL_NODE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    local_node: LsNodeDescriptor
    prefix_descriptor: LsPrefixDescriptor
    def __init__(self, local_node: _Optional[_Union[LsNodeDescriptor, _Mapping]] = ..., prefix_descriptor: _Optional[_Union[LsPrefixDescriptor, _Mapping]] = ...) -> None: ...

class LsAddrPrefix(_message.Message):
    __slots__ = ("type", "nlri", "length", "protocol_id", "identifier")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NLRI_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    type: LsNLRIType
    nlri: _any_pb2.Any
    length: int
    protocol_id: LsProtocolID
    identifier: int
    def __init__(self, type: _Optional[_Union[LsNLRIType, str]] = ..., nlri: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., length: _Optional[int] = ..., protocol_id: _Optional[_Union[LsProtocolID, str]] = ..., identifier: _Optional[int] = ...) -> None: ...

class MUPInterworkSegmentDiscoveryRoute(_message.Message):
    __slots__ = ("rd", "prefix")
    RD_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    prefix: str
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., prefix: _Optional[str] = ...) -> None: ...

class MUPDirectSegmentDiscoveryRoute(_message.Message):
    __slots__ = ("rd", "address")
    RD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    address: str
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., address: _Optional[str] = ...) -> None: ...

class MUPType1SessionTransformedRoute(_message.Message):
    __slots__ = ("rd", "prefix_length", "prefix", "teid", "qfi", "endpoint_address_length", "endpoint_address", "source_address_length", "source_address")
    RD_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    TEID_FIELD_NUMBER: _ClassVar[int]
    QFI_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ADDRESS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ADDRESS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    prefix_length: int
    prefix: str
    teid: int
    qfi: int
    endpoint_address_length: int
    endpoint_address: str
    source_address_length: int
    source_address: str
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., prefix_length: _Optional[int] = ..., prefix: _Optional[str] = ..., teid: _Optional[int] = ..., qfi: _Optional[int] = ..., endpoint_address_length: _Optional[int] = ..., endpoint_address: _Optional[str] = ..., source_address_length: _Optional[int] = ..., source_address: _Optional[str] = ...) -> None: ...

class MUPType2SessionTransformedRoute(_message.Message):
    __slots__ = ("rd", "endpoint_address_length", "endpoint_address", "teid")
    RD_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ADDRESS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TEID_FIELD_NUMBER: _ClassVar[int]
    rd: _any_pb2.Any
    endpoint_address_length: int
    endpoint_address: str
    teid: int
    def __init__(self, rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., endpoint_address_length: _Optional[int] = ..., endpoint_address: _Optional[str] = ..., teid: _Optional[int] = ...) -> None: ...

class MpReachNLRIAttribute(_message.Message):
    __slots__ = ("family", "next_hops", "nlris")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOPS_FIELD_NUMBER: _ClassVar[int]
    NLRIS_FIELD_NUMBER: _ClassVar[int]
    family: _gobgp_pb2.Family
    next_hops: _containers.RepeatedScalarFieldContainer[str]
    nlris: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ..., next_hops: _Optional[_Iterable[str]] = ..., nlris: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class MpUnreachNLRIAttribute(_message.Message):
    __slots__ = ("family", "nlris")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    NLRIS_FIELD_NUMBER: _ClassVar[int]
    family: _gobgp_pb2.Family
    nlris: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ..., nlris: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class TwoOctetAsSpecificExtended(_message.Message):
    __slots__ = ("is_transitive", "sub_type", "asn", "local_admin")
    IS_TRANSITIVE_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    is_transitive: bool
    sub_type: int
    asn: int
    local_admin: int
    def __init__(self, is_transitive: bool = ..., sub_type: _Optional[int] = ..., asn: _Optional[int] = ..., local_admin: _Optional[int] = ...) -> None: ...

class IPv4AddressSpecificExtended(_message.Message):
    __slots__ = ("is_transitive", "sub_type", "address", "local_admin")
    IS_TRANSITIVE_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    is_transitive: bool
    sub_type: int
    address: str
    local_admin: int
    def __init__(self, is_transitive: bool = ..., sub_type: _Optional[int] = ..., address: _Optional[str] = ..., local_admin: _Optional[int] = ...) -> None: ...

class FourOctetAsSpecificExtended(_message.Message):
    __slots__ = ("is_transitive", "sub_type", "asn", "local_admin")
    IS_TRANSITIVE_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    is_transitive: bool
    sub_type: int
    asn: int
    local_admin: int
    def __init__(self, is_transitive: bool = ..., sub_type: _Optional[int] = ..., asn: _Optional[int] = ..., local_admin: _Optional[int] = ...) -> None: ...

class LinkBandwidthExtended(_message.Message):
    __slots__ = ("asn", "bandwidth")
    ASN_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    asn: int
    bandwidth: float
    def __init__(self, asn: _Optional[int] = ..., bandwidth: _Optional[float] = ...) -> None: ...

class ValidationExtended(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: int
    def __init__(self, state: _Optional[int] = ...) -> None: ...

class ColorExtended(_message.Message):
    __slots__ = ("color",)
    COLOR_FIELD_NUMBER: _ClassVar[int]
    color: int
    def __init__(self, color: _Optional[int] = ...) -> None: ...

class EncapExtended(_message.Message):
    __slots__ = ("tunnel_type",)
    TUNNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    tunnel_type: int
    def __init__(self, tunnel_type: _Optional[int] = ...) -> None: ...

class DefaultGatewayExtended(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OpaqueExtended(_message.Message):
    __slots__ = ("is_transitive", "value")
    IS_TRANSITIVE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    is_transitive: bool
    value: bytes
    def __init__(self, is_transitive: bool = ..., value: _Optional[bytes] = ...) -> None: ...

class ESILabelExtended(_message.Message):
    __slots__ = ("is_single_active", "label")
    IS_SINGLE_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    is_single_active: bool
    label: int
    def __init__(self, is_single_active: bool = ..., label: _Optional[int] = ...) -> None: ...

class ESImportRouteTarget(_message.Message):
    __slots__ = ("es_import",)
    ES_IMPORT_FIELD_NUMBER: _ClassVar[int]
    es_import: str
    def __init__(self, es_import: _Optional[str] = ...) -> None: ...

class MacMobilityExtended(_message.Message):
    __slots__ = ("is_sticky", "sequence_num")
    IS_STICKY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
    is_sticky: bool
    sequence_num: int
    def __init__(self, is_sticky: bool = ..., sequence_num: _Optional[int] = ...) -> None: ...

class RouterMacExtended(_message.Message):
    __slots__ = ("mac",)
    MAC_FIELD_NUMBER: _ClassVar[int]
    mac: str
    def __init__(self, mac: _Optional[str] = ...) -> None: ...

class TrafficRateExtended(_message.Message):
    __slots__ = ("asn", "rate")
    ASN_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    asn: int
    rate: float
    def __init__(self, asn: _Optional[int] = ..., rate: _Optional[float] = ...) -> None: ...

class TrafficActionExtended(_message.Message):
    __slots__ = ("terminal", "sample")
    TERMINAL_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    terminal: bool
    sample: bool
    def __init__(self, terminal: bool = ..., sample: bool = ...) -> None: ...

class RedirectTwoOctetAsSpecificExtended(_message.Message):
    __slots__ = ("asn", "local_admin")
    ASN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    asn: int
    local_admin: int
    def __init__(self, asn: _Optional[int] = ..., local_admin: _Optional[int] = ...) -> None: ...

class RedirectIPv4AddressSpecificExtended(_message.Message):
    __slots__ = ("address", "local_admin")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    address: str
    local_admin: int
    def __init__(self, address: _Optional[str] = ..., local_admin: _Optional[int] = ...) -> None: ...

class RedirectFourOctetAsSpecificExtended(_message.Message):
    __slots__ = ("asn", "local_admin")
    ASN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    asn: int
    local_admin: int
    def __init__(self, asn: _Optional[int] = ..., local_admin: _Optional[int] = ...) -> None: ...

class TrafficRemarkExtended(_message.Message):
    __slots__ = ("dscp",)
    DSCP_FIELD_NUMBER: _ClassVar[int]
    dscp: int
    def __init__(self, dscp: _Optional[int] = ...) -> None: ...

class MUPExtended(_message.Message):
    __slots__ = ("sub_type", "segment_id2", "segment_id4")
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID2_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID4_FIELD_NUMBER: _ClassVar[int]
    sub_type: int
    segment_id2: int
    segment_id4: int
    def __init__(self, sub_type: _Optional[int] = ..., segment_id2: _Optional[int] = ..., segment_id4: _Optional[int] = ...) -> None: ...

class VPLSExtended(_message.Message):
    __slots__ = ("control_flags", "mtu")
    CONTROL_FLAGS_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    control_flags: int
    mtu: int
    def __init__(self, control_flags: _Optional[int] = ..., mtu: _Optional[int] = ...) -> None: ...

class UnknownExtended(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: bytes
    def __init__(self, type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class ExtendedCommunitiesAttribute(_message.Message):
    __slots__ = ("communities",)
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    communities: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, communities: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class As4PathAttribute(_message.Message):
    __slots__ = ("segments",)
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[AsSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[AsSegment, _Mapping]]] = ...) -> None: ...

class As4AggregatorAttribute(_message.Message):
    __slots__ = ("asn", "address")
    ASN_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    asn: int
    address: str
    def __init__(self, asn: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class PmsiTunnelAttribute(_message.Message):
    __slots__ = ("flags", "type", "label", "id")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    flags: int
    type: int
    label: int
    id: bytes
    def __init__(self, flags: _Optional[int] = ..., type: _Optional[int] = ..., label: _Optional[int] = ..., id: _Optional[bytes] = ...) -> None: ...

class TunnelEncapSubTLVEncapsulation(_message.Message):
    __slots__ = ("key", "cookie")
    KEY_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    key: int
    cookie: bytes
    def __init__(self, key: _Optional[int] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class TunnelEncapSubTLVProtocol(_message.Message):
    __slots__ = ("protocol",)
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    protocol: int
    def __init__(self, protocol: _Optional[int] = ...) -> None: ...

class TunnelEncapSubTLVColor(_message.Message):
    __slots__ = ("color",)
    COLOR_FIELD_NUMBER: _ClassVar[int]
    color: int
    def __init__(self, color: _Optional[int] = ...) -> None: ...

class TunnelEncapSubTLVSRPreference(_message.Message):
    __slots__ = ("flags", "preference")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    flags: int
    preference: int
    def __init__(self, flags: _Optional[int] = ..., preference: _Optional[int] = ...) -> None: ...

class TunnelEncapSubTLVSRCandidatePathName(_message.Message):
    __slots__ = ("candidate_path_name",)
    CANDIDATE_PATH_NAME_FIELD_NUMBER: _ClassVar[int]
    candidate_path_name: str
    def __init__(self, candidate_path_name: _Optional[str] = ...) -> None: ...

class TunnelEncapSubTLVSRPriority(_message.Message):
    __slots__ = ("priority",)
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    priority: int
    def __init__(self, priority: _Optional[int] = ...) -> None: ...

class TunnelEncapSubTLVSRBindingSID(_message.Message):
    __slots__ = ("bsid",)
    BSID_FIELD_NUMBER: _ClassVar[int]
    bsid: _any_pb2.Any
    def __init__(self, bsid: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class SRBindingSID(_message.Message):
    __slots__ = ("s_flag", "i_flag", "sid")
    S_FLAG_FIELD_NUMBER: _ClassVar[int]
    I_FLAG_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    s_flag: bool
    i_flag: bool
    sid: bytes
    def __init__(self, s_flag: bool = ..., i_flag: bool = ..., sid: _Optional[bytes] = ...) -> None: ...

class SRv6EndPointBehavior(_message.Message):
    __slots__ = ("behavior", "block_len", "node_len", "func_len", "arg_len")
    BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    BLOCK_LEN_FIELD_NUMBER: _ClassVar[int]
    NODE_LEN_FIELD_NUMBER: _ClassVar[int]
    FUNC_LEN_FIELD_NUMBER: _ClassVar[int]
    ARG_LEN_FIELD_NUMBER: _ClassVar[int]
    behavior: SRv6Behavior
    block_len: int
    node_len: int
    func_len: int
    arg_len: int
    def __init__(self, behavior: _Optional[_Union[SRv6Behavior, str]] = ..., block_len: _Optional[int] = ..., node_len: _Optional[int] = ..., func_len: _Optional[int] = ..., arg_len: _Optional[int] = ...) -> None: ...

class SRv6BindingSID(_message.Message):
    __slots__ = ("s_flag", "i_flag", "b_flag", "sid", "endpoint_behavior_structure")
    S_FLAG_FIELD_NUMBER: _ClassVar[int]
    I_FLAG_FIELD_NUMBER: _ClassVar[int]
    B_FLAG_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_BEHAVIOR_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    s_flag: bool
    i_flag: bool
    b_flag: bool
    sid: bytes
    endpoint_behavior_structure: SRv6EndPointBehavior
    def __init__(self, s_flag: bool = ..., i_flag: bool = ..., b_flag: bool = ..., sid: _Optional[bytes] = ..., endpoint_behavior_structure: _Optional[_Union[SRv6EndPointBehavior, _Mapping]] = ...) -> None: ...

class TunnelEncapSubTLVSRENLP(_message.Message):
    __slots__ = ("flags", "enlp")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ENLP_FIELD_NUMBER: _ClassVar[int]
    flags: int
    enlp: ENLPType
    def __init__(self, flags: _Optional[int] = ..., enlp: _Optional[_Union[ENLPType, str]] = ...) -> None: ...

class SRWeight(_message.Message):
    __slots__ = ("flags", "weight")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    flags: int
    weight: int
    def __init__(self, flags: _Optional[int] = ..., weight: _Optional[int] = ...) -> None: ...

class SegmentFlags(_message.Message):
    __slots__ = ("v_flag", "a_flag", "s_flag", "b_flag")
    V_FLAG_FIELD_NUMBER: _ClassVar[int]
    A_FLAG_FIELD_NUMBER: _ClassVar[int]
    S_FLAG_FIELD_NUMBER: _ClassVar[int]
    B_FLAG_FIELD_NUMBER: _ClassVar[int]
    v_flag: bool
    a_flag: bool
    s_flag: bool
    b_flag: bool
    def __init__(self, v_flag: bool = ..., a_flag: bool = ..., s_flag: bool = ..., b_flag: bool = ...) -> None: ...

class SegmentTypeA(_message.Message):
    __slots__ = ("flags", "label")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    flags: SegmentFlags
    label: int
    def __init__(self, flags: _Optional[_Union[SegmentFlags, _Mapping]] = ..., label: _Optional[int] = ...) -> None: ...

class SegmentTypeB(_message.Message):
    __slots__ = ("flags", "sid", "endpoint_behavior_structure")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_BEHAVIOR_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    flags: SegmentFlags
    sid: bytes
    endpoint_behavior_structure: SRv6EndPointBehavior
    def __init__(self, flags: _Optional[_Union[SegmentFlags, _Mapping]] = ..., sid: _Optional[bytes] = ..., endpoint_behavior_structure: _Optional[_Union[SRv6EndPointBehavior, _Mapping]] = ...) -> None: ...

class TunnelEncapSubTLVSRSegmentList(_message.Message):
    __slots__ = ("weight", "segments")
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    weight: SRWeight
    segments: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, weight: _Optional[_Union[SRWeight, _Mapping]] = ..., segments: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class TunnelEncapSubTLVEgressEndpoint(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class TunnelEncapSubTLVUDPDestPort(_message.Message):
    __slots__ = ("port",)
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: int
    def __init__(self, port: _Optional[int] = ...) -> None: ...

class TunnelEncapSubTLVUnknown(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: bytes
    def __init__(self, type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class TunnelEncapTLV(_message.Message):
    __slots__ = ("type", "tlvs")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TLVS_FIELD_NUMBER: _ClassVar[int]
    type: int
    tlvs: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, type: _Optional[int] = ..., tlvs: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class TunnelEncapAttribute(_message.Message):
    __slots__ = ("tlvs",)
    TLVS_FIELD_NUMBER: _ClassVar[int]
    tlvs: _containers.RepeatedCompositeFieldContainer[TunnelEncapTLV]
    def __init__(self, tlvs: _Optional[_Iterable[_Union[TunnelEncapTLV, _Mapping]]] = ...) -> None: ...

class IPv6AddressSpecificExtended(_message.Message):
    __slots__ = ("is_transitive", "sub_type", "address", "local_admin")
    IS_TRANSITIVE_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    is_transitive: bool
    sub_type: int
    address: str
    local_admin: int
    def __init__(self, is_transitive: bool = ..., sub_type: _Optional[int] = ..., address: _Optional[str] = ..., local_admin: _Optional[int] = ...) -> None: ...

class RedirectIPv6AddressSpecificExtended(_message.Message):
    __slots__ = ("address", "local_admin")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    address: str
    local_admin: int
    def __init__(self, address: _Optional[str] = ..., local_admin: _Optional[int] = ...) -> None: ...

class IP6ExtendedCommunitiesAttribute(_message.Message):
    __slots__ = ("communities",)
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    communities: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, communities: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class AigpTLVIGPMetric(_message.Message):
    __slots__ = ("metric",)
    METRIC_FIELD_NUMBER: _ClassVar[int]
    metric: int
    def __init__(self, metric: _Optional[int] = ...) -> None: ...

class AigpTLVUnknown(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: bytes
    def __init__(self, type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class AigpAttribute(_message.Message):
    __slots__ = ("tlvs",)
    TLVS_FIELD_NUMBER: _ClassVar[int]
    tlvs: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, tlvs: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class LargeCommunity(_message.Message):
    __slots__ = ("global_admin", "local_data1", "local_data2")
    GLOBAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA1_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DATA2_FIELD_NUMBER: _ClassVar[int]
    global_admin: int
    local_data1: int
    local_data2: int
    def __init__(self, global_admin: _Optional[int] = ..., local_data1: _Optional[int] = ..., local_data2: _Optional[int] = ...) -> None: ...

class LargeCommunitiesAttribute(_message.Message):
    __slots__ = ("communities",)
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    communities: _containers.RepeatedCompositeFieldContainer[LargeCommunity]
    def __init__(self, communities: _Optional[_Iterable[_Union[LargeCommunity, _Mapping]]] = ...) -> None: ...

class LsNodeFlags(_message.Message):
    __slots__ = ("overload", "attached", "external", "abr", "router", "v6")
    OVERLOAD_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    ABR_FIELD_NUMBER: _ClassVar[int]
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    overload: bool
    attached: bool
    external: bool
    abr: bool
    router: bool
    v6: bool
    def __init__(self, overload: bool = ..., attached: bool = ..., external: bool = ..., abr: bool = ..., router: bool = ..., v6: bool = ...) -> None: ...

class LsIGPFlags(_message.Message):
    __slots__ = ("down", "no_unicast", "local_address", "propagate_nssa")
    DOWN_FIELD_NUMBER: _ClassVar[int]
    NO_UNICAST_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROPAGATE_NSSA_FIELD_NUMBER: _ClassVar[int]
    down: bool
    no_unicast: bool
    local_address: bool
    propagate_nssa: bool
    def __init__(self, down: bool = ..., no_unicast: bool = ..., local_address: bool = ..., propagate_nssa: bool = ...) -> None: ...

class LsSrRange(_message.Message):
    __slots__ = ("begin", "end")
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    begin: int
    end: int
    def __init__(self, begin: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class LsSrCapabilities(_message.Message):
    __slots__ = ("ipv4_supported", "ipv6_supported", "ranges")
    IPV4_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IPV6_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ipv4_supported: bool
    ipv6_supported: bool
    ranges: _containers.RepeatedCompositeFieldContainer[LsSrRange]
    def __init__(self, ipv4_supported: bool = ..., ipv6_supported: bool = ..., ranges: _Optional[_Iterable[_Union[LsSrRange, _Mapping]]] = ...) -> None: ...

class LsSrLocalBlock(_message.Message):
    __slots__ = ("ranges",)
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[LsSrRange]
    def __init__(self, ranges: _Optional[_Iterable[_Union[LsSrRange, _Mapping]]] = ...) -> None: ...

class LsAttributeNode(_message.Message):
    __slots__ = ("name", "flags", "local_router_id", "local_router_id_v6", "isis_area", "opaque", "sr_capabilities", "sr_algorithms", "sr_local_block")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROUTER_ID_V6_FIELD_NUMBER: _ClassVar[int]
    ISIS_AREA_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_FIELD_NUMBER: _ClassVar[int]
    SR_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SR_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    SR_LOCAL_BLOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    flags: LsNodeFlags
    local_router_id: str
    local_router_id_v6: str
    isis_area: bytes
    opaque: bytes
    sr_capabilities: LsSrCapabilities
    sr_algorithms: bytes
    sr_local_block: LsSrLocalBlock
    def __init__(self, name: _Optional[str] = ..., flags: _Optional[_Union[LsNodeFlags, _Mapping]] = ..., local_router_id: _Optional[str] = ..., local_router_id_v6: _Optional[str] = ..., isis_area: _Optional[bytes] = ..., opaque: _Optional[bytes] = ..., sr_capabilities: _Optional[_Union[LsSrCapabilities, _Mapping]] = ..., sr_algorithms: _Optional[bytes] = ..., sr_local_block: _Optional[_Union[LsSrLocalBlock, _Mapping]] = ...) -> None: ...

class LsAttributeLink(_message.Message):
    __slots__ = ("name", "local_router_id", "local_router_id_v6", "remote_router_id", "remote_router_id_v6", "admin_group", "default_te_metric", "igp_metric", "opaque", "bandwidth", "reservable_bandwidth", "unreserved_bandwidth", "sr_adjacency_sid", "srlgs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROUTER_ID_V6_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ROUTER_ID_V6_FIELD_NUMBER: _ClassVar[int]
    ADMIN_GROUP_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TE_METRIC_FIELD_NUMBER: _ClassVar[int]
    IGP_METRIC_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    RESERVABLE_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    UNRESERVED_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    SR_ADJACENCY_SID_FIELD_NUMBER: _ClassVar[int]
    SRLGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    local_router_id: str
    local_router_id_v6: str
    remote_router_id: str
    remote_router_id_v6: str
    admin_group: int
    default_te_metric: int
    igp_metric: int
    opaque: bytes
    bandwidth: float
    reservable_bandwidth: float
    unreserved_bandwidth: _containers.RepeatedScalarFieldContainer[float]
    sr_adjacency_sid: int
    srlgs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., local_router_id: _Optional[str] = ..., local_router_id_v6: _Optional[str] = ..., remote_router_id: _Optional[str] = ..., remote_router_id_v6: _Optional[str] = ..., admin_group: _Optional[int] = ..., default_te_metric: _Optional[int] = ..., igp_metric: _Optional[int] = ..., opaque: _Optional[bytes] = ..., bandwidth: _Optional[float] = ..., reservable_bandwidth: _Optional[float] = ..., unreserved_bandwidth: _Optional[_Iterable[float]] = ..., sr_adjacency_sid: _Optional[int] = ..., srlgs: _Optional[_Iterable[int]] = ...) -> None: ...

class LsAttributePrefix(_message.Message):
    __slots__ = ("igp_flags", "opaque", "sr_prefix_sid")
    IGP_FLAGS_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_FIELD_NUMBER: _ClassVar[int]
    SR_PREFIX_SID_FIELD_NUMBER: _ClassVar[int]
    igp_flags: LsIGPFlags
    opaque: bytes
    sr_prefix_sid: int
    def __init__(self, igp_flags: _Optional[_Union[LsIGPFlags, _Mapping]] = ..., opaque: _Optional[bytes] = ..., sr_prefix_sid: _Optional[int] = ...) -> None: ...

class LsBgpPeerSegmentSIDFlags(_message.Message):
    __slots__ = ("value", "local", "backup", "persistent")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    value: bool
    local: bool
    backup: bool
    persistent: bool
    def __init__(self, value: bool = ..., local: bool = ..., backup: bool = ..., persistent: bool = ...) -> None: ...

class LsBgpPeerSegmentSID(_message.Message):
    __slots__ = ("flags", "weight", "sid")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    flags: LsBgpPeerSegmentSIDFlags
    weight: int
    sid: int
    def __init__(self, flags: _Optional[_Union[LsBgpPeerSegmentSIDFlags, _Mapping]] = ..., weight: _Optional[int] = ..., sid: _Optional[int] = ...) -> None: ...

class LsAttributeBgpPeerSegment(_message.Message):
    __slots__ = ("bgp_peer_node_sid", "bgp_peer_adjacency_sid", "bgp_peer_set_sid")
    BGP_PEER_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    BGP_PEER_ADJACENCY_SID_FIELD_NUMBER: _ClassVar[int]
    BGP_PEER_SET_SID_FIELD_NUMBER: _ClassVar[int]
    bgp_peer_node_sid: LsBgpPeerSegmentSID
    bgp_peer_adjacency_sid: LsBgpPeerSegmentSID
    bgp_peer_set_sid: LsBgpPeerSegmentSID
    def __init__(self, bgp_peer_node_sid: _Optional[_Union[LsBgpPeerSegmentSID, _Mapping]] = ..., bgp_peer_adjacency_sid: _Optional[_Union[LsBgpPeerSegmentSID, _Mapping]] = ..., bgp_peer_set_sid: _Optional[_Union[LsBgpPeerSegmentSID, _Mapping]] = ...) -> None: ...

class LsAttribute(_message.Message):
    __slots__ = ("node", "link", "prefix", "bgp_peer_segment")
    NODE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    BGP_PEER_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    node: LsAttributeNode
    link: LsAttributeLink
    prefix: LsAttributePrefix
    bgp_peer_segment: LsAttributeBgpPeerSegment
    def __init__(self, node: _Optional[_Union[LsAttributeNode, _Mapping]] = ..., link: _Optional[_Union[LsAttributeLink, _Mapping]] = ..., prefix: _Optional[_Union[LsAttributePrefix, _Mapping]] = ..., bgp_peer_segment: _Optional[_Union[LsAttributeBgpPeerSegment, _Mapping]] = ...) -> None: ...

class UnknownAttribute(_message.Message):
    __slots__ = ("flags", "type", "value")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    flags: int
    type: int
    value: bytes
    def __init__(self, flags: _Optional[int] = ..., type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class SRv6StructureSubSubTLV(_message.Message):
    __slots__ = ("locator_block_length", "locator_node_length", "function_length", "argument_length", "transposition_length", "transposition_offset")
    LOCATOR_BLOCK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LOCATOR_NODE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSITION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSITION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    locator_block_length: int
    locator_node_length: int
    function_length: int
    argument_length: int
    transposition_length: int
    transposition_offset: int
    def __init__(self, locator_block_length: _Optional[int] = ..., locator_node_length: _Optional[int] = ..., function_length: _Optional[int] = ..., argument_length: _Optional[int] = ..., transposition_length: _Optional[int] = ..., transposition_offset: _Optional[int] = ...) -> None: ...

class SRv6SIDFlags(_message.Message):
    __slots__ = ("flag_1",)
    FLAG_1_FIELD_NUMBER: _ClassVar[int]
    flag_1: bool
    def __init__(self, flag_1: bool = ...) -> None: ...

class SRv6TLV(_message.Message):
    __slots__ = ("tlv",)
    TLV_FIELD_NUMBER: _ClassVar[int]
    tlv: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, tlv: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class SRv6InformationSubTLV(_message.Message):
    __slots__ = ("sid", "flags", "endpoint_behavior", "sub_sub_tlvs")
    class SubSubTlvsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SRv6TLV
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SRv6TLV, _Mapping]] = ...) -> None: ...
    SID_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    SUB_SUB_TLVS_FIELD_NUMBER: _ClassVar[int]
    sid: bytes
    flags: SRv6SIDFlags
    endpoint_behavior: int
    sub_sub_tlvs: _containers.MessageMap[int, SRv6TLV]
    def __init__(self, sid: _Optional[bytes] = ..., flags: _Optional[_Union[SRv6SIDFlags, _Mapping]] = ..., endpoint_behavior: _Optional[int] = ..., sub_sub_tlvs: _Optional[_Mapping[int, SRv6TLV]] = ...) -> None: ...

class SRv6L3ServiceTLV(_message.Message):
    __slots__ = ("sub_tlvs",)
    class SubTlvsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SRv6TLV
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SRv6TLV, _Mapping]] = ...) -> None: ...
    SUB_TLVS_FIELD_NUMBER: _ClassVar[int]
    sub_tlvs: _containers.MessageMap[int, SRv6TLV]
    def __init__(self, sub_tlvs: _Optional[_Mapping[int, SRv6TLV]] = ...) -> None: ...

class SRv6L2ServiceTLV(_message.Message):
    __slots__ = ("sub_tlvs",)
    class SubTlvsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SRv6TLV
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SRv6TLV, _Mapping]] = ...) -> None: ...
    SUB_TLVS_FIELD_NUMBER: _ClassVar[int]
    sub_tlvs: _containers.MessageMap[int, SRv6TLV]
    def __init__(self, sub_tlvs: _Optional[_Mapping[int, SRv6TLV]] = ...) -> None: ...

class PrefixSID(_message.Message):
    __slots__ = ("tlvs",)
    TLVS_FIELD_NUMBER: _ClassVar[int]
    tlvs: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, tlvs: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
