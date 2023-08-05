# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_national_id_type_response_body import PatchNationalIdTypeResponseBody


class PatchNationalIdTypeResponse(BaseResponse):
    _types = {
        "data": PatchNationalIdTypeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchNationalIdTypeResponseBody] = None
        init(self, d, self._types)
