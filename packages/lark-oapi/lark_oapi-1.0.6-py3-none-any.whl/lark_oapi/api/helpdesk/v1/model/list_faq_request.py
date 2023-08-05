# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListFaqRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.category_id: Optional[str] = None
        self.status: Optional[str] = None
        self.search: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListFaqRequestBuilder":
        return ListFaqRequestBuilder()


class ListFaqRequestBuilder(object):

    def __init__(self) -> None:
        list_faq_request = ListFaqRequest()
        list_faq_request.http_method = HttpMethod.GET
        list_faq_request.uri = "/open-apis/helpdesk/v1/faqs"
        list_faq_request.token_types = {AccessTokenType.TENANT}
        self._list_faq_request: ListFaqRequest = list_faq_request

    def category_id(self, category_id: str) -> "ListFaqRequestBuilder":
        self._list_faq_request.category_id = category_id
        self._list_faq_request.add_query("category_id", category_id)
        return self

    def status(self, status: str) -> "ListFaqRequestBuilder":
        self._list_faq_request.status = status
        self._list_faq_request.add_query("status", status)
        return self

    def search(self, search: str) -> "ListFaqRequestBuilder":
        self._list_faq_request.search = search
        self._list_faq_request.add_query("search", search)
        return self

    def page_token(self, page_token: str) -> "ListFaqRequestBuilder":
        self._list_faq_request.page_token = page_token
        self._list_faq_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListFaqRequestBuilder":
        self._list_faq_request.page_size = page_size
        self._list_faq_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListFaqRequest:
        return self._list_faq_request
