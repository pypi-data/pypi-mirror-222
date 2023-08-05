# Code generated by Lark OpenAPI.

from typing import *
from typing import IO

from lark_oapi.core.construct import init


class File(object):
    _types = {
        "name": str,
        "file": IO[Any],
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.file: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileBuilder":
        return FileBuilder()


class FileBuilder(object):
    def __init__(self) -> None:
        self._file = File()

    def name(self, name: str) -> "FileBuilder":
        self._file.name = name
        return self

    def file(self, file: IO[Any]) -> "FileBuilder":
        self._file.file = file
        return self

    def build(self) -> "File":
        return self._file
