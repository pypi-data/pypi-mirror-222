# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .hrbp import Hrbp


class QuerySecurityGroupResponseBody(object):
    _types = {
        "hrbp_list": List[Hrbp],
    }

    def __init__(self, d=None):
        self.hrbp_list: Optional[List[Hrbp]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QuerySecurityGroupResponseBodyBuilder":
        return QuerySecurityGroupResponseBodyBuilder()


class QuerySecurityGroupResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_security_group_response_body = QuerySecurityGroupResponseBody()

    def hrbp_list(self, hrbp_list: List[Hrbp]) -> "QuerySecurityGroupResponseBodyBuilder":
        self._query_security_group_response_body.hrbp_list = hrbp_list
        return self

    def build(self) -> "QuerySecurityGroupResponseBody":
        return self._query_security_group_response_body
