# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .query_user_stats_field_request_body import QueryUserStatsFieldRequestBody


class QueryUserStatsFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.request_body: Optional[QueryUserStatsFieldRequestBody] = None

    @staticmethod
    def builder() -> "QueryUserStatsFieldRequestBuilder":
        return QueryUserStatsFieldRequestBuilder()


class QueryUserStatsFieldRequestBuilder(object):

    def __init__(self) -> None:
        query_user_stats_field_request = QueryUserStatsFieldRequest()
        query_user_stats_field_request.http_method = HttpMethod.POST
        query_user_stats_field_request.uri = "/open-apis/attendance/v1/user_stats_fields/query"
        query_user_stats_field_request.token_types = {AccessTokenType.TENANT}
        self._query_user_stats_field_request: QueryUserStatsFieldRequest = query_user_stats_field_request

    def employee_type(self, employee_type: str) -> "QueryUserStatsFieldRequestBuilder":
        self._query_user_stats_field_request.employee_type = employee_type
        self._query_user_stats_field_request.add_query("employee_type", employee_type)
        return self

    def request_body(self, request_body: QueryUserStatsFieldRequestBody) -> "QueryUserStatsFieldRequestBuilder":
        self._query_user_stats_field_request.request_body = request_body
        self._query_user_stats_field_request.body = request_body
        return self

    def build(self) -> QueryUserStatsFieldRequest:
        return self._query_user_stats_field_request
