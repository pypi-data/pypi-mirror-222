# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .functional_role_member_result import FunctionalRoleMemberResult


class ScopesFunctionalRoleMemberResponseBody(object):
    _types = {
        "results": List[FunctionalRoleMemberResult],
    }

    def __init__(self, d=None):
        self.results: Optional[List[FunctionalRoleMemberResult]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScopesFunctionalRoleMemberResponseBodyBuilder":
        return ScopesFunctionalRoleMemberResponseBodyBuilder()


class ScopesFunctionalRoleMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._scopes_functional_role_member_response_body = ScopesFunctionalRoleMemberResponseBody()

    def results(self, results: List[FunctionalRoleMemberResult]) -> "ScopesFunctionalRoleMemberResponseBodyBuilder":
        self._scopes_functional_role_member_response_body.results = results
        return self

    def build(self) -> "ScopesFunctionalRoleMemberResponseBody":
        return self._scopes_functional_role_member_response_body
