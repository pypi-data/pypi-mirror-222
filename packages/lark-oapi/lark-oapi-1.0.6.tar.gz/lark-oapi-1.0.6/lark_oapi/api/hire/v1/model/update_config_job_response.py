# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_config_job_response_body import UpdateConfigJobResponseBody


class UpdateConfigJobResponse(BaseResponse):
    _types = {
        "data": UpdateConfigJobResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateConfigJobResponseBody] = None
        init(self, d, self._types)
