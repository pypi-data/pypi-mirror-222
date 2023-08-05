# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .delete_space_member_response_body import DeleteSpaceMemberResponseBody


class DeleteSpaceMemberResponse(BaseResponse):
    _types = {
        "data": DeleteSpaceMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[DeleteSpaceMemberResponseBody] = None
        init(self, d, self._types)
