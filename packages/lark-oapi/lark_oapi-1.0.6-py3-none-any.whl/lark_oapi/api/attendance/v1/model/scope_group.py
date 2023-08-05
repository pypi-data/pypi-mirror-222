# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .scope_value import ScopeValue


class ScopeGroup(object):
    _types = {
        "scope_value_type": int,
        "operation_type": int,
        "right": List[ScopeValue],
        "member_ids": List[str],
    }

    def __init__(self, d=None):
        self.scope_value_type: Optional[int] = None
        self.operation_type: Optional[int] = None
        self.right: Optional[List[ScopeValue]] = None
        self.member_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScopeGroupBuilder":
        return ScopeGroupBuilder()


class ScopeGroupBuilder(object):
    def __init__(self) -> None:
        self._scope_group = ScopeGroup()

    def scope_value_type(self, scope_value_type: int) -> "ScopeGroupBuilder":
        self._scope_group.scope_value_type = scope_value_type
        return self

    def operation_type(self, operation_type: int) -> "ScopeGroupBuilder":
        self._scope_group.operation_type = operation_type
        return self

    def right(self, right: List[ScopeValue]) -> "ScopeGroupBuilder":
        self._scope_group.right = right
        return self

    def member_ids(self, member_ids: List[str]) -> "ScopeGroupBuilder":
        self._scope_group.member_ids = member_ids
        return self

    def build(self) -> "ScopeGroup":
        return self._scope_group
