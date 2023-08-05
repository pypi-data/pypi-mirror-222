# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class Role(object):
    _types = {
        "id": str,
        "name": I18n,
        "description": I18n,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoleBuilder":
        return RoleBuilder()


class RoleBuilder(object):
    def __init__(self) -> None:
        self._role = Role()

    def id(self, id: str) -> "RoleBuilder":
        self._role.id = id
        return self

    def name(self, name: I18n) -> "RoleBuilder":
        self._role.name = name
        return self

    def description(self, description: I18n) -> "RoleBuilder":
        self._role.description = description
        return self

    def build(self) -> "Role":
        return self._role
