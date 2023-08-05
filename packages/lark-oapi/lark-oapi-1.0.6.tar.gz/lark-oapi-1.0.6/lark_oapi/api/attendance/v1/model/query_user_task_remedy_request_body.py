# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class QueryUserTaskRemedyRequestBody(object):
    _types = {
        "user_ids": List[str],
        "check_time_from": str,
        "check_time_to": str,
        "check_date_type": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.user_ids: Optional[List[str]] = None
        self.check_time_from: Optional[str] = None
        self.check_time_to: Optional[str] = None
        self.check_date_type: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserTaskRemedyRequestBodyBuilder":
        return QueryUserTaskRemedyRequestBodyBuilder()


class QueryUserTaskRemedyRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_task_remedy_request_body = QueryUserTaskRemedyRequestBody()

    def user_ids(self, user_ids: List[str]) -> "QueryUserTaskRemedyRequestBodyBuilder":
        self._query_user_task_remedy_request_body.user_ids = user_ids
        return self

    def check_time_from(self, check_time_from: str) -> "QueryUserTaskRemedyRequestBodyBuilder":
        self._query_user_task_remedy_request_body.check_time_from = check_time_from
        return self

    def check_time_to(self, check_time_to: str) -> "QueryUserTaskRemedyRequestBodyBuilder":
        self._query_user_task_remedy_request_body.check_time_to = check_time_to
        return self

    def check_date_type(self, check_date_type: str) -> "QueryUserTaskRemedyRequestBodyBuilder":
        self._query_user_task_remedy_request_body.check_date_type = check_date_type
        return self

    def status(self, status: int) -> "QueryUserTaskRemedyRequestBodyBuilder":
        self._query_user_task_remedy_request_body.status = status
        return self

    def build(self) -> "QueryUserTaskRemedyRequestBody":
        return self._query_user_task_remedy_request_body
