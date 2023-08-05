# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Url(object):
    _types = {
        "text": str,
        "link": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UrlBuilder":
        return UrlBuilder()


class UrlBuilder(object):
    def __init__(self) -> None:
        self._url = Url()

    def text(self, text: str) -> "UrlBuilder":
        self._url.text = text
        return self

    def link(self, link: str) -> "UrlBuilder":
        self._url.link = link
        return self

    def build(self) -> "Url":
        return self._url
