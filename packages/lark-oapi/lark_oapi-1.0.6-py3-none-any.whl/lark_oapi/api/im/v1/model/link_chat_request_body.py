# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class LinkChatRequestBody(object):
    _types = {
        "validity_period": str,
    }

    def __init__(self, d=None):
        self.validity_period: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LinkChatRequestBodyBuilder":
        return LinkChatRequestBodyBuilder()


class LinkChatRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._link_chat_request_body = LinkChatRequestBody()

    def validity_period(self, validity_period: str) -> "LinkChatRequestBodyBuilder":
        self._link_chat_request_body.validity_period = validity_period
        return self

    def build(self) -> "LinkChatRequestBody":
        return self._link_chat_request_body
