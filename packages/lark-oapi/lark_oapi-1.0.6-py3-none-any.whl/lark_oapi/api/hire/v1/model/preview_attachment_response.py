# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .preview_attachment_response_body import PreviewAttachmentResponseBody


class PreviewAttachmentResponse(BaseResponse):
    _types = {
        "data": PreviewAttachmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PreviewAttachmentResponseBody] = None
        init(self, d, self._types)
