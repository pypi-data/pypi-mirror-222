# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateBotMessageResponseBody(object):
    _types = {
        "message_id": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateBotMessageResponseBodyBuilder":
        return CreateBotMessageResponseBodyBuilder()


class CreateBotMessageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_bot_message_response_body = CreateBotMessageResponseBody()

    def message_id(self, message_id: str) -> "CreateBotMessageResponseBodyBuilder":
        self._create_bot_message_response_body.message_id = message_id
        return self

    def build(self) -> "CreateBotMessageResponseBody":
        return self._create_bot_message_response_body
