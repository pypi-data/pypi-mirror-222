# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class QuerySpreadsheetSheetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None

    @staticmethod
    def builder() -> "QuerySpreadsheetSheetRequestBuilder":
        return QuerySpreadsheetSheetRequestBuilder()


class QuerySpreadsheetSheetRequestBuilder(object):

    def __init__(self) -> None:
        query_spreadsheet_sheet_request = QuerySpreadsheetSheetRequest()
        query_spreadsheet_sheet_request.http_method = HttpMethod.GET
        query_spreadsheet_sheet_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/query"
        query_spreadsheet_sheet_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._query_spreadsheet_sheet_request: QuerySpreadsheetSheetRequest = query_spreadsheet_sheet_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "QuerySpreadsheetSheetRequestBuilder":
        self._query_spreadsheet_sheet_request.spreadsheet_token = spreadsheet_token
        self._query_spreadsheet_sheet_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def build(self) -> QuerySpreadsheetSheetRequest:
        return self._query_spreadsheet_sheet_request
