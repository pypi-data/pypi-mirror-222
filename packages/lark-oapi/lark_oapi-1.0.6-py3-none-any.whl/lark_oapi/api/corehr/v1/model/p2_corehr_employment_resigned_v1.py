# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrEmploymentResignedV1Data(object):
    _types = {
        "employment_id": str,
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        init(self, d, self._types)


class P2CorehrEmploymentResignedV1(EventContext):
    _types = {
        "event": P2CorehrEmploymentResignedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrEmploymentResignedV1Data] = None
        init(self, d, self._types)
