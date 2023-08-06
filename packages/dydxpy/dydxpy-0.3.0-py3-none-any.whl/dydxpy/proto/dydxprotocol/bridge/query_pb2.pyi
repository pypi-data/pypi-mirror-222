from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from dydxprotocol.bridge import params_pb2 as _params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryEventParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryEventParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.EventParams
    def __init__(self, params: _Optional[_Union[_params_pb2.EventParams, _Mapping]] = ...) -> None: ...

class QueryProposeParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryProposeParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.ProposeParams
    def __init__(self, params: _Optional[_Union[_params_pb2.ProposeParams, _Mapping]] = ...) -> None: ...

class QuerySafetyParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QuerySafetyParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.SafetyParams
    def __init__(self, params: _Optional[_Union[_params_pb2.SafetyParams, _Mapping]] = ...) -> None: ...

class QueryNextAcknowledgedEventIdRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryNextAcknowledgedEventIdResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class QueryNextRecognizedEventIdRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryNextRecognizedEventIdResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
