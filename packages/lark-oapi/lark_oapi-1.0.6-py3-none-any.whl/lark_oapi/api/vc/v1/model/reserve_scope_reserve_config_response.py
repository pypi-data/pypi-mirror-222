# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .reserve_scope_reserve_config_response_body import ReserveScopeReserveConfigResponseBody


class ReserveScopeReserveConfigResponse(BaseResponse):
    _types = {
        "data": ReserveScopeReserveConfigResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ReserveScopeReserveConfigResponseBody] = None
        init(self, d, self._types)
