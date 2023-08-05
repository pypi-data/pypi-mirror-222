# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .remove_members_tasklist_response_body import RemoveMembersTasklistResponseBody


class RemoveMembersTasklistResponse(BaseResponse):
    _types = {
        "data": RemoveMembersTasklistResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[RemoveMembersTasklistResponseBody] = None
        init(self, d, self._types)
