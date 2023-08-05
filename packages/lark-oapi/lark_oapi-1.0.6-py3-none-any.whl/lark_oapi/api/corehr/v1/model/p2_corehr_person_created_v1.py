# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrPersonCreatedV1Data(object):
    _types = {
        "person_id": str,
    }

    def __init__(self, d=None):
        self.person_id: Optional[str] = None
        init(self, d, self._types)


class P2CorehrPersonCreatedV1(EventContext):
    _types = {
        "event": P2CorehrPersonCreatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrPersonCreatedV1Data] = None
        init(self, d, self._types)
