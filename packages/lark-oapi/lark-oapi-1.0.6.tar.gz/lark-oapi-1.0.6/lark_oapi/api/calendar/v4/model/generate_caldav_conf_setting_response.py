# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .generate_caldav_conf_setting_response_body import GenerateCaldavConfSettingResponseBody


class GenerateCaldavConfSettingResponse(BaseResponse):
    _types = {
        "data": GenerateCaldavConfSettingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GenerateCaldavConfSettingResponseBody] = None
        init(self, d, self._types)
