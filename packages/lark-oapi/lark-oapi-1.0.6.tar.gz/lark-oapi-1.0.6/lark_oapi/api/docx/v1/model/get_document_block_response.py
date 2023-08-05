# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_document_block_response_body import GetDocumentBlockResponseBody


class GetDocumentBlockResponse(BaseResponse):
    _types = {
        "data": GetDocumentBlockResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetDocumentBlockResponseBody] = None
        init(self, d, self._types)
