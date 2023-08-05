# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_id import UserId


class EventSender(object):
    _types = {
        "sender_id": UserId,
        "sender_type": str,
        "tenant_key": str,
    }

    def __init__(self, d=None):
        self.sender_id: Optional[UserId] = None
        self.sender_type: Optional[str] = None
        self.tenant_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventSenderBuilder":
        return EventSenderBuilder()


class EventSenderBuilder(object):
    def __init__(self) -> None:
        self._event_sender = EventSender()

    def sender_id(self, sender_id: UserId) -> "EventSenderBuilder":
        self._event_sender.sender_id = sender_id
        return self

    def sender_type(self, sender_type: str) -> "EventSenderBuilder":
        self._event_sender.sender_type = sender_type
        return self

    def tenant_key(self, tenant_key: str) -> "EventSenderBuilder":
        self._event_sender.tenant_key = tenant_key
        return self

    def build(self) -> "EventSender":
        return self._event_sender
