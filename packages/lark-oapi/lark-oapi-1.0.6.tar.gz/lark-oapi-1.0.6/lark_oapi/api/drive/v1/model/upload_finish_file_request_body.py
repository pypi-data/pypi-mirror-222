# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UploadFinishFileRequestBody(object):
    _types = {
        "upload_id": str,
        "block_num": int,
    }

    def __init__(self, d=None):
        self.upload_id: Optional[str] = None
        self.block_num: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadFinishFileRequestBodyBuilder":
        return UploadFinishFileRequestBodyBuilder()


class UploadFinishFileRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_finish_file_request_body = UploadFinishFileRequestBody()

    def upload_id(self, upload_id: str) -> "UploadFinishFileRequestBodyBuilder":
        self._upload_finish_file_request_body.upload_id = upload_id
        return self

    def block_num(self, block_num: int) -> "UploadFinishFileRequestBodyBuilder":
        self._upload_finish_file_request_body.block_num = block_num
        return self

    def build(self) -> "UploadFinishFileRequestBody":
        return self._upload_finish_file_request_body
