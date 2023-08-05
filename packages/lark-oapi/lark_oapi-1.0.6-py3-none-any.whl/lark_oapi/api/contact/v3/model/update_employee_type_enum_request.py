# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .employee_type_enum import EmployeeTypeEnum


class UpdateEmployeeTypeEnumRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.enum_id: Optional[str] = None
        self.request_body: Optional[EmployeeTypeEnum] = None

    @staticmethod
    def builder() -> "UpdateEmployeeTypeEnumRequestBuilder":
        return UpdateEmployeeTypeEnumRequestBuilder()


class UpdateEmployeeTypeEnumRequestBuilder(object):

    def __init__(self) -> None:
        update_employee_type_enum_request = UpdateEmployeeTypeEnumRequest()
        update_employee_type_enum_request.http_method = HttpMethod.PUT
        update_employee_type_enum_request.uri = "/open-apis/contact/v3/employee_type_enums/:enum_id"
        update_employee_type_enum_request.token_types = {AccessTokenType.TENANT}
        self._update_employee_type_enum_request: UpdateEmployeeTypeEnumRequest = update_employee_type_enum_request

    def enum_id(self, enum_id: str) -> "UpdateEmployeeTypeEnumRequestBuilder":
        self._update_employee_type_enum_request.enum_id = enum_id
        self._update_employee_type_enum_request.paths["enum_id"] = str(enum_id)
        return self

    def request_body(self, request_body: EmployeeTypeEnum) -> "UpdateEmployeeTypeEnumRequestBuilder":
        self._update_employee_type_enum_request.request_body = request_body
        self._update_employee_type_enum_request.body = request_body
        return self

    def build(self) -> UpdateEmployeeTypeEnumRequest:
        return self._update_employee_type_enum_request
