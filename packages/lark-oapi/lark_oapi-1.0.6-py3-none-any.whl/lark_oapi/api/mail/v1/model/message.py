# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mail_address import MailAddress


class Message(object):
    _types = {
        "raw": str,
        "subject": str,
        "to": List[MailAddress],
        "cc": List[MailAddress],
        "bcc": List[MailAddress],
        "head_from": MailAddress,
        "body_html": str,
        "internal_date": int,
        "message_state": int,
        "smtp_message_id": str,
        "message_id": str,
        "body_plain_text": str,
    }

    def __init__(self, d=None):
        self.raw: Optional[str] = None
        self.subject: Optional[str] = None
        self.to: Optional[List[MailAddress]] = None
        self.cc: Optional[List[MailAddress]] = None
        self.bcc: Optional[List[MailAddress]] = None
        self.head_from: Optional[MailAddress] = None
        self.body_html: Optional[str] = None
        self.internal_date: Optional[int] = None
        self.message_state: Optional[int] = None
        self.smtp_message_id: Optional[str] = None
        self.message_id: Optional[str] = None
        self.body_plain_text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessageBuilder":
        return MessageBuilder()


class MessageBuilder(object):
    def __init__(self) -> None:
        self._message = Message()

    def raw(self, raw: str) -> "MessageBuilder":
        self._message.raw = raw
        return self

    def subject(self, subject: str) -> "MessageBuilder":
        self._message.subject = subject
        return self

    def to(self, to: List[MailAddress]) -> "MessageBuilder":
        self._message.to = to
        return self

    def cc(self, cc: List[MailAddress]) -> "MessageBuilder":
        self._message.cc = cc
        return self

    def bcc(self, bcc: List[MailAddress]) -> "MessageBuilder":
        self._message.bcc = bcc
        return self

    def head_from(self, head_from: MailAddress) -> "MessageBuilder":
        self._message.head_from = head_from
        return self

    def body_html(self, body_html: str) -> "MessageBuilder":
        self._message.body_html = body_html
        return self

    def internal_date(self, internal_date: int) -> "MessageBuilder":
        self._message.internal_date = internal_date
        return self

    def message_state(self, message_state: int) -> "MessageBuilder":
        self._message.message_state = message_state
        return self

    def smtp_message_id(self, smtp_message_id: str) -> "MessageBuilder":
        self._message.smtp_message_id = smtp_message_id
        return self

    def message_id(self, message_id: str) -> "MessageBuilder":
        self._message.message_id = message_id
        return self

    def body_plain_text(self, body_plain_text: str) -> "MessageBuilder":
        self._message.body_plain_text = body_plain_text
        return self

    def build(self) -> "Message":
        return self._message
