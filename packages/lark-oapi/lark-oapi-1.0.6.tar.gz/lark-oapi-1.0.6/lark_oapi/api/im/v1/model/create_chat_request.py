# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_chat_request_body import CreateChatRequestBody


class CreateChatRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.set_bot_manager: Optional[bool] = None
        self.uuid: Optional[str] = None
        self.request_body: Optional[CreateChatRequestBody] = None

    @staticmethod
    def builder() -> "CreateChatRequestBuilder":
        return CreateChatRequestBuilder()


class CreateChatRequestBuilder(object):

    def __init__(self) -> None:
        create_chat_request = CreateChatRequest()
        create_chat_request.http_method = HttpMethod.POST
        create_chat_request.uri = "/open-apis/im/v1/chats"
        create_chat_request.token_types = {AccessTokenType.TENANT}
        self._create_chat_request: CreateChatRequest = create_chat_request

    def user_id_type(self, user_id_type: str) -> "CreateChatRequestBuilder":
        self._create_chat_request.user_id_type = user_id_type
        self._create_chat_request.add_query("user_id_type", user_id_type)
        return self

    def set_bot_manager(self, set_bot_manager: bool) -> "CreateChatRequestBuilder":
        self._create_chat_request.set_bot_manager = set_bot_manager
        self._create_chat_request.add_query("set_bot_manager", set_bot_manager)
        return self

    def uuid(self, uuid: str) -> "CreateChatRequestBuilder":
        self._create_chat_request.uuid = uuid
        self._create_chat_request.add_query("uuid", uuid)
        return self

    def request_body(self, request_body: CreateChatRequestBody) -> "CreateChatRequestBuilder":
        self._create_chat_request.request_body = request_body
        self._create_chat_request.body = request_body
        return self

    def build(self) -> CreateChatRequest:
        return self._create_chat_request
