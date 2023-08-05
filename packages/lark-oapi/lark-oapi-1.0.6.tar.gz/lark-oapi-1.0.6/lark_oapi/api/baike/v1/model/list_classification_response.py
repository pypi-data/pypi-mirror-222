# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_classification_response_body import ListClassificationResponseBody


class ListClassificationResponse(BaseResponse):
    _types = {
        "data": ListClassificationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListClassificationResponseBody] = None
        init(self, d, self._types)
