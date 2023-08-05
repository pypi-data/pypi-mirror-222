# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .change_employee_stage import ChangeEmployeeStage


class PatchEmployeeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.employee_id: Optional[str] = None
        self.request_body: Optional[ChangeEmployeeStage] = None

    @staticmethod
    def builder() -> "PatchEmployeeRequestBuilder":
        return PatchEmployeeRequestBuilder()


class PatchEmployeeRequestBuilder(object):

    def __init__(self) -> None:
        patch_employee_request = PatchEmployeeRequest()
        patch_employee_request.http_method = HttpMethod.PATCH
        patch_employee_request.uri = "/open-apis/hire/v1/employees/:employee_id"
        patch_employee_request.token_types = {AccessTokenType.TENANT}
        self._patch_employee_request: PatchEmployeeRequest = patch_employee_request

    def user_id_type(self, user_id_type: str) -> "PatchEmployeeRequestBuilder":
        self._patch_employee_request.user_id_type = user_id_type
        self._patch_employee_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "PatchEmployeeRequestBuilder":
        self._patch_employee_request.department_id_type = department_id_type
        self._patch_employee_request.add_query("department_id_type", department_id_type)
        return self

    def employee_id(self, employee_id: str) -> "PatchEmployeeRequestBuilder":
        self._patch_employee_request.employee_id = employee_id
        self._patch_employee_request.paths["employee_id"] = str(employee_id)
        return self

    def request_body(self, request_body: ChangeEmployeeStage) -> "PatchEmployeeRequestBuilder":
        self._patch_employee_request.request_body = request_body
        self._patch_employee_request.body = request_body
        return self

    def build(self) -> PatchEmployeeRequest:
        return self._patch_employee_request
