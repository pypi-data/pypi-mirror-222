# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Period(object):
    _types = {
        "id": int,
        "zh_name": str,
        "en_name": str,
        "status": int,
        "period_start_time": str,
        "period_end_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.status: Optional[int] = None
        self.period_start_time: Optional[str] = None
        self.period_end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PeriodBuilder":
        return PeriodBuilder()


class PeriodBuilder(object):
    def __init__(self) -> None:
        self._period = Period()

    def id(self, id: int) -> "PeriodBuilder":
        self._period.id = id
        return self

    def zh_name(self, zh_name: str) -> "PeriodBuilder":
        self._period.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "PeriodBuilder":
        self._period.en_name = en_name
        return self

    def status(self, status: int) -> "PeriodBuilder":
        self._period.status = status
        return self

    def period_start_time(self, period_start_time: str) -> "PeriodBuilder":
        self._period.period_start_time = period_start_time
        return self

    def period_end_time(self, period_end_time: str) -> "PeriodBuilder":
        self._period.period_end_time = period_end_time
        return self

    def build(self) -> "Period":
        return self._period
