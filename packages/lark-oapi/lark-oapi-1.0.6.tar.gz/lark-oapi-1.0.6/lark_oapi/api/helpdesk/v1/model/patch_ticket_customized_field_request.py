# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .ticket_customized_field import TicketCustomizedField


class PatchTicketCustomizedFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_customized_field_id: Optional[str] = None
        self.request_body: Optional[TicketCustomizedField] = None

    @staticmethod
    def builder() -> "PatchTicketCustomizedFieldRequestBuilder":
        return PatchTicketCustomizedFieldRequestBuilder()


class PatchTicketCustomizedFieldRequestBuilder(object):

    def __init__(self) -> None:
        patch_ticket_customized_field_request = PatchTicketCustomizedFieldRequest()
        patch_ticket_customized_field_request.http_method = HttpMethod.PATCH
        patch_ticket_customized_field_request.uri = "/open-apis/helpdesk/v1/ticket_customized_fields/:ticket_customized_field_id"
        patch_ticket_customized_field_request.token_types = {AccessTokenType.USER}
        self._patch_ticket_customized_field_request: PatchTicketCustomizedFieldRequest = patch_ticket_customized_field_request

    def ticket_customized_field_id(self, ticket_customized_field_id: str) -> "PatchTicketCustomizedFieldRequestBuilder":
        self._patch_ticket_customized_field_request.ticket_customized_field_id = ticket_customized_field_id
        self._patch_ticket_customized_field_request.paths["ticket_customized_field_id"] = str(
            ticket_customized_field_id)
        return self

    def request_body(self, request_body: TicketCustomizedField) -> "PatchTicketCustomizedFieldRequestBuilder":
        self._patch_ticket_customized_field_request.request_body = request_body
        self._patch_ticket_customized_field_request.body = request_body
        return self

    def build(self) -> PatchTicketCustomizedFieldRequest:
        return self._patch_ticket_customized_field_request
