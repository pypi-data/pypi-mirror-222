# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PunchTimeRule(object):
    _types = {
        "on_time": str,
        "off_time": str,
        "late_minutes_as_late": int,
        "late_minutes_as_lack": int,
        "on_advance_minutes": int,
        "early_minutes_as_early": int,
        "early_minutes_as_lack": int,
        "off_delay_minutes": int,
        "late_minutes_as_serious_late": int,
    }

    def __init__(self, d=None):
        self.on_time: Optional[str] = None
        self.off_time: Optional[str] = None
        self.late_minutes_as_late: Optional[int] = None
        self.late_minutes_as_lack: Optional[int] = None
        self.on_advance_minutes: Optional[int] = None
        self.early_minutes_as_early: Optional[int] = None
        self.early_minutes_as_lack: Optional[int] = None
        self.off_delay_minutes: Optional[int] = None
        self.late_minutes_as_serious_late: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PunchTimeRuleBuilder":
        return PunchTimeRuleBuilder()


class PunchTimeRuleBuilder(object):
    def __init__(self) -> None:
        self._punch_time_rule = PunchTimeRule()

    def on_time(self, on_time: str) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.on_time = on_time
        return self

    def off_time(self, off_time: str) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.off_time = off_time
        return self

    def late_minutes_as_late(self, late_minutes_as_late: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.late_minutes_as_late = late_minutes_as_late
        return self

    def late_minutes_as_lack(self, late_minutes_as_lack: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.late_minutes_as_lack = late_minutes_as_lack
        return self

    def on_advance_minutes(self, on_advance_minutes: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.on_advance_minutes = on_advance_minutes
        return self

    def early_minutes_as_early(self, early_minutes_as_early: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.early_minutes_as_early = early_minutes_as_early
        return self

    def early_minutes_as_lack(self, early_minutes_as_lack: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.early_minutes_as_lack = early_minutes_as_lack
        return self

    def off_delay_minutes(self, off_delay_minutes: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.off_delay_minutes = off_delay_minutes
        return self

    def late_minutes_as_serious_late(self, late_minutes_as_serious_late: int) -> "PunchTimeRuleBuilder":
        self._punch_time_rule.late_minutes_as_serious_late = late_minutes_as_serious_late
        return self

    def build(self) -> "PunchTimeRule":
        return self._punch_time_rule
