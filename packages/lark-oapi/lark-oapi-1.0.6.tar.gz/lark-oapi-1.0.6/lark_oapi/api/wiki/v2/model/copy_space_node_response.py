# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .copy_space_node_response_body import CopySpaceNodeResponseBody


class CopySpaceNodeResponse(BaseResponse):
    _types = {
        "data": CopySpaceNodeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CopySpaceNodeResponseBody] = None
        init(self, d, self._types)
