# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .simplelist_group_response_body import SimplelistGroupResponseBody


class SimplelistGroupResponse(BaseResponse):
    _types = {
        "data": SimplelistGroupResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SimplelistGroupResponseBody] = None
        init(self, d, self._types)
