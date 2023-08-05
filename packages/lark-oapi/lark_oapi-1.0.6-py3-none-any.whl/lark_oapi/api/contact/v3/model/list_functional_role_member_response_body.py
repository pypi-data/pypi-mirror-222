# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .functional_role_member import FunctionalRoleMember


class ListFunctionalRoleMemberResponseBody(object):
    _types = {
        "members": List[FunctionalRoleMember],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.members: Optional[List[FunctionalRoleMember]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListFunctionalRoleMemberResponseBodyBuilder":
        return ListFunctionalRoleMemberResponseBodyBuilder()


class ListFunctionalRoleMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_functional_role_member_response_body = ListFunctionalRoleMemberResponseBody()

    def members(self, members: List[FunctionalRoleMember]) -> "ListFunctionalRoleMemberResponseBodyBuilder":
        self._list_functional_role_member_response_body.members = members
        return self

    def page_token(self, page_token: str) -> "ListFunctionalRoleMemberResponseBodyBuilder":
        self._list_functional_role_member_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListFunctionalRoleMemberResponseBodyBuilder":
        self._list_functional_role_member_response_body.has_more = has_more
        return self

    def build(self) -> "ListFunctionalRoleMemberResponseBody":
        return self._list_functional_role_member_response_body
