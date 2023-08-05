# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteTimeoffEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.timeoff_event_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteTimeoffEventRequestBuilder":
        return DeleteTimeoffEventRequestBuilder()


class DeleteTimeoffEventRequestBuilder(object):

    def __init__(self) -> None:
        delete_timeoff_event_request = DeleteTimeoffEventRequest()
        delete_timeoff_event_request.http_method = HttpMethod.DELETE
        delete_timeoff_event_request.uri = "/open-apis/calendar/v4/timeoff_events/:timeoff_event_id"
        delete_timeoff_event_request.token_types = {AccessTokenType.TENANT}
        self._delete_timeoff_event_request: DeleteTimeoffEventRequest = delete_timeoff_event_request

    def timeoff_event_id(self, timeoff_event_id: str) -> "DeleteTimeoffEventRequestBuilder":
        self._delete_timeoff_event_request.timeoff_event_id = timeoff_event_id
        self._delete_timeoff_event_request.paths["timeoff_event_id"] = str(timeoff_event_id)
        return self

    def build(self) -> DeleteTimeoffEventRequest:
        return self._delete_timeoff_event_request
