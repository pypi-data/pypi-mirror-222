# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_role_member import AppRoleMember


class ListAppRoleMemberResponseBody(object):
    _types = {
        "items": List[AppRoleMember],
        "has_more": bool,
        "page_token": str,
        "total": int,
    }

    def __init__(self, d=None):
        self.items: Optional[List[AppRoleMember]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.total: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppRoleMemberResponseBodyBuilder":
        return ListAppRoleMemberResponseBodyBuilder()


class ListAppRoleMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_app_role_member_response_body = ListAppRoleMemberResponseBody()

    def items(self, items: List[AppRoleMember]) -> "ListAppRoleMemberResponseBodyBuilder":
        self._list_app_role_member_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListAppRoleMemberResponseBodyBuilder":
        self._list_app_role_member_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListAppRoleMemberResponseBodyBuilder":
        self._list_app_role_member_response_body.page_token = page_token
        return self

    def total(self, total: int) -> "ListAppRoleMemberResponseBodyBuilder":
        self._list_app_role_member_response_body.total = total
        return self

    def build(self) -> "ListAppRoleMemberResponseBody":
        return self._list_app_role_member_response_body
