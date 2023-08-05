# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .upload_image_response_body import UploadImageResponseBody


class UploadImageResponse(BaseResponse):
    _types = {
        "data": UploadImageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UploadImageResponseBody] = None
        init(self, d, self._types)
