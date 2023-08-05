# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_participant_quality_list_response_body import GetParticipantQualityListResponseBody


class GetParticipantQualityListResponse(BaseResponse):
    _types = {
        "data": GetParticipantQualityListResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetParticipantQualityListResponseBody] = None
        init(self, d, self._types)
