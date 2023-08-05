# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_badge_response_body import UpdateBadgeResponseBody


class UpdateBadgeResponse(BaseResponse):
    _types = {
        "data": UpdateBadgeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateBadgeResponseBody] = None
        init(self, d, self._types)
