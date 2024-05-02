import gobgp_pb2 as _gobgp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MultiProtocolCapability(_message.Message):
    __slots__ = ("family",)
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    family: _gobgp_pb2.Family
    def __init__(self, family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ...) -> None: ...

class RouteRefreshCapability(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarryingLabelInfoCapability(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExtendedNexthopCapabilityTuple(_message.Message):
    __slots__ = ("nlri_family", "nexthop_family")
    NLRI_FAMILY_FIELD_NUMBER: _ClassVar[int]
    NEXTHOP_FAMILY_FIELD_NUMBER: _ClassVar[int]
    nlri_family: _gobgp_pb2.Family
    nexthop_family: _gobgp_pb2.Family
    def __init__(self, nlri_family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ..., nexthop_family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ...) -> None: ...

class ExtendedNexthopCapability(_message.Message):
    __slots__ = ("tuples",)
    TUPLES_FIELD_NUMBER: _ClassVar[int]
    tuples: _containers.RepeatedCompositeFieldContainer[ExtendedNexthopCapabilityTuple]
    def __init__(self, tuples: _Optional[_Iterable[_Union[ExtendedNexthopCapabilityTuple, _Mapping]]] = ...) -> None: ...

class GracefulRestartCapabilityTuple(_message.Message):
    __slots__ = ("family", "flags")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    family: _gobgp_pb2.Family
    flags: int
    def __init__(self, family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ..., flags: _Optional[int] = ...) -> None: ...

class GracefulRestartCapability(_message.Message):
    __slots__ = ("flags", "time", "tuples")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TUPLES_FIELD_NUMBER: _ClassVar[int]
    flags: int
    time: int
    tuples: _containers.RepeatedCompositeFieldContainer[GracefulRestartCapabilityTuple]
    def __init__(self, flags: _Optional[int] = ..., time: _Optional[int] = ..., tuples: _Optional[_Iterable[_Union[GracefulRestartCapabilityTuple, _Mapping]]] = ...) -> None: ...

class FourOctetASNCapability(_message.Message):
    __slots__ = ("asn",)
    ASN_FIELD_NUMBER: _ClassVar[int]
    asn: int
    def __init__(self, asn: _Optional[int] = ...) -> None: ...

class AddPathCapabilityTuple(_message.Message):
    __slots__ = ("family", "mode")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[AddPathCapabilityTuple.Mode]
        RECEIVE: _ClassVar[AddPathCapabilityTuple.Mode]
        SEND: _ClassVar[AddPathCapabilityTuple.Mode]
        BOTH: _ClassVar[AddPathCapabilityTuple.Mode]
    NONE: AddPathCapabilityTuple.Mode
    RECEIVE: AddPathCapabilityTuple.Mode
    SEND: AddPathCapabilityTuple.Mode
    BOTH: AddPathCapabilityTuple.Mode
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    family: _gobgp_pb2.Family
    mode: AddPathCapabilityTuple.Mode
    def __init__(self, family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ..., mode: _Optional[_Union[AddPathCapabilityTuple.Mode, str]] = ...) -> None: ...

class AddPathCapability(_message.Message):
    __slots__ = ("tuples",)
    TUPLES_FIELD_NUMBER: _ClassVar[int]
    tuples: _containers.RepeatedCompositeFieldContainer[AddPathCapabilityTuple]
    def __init__(self, tuples: _Optional[_Iterable[_Union[AddPathCapabilityTuple, _Mapping]]] = ...) -> None: ...

class EnhancedRouteRefreshCapability(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LongLivedGracefulRestartCapabilityTuple(_message.Message):
    __slots__ = ("family", "flags", "time")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    family: _gobgp_pb2.Family
    flags: int
    time: int
    def __init__(self, family: _Optional[_Union[_gobgp_pb2.Family, _Mapping]] = ..., flags: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...

class LongLivedGracefulRestartCapability(_message.Message):
    __slots__ = ("tuples",)
    TUPLES_FIELD_NUMBER: _ClassVar[int]
    tuples: _containers.RepeatedCompositeFieldContainer[LongLivedGracefulRestartCapabilityTuple]
    def __init__(self, tuples: _Optional[_Iterable[_Union[LongLivedGracefulRestartCapabilityTuple, _Mapping]]] = ...) -> None: ...

class RouteRefreshCiscoCapability(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FqdnCapability(_message.Message):
    __slots__ = ("host_name", "domain_name")
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    domain_name: str
    def __init__(self, host_name: _Optional[str] = ..., domain_name: _Optional[str] = ...) -> None: ...

class SoftwareVersionCapability(_message.Message):
    __slots__ = ("software_version",)
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    software_version: str
    def __init__(self, software_version: _Optional[str] = ...) -> None: ...

class UnknownCapability(_message.Message):
    __slots__ = ("code", "value")
    CODE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    code: int
    value: bytes
    def __init__(self, code: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
