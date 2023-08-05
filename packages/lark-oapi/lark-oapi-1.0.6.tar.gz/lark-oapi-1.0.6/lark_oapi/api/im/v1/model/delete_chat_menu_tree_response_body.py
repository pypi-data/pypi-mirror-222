# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .chat_menu_tree import ChatMenuTree


class DeleteChatMenuTreeResponseBody(object):
    _types = {
        "menu_tree": ChatMenuTree,
    }

    def __init__(self, d=None):
        self.menu_tree: Optional[ChatMenuTree] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteChatMenuTreeResponseBodyBuilder":
        return DeleteChatMenuTreeResponseBodyBuilder()


class DeleteChatMenuTreeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_chat_menu_tree_response_body = DeleteChatMenuTreeResponseBody()

    def menu_tree(self, menu_tree: ChatMenuTree) -> "DeleteChatMenuTreeResponseBodyBuilder":
        self._delete_chat_menu_tree_response_body.menu_tree = menu_tree
        return self

    def build(self) -> "DeleteChatMenuTreeResponseBody":
        return self._delete_chat_menu_tree_response_body
