# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_create_user_daily_shift_response_body import BatchCreateUserDailyShiftResponseBody


class BatchCreateUserDailyShiftResponse(BaseResponse):
    _types = {
        "data": BatchCreateUserDailyShiftResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchCreateUserDailyShiftResponseBody] = None
        init(self, d, self._types)
