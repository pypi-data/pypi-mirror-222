# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_work_city_response_body import GetWorkCityResponseBody


class GetWorkCityResponse(BaseResponse):
    _types = {
        "data": GetWorkCityResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetWorkCityResponseBody] = None
        init(self, d, self._types)
