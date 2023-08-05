# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .set_host_meeting_request_body import SetHostMeetingRequestBody


class SetHostMeetingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.meeting_id: Optional[int] = None
        self.request_body: Optional[SetHostMeetingRequestBody] = None

    @staticmethod
    def builder() -> "SetHostMeetingRequestBuilder":
        return SetHostMeetingRequestBuilder()


class SetHostMeetingRequestBuilder(object):

    def __init__(self) -> None:
        set_host_meeting_request = SetHostMeetingRequest()
        set_host_meeting_request.http_method = HttpMethod.PATCH
        set_host_meeting_request.uri = "/open-apis/vc/v1/meetings/:meeting_id/set_host"
        set_host_meeting_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._set_host_meeting_request: SetHostMeetingRequest = set_host_meeting_request

    def user_id_type(self, user_id_type: str) -> "SetHostMeetingRequestBuilder":
        self._set_host_meeting_request.user_id_type = user_id_type
        self._set_host_meeting_request.add_query("user_id_type", user_id_type)
        return self

    def meeting_id(self, meeting_id: int) -> "SetHostMeetingRequestBuilder":
        self._set_host_meeting_request.meeting_id = meeting_id
        self._set_host_meeting_request.paths["meeting_id"] = str(meeting_id)
        return self

    def request_body(self, request_body: SetHostMeetingRequestBody) -> "SetHostMeetingRequestBuilder":
        self._set_host_meeting_request.request_body = request_body
        self._set_host_meeting_request.body = request_body
        return self

    def build(self) -> SetHostMeetingRequest:
        return self._set_host_meeting_request
