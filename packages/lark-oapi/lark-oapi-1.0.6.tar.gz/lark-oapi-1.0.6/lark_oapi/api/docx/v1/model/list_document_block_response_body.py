# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .block import Block


class ListDocumentBlockResponseBody(object):
    _types = {
        "items": List[Block],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Block]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListDocumentBlockResponseBodyBuilder":
        return ListDocumentBlockResponseBodyBuilder()


class ListDocumentBlockResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_document_block_response_body = ListDocumentBlockResponseBody()

    def items(self, items: List[Block]) -> "ListDocumentBlockResponseBodyBuilder":
        self._list_document_block_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListDocumentBlockResponseBodyBuilder":
        self._list_document_block_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListDocumentBlockResponseBodyBuilder":
        self._list_document_block_response_body.has_more = has_more
        return self

    def build(self) -> "ListDocumentBlockResponseBody":
        return self._list_document_block_response_body
