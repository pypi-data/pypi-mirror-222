# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .data_source import DataSource


class ListDataSourceResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[DataSource],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[DataSource]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListDataSourceResponseBodyBuilder":
        return ListDataSourceResponseBodyBuilder()


class ListDataSourceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_data_source_response_body = ListDataSourceResponseBody()

    def has_more(self, has_more: bool) -> "ListDataSourceResponseBodyBuilder":
        self._list_data_source_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListDataSourceResponseBodyBuilder":
        self._list_data_source_response_body.page_token = page_token
        return self

    def items(self, items: List[DataSource]) -> "ListDataSourceResponseBodyBuilder":
        self._list_data_source_response_body.items = items
        return self

    def build(self) -> "ListDataSourceResponseBody":
        return self._list_data_source_response_body
