# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mask_session import MaskSession


class QuerySessionResponseBody(object):
    _types = {
        "mask_sessions": List[MaskSession],
    }

    def __init__(self, d=None):
        self.mask_sessions: Optional[List[MaskSession]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QuerySessionResponseBodyBuilder":
        return QuerySessionResponseBodyBuilder()


class QuerySessionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_session_response_body = QuerySessionResponseBody()

    def mask_sessions(self, mask_sessions: List[MaskSession]) -> "QuerySessionResponseBodyBuilder":
        self._query_session_response_body.mask_sessions = mask_sessions
        return self

    def build(self) -> "QuerySessionResponseBody":
        return self._query_session_response_body
