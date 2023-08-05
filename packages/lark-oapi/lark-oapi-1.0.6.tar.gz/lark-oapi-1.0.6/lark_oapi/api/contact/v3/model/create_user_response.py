# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_user_response_body import CreateUserResponseBody


class CreateUserResponse(BaseResponse):
    _types = {
        "data": CreateUserResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateUserResponseBody] = None
        init(self, d, self._types)
