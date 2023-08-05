# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class File(object):
    _types = {
        "file_id": str,
    }

    def __init__(self, d=None):
        self.file_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileBuilder":
        return FileBuilder()


class FileBuilder(object):
    def __init__(self) -> None:
        self._file = File()

    def file_id(self, file_id: str) -> "FileBuilder":
        self._file.file_id = file_id
        return self

    def build(self) -> "File":
        return self._file
