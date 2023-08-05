# Code generated by Lark OpenAPI.

from typing import *
from typing import IO

from lark_oapi.core.construct import init


class UploadAllMediaRequestBody(object):
    _types = {
        "file_name": str,
        "parent_type": str,
        "parent_node": str,
        "size": int,
        "checksum": str,
        "extra": str,
        "file": IO[Any],
    }

    def __init__(self, d=None):
        self.file_name: Optional[str] = None
        self.parent_type: Optional[str] = None
        self.parent_node: Optional[str] = None
        self.size: Optional[int] = None
        self.checksum: Optional[str] = None
        self.extra: Optional[str] = None
        self.file: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadAllMediaRequestBodyBuilder":
        return UploadAllMediaRequestBodyBuilder()


class UploadAllMediaRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_all_media_request_body = UploadAllMediaRequestBody()

    def file_name(self, file_name: str) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.file_name = file_name
        return self

    def parent_type(self, parent_type: str) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.parent_type = parent_type
        return self

    def parent_node(self, parent_node: str) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.parent_node = parent_node
        return self

    def size(self, size: int) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.size = size
        return self

    def checksum(self, checksum: str) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.checksum = checksum
        return self

    def extra(self, extra: str) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.extra = extra
        return self

    def file(self, file: IO[Any]) -> "UploadAllMediaRequestBodyBuilder":
        self._upload_all_media_request_body.file = file
        return self

    def build(self) -> "UploadAllMediaRequestBody":
        return self._upload_all_media_request_body
