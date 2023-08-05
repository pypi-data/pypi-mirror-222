# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ManageableDefinition(object):
    _types = {
        "approval_code": str,
        "approval_name": str,
        "approval_status": str,
        "approval_admin_ids": List[str],
    }

    def __init__(self, d=None):
        self.approval_code: Optional[str] = None
        self.approval_name: Optional[str] = None
        self.approval_status: Optional[str] = None
        self.approval_admin_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ManageableDefinitionBuilder":
        return ManageableDefinitionBuilder()


class ManageableDefinitionBuilder(object):
    def __init__(self) -> None:
        self._manageable_definition = ManageableDefinition()

    def approval_code(self, approval_code: str) -> "ManageableDefinitionBuilder":
        self._manageable_definition.approval_code = approval_code
        return self

    def approval_name(self, approval_name: str) -> "ManageableDefinitionBuilder":
        self._manageable_definition.approval_name = approval_name
        return self

    def approval_status(self, approval_status: str) -> "ManageableDefinitionBuilder":
        self._manageable_definition.approval_status = approval_status
        return self

    def approval_admin_ids(self, approval_admin_ids: List[str]) -> "ManageableDefinitionBuilder":
        self._manageable_definition.approval_admin_ids = approval_admin_ids
        return self

    def build(self) -> "ManageableDefinition":
        return self._manageable_definition
