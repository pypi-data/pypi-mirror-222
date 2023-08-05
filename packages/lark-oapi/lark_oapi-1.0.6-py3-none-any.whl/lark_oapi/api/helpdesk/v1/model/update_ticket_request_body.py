# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .customized_field_display_item import CustomizedFieldDisplayItem


class UpdateTicketRequestBody(object):
    _types = {
        "status": int,
        "tag_names": List[str],
        "comment": str,
        "customized_fields": List[CustomizedFieldDisplayItem],
        "ticket_type": int,
        "solved": int,
        "channel": int,
    }

    def __init__(self, d=None):
        self.status: Optional[int] = None
        self.tag_names: Optional[List[str]] = None
        self.comment: Optional[str] = None
        self.customized_fields: Optional[List[CustomizedFieldDisplayItem]] = None
        self.ticket_type: Optional[int] = None
        self.solved: Optional[int] = None
        self.channel: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateTicketRequestBodyBuilder":
        return UpdateTicketRequestBodyBuilder()


class UpdateTicketRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._update_ticket_request_body = UpdateTicketRequestBody()

    def status(self, status: int) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.status = status
        return self

    def tag_names(self, tag_names: List[str]) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.tag_names = tag_names
        return self

    def comment(self, comment: str) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.comment = comment
        return self

    def customized_fields(self,
                          customized_fields: List[CustomizedFieldDisplayItem]) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.customized_fields = customized_fields
        return self

    def ticket_type(self, ticket_type: int) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.ticket_type = ticket_type
        return self

    def solved(self, solved: int) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.solved = solved
        return self

    def channel(self, channel: int) -> "UpdateTicketRequestBodyBuilder":
        self._update_ticket_request_body.channel = channel
        return self

    def build(self) -> "UpdateTicketRequestBody":
        return self._update_ticket_request_body
