# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_room_level_response_body import SearchRoomLevelResponseBody


class SearchRoomLevelResponse(BaseResponse):
    _types = {
        "data": SearchRoomLevelResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchRoomLevelResponseBody] = None
        init(self, d, self._types)
