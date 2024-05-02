from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GLOBAL: _ClassVar[TableType]
    LOCAL: _ClassVar[TableType]
    ADJ_IN: _ClassVar[TableType]
    ADJ_OUT: _ClassVar[TableType]
    VRF: _ClassVar[TableType]

class PeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERNAL: _ClassVar[PeerType]
    EXTERNAL: _ClassVar[PeerType]

class RemovePrivate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REMOVE_NONE: _ClassVar[RemovePrivate]
    REMOVE_ALL: _ClassVar[RemovePrivate]
    REPLACE: _ClassVar[RemovePrivate]

class DefinedType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PREFIX: _ClassVar[DefinedType]
    NEIGHBOR: _ClassVar[DefinedType]
    TAG: _ClassVar[DefinedType]
    AS_PATH: _ClassVar[DefinedType]
    COMMUNITY: _ClassVar[DefinedType]
    EXT_COMMUNITY: _ClassVar[DefinedType]
    LARGE_COMMUNITY: _ClassVar[DefinedType]
    NEXT_HOP: _ClassVar[DefinedType]

class RouteAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[RouteAction]
    ACCEPT: _ClassVar[RouteAction]
    REJECT: _ClassVar[RouteAction]

class PolicyDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[PolicyDirection]
    IMPORT: _ClassVar[PolicyDirection]
    EXPORT: _ClassVar[PolicyDirection]
GLOBAL: TableType
LOCAL: TableType
ADJ_IN: TableType
ADJ_OUT: TableType
VRF: TableType
INTERNAL: PeerType
EXTERNAL: PeerType
REMOVE_NONE: RemovePrivate
REMOVE_ALL: RemovePrivate
REPLACE: RemovePrivate
PREFIX: DefinedType
NEIGHBOR: DefinedType
TAG: DefinedType
AS_PATH: DefinedType
COMMUNITY: DefinedType
EXT_COMMUNITY: DefinedType
LARGE_COMMUNITY: DefinedType
NEXT_HOP: DefinedType
NONE: RouteAction
ACCEPT: RouteAction
REJECT: RouteAction
UNKNOWN: PolicyDirection
IMPORT: PolicyDirection
EXPORT: PolicyDirection

