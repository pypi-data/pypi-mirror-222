# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .object_field_data import ObjectFieldData


class EmployeeType(object):
    _types = {
        "id": str,
        "name": List[I18n],
        "default_employee_type": bool,
        "active": bool,
        "code": str,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.default_employee_type: Optional[bool] = None
        self.active: Optional[bool] = None
        self.code: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeTypeBuilder":
        return EmployeeTypeBuilder()


class EmployeeTypeBuilder(object):
    def __init__(self) -> None:
        self._employee_type = EmployeeType()

    def id(self, id: str) -> "EmployeeTypeBuilder":
        self._employee_type.id = id
        return self

    def name(self, name: List[I18n]) -> "EmployeeTypeBuilder":
        self._employee_type.name = name
        return self

    def default_employee_type(self, default_employee_type: bool) -> "EmployeeTypeBuilder":
        self._employee_type.default_employee_type = default_employee_type
        return self

    def active(self, active: bool) -> "EmployeeTypeBuilder":
        self._employee_type.active = active
        return self

    def code(self, code: str) -> "EmployeeTypeBuilder":
        self._employee_type.code = code
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "EmployeeTypeBuilder":
        self._employee_type.custom_fields = custom_fields
        return self

    def build(self) -> "EmployeeType":
        return self._employee_type
