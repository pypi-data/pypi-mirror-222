# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Schedule(object):
    _types = {
        "group_id": str,
        "shifts": List[str],
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        self.shifts: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScheduleBuilder":
        return ScheduleBuilder()


class ScheduleBuilder(object):
    def __init__(self) -> None:
        self._schedule = Schedule()

    def group_id(self, group_id: str) -> "ScheduleBuilder":
        self._schedule.group_id = group_id
        return self

    def shifts(self, shifts: List[str]) -> "ScheduleBuilder":
        self._schedule.shifts = shifts
        return self

    def build(self) -> "Schedule":
        return self._schedule
