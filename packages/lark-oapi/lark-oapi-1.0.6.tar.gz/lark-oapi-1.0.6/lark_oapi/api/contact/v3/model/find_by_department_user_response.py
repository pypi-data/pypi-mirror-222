# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .find_by_department_user_response_body import FindByDepartmentUserResponseBody


class FindByDepartmentUserResponse(BaseResponse):
    _types = {
        "data": FindByDepartmentUserResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[FindByDepartmentUserResponseBody] = None
        init(self, d, self._types)
