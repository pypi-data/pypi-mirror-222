# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .employee import Employee


class SearchEmployeeResponseBody(object):
    _types = {
        "items": List[Employee],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Employee]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchEmployeeResponseBodyBuilder":
        return SearchEmployeeResponseBodyBuilder()


class SearchEmployeeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_employee_response_body = SearchEmployeeResponseBody()

    def items(self, items: List[Employee]) -> "SearchEmployeeResponseBodyBuilder":
        self._search_employee_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchEmployeeResponseBodyBuilder":
        self._search_employee_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchEmployeeResponseBodyBuilder":
        self._search_employee_response_body.has_more = has_more
        return self

    def build(self) -> "SearchEmployeeResponseBody":
        return self._search_employee_response_body
