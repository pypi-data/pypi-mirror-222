# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .approval_event import ApprovalEvent


class P2ApprovalApprovalUpdatedV4Data(object):
    _types = {
        "object": ApprovalEvent,
    }

    def __init__(self, d=None):
        self.object: Optional[ApprovalEvent] = None
        init(self, d, self._types)


class P2ApprovalApprovalUpdatedV4(EventContext):
    _types = {
        "event": P2ApprovalApprovalUpdatedV4Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ApprovalApprovalUpdatedV4Data] = None
        init(self, d, self._types)
