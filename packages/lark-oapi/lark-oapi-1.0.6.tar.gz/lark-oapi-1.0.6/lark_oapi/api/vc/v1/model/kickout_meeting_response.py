# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .kickout_meeting_response_body import KickoutMeetingResponseBody


class KickoutMeetingResponse(BaseResponse):
    _types = {
        "data": KickoutMeetingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[KickoutMeetingResponseBody] = None
        init(self, d, self._types)
