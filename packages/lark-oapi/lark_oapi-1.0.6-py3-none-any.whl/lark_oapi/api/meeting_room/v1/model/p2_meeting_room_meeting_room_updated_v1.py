# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2MeetingRoomMeetingRoomUpdatedV1Data(object):
    _types = {
        "room_name": str,
        "room_id": str,
    }

    def __init__(self, d=None):
        self.room_name: Optional[str] = None
        self.room_id: Optional[str] = None
        init(self, d, self._types)


class P2MeetingRoomMeetingRoomUpdatedV1(EventContext):
    _types = {
        "event": P2MeetingRoomMeetingRoomUpdatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2MeetingRoomMeetingRoomUpdatedV1Data] = None
        init(self, d, self._types)
