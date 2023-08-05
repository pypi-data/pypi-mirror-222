# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.find_spreadsheet_sheet_request import FindSpreadsheetSheetRequest
from ..model.find_spreadsheet_sheet_response import FindSpreadsheetSheetResponse
from ..model.get_spreadsheet_sheet_request import GetSpreadsheetSheetRequest
from ..model.get_spreadsheet_sheet_response import GetSpreadsheetSheetResponse
from ..model.move_dimension_spreadsheet_sheet_request import MoveDimensionSpreadsheetSheetRequest
from ..model.move_dimension_spreadsheet_sheet_response import MoveDimensionSpreadsheetSheetResponse
from ..model.query_spreadsheet_sheet_request import QuerySpreadsheetSheetRequest
from ..model.query_spreadsheet_sheet_response import QuerySpreadsheetSheetResponse
from ..model.replace_spreadsheet_sheet_request import ReplaceSpreadsheetSheetRequest
from ..model.replace_spreadsheet_sheet_response import ReplaceSpreadsheetSheetResponse


class SpreadsheetSheet(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def find(self, request: FindSpreadsheetSheetRequest,
             option: Optional[RequestOption] = None) -> FindSpreadsheetSheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: FindSpreadsheetSheetResponse = JSON.unmarshal(str(resp.content, UTF_8), FindSpreadsheetSheetResponse)
        response.raw = resp

        return response

    def get(self, request: GetSpreadsheetSheetRequest,
            option: Optional[RequestOption] = None) -> GetSpreadsheetSheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSpreadsheetSheetResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSpreadsheetSheetResponse)
        response.raw = resp

        return response

    def move_dimension(self, request: MoveDimensionSpreadsheetSheetRequest,
                       option: Optional[RequestOption] = None) -> MoveDimensionSpreadsheetSheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: MoveDimensionSpreadsheetSheetResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                         MoveDimensionSpreadsheetSheetResponse)
        response.raw = resp

        return response

    def query(self, request: QuerySpreadsheetSheetRequest,
              option: Optional[RequestOption] = None) -> QuerySpreadsheetSheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QuerySpreadsheetSheetResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 QuerySpreadsheetSheetResponse)
        response.raw = resp

        return response

    def replace(self, request: ReplaceSpreadsheetSheetRequest,
                option: Optional[RequestOption] = None) -> ReplaceSpreadsheetSheetResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ReplaceSpreadsheetSheetResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   ReplaceSpreadsheetSheetResponse)
        response.raw = resp

        return response
