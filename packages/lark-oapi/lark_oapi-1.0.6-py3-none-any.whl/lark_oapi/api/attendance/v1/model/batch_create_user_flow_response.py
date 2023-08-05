# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_create_user_flow_response_body import BatchCreateUserFlowResponseBody


class BatchCreateUserFlowResponse(BaseResponse):
    _types = {
        "data": BatchCreateUserFlowResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchCreateUserFlowResponseBody] = None
        init(self, d, self._types)
