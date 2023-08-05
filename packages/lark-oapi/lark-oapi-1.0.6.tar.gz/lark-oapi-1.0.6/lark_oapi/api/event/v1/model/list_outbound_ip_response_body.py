# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ListOutboundIpResponseBody(object):
    _types = {
        "ip_list": List[str],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.ip_list: Optional[List[str]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListOutboundIpResponseBodyBuilder":
        return ListOutboundIpResponseBodyBuilder()


class ListOutboundIpResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_outbound_ip_response_body = ListOutboundIpResponseBody()

    def ip_list(self, ip_list: List[str]) -> "ListOutboundIpResponseBodyBuilder":
        self._list_outbound_ip_response_body.ip_list = ip_list
        return self

    def page_token(self, page_token: str) -> "ListOutboundIpResponseBodyBuilder":
        self._list_outbound_ip_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListOutboundIpResponseBodyBuilder":
        self._list_outbound_ip_response_body.has_more = has_more
        return self

    def build(self) -> "ListOutboundIpResponseBody":
        return self._list_outbound_ip_response_body
