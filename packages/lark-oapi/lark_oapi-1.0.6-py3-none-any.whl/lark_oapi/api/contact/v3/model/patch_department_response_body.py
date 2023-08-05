# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department import Department


class PatchDepartmentResponseBody(object):
    _types = {
        "department": Department,
    }

    def __init__(self, d=None):
        self.department: Optional[Department] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchDepartmentResponseBodyBuilder":
        return PatchDepartmentResponseBodyBuilder()


class PatchDepartmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_department_response_body = PatchDepartmentResponseBody()

    def department(self, department: Department) -> "PatchDepartmentResponseBodyBuilder":
        self._patch_department_response_body.department = department
        return self

    def build(self) -> "PatchDepartmentResponseBody":
        return self._patch_department_response_body
