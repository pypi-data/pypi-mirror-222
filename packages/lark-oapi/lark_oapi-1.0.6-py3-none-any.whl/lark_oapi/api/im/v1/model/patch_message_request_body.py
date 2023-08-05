# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PatchMessageRequestBody(object):
    _types = {
        "content": str,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchMessageRequestBodyBuilder":
        return PatchMessageRequestBodyBuilder()


class PatchMessageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_message_request_body = PatchMessageRequestBody()

    def content(self, content: str) -> "PatchMessageRequestBodyBuilder":
        self._patch_message_request_body.content = content
        return self

    def build(self) -> "PatchMessageRequestBody":
        return self._patch_message_request_body