class StartBgpRequest(_message.Message):
    __slots__ = ()
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class StopBgpRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBgpRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBgpResponse(_message.Message):
    __slots__ = ()
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class WatchEventRequest(_message.Message):
    __slots__ = ("peer", "table")
    class Peer(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Table(_message.Message):
        __slots__ = ("filters",)
        class Filter(_message.Message):
            __slots__ = ("type", "init", "peer_address", "peer_group")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                BEST: _ClassVar[WatchEventRequest.Table.Filter.Type]
                ADJIN: _ClassVar[WatchEventRequest.Table.Filter.Type]
                POST_POLICY: _ClassVar[WatchEventRequest.Table.Filter.Type]
                EOR: _ClassVar[WatchEventRequest.Table.Filter.Type]
            BEST: WatchEventRequest.Table.Filter.Type
            ADJIN: WatchEventRequest.Table.Filter.Type
            POST_POLICY: WatchEventRequest.Table.Filter.Type
            EOR: WatchEventRequest.Table.Filter.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            INIT_FIELD_NUMBER: _ClassVar[int]
            PEER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
            type: WatchEventRequest.Table.Filter.Type
            init: bool
            peer_address: str
            peer_group: str
            def __init__(self, type: _Optional[_Union[WatchEventRequest.Table.Filter.Type, str]] = ..., init: bool = ..., peer_address: _Optional[str] = ..., peer_group: _Optional[str] = ...) -> None: ...
        FILTERS_FIELD_NUMBER: _ClassVar[int]
        filters: _containers.RepeatedCompositeFieldContainer[WatchEventRequest.Table.Filter]
        def __init__(self, filters: _Optional[_Iterable[_Union[WatchEventRequest.Table.Filter, _Mapping]]] = ...) -> None: ...
    PEER_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    peer: WatchEventRequest.Peer
    table: WatchEventRequest.Table
    def __init__(self, peer: _Optional[_Union[WatchEventRequest.Peer, _Mapping]] = ..., table: _Optional[_Union[WatchEventRequest.Table, _Mapping]] = ...) -> None: ...

class WatchEventResponse(_message.Message):
    __slots__ = ("peer", "table")
    class PeerEvent(_message.Message):
        __slots__ = ("type", "peer")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[WatchEventResponse.PeerEvent.Type]
            INIT: _ClassVar[WatchEventResponse.PeerEvent.Type]
            END_OF_INIT: _ClassVar[WatchEventResponse.PeerEvent.Type]
            STATE: _ClassVar[WatchEventResponse.PeerEvent.Type]
        UNKNOWN: WatchEventResponse.PeerEvent.Type
        INIT: WatchEventResponse.PeerEvent.Type
        END_OF_INIT: WatchEventResponse.PeerEvent.Type
        STATE: WatchEventResponse.PeerEvent.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PEER_FIELD_NUMBER: _ClassVar[int]
        type: WatchEventResponse.PeerEvent.Type
        peer: Peer
        def __init__(self, type: _Optional[_Union[WatchEventResponse.PeerEvent.Type, str]] = ..., peer: _Optional[_Union[Peer, _Mapping]] = ...) -> None: ...
    class TableEvent(_message.Message):
        __slots__ = ("paths",)
        PATHS_FIELD_NUMBER: _ClassVar[int]
        paths: _containers.RepeatedCompositeFieldContainer[Path]
        def __init__(self, paths: _Optional[_Iterable[_Union[Path, _Mapping]]] = ...) -> None: ...
    PEER_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    peer: WatchEventResponse.PeerEvent
    table: WatchEventResponse.TableEvent
    def __init__(self, peer: _Optional[_Union[WatchEventResponse.PeerEvent, _Mapping]] = ..., table: _Optional[_Union[WatchEventResponse.TableEvent, _Mapping]] = ...) -> None: ...

class AddPeerRequest(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: Peer
    def __init__(self, peer: _Optional[_Union[Peer, _Mapping]] = ...) -> None: ...

class DeletePeerRequest(_message.Message):
    __slots__ = ("address", "interface")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    address: str
    interface: str
    def __init__(self, address: _Optional[str] = ..., interface: _Optional[str] = ...) -> None: ...

class ListPeerRequest(_message.Message):
    __slots__ = ("address", "enableAdvertised")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLEADVERTISED_FIELD_NUMBER: _ClassVar[int]
    address: str
    enableAdvertised: bool
    def __init__(self, address: _Optional[str] = ..., enableAdvertised: bool = ...) -> None: ...

class ListPeerResponse(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: Peer
    def __init__(self, peer: _Optional[_Union[Peer, _Mapping]] = ...) -> None: ...

class UpdatePeerRequest(_message.Message):
    __slots__ = ("peer", "do_soft_reset_in")
    PEER_FIELD_NUMBER: _ClassVar[int]
    DO_SOFT_RESET_IN_FIELD_NUMBER: _ClassVar[int]
    peer: Peer
    do_soft_reset_in: bool
    def __init__(self, peer: _Optional[_Union[Peer, _Mapping]] = ..., do_soft_reset_in: bool = ...) -> None: ...

class UpdatePeerResponse(_message.Message):
    __slots__ = ("needs_soft_reset_in",)
    NEEDS_SOFT_RESET_IN_FIELD_NUMBER: _ClassVar[int]
    needs_soft_reset_in: bool
    def __init__(self, needs_soft_reset_in: bool = ...) -> None: ...

class ResetPeerRequest(_message.Message):
    __slots__ = ("address", "communication", "soft", "direction")
    class SoftResetDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IN: _ClassVar[ResetPeerRequest.SoftResetDirection]
        OUT: _ClassVar[ResetPeerRequest.SoftResetDirection]
        BOTH: _ClassVar[ResetPeerRequest.SoftResetDirection]
    IN: ResetPeerRequest.SoftResetDirection
    OUT: ResetPeerRequest.SoftResetDirection
    BOTH: ResetPeerRequest.SoftResetDirection
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    SOFT_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    address: str
    communication: str
    soft: bool
    direction: ResetPeerRequest.SoftResetDirection
    def __init__(self, address: _Optional[str] = ..., communication: _Optional[str] = ..., soft: bool = ..., direction: _Optional[_Union[ResetPeerRequest.SoftResetDirection, str]] = ...) -> None: ...

class ShutdownPeerRequest(_message.Message):
    __slots__ = ("address", "communication")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    communication: str
    def __init__(self, address: _Optional[str] = ..., communication: _Optional[str] = ...) -> None: ...

class EnablePeerRequest(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class DisablePeerRequest(_message.Message):
    __slots__ = ("address", "communication")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    address: str
    communication: str
    def __init__(self, address: _Optional[str] = ..., communication: _Optional[str] = ...) -> None: ...

class AddPeerGroupRequest(_message.Message):
    __slots__ = ("peer_group",)
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    peer_group: PeerGroup
    def __init__(self, peer_group: _Optional[_Union[PeerGroup, _Mapping]] = ...) -> None: ...

class DeletePeerGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdatePeerGroupRequest(_message.Message):
    __slots__ = ("peer_group", "do_soft_reset_in")
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DO_SOFT_RESET_IN_FIELD_NUMBER: _ClassVar[int]
    peer_group: PeerGroup
    do_soft_reset_in: bool
    def __init__(self, peer_group: _Optional[_Union[PeerGroup, _Mapping]] = ..., do_soft_reset_in: bool = ...) -> None: ...

class UpdatePeerGroupResponse(_message.Message):
    __slots__ = ("needs_soft_reset_in",)
    NEEDS_SOFT_RESET_IN_FIELD_NUMBER: _ClassVar[int]
    needs_soft_reset_in: bool
    def __init__(self, needs_soft_reset_in: bool = ...) -> None: ...

class ListPeerGroupRequest(_message.Message):
    __slots__ = ("peer_group_name",)
    PEER_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    peer_group_name: str
    def __init__(self, peer_group_name: _Optional[str] = ...) -> None: ...

class ListPeerGroupResponse(_message.Message):
    __slots__ = ("peer_group",)
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    peer_group: PeerGroup
    def __init__(self, peer_group: _Optional[_Union[PeerGroup, _Mapping]] = ...) -> None: ...

class AddDynamicNeighborRequest(_message.Message):
    __slots__ = ("dynamic_neighbor",)
    DYNAMIC_NEIGHBOR_FIELD_NUMBER: _ClassVar[int]
    dynamic_neighbor: DynamicNeighbor
    def __init__(self, dynamic_neighbor: _Optional[_Union[DynamicNeighbor, _Mapping]] = ...) -> None: ...

class DeleteDynamicNeighborRequest(_message.Message):
    __slots__ = ("prefix", "peer_group")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    peer_group: str
    def __init__(self, prefix: _Optional[str] = ..., peer_group: _Optional[str] = ...) -> None: ...

class ListDynamicNeighborRequest(_message.Message):
    __slots__ = ("peer_group",)
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    peer_group: str
    def __init__(self, peer_group: _Optional[str] = ...) -> None: ...

class ListDynamicNeighborResponse(_message.Message):
    __slots__ = ("dynamic_neighbor",)
    DYNAMIC_NEIGHBOR_FIELD_NUMBER: _ClassVar[int]
    dynamic_neighbor: DynamicNeighbor
    def __init__(self, dynamic_neighbor: _Optional[_Union[DynamicNeighbor, _Mapping]] = ...) -> None: ...

class AddPathRequest(_message.Message):
    __slots__ = ("table_type", "vrf_id", "path")
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VRF_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    table_type: TableType
    vrf_id: str
    path: Path
    def __init__(self, table_type: _Optional[_Union[TableType, str]] = ..., vrf_id: _Optional[str] = ..., path: _Optional[_Union[Path, _Mapping]] = ...) -> None: ...

class AddPathResponse(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: bytes
    def __init__(self, uuid: _Optional[bytes] = ...) -> None: ...

class DeletePathRequest(_message.Message):
    __slots__ = ("table_type", "vrf_id", "family", "path", "uuid")
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VRF_ID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    table_type: TableType
    vrf_id: str
    family: Family
    path: Path
    uuid: bytes
    def __init__(self, table_type: _Optional[_Union[TableType, str]] = ..., vrf_id: _Optional[str] = ..., family: _Optional[_Union[Family, _Mapping]] = ..., path: _Optional[_Union[Path, _Mapping]] = ..., uuid: _Optional[bytes] = ...) -> None: ...

class TableLookupPrefix(_message.Message):
    __slots__ = ("prefix", "type", "rd")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXACT: _ClassVar[TableLookupPrefix.Type]
        LONGER: _ClassVar[TableLookupPrefix.Type]
        SHORTER: _ClassVar[TableLookupPrefix.Type]
    EXACT: TableLookupPrefix.Type
    LONGER: TableLookupPrefix.Type
    SHORTER: TableLookupPrefix.Type
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RD_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    type: TableLookupPrefix.Type
    rd: str
    def __init__(self, prefix: _Optional[str] = ..., type: _Optional[_Union[TableLookupPrefix.Type, str]] = ..., rd: _Optional[str] = ...) -> None: ...

class ListPathRequest(_message.Message):
    __slots__ = ("table_type", "name", "family", "prefixes", "sort_type", "enable_filtered", "enable_nlri_binary", "enable_attribute_binary", "enable_only_binary", "batch_size")
    class SortType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ListPathRequest.SortType]
        PREFIX: _ClassVar[ListPathRequest.SortType]
    NONE: ListPathRequest.SortType
    PREFIX: ListPathRequest.SortType
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    SORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FILTERED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NLRI_BINARY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ATTRIBUTE_BINARY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ONLY_BINARY_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    table_type: TableType
    name: str
    family: Family
    prefixes: _containers.RepeatedCompositeFieldContainer[TableLookupPrefix]
    sort_type: ListPathRequest.SortType
    enable_filtered: bool
    enable_nlri_binary: bool
    enable_attribute_binary: bool
    enable_only_binary: bool
    batch_size: int
    def __init__(self, table_type: _Optional[_Union[TableType, str]] = ..., name: _Optional[str] = ..., family: _Optional[_Union[Family, _Mapping]] = ..., prefixes: _Optional[_Iterable[_Union[TableLookupPrefix, _Mapping]]] = ..., sort_type: _Optional[_Union[ListPathRequest.SortType, str]] = ..., enable_filtered: bool = ..., enable_nlri_binary: bool = ..., enable_attribute_binary: bool = ..., enable_only_binary: bool = ..., batch_size: _Optional[int] = ...) -> None: ...

class ListPathResponse(_message.Message):
    __slots__ = ("destination",)
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    destination: Destination
    def __init__(self, destination: _Optional[_Union[Destination, _Mapping]] = ...) -> None: ...

class AddPathStreamRequest(_message.Message):
    __slots__ = ("table_type", "vrf_id", "paths")
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VRF_ID_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    table_type: TableType
    vrf_id: str
    paths: _containers.RepeatedCompositeFieldContainer[Path]
    def __init__(self, table_type: _Optional[_Union[TableType, str]] = ..., vrf_id: _Optional[str] = ..., paths: _Optional[_Iterable[_Union[Path, _Mapping]]] = ...) -> None: ...

class GetTableRequest(_message.Message):
    __slots__ = ("table_type", "family", "name")
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    table_type: TableType
    family: Family
    name: str
    def __init__(self, table_type: _Optional[_Union[TableType, str]] = ..., family: _Optional[_Union[Family, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class GetTableResponse(_message.Message):
    __slots__ = ("num_destination", "num_path", "num_accepted")
    NUM_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    NUM_PATH_FIELD_NUMBER: _ClassVar[int]
    NUM_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    num_destination: int
    num_path: int
    num_accepted: int
    def __init__(self, num_destination: _Optional[int] = ..., num_path: _Optional[int] = ..., num_accepted: _Optional[int] = ...) -> None: ...

class AddVrfRequest(_message.Message):
    __slots__ = ("vrf",)
    VRF_FIELD_NUMBER: _ClassVar[int]
    vrf: Vrf
    def __init__(self, vrf: _Optional[_Union[Vrf, _Mapping]] = ...) -> None: ...

class DeleteVrfRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListVrfRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListVrfResponse(_message.Message):
    __slots__ = ("vrf",)
    VRF_FIELD_NUMBER: _ClassVar[int]
    vrf: Vrf
    def __init__(self, vrf: _Optional[_Union[Vrf, _Mapping]] = ...) -> None: ...

class AddPolicyRequest(_message.Message):
    __slots__ = ("policy", "refer_existing_statements")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    REFER_EXISTING_STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    refer_existing_statements: bool
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ..., refer_existing_statements: bool = ...) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ("policy", "preserve_statements", "all")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    preserve_statements: bool
    all: bool
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ..., preserve_statements: bool = ..., all: bool = ...) -> None: ...

class ListPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPolicyResponse(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: Policy
    def __init__(self, policy: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...

class SetPoliciesRequest(_message.Message):
    __slots__ = ("defined_sets", "policies", "assignments")
    DEFINED_SETS_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    defined_sets: _containers.RepeatedCompositeFieldContainer[DefinedSet]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    assignments: _containers.RepeatedCompositeFieldContainer[PolicyAssignment]
    def __init__(self, defined_sets: _Optional[_Iterable[_Union[DefinedSet, _Mapping]]] = ..., policies: _Optional[_Iterable[_Union[Policy, _Mapping]]] = ..., assignments: _Optional[_Iterable[_Union[PolicyAssignment, _Mapping]]] = ...) -> None: ...

class AddDefinedSetRequest(_message.Message):
    __slots__ = ("defined_set", "replace")
    DEFINED_SET_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    defined_set: DefinedSet
    replace: bool
    def __init__(self, defined_set: _Optional[_Union[DefinedSet, _Mapping]] = ..., replace: bool = ...) -> None: ...

class DeleteDefinedSetRequest(_message.Message):
    __slots__ = ("defined_set", "all")
    DEFINED_SET_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    defined_set: DefinedSet
    all: bool
    def __init__(self, defined_set: _Optional[_Union[DefinedSet, _Mapping]] = ..., all: bool = ...) -> None: ...

class ListDefinedSetRequest(_message.Message):
    __slots__ = ("defined_type", "name")
    DEFINED_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    defined_type: DefinedType
    name: str
    def __init__(self, defined_type: _Optional[_Union[DefinedType, str]] = ..., name: _Optional[str] = ...) -> None: ...

class ListDefinedSetResponse(_message.Message):
    __slots__ = ("defined_set",)
    DEFINED_SET_FIELD_NUMBER: _ClassVar[int]
    defined_set: DefinedSet
    def __init__(self, defined_set: _Optional[_Union[DefinedSet, _Mapping]] = ...) -> None: ...

class AddStatementRequest(_message.Message):
    __slots__ = ("statement",)
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: Statement
    def __init__(self, statement: _Optional[_Union[Statement, _Mapping]] = ...) -> None: ...

class DeleteStatementRequest(_message.Message):
    __slots__ = ("statement", "all")
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    statement: Statement
    all: bool
    def __init__(self, statement: _Optional[_Union[Statement, _Mapping]] = ..., all: bool = ...) -> None: ...

class ListStatementRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListStatementResponse(_message.Message):
    __slots__ = ("statement",)
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: Statement
    def __init__(self, statement: _Optional[_Union[Statement, _Mapping]] = ...) -> None: ...

class AddPolicyAssignmentRequest(_message.Message):
    __slots__ = ("assignment",)
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: PolicyAssignment
    def __init__(self, assignment: _Optional[_Union[PolicyAssignment, _Mapping]] = ...) -> None: ...

class DeletePolicyAssignmentRequest(_message.Message):
    __slots__ = ("assignment", "all")
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    assignment: PolicyAssignment
    all: bool
    def __init__(self, assignment: _Optional[_Union[PolicyAssignment, _Mapping]] = ..., all: bool = ...) -> None: ...

class ListPolicyAssignmentRequest(_message.Message):
    __slots__ = ("name", "direction")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    direction: PolicyDirection
    def __init__(self, name: _Optional[str] = ..., direction: _Optional[_Union[PolicyDirection, str]] = ...) -> None: ...

class ListPolicyAssignmentResponse(_message.Message):
    __slots__ = ("assignment",)
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: PolicyAssignment
    def __init__(self, assignment: _Optional[_Union[PolicyAssignment, _Mapping]] = ...) -> None: ...

class SetPolicyAssignmentRequest(_message.Message):
    __slots__ = ("assignment",)
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: PolicyAssignment
    def __init__(self, assignment: _Optional[_Union[PolicyAssignment, _Mapping]] = ...) -> None: ...

class AddRpkiRequest(_message.Message):
    __slots__ = ("address", "port", "lifetime")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    lifetime: int
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., lifetime: _Optional[int] = ...) -> None: ...

class DeleteRpkiRequest(_message.Message):
    __slots__ = ("address", "port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ListRpkiRequest(_message.Message):
    __slots__ = ("family",)
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    family: Family
    def __init__(self, family: _Optional[_Union[Family, _Mapping]] = ...) -> None: ...

class ListRpkiResponse(_message.Message):
    __slots__ = ("server",)
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: Rpki
    def __init__(self, server: _Optional[_Union[Rpki, _Mapping]] = ...) -> None: ...

class EnableRpkiRequest(_message.Message):
    __slots__ = ("address", "port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class DisableRpkiRequest(_message.Message):
    __slots__ = ("address", "port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ResetRpkiRequest(_message.Message):
    __slots__ = ("address", "port", "soft")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    SOFT_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    soft: bool
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., soft: bool = ...) -> None: ...

class ListRpkiTableRequest(_message.Message):
    __slots__ = ("family",)
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    family: Family
    def __init__(self, family: _Optional[_Union[Family, _Mapping]] = ...) -> None: ...

class ListRpkiTableResponse(_message.Message):
    __slots__ = ("roa",)
    ROA_FIELD_NUMBER: _ClassVar[int]
    roa: Roa
    def __init__(self, roa: _Optional[_Union[Roa, _Mapping]] = ...) -> None: ...

class EnableZebraRequest(_message.Message):
    __slots__ = ("url", "route_types", "version", "nexthop_trigger_enable", "nexthop_trigger_delay", "mpls_label_range_size", "software_name")
    URL_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TYPES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_TRIGGER_ENABLE_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_TRIGGER_DELAY_FIELD_NUMBER: _ClassVar[int]
    MPLS_LABEL_RANGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_NAME_FIELD_NUMBER: _ClassVar[int]
    url: str
    route_types: _containers.RepeatedScalarFieldContainer[str]
    version: int
    nexthop_trigger_enable: bool
    nexthop_trigger_delay: int
    mpls_label_range_size: int
    software_name: str
    def __init__(self, url: _Optional[str] = ..., route_types: _Optional[_Iterable[str]] = ..., version: _Optional[int] = ..., nexthop_trigger_enable: bool = ..., nexthop_trigger_delay: _Optional[int] = ..., mpls_label_range_size: _Optional[int] = ..., software_name: _Optional[str] = ...) -> None: ...

class EnableMrtRequest(_message.Message):
    __slots__ = ("type", "filename", "dump_interval", "rotation_interval")
    class DumpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATES: _ClassVar[EnableMrtRequest.DumpType]
        TABLE: _ClassVar[EnableMrtRequest.DumpType]
    UPDATES: EnableMrtRequest.DumpType
    TABLE: EnableMrtRequest.DumpType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DUMP_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ROTATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    type: EnableMrtRequest.DumpType
    filename: str
    dump_interval: int
    rotation_interval: int
    def __init__(self, type: _Optional[_Union[EnableMrtRequest.DumpType, str]] = ..., filename: _Optional[str] = ..., dump_interval: _Optional[int] = ..., rotation_interval: _Optional[int] = ...) -> None: ...

class DisableMrtRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class AddBmpRequest(_message.Message):
    __slots__ = ("address", "port", "policy", "StatisticsTimeout", "SysName", "SysDescr")
    class MonitoringPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRE: _ClassVar[AddBmpRequest.MonitoringPolicy]
        POST: _ClassVar[AddBmpRequest.MonitoringPolicy]
        BOTH: _ClassVar[AddBmpRequest.MonitoringPolicy]
        LOCAL: _ClassVar[AddBmpRequest.MonitoringPolicy]
        ALL: _ClassVar[AddBmpRequest.MonitoringPolicy]
    PRE: AddBmpRequest.MonitoringPolicy
    POST: AddBmpRequest.MonitoringPolicy
    BOTH: AddBmpRequest.MonitoringPolicy
    LOCAL: AddBmpRequest.MonitoringPolicy
    ALL: AddBmpRequest.MonitoringPolicy
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    STATISTICSTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SYSNAME_FIELD_NUMBER: _ClassVar[int]
    SYSDESCR_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    policy: AddBmpRequest.MonitoringPolicy
    StatisticsTimeout: int
    SysName: str
    SysDescr: str
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., policy: _Optional[_Union[AddBmpRequest.MonitoringPolicy, str]] = ..., StatisticsTimeout: _Optional[int] = ..., SysName: _Optional[str] = ..., SysDescr: _Optional[str] = ...) -> None: ...

class DeleteBmpRequest(_message.Message):
    __slots__ = ("address", "port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ListBmpRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBmpResponse(_message.Message):
    __slots__ = ("station",)
    class BmpStation(_message.Message):
        __slots__ = ("conf", "state")
        class Conf(_message.Message):
            __slots__ = ("address", "port")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            address: str
            port: int
            def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
        class State(_message.Message):
            __slots__ = ("uptime", "downtime")
            UPTIME_FIELD_NUMBER: _ClassVar[int]
            DOWNTIME_FIELD_NUMBER: _ClassVar[int]
            uptime: _timestamp_pb2.Timestamp
            downtime: _timestamp_pb2.Timestamp
            def __init__(self, uptime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., downtime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        CONF_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        conf: ListBmpResponse.BmpStation.Conf
        state: ListBmpResponse.BmpStation.State
        def __init__(self, conf: _Optional[_Union[ListBmpResponse.BmpStation.Conf, _Mapping]] = ..., state: _Optional[_Union[ListBmpResponse.BmpStation.State, _Mapping]] = ...) -> None: ...
    STATION_FIELD_NUMBER: _ClassVar[int]
    station: ListBmpResponse.BmpStation
    def __init__(self, station: _Optional[_Union[ListBmpResponse.BmpStation, _Mapping]] = ...) -> None: ...

class Family(_message.Message):
    __slots__ = ("afi", "safi")
    class Afi(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AFI_UNKNOWN: _ClassVar[Family.Afi]
        AFI_IP: _ClassVar[Family.Afi]
        AFI_IP6: _ClassVar[Family.Afi]
        AFI_L2VPN: _ClassVar[Family.Afi]
        AFI_LS: _ClassVar[Family.Afi]
        AFI_OPAQUE: _ClassVar[Family.Afi]
    AFI_UNKNOWN: Family.Afi
    AFI_IP: Family.Afi
    AFI_IP6: Family.Afi
    AFI_L2VPN: Family.Afi
    AFI_LS: Family.Afi
    AFI_OPAQUE: Family.Afi
    class Safi(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAFI_UNKNOWN: _ClassVar[Family.Safi]
        SAFI_UNICAST: _ClassVar[Family.Safi]
        SAFI_MULTICAST: _ClassVar[Family.Safi]
        SAFI_MPLS_LABEL: _ClassVar[Family.Safi]
        SAFI_ENCAPSULATION: _ClassVar[Family.Safi]
        SAFI_VPLS: _ClassVar[Family.Safi]
        SAFI_EVPN: _ClassVar[Family.Safi]
        SAFI_LS: _ClassVar[Family.Safi]
        SAFI_SR_POLICY: _ClassVar[Family.Safi]
        SAFI_MUP: _ClassVar[Family.Safi]
        SAFI_MPLS_VPN: _ClassVar[Family.Safi]
        SAFI_MPLS_VPN_MULTICAST: _ClassVar[Family.Safi]
        SAFI_ROUTE_TARGET_CONSTRAINTS: _ClassVar[Family.Safi]
        SAFI_FLOW_SPEC_UNICAST: _ClassVar[Family.Safi]
        SAFI_FLOW_SPEC_VPN: _ClassVar[Family.Safi]
        SAFI_KEY_VALUE: _ClassVar[Family.Safi]
    SAFI_UNKNOWN: Family.Safi
    SAFI_UNICAST: Family.Safi
    SAFI_MULTICAST: Family.Safi
    SAFI_MPLS_LABEL: Family.Safi
    SAFI_ENCAPSULATION: Family.Safi
    SAFI_VPLS: Family.Safi
    SAFI_EVPN: Family.Safi
    SAFI_LS: Family.Safi
    SAFI_SR_POLICY: Family.Safi
    SAFI_MUP: Family.Safi
    SAFI_MPLS_VPN: Family.Safi
    SAFI_MPLS_VPN_MULTICAST: Family.Safi
    SAFI_ROUTE_TARGET_CONSTRAINTS: Family.Safi
    SAFI_FLOW_SPEC_UNICAST: Family.Safi
    SAFI_FLOW_SPEC_VPN: Family.Safi
    SAFI_KEY_VALUE: Family.Safi
    AFI_FIELD_NUMBER: _ClassVar[int]
    SAFI_FIELD_NUMBER: _ClassVar[int]
    afi: Family.Afi
    safi: Family.Safi
    def __init__(self, afi: _Optional[_Union[Family.Afi, str]] = ..., safi: _Optional[_Union[Family.Safi, str]] = ...) -> None: ...

class Validation(_message.Message):
    __slots__ = ("state", "reason", "matched", "unmatched_asn", "unmatched_length")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NONE: _ClassVar[Validation.State]
        STATE_NOT_FOUND: _ClassVar[Validation.State]
        STATE_VALID: _ClassVar[Validation.State]
        STATE_INVALID: _ClassVar[Validation.State]
    STATE_NONE: Validation.State
    STATE_NOT_FOUND: Validation.State
    STATE_VALID: Validation.State
    STATE_INVALID: Validation.State
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_NONE: _ClassVar[Validation.Reason]
        REASON_ASN: _ClassVar[Validation.Reason]
        REASON_LENGTH: _ClassVar[Validation.Reason]
    REASON_NONE: Validation.Reason
    REASON_ASN: Validation.Reason
    REASON_LENGTH: Validation.Reason
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MATCHED_FIELD_NUMBER: _ClassVar[int]
    UNMATCHED_ASN_FIELD_NUMBER: _ClassVar[int]
    UNMATCHED_LENGTH_FIELD_NUMBER: _ClassVar[int]
    state: Validation.State
    reason: Validation.Reason
    matched: _containers.RepeatedCompositeFieldContainer[Roa]
    unmatched_asn: _containers.RepeatedCompositeFieldContainer[Roa]
    unmatched_length: _containers.RepeatedCompositeFieldContainer[Roa]
    def __init__(self, state: _Optional[_Union[Validation.State, str]] = ..., reason: _Optional[_Union[Validation.Reason, str]] = ..., matched: _Optional[_Iterable[_Union[Roa, _Mapping]]] = ..., unmatched_asn: _Optional[_Iterable[_Union[Roa, _Mapping]]] = ..., unmatched_length: _Optional[_Iterable[_Union[Roa, _Mapping]]] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ("nlri", "pattrs", "age", "best", "is_withdraw", "validation", "no_implicit_withdraw", "family", "source_asn", "source_id", "filtered", "stale", "is_from_external", "neighbor_ip", "uuid", "is_nexthop_invalid", "identifier", "local_identifier", "nlri_binary", "pattrs_binary", "send_max_filtered")
    NLRI_FIELD_NUMBER: _ClassVar[int]
    PATTRS_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    BEST_FIELD_NUMBER: _ClassVar[int]
    IS_WITHDRAW_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    NO_IMPLICIT_WITHDRAW_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ASN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERED_FIELD_NUMBER: _ClassVar[int]
    STALE_FIELD_NUMBER: _ClassVar[int]
    IS_FROM_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_IP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    IS_NEXTHOP_INVALID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NLRI_BINARY_FIELD_NUMBER: _ClassVar[int]
    PATTRS_BINARY_FIELD_NUMBER: _ClassVar[int]
    SEND_MAX_FILTERED_FIELD_NUMBER: _ClassVar[int]
    nlri: _any_pb2.Any
    pattrs: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    age: _timestamp_pb2.Timestamp
    best: bool
    is_withdraw: bool
    validation: Validation
    no_implicit_withdraw: bool
    family: Family
    source_asn: int
    source_id: str
    filtered: bool
    stale: bool
    is_from_external: bool
    neighbor_ip: str
    uuid: bytes
    is_nexthop_invalid: bool
    identifier: int
    local_identifier: int
    nlri_binary: bytes
    pattrs_binary: _containers.RepeatedScalarFieldContainer[bytes]
    send_max_filtered: bool
    def __init__(self, nlri: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., pattrs: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., age: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., best: bool = ..., is_withdraw: bool = ..., validation: _Optional[_Union[Validation, _Mapping]] = ..., no_implicit_withdraw: bool = ..., family: _Optional[_Union[Family, _Mapping]] = ..., source_asn: _Optional[int] = ..., source_id: _Optional[str] = ..., filtered: bool = ..., stale: bool = ..., is_from_external: bool = ..., neighbor_ip: _Optional[str] = ..., uuid: _Optional[bytes] = ..., is_nexthop_invalid: bool = ..., identifier: _Optional[int] = ..., local_identifier: _Optional[int] = ..., nlri_binary: _Optional[bytes] = ..., pattrs_binary: _Optional[_Iterable[bytes]] = ..., send_max_filtered: bool = ...) -> None: ...

class Destination(_message.Message):
    __slots__ = ("prefix", "paths")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    paths: _containers.RepeatedCompositeFieldContainer[Path]
    def __init__(self, prefix: _Optional[str] = ..., paths: _Optional[_Iterable[_Union[Path, _Mapping]]] = ...) -> None: ...

class Peer(_message.Message):
    __slots__ = ("apply_policy", "conf", "ebgp_multihop", "route_reflector", "state", "timers", "transport", "route_server", "graceful_restart", "afi_safis", "ttl_security")
    APPLY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONF_FIELD_NUMBER: _ClassVar[int]
    EBGP_MULTIHOP_FIELD_NUMBER: _ClassVar[int]
    ROUTE_REFLECTOR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIMERS_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_RESTART_FIELD_NUMBER: _ClassVar[int]
    AFI_SAFIS_FIELD_NUMBER: _ClassVar[int]
    TTL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    apply_policy: ApplyPolicy
    conf: PeerConf
    ebgp_multihop: EbgpMultihop
    route_reflector: RouteReflector
    state: PeerState
    timers: Timers
    transport: Transport
    route_server: RouteServer
    graceful_restart: GracefulRestart
    afi_safis: _containers.RepeatedCompositeFieldContainer[AfiSafi]
    ttl_security: TtlSecurity
    def __init__(self, apply_policy: _Optional[_Union[ApplyPolicy, _Mapping]] = ..., conf: _Optional[_Union[PeerConf, _Mapping]] = ..., ebgp_multihop: _Optional[_Union[EbgpMultihop, _Mapping]] = ..., route_reflector: _Optional[_Union[RouteReflector, _Mapping]] = ..., state: _Optional[_Union[PeerState, _Mapping]] = ..., timers: _Optional[_Union[Timers, _Mapping]] = ..., transport: _Optional[_Union[Transport, _Mapping]] = ..., route_server: _Optional[_Union[RouteServer, _Mapping]] = ..., graceful_restart: _Optional[_Union[GracefulRestart, _Mapping]] = ..., afi_safis: _Optional[_Iterable[_Union[AfiSafi, _Mapping]]] = ..., ttl_security: _Optional[_Union[TtlSecurity, _Mapping]] = ...) -> None: ...

class PeerGroup(_message.Message):
    __slots__ = ("apply_policy", "conf", "ebgp_multihop", "route_reflector", "info", "timers", "transport", "route_server", "graceful_restart", "afi_safis", "ttl_security")
    APPLY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONF_FIELD_NUMBER: _ClassVar[int]
    EBGP_MULTIHOP_FIELD_NUMBER: _ClassVar[int]
    ROUTE_REFLECTOR_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    TIMERS_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_RESTART_FIELD_NUMBER: _ClassVar[int]
    AFI_SAFIS_FIELD_NUMBER: _ClassVar[int]
    TTL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    apply_policy: ApplyPolicy
    conf: PeerGroupConf
    ebgp_multihop: EbgpMultihop
    route_reflector: RouteReflector
    info: PeerGroupState
    timers: Timers
    transport: Transport
    route_server: RouteServer
    graceful_restart: GracefulRestart
    afi_safis: _containers.RepeatedCompositeFieldContainer[AfiSafi]
    ttl_security: TtlSecurity
    def __init__(self, apply_policy: _Optional[_Union[ApplyPolicy, _Mapping]] = ..., conf: _Optional[_Union[PeerGroupConf, _Mapping]] = ..., ebgp_multihop: _Optional[_Union[EbgpMultihop, _Mapping]] = ..., route_reflector: _Optional[_Union[RouteReflector, _Mapping]] = ..., info: _Optional[_Union[PeerGroupState, _Mapping]] = ..., timers: _Optional[_Union[Timers, _Mapping]] = ..., transport: _Optional[_Union[Transport, _Mapping]] = ..., route_server: _Optional[_Union[RouteServer, _Mapping]] = ..., graceful_restart: _Optional[_Union[GracefulRestart, _Mapping]] = ..., afi_safis: _Optional[_Iterable[_Union[AfiSafi, _Mapping]]] = ..., ttl_security: _Optional[_Union[TtlSecurity, _Mapping]] = ...) -> None: ...

class DynamicNeighbor(_message.Message):
    __slots__ = ("prefix", "peer_group")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    peer_group: str
    def __init__(self, prefix: _Optional[str] = ..., peer_group: _Optional[str] = ...) -> None: ...

class ApplyPolicy(_message.Message):
    __slots__ = ("in_policy", "export_policy", "import_policy")
    IN_POLICY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
    IMPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
    in_policy: PolicyAssignment
    export_policy: PolicyAssignment
    import_policy: PolicyAssignment
    def __init__(self, in_policy: _Optional[_Union[PolicyAssignment, _Mapping]] = ..., export_policy: _Optional[_Union[PolicyAssignment, _Mapping]] = ..., import_policy: _Optional[_Union[PolicyAssignment, _Mapping]] = ...) -> None: ...

class PrefixLimit(_message.Message):
    __slots__ = ("family", "max_prefixes", "shutdown_threshold_pct")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    MAX_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    family: Family
    max_prefixes: int
    shutdown_threshold_pct: int
    def __init__(self, family: _Optional[_Union[Family, _Mapping]] = ..., max_prefixes: _Optional[int] = ..., shutdown_threshold_pct: _Optional[int] = ...) -> None: ...

class PeerConf(_message.Message):
    __slots__ = ("auth_password", "description", "local_asn", "neighbor_address", "peer_asn", "peer_group", "type", "remove_private", "route_flap_damping", "send_community", "neighbor_interface", "vrf", "allow_own_asn", "replace_peer_asn", "admin_down", "send_software_version")
    AUTH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ASN_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FLAP_DAMPING_FIELD_NUMBER: _ClassVar[int]
    SEND_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    VRF_FIELD_NUMBER: _ClassVar[int]
    ALLOW_OWN_ASN_FIELD_NUMBER: _ClassVar[int]
    REPLACE_PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    ADMIN_DOWN_FIELD_NUMBER: _ClassVar[int]
    SEND_SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    auth_password: str
    description: str
    local_asn: int
    neighbor_address: str
    peer_asn: int
    peer_group: str
    type: PeerType
    remove_private: RemovePrivate
    route_flap_damping: bool
    send_community: int
    neighbor_interface: str
    vrf: str
    allow_own_asn: int
    replace_peer_asn: bool
    admin_down: bool
    send_software_version: bool
    def __init__(self, auth_password: _Optional[str] = ..., description: _Optional[str] = ..., local_asn: _Optional[int] = ..., neighbor_address: _Optional[str] = ..., peer_asn: _Optional[int] = ..., peer_group: _Optional[str] = ..., type: _Optional[_Union[PeerType, str]] = ..., remove_private: _Optional[_Union[RemovePrivate, str]] = ..., route_flap_damping: bool = ..., send_community: _Optional[int] = ..., neighbor_interface: _Optional[str] = ..., vrf: _Optional[str] = ..., allow_own_asn: _Optional[int] = ..., replace_peer_asn: bool = ..., admin_down: bool = ..., send_software_version: bool = ...) -> None: ...

class PeerGroupConf(_message.Message):
    __slots__ = ("auth_password", "description", "local_asn", "peer_asn", "peer_group_name", "type", "remove_private", "route_flap_damping", "send_community")
    AUTH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FLAP_DAMPING_FIELD_NUMBER: _ClassVar[int]
    SEND_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    auth_password: str
    description: str
    local_asn: int
    peer_asn: int
    peer_group_name: str
    type: PeerType
    remove_private: RemovePrivate
    route_flap_damping: bool
    send_community: int
    def __init__(self, auth_password: _Optional[str] = ..., description: _Optional[str] = ..., local_asn: _Optional[int] = ..., peer_asn: _Optional[int] = ..., peer_group_name: _Optional[str] = ..., type: _Optional[_Union[PeerType, str]] = ..., remove_private: _Optional[_Union[RemovePrivate, str]] = ..., route_flap_damping: bool = ..., send_community: _Optional[int] = ...) -> None: ...

class PeerGroupState(_message.Message):
    __slots__ = ("auth_password", "description", "local_asn", "peer_asn", "peer_group_name", "type", "remove_private", "route_flap_damping", "send_community", "total_paths", "total_prefixes")
    AUTH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FLAP_DAMPING_FIELD_NUMBER: _ClassVar[int]
    SEND_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PATHS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    auth_password: str
    description: str
    local_asn: int
    peer_asn: int
    peer_group_name: str
    type: PeerType
    remove_private: RemovePrivate
    route_flap_damping: bool
    send_community: int
    total_paths: int
    total_prefixes: int
    def __init__(self, auth_password: _Optional[str] = ..., description: _Optional[str] = ..., local_asn: _Optional[int] = ..., peer_asn: _Optional[int] = ..., peer_group_name: _Optional[str] = ..., type: _Optional[_Union[PeerType, str]] = ..., remove_private: _Optional[_Union[RemovePrivate, str]] = ..., route_flap_damping: bool = ..., send_community: _Optional[int] = ..., total_paths: _Optional[int] = ..., total_prefixes: _Optional[int] = ...) -> None: ...

class TtlSecurity(_message.Message):
    __slots__ = ("enabled", "ttl_min")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TTL_MIN_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    ttl_min: int
    def __init__(self, enabled: bool = ..., ttl_min: _Optional[int] = ...) -> None: ...

class EbgpMultihop(_message.Message):
    __slots__ = ("enabled", "multihop_ttl")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MULTIHOP_TTL_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    multihop_ttl: int
    def __init__(self, enabled: bool = ..., multihop_ttl: _Optional[int] = ...) -> None: ...

class RouteReflector(_message.Message):
    __slots__ = ("route_reflector_client", "route_reflector_cluster_id")
    ROUTE_REFLECTOR_CLIENT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_REFLECTOR_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    route_reflector_client: bool
    route_reflector_cluster_id: str
    def __init__(self, route_reflector_client: bool = ..., route_reflector_cluster_id: _Optional[str] = ...) -> None: ...

class PeerState(_message.Message):
    __slots__ = ("auth_password", "description", "local_asn", "messages", "neighbor_address", "peer_asn", "peer_group", "type", "queues", "remove_private", "route_flap_damping", "send_community", "session_state", "admin_state", "out_q", "flops", "remote_cap", "local_cap", "router_id")
    class SessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[PeerState.SessionState]
        IDLE: _ClassVar[PeerState.SessionState]
        CONNECT: _ClassVar[PeerState.SessionState]
        ACTIVE: _ClassVar[PeerState.SessionState]
        OPENSENT: _ClassVar[PeerState.SessionState]
        OPENCONFIRM: _ClassVar[PeerState.SessionState]
        ESTABLISHED: _ClassVar[PeerState.SessionState]
    UNKNOWN: PeerState.SessionState
    IDLE: PeerState.SessionState
    CONNECT: PeerState.SessionState
    ACTIVE: PeerState.SessionState
    OPENSENT: PeerState.SessionState
    OPENCONFIRM: PeerState.SessionState
    ESTABLISHED: PeerState.SessionState
    class AdminState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UP: _ClassVar[PeerState.AdminState]
        DOWN: _ClassVar[PeerState.AdminState]
        PFX_CT: _ClassVar[PeerState.AdminState]
    UP: PeerState.AdminState
    DOWN: PeerState.AdminState
    PFX_CT: PeerState.AdminState
    AUTH_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ASN_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PEER_ASN_FIELD_NUMBER: _ClassVar[int]
    PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FLAP_DAMPING_FIELD_NUMBER: _ClassVar[int]
    SEND_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    ADMIN_STATE_FIELD_NUMBER: _ClassVar[int]
    OUT_Q_FIELD_NUMBER: _ClassVar[int]
    FLOPS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CAP_FIELD_NUMBER: _ClassVar[int]
    LOCAL_CAP_FIELD_NUMBER: _ClassVar[int]
    ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    auth_password: str
    description: str
    local_asn: int
    messages: Messages
    neighbor_address: str
    peer_asn: int
    peer_group: str
    type: PeerType
    queues: Queues
    remove_private: RemovePrivate
    route_flap_damping: bool
    send_community: int
    session_state: PeerState.SessionState
    admin_state: PeerState.AdminState
    out_q: int
    flops: int
    remote_cap: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    local_cap: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    router_id: str
    def __init__(self, auth_password: _Optional[str] = ..., description: _Optional[str] = ..., local_asn: _Optional[int] = ..., messages: _Optional[_Union[Messages, _Mapping]] = ..., neighbor_address: _Optional[str] = ..., peer_asn: _Optional[int] = ..., peer_group: _Optional[str] = ..., type: _Optional[_Union[PeerType, str]] = ..., queues: _Optional[_Union[Queues, _Mapping]] = ..., remove_private: _Optional[_Union[RemovePrivate, str]] = ..., route_flap_damping: bool = ..., send_community: _Optional[int] = ..., session_state: _Optional[_Union[PeerState.SessionState, str]] = ..., admin_state: _Optional[_Union[PeerState.AdminState, str]] = ..., out_q: _Optional[int] = ..., flops: _Optional[int] = ..., remote_cap: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., local_cap: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., router_id: _Optional[str] = ...) -> None: ...

class Messages(_message.Message):
    __slots__ = ("received", "sent")
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    SENT_FIELD_NUMBER: _ClassVar[int]
    received: Message
    sent: Message
    def __init__(self, received: _Optional[_Union[Message, _Mapping]] = ..., sent: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("notification", "update", "open", "keepalive", "refresh", "discarded", "total", "withdraw_update", "withdraw_prefix")
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    KEEPALIVE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    DISCARDED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_UPDATE_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_PREFIX_FIELD_NUMBER: _ClassVar[int]
    notification: int
    update: int
    open: int
    keepalive: int
    refresh: int
    discarded: int
    total: int
    withdraw_update: int
    withdraw_prefix: int
    def __init__(self, notification: _Optional[int] = ..., update: _Optional[int] = ..., open: _Optional[int] = ..., keepalive: _Optional[int] = ..., refresh: _Optional[int] = ..., discarded: _Optional[int] = ..., total: _Optional[int] = ..., withdraw_update: _Optional[int] = ..., withdraw_prefix: _Optional[int] = ...) -> None: ...

class Queues(_message.Message):
    __slots__ = ("input", "output")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    input: int
    output: int
    def __init__(self, input: _Optional[int] = ..., output: _Optional[int] = ...) -> None: ...

class Timers(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: TimersConfig
    state: TimersState
    def __init__(self, config: _Optional[_Union[TimersConfig, _Mapping]] = ..., state: _Optional[_Union[TimersState, _Mapping]] = ...) -> None: ...

class TimersConfig(_message.Message):
    __slots__ = ("connect_retry", "hold_time", "keepalive_interval", "minimum_advertisement_interval", "idle_hold_time_after_reset")
    CONNECT_RETRY_FIELD_NUMBER: _ClassVar[int]
    HOLD_TIME_FIELD_NUMBER: _ClassVar[int]
    KEEPALIVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ADVERTISEMENT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    IDLE_HOLD_TIME_AFTER_RESET_FIELD_NUMBER: _ClassVar[int]
    connect_retry: int
    hold_time: int
    keepalive_interval: int
    minimum_advertisement_interval: int
    idle_hold_time_after_reset: int
    def __init__(self, connect_retry: _Optional[int] = ..., hold_time: _Optional[int] = ..., keepalive_interval: _Optional[int] = ..., minimum_advertisement_interval: _Optional[int] = ..., idle_hold_time_after_reset: _Optional[int] = ...) -> None: ...

class TimersState(_message.Message):
    __slots__ = ("connect_retry", "hold_time", "keepalive_interval", "minimum_advertisement_interval", "negotiated_hold_time", "uptime", "downtime")
    CONNECT_RETRY_FIELD_NUMBER: _ClassVar[int]
    HOLD_TIME_FIELD_NUMBER: _ClassVar[int]
    KEEPALIVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ADVERTISEMENT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    NEGOTIATED_HOLD_TIME_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    DOWNTIME_FIELD_NUMBER: _ClassVar[int]
    connect_retry: int
    hold_time: int
    keepalive_interval: int
    minimum_advertisement_interval: int
    negotiated_hold_time: int
    uptime: _timestamp_pb2.Timestamp
    downtime: _timestamp_pb2.Timestamp
    def __init__(self, connect_retry: _Optional[int] = ..., hold_time: _Optional[int] = ..., keepalive_interval: _Optional[int] = ..., minimum_advertisement_interval: _Optional[int] = ..., negotiated_hold_time: _Optional[int] = ..., uptime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., downtime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Transport(_message.Message):
    __slots__ = ("local_address", "local_port", "mtu_discovery", "passive_mode", "remote_address", "remote_port", "tcp_mss", "bind_interface")
    LOCAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PORT_FIELD_NUMBER: _ClassVar[int]
    MTU_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_MODE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PORT_FIELD_NUMBER: _ClassVar[int]
    TCP_MSS_FIELD_NUMBER: _ClassVar[int]
    BIND_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    local_address: str
    local_port: int
    mtu_discovery: bool
    passive_mode: bool
    remote_address: str
    remote_port: int
    tcp_mss: int
    bind_interface: str
    def __init__(self, local_address: _Optional[str] = ..., local_port: _Optional[int] = ..., mtu_discovery: bool = ..., passive_mode: bool = ..., remote_address: _Optional[str] = ..., remote_port: _Optional[int] = ..., tcp_mss: _Optional[int] = ..., bind_interface: _Optional[str] = ...) -> None: ...

class RouteServer(_message.Message):
    __slots__ = ("route_server_client", "secondary_route")
    ROUTE_SERVER_CLIENT_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ROUTE_FIELD_NUMBER: _ClassVar[int]
    route_server_client: bool
    secondary_route: bool
    def __init__(self, route_server_client: bool = ..., secondary_route: bool = ...) -> None: ...

class GracefulRestart(_message.Message):
    __slots__ = ("enabled", "restart_time", "helper_only", "deferral_time", "notification_enabled", "longlived_enabled", "stale_routes_time", "peer_restart_time", "peer_restarting", "local_restarting", "mode")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RESTART_TIME_FIELD_NUMBER: _ClassVar[int]
    HELPER_ONLY_FIELD_NUMBER: _ClassVar[int]
    DEFERRAL_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LONGLIVED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STALE_ROUTES_TIME_FIELD_NUMBER: _ClassVar[int]
    PEER_RESTART_TIME_FIELD_NUMBER: _ClassVar[int]
    PEER_RESTARTING_FIELD_NUMBER: _ClassVar[int]
    LOCAL_RESTARTING_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    restart_time: int
    helper_only: bool
    deferral_time: int
    notification_enabled: bool
    longlived_enabled: bool
    stale_routes_time: int
    peer_restart_time: int
    peer_restarting: bool
    local_restarting: bool
    mode: str
    def __init__(self, enabled: bool = ..., restart_time: _Optional[int] = ..., helper_only: bool = ..., deferral_time: _Optional[int] = ..., notification_enabled: bool = ..., longlived_enabled: bool = ..., stale_routes_time: _Optional[int] = ..., peer_restart_time: _Optional[int] = ..., peer_restarting: bool = ..., local_restarting: bool = ..., mode: _Optional[str] = ...) -> None: ...

class MpGracefulRestartConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class MpGracefulRestartState(_message.Message):
    __slots__ = ("enabled", "received", "advertised", "end_of_rib_received", "end_of_rib_sent")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    ADVERTISED_FIELD_NUMBER: _ClassVar[int]
    END_OF_RIB_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    END_OF_RIB_SENT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    received: bool
    advertised: bool
    end_of_rib_received: bool
    end_of_rib_sent: bool
    def __init__(self, enabled: bool = ..., received: bool = ..., advertised: bool = ..., end_of_rib_received: bool = ..., end_of_rib_sent: bool = ...) -> None: ...

class MpGracefulRestart(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: MpGracefulRestartConfig
    state: MpGracefulRestartState
    def __init__(self, config: _Optional[_Union[MpGracefulRestartConfig, _Mapping]] = ..., state: _Optional[_Union[MpGracefulRestartState, _Mapping]] = ...) -> None: ...

class AfiSafiConfig(_message.Message):
    __slots__ = ("family", "enabled")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    family: Family
    enabled: bool
    def __init__(self, family: _Optional[_Union[Family, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class AfiSafiState(_message.Message):
    __slots__ = ("family", "enabled", "received", "accepted", "advertised")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    ADVERTISED_FIELD_NUMBER: _ClassVar[int]
    family: Family
    enabled: bool
    received: int
    accepted: int
    advertised: int
    def __init__(self, family: _Optional[_Union[Family, _Mapping]] = ..., enabled: bool = ..., received: _Optional[int] = ..., accepted: _Optional[int] = ..., advertised: _Optional[int] = ...) -> None: ...

class RouteSelectionOptionsConfig(_message.Message):
    __slots__ = ("always_compare_med", "ignore_as_path_length", "external_compare_router_id", "advertise_inactive_routes", "enable_aigp", "ignore_next_hop_igp_metric", "disable_best_path_selection")
    ALWAYS_COMPARE_MED_FIELD_NUMBER: _ClassVar[int]
    IGNORE_AS_PATH_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_COMPARE_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    ADVERTISE_INACTIVE_ROUTES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AIGP_FIELD_NUMBER: _ClassVar[int]
    IGNORE_NEXT_HOP_IGP_METRIC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_BEST_PATH_SELECTION_FIELD_NUMBER: _ClassVar[int]
    always_compare_med: bool
    ignore_as_path_length: bool
    external_compare_router_id: bool
    advertise_inactive_routes: bool
    enable_aigp: bool
    ignore_next_hop_igp_metric: bool
    disable_best_path_selection: bool
    def __init__(self, always_compare_med: bool = ..., ignore_as_path_length: bool = ..., external_compare_router_id: bool = ..., advertise_inactive_routes: bool = ..., enable_aigp: bool = ..., ignore_next_hop_igp_metric: bool = ..., disable_best_path_selection: bool = ...) -> None: ...

class RouteSelectionOptionsState(_message.Message):
    __slots__ = ("always_compare_med", "ignore_as_path_length", "external_compare_router_id", "advertise_inactive_routes", "enable_aigp", "ignore_next_hop_igp_metric", "disable_best_path_selection")
    ALWAYS_COMPARE_MED_FIELD_NUMBER: _ClassVar[int]
    IGNORE_AS_PATH_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_COMPARE_ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    ADVERTISE_INACTIVE_ROUTES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AIGP_FIELD_NUMBER: _ClassVar[int]
    IGNORE_NEXT_HOP_IGP_METRIC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_BEST_PATH_SELECTION_FIELD_NUMBER: _ClassVar[int]
    always_compare_med: bool
    ignore_as_path_length: bool
    external_compare_router_id: bool
    advertise_inactive_routes: bool
    enable_aigp: bool
    ignore_next_hop_igp_metric: bool
    disable_best_path_selection: bool
    def __init__(self, always_compare_med: bool = ..., ignore_as_path_length: bool = ..., external_compare_router_id: bool = ..., advertise_inactive_routes: bool = ..., enable_aigp: bool = ..., ignore_next_hop_igp_metric: bool = ..., disable_best_path_selection: bool = ...) -> None: ...

class RouteSelectionOptions(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: RouteSelectionOptionsConfig
    state: RouteSelectionOptionsState
    def __init__(self, config: _Optional[_Union[RouteSelectionOptionsConfig, _Mapping]] = ..., state: _Optional[_Union[RouteSelectionOptionsState, _Mapping]] = ...) -> None: ...

class UseMultiplePathsConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class UseMultiplePathsState(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class EbgpConfig(_message.Message):
    __slots__ = ("allow_multiple_asn", "maximum_paths")
    ALLOW_MULTIPLE_ASN_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PATHS_FIELD_NUMBER: _ClassVar[int]
    allow_multiple_asn: bool
    maximum_paths: int
    def __init__(self, allow_multiple_asn: bool = ..., maximum_paths: _Optional[int] = ...) -> None: ...

class EbgpState(_message.Message):
    __slots__ = ("allow_multiple_asn", "maximum_paths")
    ALLOW_MULTIPLE_ASN_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PATHS_FIELD_NUMBER: _ClassVar[int]
    allow_multiple_asn: bool
    maximum_paths: int
    def __init__(self, allow_multiple_asn: bool = ..., maximum_paths: _Optional[int] = ...) -> None: ...

class Ebgp(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: EbgpConfig
    state: EbgpState
    def __init__(self, config: _Optional[_Union[EbgpConfig, _Mapping]] = ..., state: _Optional[_Union[EbgpState, _Mapping]] = ...) -> None: ...

class IbgpConfig(_message.Message):
    __slots__ = ("maximum_paths",)
    MAXIMUM_PATHS_FIELD_NUMBER: _ClassVar[int]
    maximum_paths: int
    def __init__(self, maximum_paths: _Optional[int] = ...) -> None: ...

class IbgpState(_message.Message):
    __slots__ = ("maximum_paths",)
    MAXIMUM_PATHS_FIELD_NUMBER: _ClassVar[int]
    maximum_paths: int
    def __init__(self, maximum_paths: _Optional[int] = ...) -> None: ...

class Ibgp(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: IbgpConfig
    state: IbgpState
    def __init__(self, config: _Optional[_Union[IbgpConfig, _Mapping]] = ..., state: _Optional[_Union[IbgpState, _Mapping]] = ...) -> None: ...

class UseMultiplePaths(_message.Message):
    __slots__ = ("config", "state", "ebgp", "ibgp")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EBGP_FIELD_NUMBER: _ClassVar[int]
    IBGP_FIELD_NUMBER: _ClassVar[int]
    config: UseMultiplePathsConfig
    state: UseMultiplePathsState
    ebgp: Ebgp
    ibgp: Ibgp
    def __init__(self, config: _Optional[_Union[UseMultiplePathsConfig, _Mapping]] = ..., state: _Optional[_Union[UseMultiplePathsState, _Mapping]] = ..., ebgp: _Optional[_Union[Ebgp, _Mapping]] = ..., ibgp: _Optional[_Union[Ibgp, _Mapping]] = ...) -> None: ...

class RouteTargetMembershipConfig(_message.Message):
    __slots__ = ("deferral_time",)
    DEFERRAL_TIME_FIELD_NUMBER: _ClassVar[int]
    deferral_time: int
    def __init__(self, deferral_time: _Optional[int] = ...) -> None: ...

class RouteTargetMembershipState(_message.Message):
    __slots__ = ("deferral_time",)
    DEFERRAL_TIME_FIELD_NUMBER: _ClassVar[int]
    deferral_time: int
    def __init__(self, deferral_time: _Optional[int] = ...) -> None: ...

class RouteTargetMembership(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: RouteTargetMembershipConfig
    state: RouteTargetMembershipState
    def __init__(self, config: _Optional[_Union[RouteTargetMembershipConfig, _Mapping]] = ..., state: _Optional[_Union[RouteTargetMembershipState, _Mapping]] = ...) -> None: ...

class LongLivedGracefulRestartConfig(_message.Message):
    __slots__ = ("enabled", "restart_time")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RESTART_TIME_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    restart_time: int
    def __init__(self, enabled: bool = ..., restart_time: _Optional[int] = ...) -> None: ...

class LongLivedGracefulRestartState(_message.Message):
    __slots__ = ("enabled", "received", "advertised", "peer_restart_time", "peer_restart_timer_expired")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    ADVERTISED_FIELD_NUMBER: _ClassVar[int]
    PEER_RESTART_TIME_FIELD_NUMBER: _ClassVar[int]
    PEER_RESTART_TIMER_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    received: bool
    advertised: bool
    peer_restart_time: int
    peer_restart_timer_expired: bool
    def __init__(self, enabled: bool = ..., received: bool = ..., advertised: bool = ..., peer_restart_time: _Optional[int] = ..., peer_restart_timer_expired: bool = ...) -> None: ...

class LongLivedGracefulRestart(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: LongLivedGracefulRestartConfig
    state: LongLivedGracefulRestartState
    def __init__(self, config: _Optional[_Union[LongLivedGracefulRestartConfig, _Mapping]] = ..., state: _Optional[_Union[LongLivedGracefulRestartState, _Mapping]] = ...) -> None: ...

class AfiSafi(_message.Message):
    __slots__ = ("mp_graceful_restart", "config", "state", "apply_policy", "route_selection_options", "use_multiple_paths", "prefix_limits", "route_target_membership", "long_lived_graceful_restart", "add_paths")
    MP_GRACEFUL_RESTART_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    APPLY_POLICY_FIELD_NUMBER: _ClassVar[int]
    ROUTE_SELECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    USE_MULTIPLE_PATHS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LIMITS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TARGET_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    LONG_LIVED_GRACEFUL_RESTART_FIELD_NUMBER: _ClassVar[int]
    ADD_PATHS_FIELD_NUMBER: _ClassVar[int]
    mp_graceful_restart: MpGracefulRestart
    config: AfiSafiConfig
    state: AfiSafiState
    apply_policy: ApplyPolicy
    route_selection_options: RouteSelectionOptions
    use_multiple_paths: UseMultiplePaths
    prefix_limits: PrefixLimit
    route_target_membership: RouteTargetMembership
    long_lived_graceful_restart: LongLivedGracefulRestart
    add_paths: AddPaths
    def __init__(self, mp_graceful_restart: _Optional[_Union[MpGracefulRestart, _Mapping]] = ..., config: _Optional[_Union[AfiSafiConfig, _Mapping]] = ..., state: _Optional[_Union[AfiSafiState, _Mapping]] = ..., apply_policy: _Optional[_Union[ApplyPolicy, _Mapping]] = ..., route_selection_options: _Optional[_Union[RouteSelectionOptions, _Mapping]] = ..., use_multiple_paths: _Optional[_Union[UseMultiplePaths, _Mapping]] = ..., prefix_limits: _Optional[_Union[PrefixLimit, _Mapping]] = ..., route_target_membership: _Optional[_Union[RouteTargetMembership, _Mapping]] = ..., long_lived_graceful_restart: _Optional[_Union[LongLivedGracefulRestart, _Mapping]] = ..., add_paths: _Optional[_Union[AddPaths, _Mapping]] = ...) -> None: ...

class AddPathsConfig(_message.Message):
    __slots__ = ("receive", "send_max")
    RECEIVE_FIELD_NUMBER: _ClassVar[int]
    SEND_MAX_FIELD_NUMBER: _ClassVar[int]
    receive: bool
    send_max: int
    def __init__(self, receive: bool = ..., send_max: _Optional[int] = ...) -> None: ...

class AddPathsState(_message.Message):
    __slots__ = ("receive", "send_max")
    RECEIVE_FIELD_NUMBER: _ClassVar[int]
    SEND_MAX_FIELD_NUMBER: _ClassVar[int]
    receive: bool
    send_max: int
    def __init__(self, receive: bool = ..., send_max: _Optional[int] = ...) -> None: ...

class AddPaths(_message.Message):
    __slots__ = ("config", "state")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    config: AddPathsConfig
    state: AddPathsState
    def __init__(self, config: _Optional[_Union[AddPathsConfig, _Mapping]] = ..., state: _Optional[_Union[AddPathsState, _Mapping]] = ...) -> None: ...

class Prefix(_message.Message):
    __slots__ = ("ip_prefix", "mask_length_min", "mask_length_max")
    IP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MASK_LENGTH_MIN_FIELD_NUMBER: _ClassVar[int]
    MASK_LENGTH_MAX_FIELD_NUMBER: _ClassVar[int]
    ip_prefix: str
    mask_length_min: int
    mask_length_max: int
    def __init__(self, ip_prefix: _Optional[str] = ..., mask_length_min: _Optional[int] = ..., mask_length_max: _Optional[int] = ...) -> None: ...

class DefinedSet(_message.Message):
    __slots__ = ("defined_type", "name", "list", "prefixes")
    DEFINED_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    defined_type: DefinedType
    name: str
    list: _containers.RepeatedScalarFieldContainer[str]
    prefixes: _containers.RepeatedCompositeFieldContainer[Prefix]
    def __init__(self, defined_type: _Optional[_Union[DefinedType, str]] = ..., name: _Optional[str] = ..., list: _Optional[_Iterable[str]] = ..., prefixes: _Optional[_Iterable[_Union[Prefix, _Mapping]]] = ...) -> None: ...

class MatchSet(_message.Message):
    __slots__ = ("type", "name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[MatchSet.Type]
        ALL: _ClassVar[MatchSet.Type]
        INVERT: _ClassVar[MatchSet.Type]
    ANY: MatchSet.Type
    ALL: MatchSet.Type
    INVERT: MatchSet.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    type: MatchSet.Type
    name: str
    def __init__(self, type: _Optional[_Union[MatchSet.Type, str]] = ..., name: _Optional[str] = ...) -> None: ...

class AsPathLength(_message.Message):
    __slots__ = ("type", "length")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EQ: _ClassVar[AsPathLength.Type]
        GE: _ClassVar[AsPathLength.Type]
        LE: _ClassVar[AsPathLength.Type]
    EQ: AsPathLength.Type
    GE: AsPathLength.Type
    LE: AsPathLength.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    type: AsPathLength.Type
    length: int
    def __init__(self, type: _Optional[_Union[AsPathLength.Type, str]] = ..., length: _Optional[int] = ...) -> None: ...

class CommunityCount(_message.Message):
    __slots__ = ("type", "count")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EQ: _ClassVar[CommunityCount.Type]
        GE: _ClassVar[CommunityCount.Type]
        LE: _ClassVar[CommunityCount.Type]
    EQ: CommunityCount.Type
    GE: CommunityCount.Type
    LE: CommunityCount.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    type: CommunityCount.Type
    count: int
    def __init__(self, type: _Optional[_Union[CommunityCount.Type, str]] = ..., count: _Optional[int] = ...) -> None: ...

class Conditions(_message.Message):
    __slots__ = ("prefix_set", "neighbor_set", "as_path_length", "as_path_set", "community_set", "ext_community_set", "rpki_result", "route_type", "large_community_set", "next_hop_in_list", "afi_safi_in", "community_count")
    class RouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTE_TYPE_NONE: _ClassVar[Conditions.RouteType]
        ROUTE_TYPE_INTERNAL: _ClassVar[Conditions.RouteType]
        ROUTE_TYPE_EXTERNAL: _ClassVar[Conditions.RouteType]
        ROUTE_TYPE_LOCAL: _ClassVar[Conditions.RouteType]
    ROUTE_TYPE_NONE: Conditions.RouteType
    ROUTE_TYPE_INTERNAL: Conditions.RouteType
    ROUTE_TYPE_EXTERNAL: Conditions.RouteType
    ROUTE_TYPE_LOCAL: Conditions.RouteType
    PREFIX_SET_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_SET_FIELD_NUMBER: _ClassVar[int]
    AS_PATH_LENGTH_FIELD_NUMBER: _ClassVar[int]
    AS_PATH_SET_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_SET_FIELD_NUMBER: _ClassVar[int]
    EXT_COMMUNITY_SET_FIELD_NUMBER: _ClassVar[int]
    RPKI_RESULT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LARGE_COMMUNITY_SET_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_IN_LIST_FIELD_NUMBER: _ClassVar[int]
    AFI_SAFI_IN_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    prefix_set: MatchSet
    neighbor_set: MatchSet
    as_path_length: AsPathLength
    as_path_set: MatchSet
    community_set: MatchSet
    ext_community_set: MatchSet
    rpki_result: int
    route_type: Conditions.RouteType
    large_community_set: MatchSet
    next_hop_in_list: _containers.RepeatedScalarFieldContainer[str]
    afi_safi_in: _containers.RepeatedCompositeFieldContainer[Family]
    community_count: CommunityCount
    def __init__(self, prefix_set: _Optional[_Union[MatchSet, _Mapping]] = ..., neighbor_set: _Optional[_Union[MatchSet, _Mapping]] = ..., as_path_length: _Optional[_Union[AsPathLength, _Mapping]] = ..., as_path_set: _Optional[_Union[MatchSet, _Mapping]] = ..., community_set: _Optional[_Union[MatchSet, _Mapping]] = ..., ext_community_set: _Optional[_Union[MatchSet, _Mapping]] = ..., rpki_result: _Optional[int] = ..., route_type: _Optional[_Union[Conditions.RouteType, str]] = ..., large_community_set: _Optional[_Union[MatchSet, _Mapping]] = ..., next_hop_in_list: _Optional[_Iterable[str]] = ..., afi_safi_in: _Optional[_Iterable[_Union[Family, _Mapping]]] = ..., community_count: _Optional[_Union[CommunityCount, _Mapping]] = ...) -> None: ...

class CommunityAction(_message.Message):
    __slots__ = ("type", "communities")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADD: _ClassVar[CommunityAction.Type]
        REMOVE: _ClassVar[CommunityAction.Type]
        REPLACE: _ClassVar[CommunityAction.Type]
    ADD: CommunityAction.Type
    REMOVE: CommunityAction.Type
    REPLACE: CommunityAction.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    type: CommunityAction.Type
    communities: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[CommunityAction.Type, str]] = ..., communities: _Optional[_Iterable[str]] = ...) -> None: ...

class MedAction(_message.Message):
    __slots__ = ("type", "value")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOD: _ClassVar[MedAction.Type]
        REPLACE: _ClassVar[MedAction.Type]
    MOD: MedAction.Type
    REPLACE: MedAction.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: MedAction.Type
    value: int
    def __init__(self, type: _Optional[_Union[MedAction.Type, str]] = ..., value: _Optional[int] = ...) -> None: ...

class AsPrependAction(_message.Message):
    __slots__ = ("asn", "repeat", "use_left_most")
    ASN_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FIELD_NUMBER: _ClassVar[int]
    USE_LEFT_MOST_FIELD_NUMBER: _ClassVar[int]
    asn: int
    repeat: int
    use_left_most: bool
    def __init__(self, asn: _Optional[int] = ..., repeat: _Optional[int] = ..., use_left_most: bool = ...) -> None: ...

class NexthopAction(_message.Message):
    __slots__ = ("address", "self", "unchanged")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    UNCHANGED_FIELD_NUMBER: _ClassVar[int]
    address: str
    self: bool
    unchanged: bool
    def __init__(self, address: _Optional[str] = ..., self: bool = ..., unchanged: bool = ...) -> None: ...

class LocalPrefAction(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class Actions(_message.Message):
    __slots__ = ("route_action", "community", "med", "as_prepend", "ext_community", "nexthop", "local_pref", "large_community")
    ROUTE_ACTION_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    MED_FIELD_NUMBER: _ClassVar[int]
    AS_PREPEND_FIELD_NUMBER: _ClassVar[int]
    EXT_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PREF_FIELD_NUMBER: _ClassVar[int]
    LARGE_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    route_action: RouteAction
    community: CommunityAction
    med: MedAction
    as_prepend: AsPrependAction
    ext_community: CommunityAction
    nexthop: NexthopAction
    local_pref: LocalPrefAction
    large_community: CommunityAction
    def __init__(self, route_action: _Optional[_Union[RouteAction, str]] = ..., community: _Optional[_Union[CommunityAction, _Mapping]] = ..., med: _Optional[_Union[MedAction, _Mapping]] = ..., as_prepend: _Optional[_Union[AsPrependAction, _Mapping]] = ..., ext_community: _Optional[_Union[CommunityAction, _Mapping]] = ..., nexthop: _Optional[_Union[NexthopAction, _Mapping]] = ..., local_pref: _Optional[_Union[LocalPrefAction, _Mapping]] = ..., large_community: _Optional[_Union[CommunityAction, _Mapping]] = ...) -> None: ...

class Statement(_message.Message):
    __slots__ = ("name", "conditions", "actions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    conditions: Conditions
    actions: Actions
    def __init__(self, name: _Optional[str] = ..., conditions: _Optional[_Union[Conditions, _Mapping]] = ..., actions: _Optional[_Union[Actions, _Mapping]] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ("name", "statements")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    statements: _containers.RepeatedCompositeFieldContainer[Statement]
    def __init__(self, name: _Optional[str] = ..., statements: _Optional[_Iterable[_Union[Statement, _Mapping]]] = ...) -> None: ...

class PolicyAssignment(_message.Message):
    __slots__ = ("name", "direction", "policies", "default_action")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    direction: PolicyDirection
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    default_action: RouteAction
    def __init__(self, name: _Optional[str] = ..., direction: _Optional[_Union[PolicyDirection, str]] = ..., policies: _Optional[_Iterable[_Union[Policy, _Mapping]]] = ..., default_action: _Optional[_Union[RouteAction, str]] = ...) -> None: ...

class RoutingPolicy(_message.Message):
    __slots__ = ("defined_sets", "policies")
    DEFINED_SETS_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    defined_sets: _containers.RepeatedCompositeFieldContainer[DefinedSet]
    policies: _containers.RepeatedCompositeFieldContainer[Policy]
    def __init__(self, defined_sets: _Optional[_Iterable[_Union[DefinedSet, _Mapping]]] = ..., policies: _Optional[_Iterable[_Union[Policy, _Mapping]]] = ...) -> None: ...

class Roa(_message.Message):
    __slots__ = ("asn", "prefixlen", "maxlen", "prefix", "conf")
    ASN_FIELD_NUMBER: _ClassVar[int]
    PREFIXLEN_FIELD_NUMBER: _ClassVar[int]
    MAXLEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONF_FIELD_NUMBER: _ClassVar[int]
    asn: int
    prefixlen: int
    maxlen: int
    prefix: str
    conf: RPKIConf
    def __init__(self, asn: _Optional[int] = ..., prefixlen: _Optional[int] = ..., maxlen: _Optional[int] = ..., prefix: _Optional[str] = ..., conf: _Optional[_Union[RPKIConf, _Mapping]] = ...) -> None: ...

class Vrf(_message.Message):
    __slots__ = ("name", "rd", "import_rt", "export_rt", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RD_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    rd: _any_pb2.Any
    import_rt: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    export_rt: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    id: int
    def __init__(self, name: _Optional[str] = ..., rd: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., import_rt: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., export_rt: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., id: _Optional[int] = ...) -> None: ...

class DefaultRouteDistance(_message.Message):
    __slots__ = ("external_route_distance", "internal_route_distance")
    EXTERNAL_ROUTE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ROUTE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    external_route_distance: int
    internal_route_distance: int
    def __init__(self, external_route_distance: _Optional[int] = ..., internal_route_distance: _Optional[int] = ...) -> None: ...

class Global(_message.Message):
    __slots__ = ("asn", "router_id", "listen_port", "listen_addresses", "families", "use_multiple_paths", "route_selection_options", "default_route_distance", "confederation", "graceful_restart", "apply_policy", "bind_to_device")
    ASN_FIELD_NUMBER: _ClassVar[int]
    ROUTER_ID_FIELD_NUMBER: _ClassVar[int]
    LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
    LISTEN_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    USE_MULTIPLE_PATHS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_SELECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUTE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    CONFEDERATION_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_RESTART_FIELD_NUMBER: _ClassVar[int]
    APPLY_POLICY_FIELD_NUMBER: _ClassVar[int]
    BIND_TO_DEVICE_FIELD_NUMBER: _ClassVar[int]
    asn: int
    router_id: str
    listen_port: int
    listen_addresses: _containers.RepeatedScalarFieldContainer[str]
    families: _containers.RepeatedScalarFieldContainer[int]
    use_multiple_paths: bool
    route_selection_options: RouteSelectionOptionsConfig
    default_route_distance: DefaultRouteDistance
    confederation: Confederation
    graceful_restart: GracefulRestart
    apply_policy: ApplyPolicy
    bind_to_device: str
    def __init__(self, asn: _Optional[int] = ..., router_id: _Optional[str] = ..., listen_port: _Optional[int] = ..., listen_addresses: _Optional[_Iterable[str]] = ..., families: _Optional[_Iterable[int]] = ..., use_multiple_paths: bool = ..., route_selection_options: _Optional[_Union[RouteSelectionOptionsConfig, _Mapping]] = ..., default_route_distance: _Optional[_Union[DefaultRouteDistance, _Mapping]] = ..., confederation: _Optional[_Union[Confederation, _Mapping]] = ..., graceful_restart: _Optional[_Union[GracefulRestart, _Mapping]] = ..., apply_policy: _Optional[_Union[ApplyPolicy, _Mapping]] = ..., bind_to_device: _Optional[str] = ...) -> None: ...

class Confederation(_message.Message):
    __slots__ = ("enabled", "identifier", "member_as_list")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AS_LIST_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    identifier: int
    member_as_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, enabled: bool = ..., identifier: _Optional[int] = ..., member_as_list: _Optional[_Iterable[int]] = ...) -> None: ...

class RPKIConf(_message.Message):
    __slots__ = ("address", "remote_port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    remote_port: int
    def __init__(self, address: _Optional[str] = ..., remote_port: _Optional[int] = ...) -> None: ...

class RPKIState(_message.Message):
    __slots__ = ("uptime", "downtime", "up", "record_ipv4", "record_ipv6", "prefix_ipv4", "prefix_ipv6", "serial", "received_ipv4", "received_ipv6", "serial_notify", "cache_reset", "cache_response", "end_of_data", "error", "serial_query", "reset_query")
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    DOWNTIME_FIELD_NUMBER: _ClassVar[int]
    UP_FIELD_NUMBER: _ClassVar[int]
    RECORD_IPV4_FIELD_NUMBER: _ClassVar[int]
    RECORD_IPV6_FIELD_NUMBER: _ClassVar[int]
    PREFIX_IPV4_FIELD_NUMBER: _ClassVar[int]
    PREFIX_IPV6_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_IPV4_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_IPV6_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    CACHE_RESET_FIELD_NUMBER: _ClassVar[int]
    CACHE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    END_OF_DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_QUERY_FIELD_NUMBER: _ClassVar[int]
    RESET_QUERY_FIELD_NUMBER: _ClassVar[int]
    uptime: _timestamp_pb2.Timestamp
    downtime: _timestamp_pb2.Timestamp
    up: bool
    record_ipv4: int
    record_ipv6: int
    prefix_ipv4: int
    prefix_ipv6: int
    serial: int
    received_ipv4: int
    received_ipv6: int
    serial_notify: int
    cache_reset: int
    cache_response: int
    end_of_data: int
    error: int
    serial_query: int
    reset_query: int
    def __init__(self, uptime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., downtime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., up: bool = ..., record_ipv4: _Optional[int] = ..., record_ipv6: _Optional[int] = ..., prefix_ipv4: _Optional[int] = ..., prefix_ipv6: _Optional[int] = ..., serial: _Optional[int] = ..., received_ipv4: _Optional[int] = ..., received_ipv6: _Optional[int] = ..., serial_notify: _Optional[int] = ..., cache_reset: _Optional[int] = ..., cache_response: _Optional[int] = ..., end_of_data: _Optional[int] = ..., error: _Optional[int] = ..., serial_query: _Optional[int] = ..., reset_query: _Optional[int] = ...) -> None: ...

class Rpki(_message.Message):
    __slots__ = ("conf", "state")
    CONF_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    conf: RPKIConf
    state: RPKIState
    def __init__(self, conf: _Optional[_Union[RPKIConf, _Mapping]] = ..., state: _Optional[_Union[RPKIState, _Mapping]] = ...) -> None: ...

class SetLogLevelRequest(_message.Message):
    __slots__ = ("level",)
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PANIC: _ClassVar[SetLogLevelRequest.Level]
        FATAL: _ClassVar[SetLogLevelRequest.Level]
        ERROR: _ClassVar[SetLogLevelRequest.Level]
        WARN: _ClassVar[SetLogLevelRequest.Level]
        INFO: _ClassVar[SetLogLevelRequest.Level]
        DEBUG: _ClassVar[SetLogLevelRequest.Level]
        TRACE: _ClassVar[SetLogLevelRequest.Level]
    PANIC: SetLogLevelRequest.Level
    FATAL: SetLogLevelRequest.Level
    ERROR: SetLogLevelRequest.Level
    WARN: SetLogLevelRequest.Level
    INFO: SetLogLevelRequest.Level
    DEBUG: SetLogLevelRequest.Level
    TRACE: SetLogLevelRequest.Level
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: SetLogLevelRequest.Level
    def __init__(self, level: _Optional[_Union[SetLogLevelRequest.Level, str]] = ...) -> None: ...
