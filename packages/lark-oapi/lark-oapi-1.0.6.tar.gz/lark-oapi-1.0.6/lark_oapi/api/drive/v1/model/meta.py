# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Meta(object):
    _types = {
        "doc_token": str,
        "doc_type": str,
        "title": str,
        "owner_id": str,
        "create_time": int,
        "latest_modify_user": str,
        "latest_modify_time": int,
        "url": str,
        "sec_label_name": str,
    }

    def __init__(self, d=None):
        self.doc_token: Optional[str] = None
        self.doc_type: Optional[str] = None
        self.title: Optional[str] = None
        self.owner_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.latest_modify_user: Optional[str] = None
        self.latest_modify_time: Optional[int] = None
        self.url: Optional[str] = None
        self.sec_label_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetaBuilder":
        return MetaBuilder()


class MetaBuilder(object):
    def __init__(self) -> None:
        self._meta = Meta()

    def doc_token(self, doc_token: str) -> "MetaBuilder":
        self._meta.doc_token = doc_token
        return self

    def doc_type(self, doc_type: str) -> "MetaBuilder":
        self._meta.doc_type = doc_type
        return self

    def title(self, title: str) -> "MetaBuilder":
        self._meta.title = title
        return self

    def owner_id(self, owner_id: str) -> "MetaBuilder":
        self._meta.owner_id = owner_id
        return self

    def create_time(self, create_time: int) -> "MetaBuilder":
        self._meta.create_time = create_time
        return self

    def latest_modify_user(self, latest_modify_user: str) -> "MetaBuilder":
        self._meta.latest_modify_user = latest_modify_user
        return self

    def latest_modify_time(self, latest_modify_time: int) -> "MetaBuilder":
        self._meta.latest_modify_time = latest_modify_time
        return self

    def url(self, url: str) -> "MetaBuilder":
        self._meta.url = url
        return self

    def sec_label_name(self, sec_label_name: str) -> "MetaBuilder":
        self._meta.sec_label_name = sec_label_name
        return self

    def build(self) -> "Meta":
        return self._meta
