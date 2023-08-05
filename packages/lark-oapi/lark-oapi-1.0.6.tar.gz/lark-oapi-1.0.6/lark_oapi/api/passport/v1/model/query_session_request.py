# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .query_session_request_body import QuerySessionRequestBody


class QuerySessionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[QuerySessionRequestBody] = None

    @staticmethod
    def builder() -> "QuerySessionRequestBuilder":
        return QuerySessionRequestBuilder()


class QuerySessionRequestBuilder(object):

    def __init__(self) -> None:
        query_session_request = QuerySessionRequest()
        query_session_request.http_method = HttpMethod.POST
        query_session_request.uri = "/open-apis/passport/v1/sessions/query"
        query_session_request.token_types = {AccessTokenType.TENANT}
        self._query_session_request: QuerySessionRequest = query_session_request

    def user_id_type(self, user_id_type: str) -> "QuerySessionRequestBuilder":
        self._query_session_request.user_id_type = user_id_type
        self._query_session_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: QuerySessionRequestBody) -> "QuerySessionRequestBuilder":
        self._query_session_request.request_body = request_body
        self._query_session_request.body = request_body
        return self

    def build(self) -> QuerySessionRequest:
        return self._query_session_request
