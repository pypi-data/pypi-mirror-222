# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .search_entity_request_body import SearchEntityRequestBody


class SearchEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[SearchEntityRequestBody] = None

    @staticmethod
    def builder() -> "SearchEntityRequestBuilder":
        return SearchEntityRequestBuilder()


class SearchEntityRequestBuilder(object):

    def __init__(self) -> None:
        search_entity_request = SearchEntityRequest()
        search_entity_request.http_method = HttpMethod.POST
        search_entity_request.uri = "/open-apis/baike/v1/entities/search"
        search_entity_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._search_entity_request: SearchEntityRequest = search_entity_request

    def page_size(self, page_size: int) -> "SearchEntityRequestBuilder":
        self._search_entity_request.page_size = page_size
        self._search_entity_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchEntityRequestBuilder":
        self._search_entity_request.page_token = page_token
        self._search_entity_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "SearchEntityRequestBuilder":
        self._search_entity_request.user_id_type = user_id_type
        self._search_entity_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: SearchEntityRequestBody) -> "SearchEntityRequestBuilder":
        self._search_entity_request.request_body = request_body
        self._search_entity_request.body = request_body
        return self

    def build(self) -> SearchEntityRequest:
        return self._search_entity_request
