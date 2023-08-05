# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Due(object):
    _types = {
        "timestamp": int,
        "is_all_day": bool,
    }

    def __init__(self, d=None):
        self.timestamp: Optional[int] = None
        self.is_all_day: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DueBuilder":
        return DueBuilder()


class DueBuilder(object):
    def __init__(self) -> None:
        self._due = Due()

    def timestamp(self, timestamp: int) -> "DueBuilder":
        self._due.timestamp = timestamp
        return self

    def is_all_day(self, is_all_day: bool) -> "DueBuilder":
        self._due.is_all_day = is_all_day
        return self

    def build(self) -> "Due":
        return self._due
