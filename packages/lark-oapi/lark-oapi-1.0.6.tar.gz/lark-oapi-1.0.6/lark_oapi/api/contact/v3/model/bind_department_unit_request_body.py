# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BindDepartmentUnitRequestBody(object):
    _types = {
        "unit_id": str,
        "department_id": str,
        "department_id_type": str,
    }

    def __init__(self, d=None):
        self.unit_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.department_id_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BindDepartmentUnitRequestBodyBuilder":
        return BindDepartmentUnitRequestBodyBuilder()


class BindDepartmentUnitRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._bind_department_unit_request_body = BindDepartmentUnitRequestBody()

    def unit_id(self, unit_id: str) -> "BindDepartmentUnitRequestBodyBuilder":
        self._bind_department_unit_request_body.unit_id = unit_id
        return self

    def department_id(self, department_id: str) -> "BindDepartmentUnitRequestBodyBuilder":
        self._bind_department_unit_request_body.department_id = department_id
        return self

    def department_id_type(self, department_id_type: str) -> "BindDepartmentUnitRequestBodyBuilder":
        self._bind_department_unit_request_body.department_id_type = department_id_type
        return self

    def build(self) -> "BindDepartmentUnitRequestBody":
        return self._bind_department_unit_request_body
