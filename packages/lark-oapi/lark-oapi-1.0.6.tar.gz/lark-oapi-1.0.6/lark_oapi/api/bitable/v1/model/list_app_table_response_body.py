# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_table import AppTable


class ListAppTableResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "total": int,
        "items": List[AppTable],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.total: Optional[int] = None
        self.items: Optional[List[AppTable]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppTableResponseBodyBuilder":
        return ListAppTableResponseBodyBuilder()


class ListAppTableResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_app_table_response_body = ListAppTableResponseBody()

    def has_more(self, has_more: bool) -> "ListAppTableResponseBodyBuilder":
        self._list_app_table_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListAppTableResponseBodyBuilder":
        self._list_app_table_response_body.page_token = page_token
        return self

    def total(self, total: int) -> "ListAppTableResponseBodyBuilder":
        self._list_app_table_response_body.total = total
        return self

    def items(self, items: List[AppTable]) -> "ListAppTableResponseBodyBuilder":
        self._list_app_table_response_body.items = items
        return self

    def build(self) -> "ListAppTableResponseBody":
        return self._list_app_table_response_body
