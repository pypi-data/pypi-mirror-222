# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .faq import Faq


class ListFaqResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "page_size": int,
        "total": int,
        "items": List[Faq],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.total: Optional[int] = None
        self.items: Optional[List[Faq]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListFaqResponseBodyBuilder":
        return ListFaqResponseBodyBuilder()


class ListFaqResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_faq_response_body = ListFaqResponseBody()

    def has_more(self, has_more: bool) -> "ListFaqResponseBodyBuilder":
        self._list_faq_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListFaqResponseBodyBuilder":
        self._list_faq_response_body.page_token = page_token
        return self

    def page_size(self, page_size: int) -> "ListFaqResponseBodyBuilder":
        self._list_faq_response_body.page_size = page_size
        return self

    def total(self, total: int) -> "ListFaqResponseBodyBuilder":
        self._list_faq_response_body.total = total
        return self

    def items(self, items: List[Faq]) -> "ListFaqResponseBodyBuilder":
        self._list_faq_response_body.items = items
        return self

    def build(self) -> "ListFaqResponseBody":
        return self._list_faq_response_body
