# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UploadPrepareFileResponseBody(object):
    _types = {
        "upload_id": str,
        "block_size": int,
        "block_num": int,
    }

    def __init__(self, d=None):
        self.upload_id: Optional[str] = None
        self.block_size: Optional[int] = None
        self.block_num: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadPrepareFileResponseBodyBuilder":
        return UploadPrepareFileResponseBodyBuilder()


class UploadPrepareFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_prepare_file_response_body = UploadPrepareFileResponseBody()

    def upload_id(self, upload_id: str) -> "UploadPrepareFileResponseBodyBuilder":
        self._upload_prepare_file_response_body.upload_id = upload_id
        return self

    def block_size(self, block_size: int) -> "UploadPrepareFileResponseBodyBuilder":
        self._upload_prepare_file_response_body.block_size = block_size
        return self

    def block_num(self, block_num: int) -> "UploadPrepareFileResponseBodyBuilder":
        self._upload_prepare_file_response_body.block_num = block_num
        return self

    def build(self) -> "UploadPrepareFileResponseBody":
        return self._upload_prepare_file_response_body
