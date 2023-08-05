# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .file import File


class FileList(object):
    _types = {
        "files": List[File],
    }

    def __init__(self, d=None):
        self.files: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileListBuilder":
        return FileListBuilder()


class FileListBuilder(object):
    def __init__(self) -> None:
        self._file_list = FileList()

    def files(self, files: List[File]) -> "FileListBuilder":
        self._file_list.files = files
        return self

    def build(self) -> "FileList":
        return self._file_list
