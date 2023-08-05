# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar_event_attendee import CalendarEventAttendee


class ListCalendarEventAttendeeResponseBody(object):
    _types = {
        "items": List[CalendarEventAttendee],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[CalendarEventAttendee]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCalendarEventAttendeeResponseBodyBuilder":
        return ListCalendarEventAttendeeResponseBodyBuilder()


class ListCalendarEventAttendeeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_calendar_event_attendee_response_body = ListCalendarEventAttendeeResponseBody()

    def items(self, items: List[CalendarEventAttendee]) -> "ListCalendarEventAttendeeResponseBodyBuilder":
        self._list_calendar_event_attendee_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListCalendarEventAttendeeResponseBodyBuilder":
        self._list_calendar_event_attendee_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListCalendarEventAttendeeResponseBodyBuilder":
        self._list_calendar_event_attendee_response_body.page_token = page_token
        return self

    def build(self) -> "ListCalendarEventAttendeeResponseBody":
        return self._list_calendar_event_attendee_response_body
