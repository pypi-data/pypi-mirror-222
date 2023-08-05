# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class GetChatAnnouncementResponseBody(object):
    _types = {
        "content": str,
        "revision": str,
        "create_time": str,
        "update_time": str,
        "owner_id_type": str,
        "owner_id": str,
        "modifier_id_type": str,
        "modifier_id": str,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.revision: Optional[str] = None
        self.create_time: Optional[str] = None
        self.update_time: Optional[str] = None
        self.owner_id_type: Optional[str] = None
        self.owner_id: Optional[str] = None
        self.modifier_id_type: Optional[str] = None
        self.modifier_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetChatAnnouncementResponseBodyBuilder":
        return GetChatAnnouncementResponseBodyBuilder()


class GetChatAnnouncementResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_chat_announcement_response_body = GetChatAnnouncementResponseBody()

    def content(self, content: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.content = content
        return self

    def revision(self, revision: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.revision = revision
        return self

    def create_time(self, create_time: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.create_time = create_time
        return self

    def update_time(self, update_time: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.update_time = update_time
        return self

    def owner_id_type(self, owner_id_type: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.owner_id_type = owner_id_type
        return self

    def owner_id(self, owner_id: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.owner_id = owner_id
        return self

    def modifier_id_type(self, modifier_id_type: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.modifier_id_type = modifier_id_type
        return self

    def modifier_id(self, modifier_id: str) -> "GetChatAnnouncementResponseBodyBuilder":
        self._get_chat_announcement_response_body.modifier_id = modifier_id
        return self

    def build(self) -> "GetChatAnnouncementResponseBody":
        return self._get_chat_announcement_response_body
