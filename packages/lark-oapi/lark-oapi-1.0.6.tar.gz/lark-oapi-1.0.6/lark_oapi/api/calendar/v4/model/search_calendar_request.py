# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .search_calendar_request_body import SearchCalendarRequestBody


class SearchCalendarRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.request_body: Optional[SearchCalendarRequestBody] = None

    @staticmethod
    def builder() -> "SearchCalendarRequestBuilder":
        return SearchCalendarRequestBuilder()


class SearchCalendarRequestBuilder(object):

    def __init__(self) -> None:
        search_calendar_request = SearchCalendarRequest()
        search_calendar_request.http_method = HttpMethod.POST
        search_calendar_request.uri = "/open-apis/calendar/v4/calendars/search"
        search_calendar_request.token_types = {AccessTokenType.TENANT}
        self._search_calendar_request: SearchCalendarRequest = search_calendar_request

    def page_token(self, page_token: str) -> "SearchCalendarRequestBuilder":
        self._search_calendar_request.page_token = page_token
        self._search_calendar_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "SearchCalendarRequestBuilder":
        self._search_calendar_request.page_size = page_size
        self._search_calendar_request.add_query("page_size", page_size)
        return self

    def request_body(self, request_body: SearchCalendarRequestBody) -> "SearchCalendarRequestBuilder":
        self._search_calendar_request.request_body = request_body
        self._search_calendar_request.body = request_body
        return self

    def build(self) -> SearchCalendarRequest:
        return self._search_calendar_request
