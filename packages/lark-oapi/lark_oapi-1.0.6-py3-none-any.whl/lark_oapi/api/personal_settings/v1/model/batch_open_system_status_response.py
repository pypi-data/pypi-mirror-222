# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_open_system_status_response_body import BatchOpenSystemStatusResponseBody


class BatchOpenSystemStatusResponse(BaseResponse):
    _types = {
        "data": BatchOpenSystemStatusResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchOpenSystemStatusResponseBody] = None
        init(self, d, self._types)
