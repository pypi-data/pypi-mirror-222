# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar import Calendar


class SubscribeCalendarResponseBody(object):
    _types = {
        "calendar": Calendar,
    }

    def __init__(self, d=None):
        self.calendar: Optional[Calendar] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubscribeCalendarResponseBodyBuilder":
        return SubscribeCalendarResponseBodyBuilder()


class SubscribeCalendarResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._subscribe_calendar_response_body = SubscribeCalendarResponseBody()

    def calendar(self, calendar: Calendar) -> "SubscribeCalendarResponseBodyBuilder":
        self._subscribe_calendar_response_body.calendar = calendar
        return self

    def build(self) -> "SubscribeCalendarResponseBody":
        return self._subscribe_calendar_response_body
