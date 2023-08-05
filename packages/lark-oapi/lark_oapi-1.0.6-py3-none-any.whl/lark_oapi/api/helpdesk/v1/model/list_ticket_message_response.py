# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_ticket_message_response_body import ListTicketMessageResponseBody


class ListTicketMessageResponse(BaseResponse):
    _types = {
        "data": ListTicketMessageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListTicketMessageResponseBody] = None
        init(self, d, self._types)
