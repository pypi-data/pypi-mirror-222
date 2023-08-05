# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DeleteChatMembersRequestBody(object):
    _types = {
        "id_list": List[str],
    }

    def __init__(self, d=None):
        self.id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteChatMembersRequestBodyBuilder":
        return DeleteChatMembersRequestBodyBuilder()


class DeleteChatMembersRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_chat_members_request_body = DeleteChatMembersRequestBody()

    def id_list(self, id_list: List[str]) -> "DeleteChatMembersRequestBodyBuilder":
        self._delete_chat_members_request_body.id_list = id_list
        return self

    def build(self) -> "DeleteChatMembersRequestBody":
        return self._delete_chat_members_request_body
