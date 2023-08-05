# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TicketMessage(object):
    _types = {
        "id": str,
        "message_id": str,
        "message_type": str,
        "created_at": int,
        "content": str,
        "user_name": str,
        "avatar_url": str,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.message_id: Optional[str] = None
        self.message_type: Optional[str] = None
        self.created_at: Optional[int] = None
        self.content: Optional[str] = None
        self.user_name: Optional[str] = None
        self.avatar_url: Optional[str] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TicketMessageBuilder":
        return TicketMessageBuilder()


class TicketMessageBuilder(object):
    def __init__(self) -> None:
        self._ticket_message = TicketMessage()

    def id(self, id: str) -> "TicketMessageBuilder":
        self._ticket_message.id = id
        return self

    def message_id(self, message_id: str) -> "TicketMessageBuilder":
        self._ticket_message.message_id = message_id
        return self

    def message_type(self, message_type: str) -> "TicketMessageBuilder":
        self._ticket_message.message_type = message_type
        return self

    def created_at(self, created_at: int) -> "TicketMessageBuilder":
        self._ticket_message.created_at = created_at
        return self

    def content(self, content: str) -> "TicketMessageBuilder":
        self._ticket_message.content = content
        return self

    def user_name(self, user_name: str) -> "TicketMessageBuilder":
        self._ticket_message.user_name = user_name
        return self

    def avatar_url(self, avatar_url: str) -> "TicketMessageBuilder":
        self._ticket_message.avatar_url = avatar_url
        return self

    def user_id(self, user_id: str) -> "TicketMessageBuilder":
        self._ticket_message.user_id = user_id
        return self

    def build(self) -> "TicketMessage":
        return self._ticket_message
