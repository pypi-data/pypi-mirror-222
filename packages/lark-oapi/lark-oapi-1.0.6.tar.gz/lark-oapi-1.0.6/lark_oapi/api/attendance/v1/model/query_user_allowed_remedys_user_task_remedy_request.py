# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .query_user_allowed_remedys_user_task_remedy_request_body import QueryUserAllowedRemedysUserTaskRemedyRequestBody


class QueryUserAllowedRemedysUserTaskRemedyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[QueryUserAllowedRemedysUserTaskRemedyRequestBody] = None

    @staticmethod
    def builder() -> "QueryUserAllowedRemedysUserTaskRemedyRequestBuilder":
        return QueryUserAllowedRemedysUserTaskRemedyRequestBuilder()


class QueryUserAllowedRemedysUserTaskRemedyRequestBuilder(object):

    def __init__(self) -> None:
        query_user_allowed_remedys_user_task_remedy_request = QueryUserAllowedRemedysUserTaskRemedyRequest()
        query_user_allowed_remedys_user_task_remedy_request.http_method = HttpMethod.POST
        query_user_allowed_remedys_user_task_remedy_request.uri = "/open-apis/attendance/v1/user_task_remedys/query_user_allowed_remedys"
        query_user_allowed_remedys_user_task_remedy_request.token_types = {AccessTokenType.TENANT}
        self._query_user_allowed_remedys_user_task_remedy_request: QueryUserAllowedRemedysUserTaskRemedyRequest = query_user_allowed_remedys_user_task_remedy_request

    def employee_type(self, employee_type: str) -> "QueryUserAllowedRemedysUserTaskRemedyRequestBuilder":
        self._query_user_allowed_remedys_user_task_remedy_request.employee_type = employee_type
        self._query_user_allowed_remedys_user_task_remedy_request.add_query("employee_type", employee_type)
        return self

    def request_body(self,
                     request_body: QueryUserAllowedRemedysUserTaskRemedyRequestBody) -> "QueryUserAllowedRemedysUserTaskRemedyRequestBuilder":
        self._query_user_allowed_remedys_user_task_remedy_request.request_body = request_body
        self._query_user_allowed_remedys_user_task_remedy_request.body = request_body
        return self

    def build(self) -> QueryUserAllowedRemedysUserTaskRemedyRequest:
        return self._query_user_allowed_remedys_user_task_remedy_request
