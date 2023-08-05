# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .meeting_event_meeting import MeetingEventMeeting
from .meeting_event_user import MeetingEventUser


class P2VcMeetingRecordingEndedV1Data(object):
    _types = {
        "meeting": MeetingEventMeeting,
        "operator": MeetingEventUser,
    }

    def __init__(self, d=None):
        self.meeting: Optional[MeetingEventMeeting] = None
        self.operator: Optional[MeetingEventUser] = None
        init(self, d, self._types)


class P2VcMeetingRecordingEndedV1(EventContext):
    _types = {
        "event": P2VcMeetingRecordingEndedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2VcMeetingRecordingEndedV1Data] = None
        init(self, d, self._types)
