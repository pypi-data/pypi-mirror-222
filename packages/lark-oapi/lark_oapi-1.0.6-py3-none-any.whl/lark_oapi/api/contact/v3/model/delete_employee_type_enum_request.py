# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteEmployeeTypeEnumRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.enum_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteEmployeeTypeEnumRequestBuilder":
        return DeleteEmployeeTypeEnumRequestBuilder()


class DeleteEmployeeTypeEnumRequestBuilder(object):

    def __init__(self) -> None:
        delete_employee_type_enum_request = DeleteEmployeeTypeEnumRequest()
        delete_employee_type_enum_request.http_method = HttpMethod.DELETE
        delete_employee_type_enum_request.uri = "/open-apis/contact/v3/employee_type_enums/:enum_id"
        delete_employee_type_enum_request.token_types = {AccessTokenType.TENANT}
        self._delete_employee_type_enum_request: DeleteEmployeeTypeEnumRequest = delete_employee_type_enum_request

    def enum_id(self, enum_id: str) -> "DeleteEmployeeTypeEnumRequestBuilder":
        self._delete_employee_type_enum_request.enum_id = enum_id
        self._delete_employee_type_enum_request.paths["enum_id"] = str(enum_id)
        return self

    def build(self) -> DeleteEmployeeTypeEnumRequest:
        return self._delete_employee_type_enum_request
