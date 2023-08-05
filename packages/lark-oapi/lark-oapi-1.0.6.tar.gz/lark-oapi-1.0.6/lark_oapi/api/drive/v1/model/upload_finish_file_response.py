# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_finish_file_response_body import UploadFinishFileResponseBody


class UploadFinishFileResponse(BaseResponse):
    _types = {
        "data": UploadFinishFileResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UploadFinishFileResponseBody] = None
        init(self, d, self._types)
