# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_functional_role_response_body import CreateFunctionalRoleResponseBody


class CreateFunctionalRoleResponse(BaseResponse):
    _types = {
        "data": CreateFunctionalRoleResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateFunctionalRoleResponseBody] = None
        init(self, d, self._types)
