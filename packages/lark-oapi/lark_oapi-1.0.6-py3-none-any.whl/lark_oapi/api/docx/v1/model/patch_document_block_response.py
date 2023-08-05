# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_document_block_response_body import PatchDocumentBlockResponseBody


class PatchDocumentBlockResponse(BaseResponse):
    _types = {
        "data": PatchDocumentBlockResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchDocumentBlockResponseBody] = None
        init(self, d, self._types)
