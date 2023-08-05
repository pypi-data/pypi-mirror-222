# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_application_app_version_response_body import GetApplicationAppVersionResponseBody


class GetApplicationAppVersionResponse(BaseResponse):
    _types = {
        "data": GetApplicationAppVersionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetApplicationAppVersionResponseBody] = None
        init(self, d, self._types)
