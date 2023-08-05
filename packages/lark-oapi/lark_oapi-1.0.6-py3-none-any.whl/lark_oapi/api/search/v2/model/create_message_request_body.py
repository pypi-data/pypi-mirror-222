# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateMessageRequestBody(object):
    _types = {
        "query": str,
        "from_ids": List[int],
        "chat_ids": List[int],
        "message_type": str,
        "at_chatter_ids": List[int],
        "from_type": str,
        "chat_type": str,
        "start_time": int,
        "end_time": int,
    }

    def __init__(self, d=None):
        self.query: Optional[str] = None
        self.from_ids: Optional[List[int]] = None
        self.chat_ids: Optional[List[int]] = None
        self.message_type: Optional[str] = None
        self.at_chatter_ids: Optional[List[int]] = None
        self.from_type: Optional[str] = None
        self.chat_type: Optional[str] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMessageRequestBodyBuilder":
        return CreateMessageRequestBodyBuilder()


class CreateMessageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_message_request_body = CreateMessageRequestBody()

    def query(self, query: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.query = query
        return self

    def from_ids(self, from_ids: List[int]) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.from_ids = from_ids
        return self

    def chat_ids(self, chat_ids: List[int]) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.chat_ids = chat_ids
        return self

    def message_type(self, message_type: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.message_type = message_type
        return self

    def at_chatter_ids(self, at_chatter_ids: List[int]) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.at_chatter_ids = at_chatter_ids
        return self

    def from_type(self, from_type: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.from_type = from_type
        return self

    def chat_type(self, chat_type: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.chat_type = chat_type
        return self

    def start_time(self, start_time: int) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.start_time = start_time
        return self

    def end_time(self, end_time: int) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.end_time = end_time
        return self

    def build(self) -> "CreateMessageRequestBody":
        return self._create_message_request_body
