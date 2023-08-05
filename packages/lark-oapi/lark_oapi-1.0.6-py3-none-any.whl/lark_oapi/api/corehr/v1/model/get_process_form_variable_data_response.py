# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_process_form_variable_data_response_body import GetProcessFormVariableDataResponseBody


class GetProcessFormVariableDataResponse(BaseResponse):
    _types = {
        "data": GetProcessFormVariableDataResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetProcessFormVariableDataResponseBody] = None
        init(self, d, self._types)
