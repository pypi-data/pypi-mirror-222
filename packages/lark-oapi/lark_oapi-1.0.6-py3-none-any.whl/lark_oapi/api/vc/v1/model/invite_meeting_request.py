# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .invite_meeting_request_body import InviteMeetingRequestBody


class InviteMeetingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.meeting_id: Optional[int] = None
        self.request_body: Optional[InviteMeetingRequestBody] = None

    @staticmethod
    def builder() -> "InviteMeetingRequestBuilder":
        return InviteMeetingRequestBuilder()


class InviteMeetingRequestBuilder(object):

    def __init__(self) -> None:
        invite_meeting_request = InviteMeetingRequest()
        invite_meeting_request.http_method = HttpMethod.PATCH
        invite_meeting_request.uri = "/open-apis/vc/v1/meetings/:meeting_id/invite"
        invite_meeting_request.token_types = {AccessTokenType.USER}
        self._invite_meeting_request: InviteMeetingRequest = invite_meeting_request

    def user_id_type(self, user_id_type: str) -> "InviteMeetingRequestBuilder":
        self._invite_meeting_request.user_id_type = user_id_type
        self._invite_meeting_request.add_query("user_id_type", user_id_type)
        return self

    def meeting_id(self, meeting_id: int) -> "InviteMeetingRequestBuilder":
        self._invite_meeting_request.meeting_id = meeting_id
        self._invite_meeting_request.paths["meeting_id"] = str(meeting_id)
        return self

    def request_body(self, request_body: InviteMeetingRequestBody) -> "InviteMeetingRequestBuilder":
        self._invite_meeting_request.request_body = request_body
        self._invite_meeting_request.body = request_body
        return self

    def build(self) -> InviteMeetingRequest:
        return self._invite_meeting_request
