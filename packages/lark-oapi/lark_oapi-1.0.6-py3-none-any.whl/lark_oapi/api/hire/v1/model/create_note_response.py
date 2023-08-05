# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_note_response_body import CreateNoteResponseBody


class CreateNoteResponse(BaseResponse):
    _types = {
        "data": CreateNoteResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateNoteResponseBody] = None
        init(self, d, self._types)
