# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .delete_app_table_record_response_body import DeleteAppTableRecordResponseBody


class DeleteAppTableRecordResponse(BaseResponse):
    _types = {
        "data": DeleteAppTableRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[DeleteAppTableRecordResponseBody] = None
        init(self, d, self._types)
