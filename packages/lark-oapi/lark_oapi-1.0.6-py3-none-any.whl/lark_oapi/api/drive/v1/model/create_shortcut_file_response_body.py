# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .file import File


class CreateShortcutFileResponseBody(object):
    _types = {
        "succ_shortcut_node": File,
    }

    def __init__(self, d=None):
        self.succ_shortcut_node: Optional[File] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateShortcutFileResponseBodyBuilder":
        return CreateShortcutFileResponseBodyBuilder()


class CreateShortcutFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_shortcut_file_response_body = CreateShortcutFileResponseBody()

    def succ_shortcut_node(self, succ_shortcut_node: File) -> "CreateShortcutFileResponseBodyBuilder":
        self._create_shortcut_file_response_body.succ_shortcut_node = succ_shortcut_node
        return self

    def build(self) -> "CreateShortcutFileResponseBody":
        return self._create_shortcut_file_response_body
