from gogoproto import gogo_pb2 as _gogo_pb2
from dydxprotocol.indexer.protocol.v1 import clob_pb2 as _clob_pb2
from dydxprotocol.indexer.protocol.v1 import subaccount_pb2 as _subaccount_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FundingUpdateV1(_message.Message):
    __slots__ = ["perpetual_id", "funding_value_ppm", "funding_index"]
    PERPETUAL_ID_FIELD_NUMBER: _ClassVar[int]
    FUNDING_VALUE_PPM_FIELD_NUMBER: _ClassVar[int]
    FUNDING_INDEX_FIELD_NUMBER: _ClassVar[int]
    perpetual_id: int
    funding_value_ppm: int
    funding_index: bytes
    def __init__(self, perpetual_id: _Optional[int] = ..., funding_value_ppm: _Optional[int] = ..., funding_index: _Optional[bytes] = ...) -> None: ...

class FundingEventV1(_message.Message):
    __slots__ = ["updates", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        TYPE_UNSPECIFIED: _ClassVar[FundingEventV1.Type]
        TYPE_PREMIUM_SAMPLE: _ClassVar[FundingEventV1.Type]
        TYPE_FUNDING_RATE_AND_INDEX: _ClassVar[FundingEventV1.Type]
        TYPE_PREMIUM_VOTE: _ClassVar[FundingEventV1.Type]
    TYPE_UNSPECIFIED: FundingEventV1.Type
    TYPE_PREMIUM_SAMPLE: FundingEventV1.Type
    TYPE_FUNDING_RATE_AND_INDEX: FundingEventV1.Type
    TYPE_PREMIUM_VOTE: FundingEventV1.Type
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[FundingUpdateV1]
    type: FundingEventV1.Type
    def __init__(self, updates: _Optional[_Iterable[_Union[FundingUpdateV1, _Mapping]]] = ..., type: _Optional[_Union[FundingEventV1.Type, str]] = ...) -> None: ...

class MarketEventV1(_message.Message):
    __slots__ = ["market_id", "price_update", "market_create", "market_modify"]
    MARKET_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    MARKET_CREATE_FIELD_NUMBER: _ClassVar[int]
    MARKET_MODIFY_FIELD_NUMBER: _ClassVar[int]
    market_id: int
    price_update: MarketPriceUpdateEventV1
    market_create: MarketCreateEventV1
    market_modify: MarketModifyEventV1
    def __init__(self, market_id: _Optional[int] = ..., price_update: _Optional[_Union[MarketPriceUpdateEventV1, _Mapping]] = ..., market_create: _Optional[_Union[MarketCreateEventV1, _Mapping]] = ..., market_modify: _Optional[_Union[MarketModifyEventV1, _Mapping]] = ...) -> None: ...

class MarketPriceUpdateEventV1(_message.Message):
    __slots__ = ["price_with_exponent"]
    PRICE_WITH_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    price_with_exponent: int
    def __init__(self, price_with_exponent: _Optional[int] = ...) -> None: ...

class MarketBaseEventV1(_message.Message):
    __slots__ = ["pair", "min_price_change_ppm"]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_CHANGE_PPM_FIELD_NUMBER: _ClassVar[int]
    pair: str
    min_price_change_ppm: int
    def __init__(self, pair: _Optional[str] = ..., min_price_change_ppm: _Optional[int] = ...) -> None: ...

class MarketCreateEventV1(_message.Message):
    __slots__ = ["base", "exponent"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXPONENT_FIELD_NUMBER: _ClassVar[int]
    base: MarketBaseEventV1
    exponent: int
    def __init__(self, base: _Optional[_Union[MarketBaseEventV1, _Mapping]] = ..., exponent: _Optional[int] = ...) -> None: ...

class MarketModifyEventV1(_message.Message):
    __slots__ = ["base"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: MarketBaseEventV1
    def __init__(self, base: _Optional[_Union[MarketBaseEventV1, _Mapping]] = ...) -> None: ...

class TransferEventV1(_message.Message):
    __slots__ = ["sender_subaccount_id", "recipient_subaccount_id", "asset_id", "amount"]
    SENDER_SUBACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_SUBACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender_subaccount_id: _subaccount_pb2.IndexerSubaccountId
    recipient_subaccount_id: _subaccount_pb2.IndexerSubaccountId
    asset_id: int
    amount: int
    def __init__(self, sender_subaccount_id: _Optional[_Union[_subaccount_pb2.IndexerSubaccountId, _Mapping]] = ..., recipient_subaccount_id: _Optional[_Union[_subaccount_pb2.IndexerSubaccountId, _Mapping]] = ..., asset_id: _Optional[int] = ..., amount: _Optional[int] = ...) -> None: ...

class OrderFillEventV1(_message.Message):
    __slots__ = ["maker_order", "order", "liquidation_order", "fill_amount", "maker_fee", "taker_fee"]
    MAKER_ORDER_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIQUIDATION_ORDER_FIELD_NUMBER: _ClassVar[int]
    FILL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    maker_order: _clob_pb2.IndexerOrder
    order: _clob_pb2.IndexerOrder
    liquidation_order: LiquidationOrderV1
    fill_amount: int
    maker_fee: int
    taker_fee: int
    def __init__(self, maker_order: _Optional[_Union[_clob_pb2.IndexerOrder, _Mapping]] = ..., order: _Optional[_Union[_clob_pb2.IndexerOrder, _Mapping]] = ..., liquidation_order: _Optional[_Union[LiquidationOrderV1, _Mapping]] = ..., fill_amount: _Optional[int] = ..., maker_fee: _Optional[int] = ..., taker_fee: _Optional[int] = ...) -> None: ...

class LiquidationOrderV1(_message.Message):
    __slots__ = ["liquidated", "clob_pair_id", "perpetual_id", "total_size", "is_buy", "subticks"]
    LIQUIDATED_FIELD_NUMBER: _ClassVar[int]
    CLOB_PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    PERPETUAL_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_BUY_FIELD_NUMBER: _ClassVar[int]
    SUBTICKS_FIELD_NUMBER: _ClassVar[int]
    liquidated: _subaccount_pb2.IndexerSubaccountId
    clob_pair_id: int
    perpetual_id: int
    total_size: int
    is_buy: bool
    subticks: int
    def __init__(self, liquidated: _Optional[_Union[_subaccount_pb2.IndexerSubaccountId, _Mapping]] = ..., clob_pair_id: _Optional[int] = ..., perpetual_id: _Optional[int] = ..., total_size: _Optional[int] = ..., is_buy: bool = ..., subticks: _Optional[int] = ...) -> None: ...

class SubaccountUpdateEventV1(_message.Message):
    __slots__ = ["subaccount_id", "updated_perpetual_positions", "updated_asset_positions"]
    SUBACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_PERPETUAL_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ASSET_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    subaccount_id: _subaccount_pb2.IndexerSubaccountId
    updated_perpetual_positions: _containers.RepeatedCompositeFieldContainer[_subaccount_pb2.IndexerPerpetualPosition]
    updated_asset_positions: _containers.RepeatedCompositeFieldContainer[_subaccount_pb2.IndexerAssetPosition]
    def __init__(self, subaccount_id: _Optional[_Union[_subaccount_pb2.IndexerSubaccountId, _Mapping]] = ..., updated_perpetual_positions: _Optional[_Iterable[_Union[_subaccount_pb2.IndexerPerpetualPosition, _Mapping]]] = ..., updated_asset_positions: _Optional[_Iterable[_Union[_subaccount_pb2.IndexerAssetPosition, _Mapping]]] = ...) -> None: ...

class StatefulOrderEventV1(_message.Message):
    __slots__ = ["order_place", "order_cancel", "order_expiration"]
    class StatefulOrderPlacementV1(_message.Message):
        __slots__ = ["order"]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        order: _clob_pb2.IndexerOrder
        def __init__(self, order: _Optional[_Union[_clob_pb2.IndexerOrder, _Mapping]] = ...) -> None: ...
    class StatefulOrderCancelationV1(_message.Message):
        __slots__ = ["canceled_order_id"]
        CANCELED_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
        canceled_order_id: _clob_pb2.IndexerOrderId
        def __init__(self, canceled_order_id: _Optional[_Union[_clob_pb2.IndexerOrderId, _Mapping]] = ...) -> None: ...
    class StatefulOrderExpirationV1(_message.Message):
        __slots__ = ["expired_order_id"]
        EXPIRED_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
        expired_order_id: _clob_pb2.IndexerOrderId
        def __init__(self, expired_order_id: _Optional[_Union[_clob_pb2.IndexerOrderId, _Mapping]] = ...) -> None: ...
    ORDER_PLACE_FIELD_NUMBER: _ClassVar[int]
    ORDER_CANCEL_FIELD_NUMBER: _ClassVar[int]
    ORDER_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    order_place: StatefulOrderEventV1.StatefulOrderPlacementV1
    order_cancel: StatefulOrderEventV1.StatefulOrderCancelationV1
    order_expiration: StatefulOrderEventV1.StatefulOrderExpirationV1
    def __init__(self, order_place: _Optional[_Union[StatefulOrderEventV1.StatefulOrderPlacementV1, _Mapping]] = ..., order_cancel: _Optional[_Union[StatefulOrderEventV1.StatefulOrderCancelationV1, _Mapping]] = ..., order_expiration: _Optional[_Union[StatefulOrderEventV1.StatefulOrderExpirationV1, _Mapping]] = ...) -> None: ...
