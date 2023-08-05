# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_job_family_response_body import ListJobFamilyResponseBody


class ListJobFamilyResponse(BaseResponse):
    _types = {
        "data": ListJobFamilyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListJobFamilyResponseBody] = None
        init(self, d, self._types)
