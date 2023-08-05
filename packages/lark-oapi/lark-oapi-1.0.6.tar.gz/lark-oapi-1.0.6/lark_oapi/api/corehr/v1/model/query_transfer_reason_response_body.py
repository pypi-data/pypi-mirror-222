# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .transfer_reason import TransferReason


class QueryTransferReasonResponseBody(object):
    _types = {
        "items": List[TransferReason],
    }

    def __init__(self, d=None):
        self.items: Optional[List[TransferReason]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryTransferReasonResponseBodyBuilder":
        return QueryTransferReasonResponseBodyBuilder()


class QueryTransferReasonResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_transfer_reason_response_body = QueryTransferReasonResponseBody()

    def items(self, items: List[TransferReason]) -> "QueryTransferReasonResponseBodyBuilder":
        self._query_transfer_reason_response_body.items = items
        return self

    def build(self) -> "QueryTransferReasonResponseBody":
        return self._query_transfer_reason_response_body
