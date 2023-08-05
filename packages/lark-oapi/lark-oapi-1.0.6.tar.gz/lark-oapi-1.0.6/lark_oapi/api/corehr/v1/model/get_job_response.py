# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_job_response_body import GetJobResponseBody


class GetJobResponse(BaseResponse):
    _types = {
        "data": GetJobResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetJobResponseBody] = None
        init(self, d, self._types)
