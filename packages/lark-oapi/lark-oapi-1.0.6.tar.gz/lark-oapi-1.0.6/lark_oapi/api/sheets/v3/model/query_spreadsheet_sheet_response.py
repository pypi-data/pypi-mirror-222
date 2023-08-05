# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_spreadsheet_sheet_response_body import QuerySpreadsheetSheetResponseBody


class QuerySpreadsheetSheetResponse(BaseResponse):
    _types = {
        "data": QuerySpreadsheetSheetResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QuerySpreadsheetSheetResponseBody] = None
        init(self, d, self._types)
