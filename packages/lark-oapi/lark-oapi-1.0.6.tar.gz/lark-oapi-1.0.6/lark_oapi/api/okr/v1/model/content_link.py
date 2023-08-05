# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ContentLink(object):
    _types = {
        "url": str,
    }

    def __init__(self, d=None):
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentLinkBuilder":
        return ContentLinkBuilder()


class ContentLinkBuilder(object):
    def __init__(self) -> None:
        self._content_link = ContentLink()

    def url(self, url: str) -> "ContentLinkBuilder":
        self._content_link.url = url
        return self

    def build(self) -> "ContentLink":
        return self._content_link
