# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_external_application_response_body import CreateExternalApplicationResponseBody


class CreateExternalApplicationResponse(BaseResponse):
    _types = {
        "data": CreateExternalApplicationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateExternalApplicationResponseBody] = None
        init(self, d, self._types)
