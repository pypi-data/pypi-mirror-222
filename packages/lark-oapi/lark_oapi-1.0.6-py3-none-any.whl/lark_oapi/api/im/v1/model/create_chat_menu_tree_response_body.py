# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .chat_menu_tree import ChatMenuTree


class CreateChatMenuTreeResponseBody(object):
    _types = {
        "menu_tree": ChatMenuTree,
    }

    def __init__(self, d=None):
        self.menu_tree: Optional[ChatMenuTree] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateChatMenuTreeResponseBodyBuilder":
        return CreateChatMenuTreeResponseBodyBuilder()


class CreateChatMenuTreeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_chat_menu_tree_response_body = CreateChatMenuTreeResponseBody()

    def menu_tree(self, menu_tree: ChatMenuTree) -> "CreateChatMenuTreeResponseBodyBuilder":
        self._create_chat_menu_tree_response_body.menu_tree = menu_tree
        return self

    def build(self) -> "CreateChatMenuTreeResponseBody":
        return self._create_chat_menu_tree_response_body
