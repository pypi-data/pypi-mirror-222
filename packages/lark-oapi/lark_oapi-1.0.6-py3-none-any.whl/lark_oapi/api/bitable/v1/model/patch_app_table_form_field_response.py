# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_app_table_form_field_response_body import PatchAppTableFormFieldResponseBody


class PatchAppTableFormFieldResponse(BaseResponse):
    _types = {
        "data": PatchAppTableFormFieldResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchAppTableFormFieldResponseBody] = None
        init(self, d, self._types)
