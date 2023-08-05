# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .check_white_black_list_application_visibility_response_body import \
    CheckWhiteBlackListApplicationVisibilityResponseBody


class CheckWhiteBlackListApplicationVisibilityResponse(BaseResponse):
    _types = {
        "data": CheckWhiteBlackListApplicationVisibilityResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CheckWhiteBlackListApplicationVisibilityResponseBody] = None
        init(self, d, self._types)
