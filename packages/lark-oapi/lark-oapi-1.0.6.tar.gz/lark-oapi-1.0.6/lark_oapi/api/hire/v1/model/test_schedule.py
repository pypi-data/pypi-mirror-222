# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TestSchedule(object):
    _types = {
        "start_time": str,
        "end_time": str,
    }

    def __init__(self, d=None):
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TestScheduleBuilder":
        return TestScheduleBuilder()


class TestScheduleBuilder(object):
    def __init__(self) -> None:
        self._test_schedule = TestSchedule()

    def start_time(self, start_time: str) -> "TestScheduleBuilder":
        self._test_schedule.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TestScheduleBuilder":
        self._test_schedule.end_time = end_time
        return self

    def build(self) -> "TestSchedule":
        return self._test_schedule
