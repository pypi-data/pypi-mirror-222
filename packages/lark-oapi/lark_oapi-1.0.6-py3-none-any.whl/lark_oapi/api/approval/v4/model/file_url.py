# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FileUrl(object):
    _types = {
        "name": str,
        "url": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileUrlBuilder":
        return FileUrlBuilder()


class FileUrlBuilder(object):
    def __init__(self) -> None:
        self._file_url = FileUrl()

    def name(self, name: str) -> "FileUrlBuilder":
        self._file_url.name = name
        return self

    def url(self, url: str) -> "FileUrlBuilder":
        self._file_url.url = url
        return self

    def build(self) -> "FileUrl":
        return self._file_url
