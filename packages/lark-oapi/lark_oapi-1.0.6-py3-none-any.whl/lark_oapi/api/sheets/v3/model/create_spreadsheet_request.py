# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .spreadsheet import Spreadsheet


class CreateSpreadsheetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[Spreadsheet] = None

    @staticmethod
    def builder() -> "CreateSpreadsheetRequestBuilder":
        return CreateSpreadsheetRequestBuilder()


class CreateSpreadsheetRequestBuilder(object):

    def __init__(self) -> None:
        create_spreadsheet_request = CreateSpreadsheetRequest()
        create_spreadsheet_request.http_method = HttpMethod.POST
        create_spreadsheet_request.uri = "/open-apis/sheets/v3/spreadsheets"
        create_spreadsheet_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_spreadsheet_request: CreateSpreadsheetRequest = create_spreadsheet_request

    def request_body(self, request_body: Spreadsheet) -> "CreateSpreadsheetRequestBuilder":
        self._create_spreadsheet_request.request_body = request_body
        self._create_spreadsheet_request.body = request_body
        return self

    def build(self) -> CreateSpreadsheetRequest:
        return self._create_spreadsheet_request
