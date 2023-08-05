# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n_names import I18nNames


class UserOut(object):
    _types = {
        "approval_id": str,
        "uniq_id": str,
        "unit": int,
        "interval": int,
        "start_time": str,
        "end_time": str,
        "i18n_names": I18nNames,
        "default_locale": str,
        "reason": str,
        "approve_pass_time": str,
        "approve_apply_time": str,
    }

    def __init__(self, d=None):
        self.approval_id: Optional[str] = None
        self.uniq_id: Optional[str] = None
        self.unit: Optional[int] = None
        self.interval: Optional[int] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        self.default_locale: Optional[str] = None
        self.reason: Optional[str] = None
        self.approve_pass_time: Optional[str] = None
        self.approve_apply_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserOutBuilder":
        return UserOutBuilder()


class UserOutBuilder(object):
    def __init__(self) -> None:
        self._user_out = UserOut()

    def approval_id(self, approval_id: str) -> "UserOutBuilder":
        self._user_out.approval_id = approval_id
        return self

    def uniq_id(self, uniq_id: str) -> "UserOutBuilder":
        self._user_out.uniq_id = uniq_id
        return self

    def unit(self, unit: int) -> "UserOutBuilder":
        self._user_out.unit = unit
        return self

    def interval(self, interval: int) -> "UserOutBuilder":
        self._user_out.interval = interval
        return self

    def start_time(self, start_time: str) -> "UserOutBuilder":
        self._user_out.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "UserOutBuilder":
        self._user_out.end_time = end_time
        return self

    def i18n_names(self, i18n_names: I18nNames) -> "UserOutBuilder":
        self._user_out.i18n_names = i18n_names
        return self

    def default_locale(self, default_locale: str) -> "UserOutBuilder":
        self._user_out.default_locale = default_locale
        return self

    def reason(self, reason: str) -> "UserOutBuilder":
        self._user_out.reason = reason
        return self

    def approve_pass_time(self, approve_pass_time: str) -> "UserOutBuilder":
        self._user_out.approve_pass_time = approve_pass_time
        return self

    def approve_apply_time(self, approve_apply_time: str) -> "UserOutBuilder":
        self._user_out.approve_apply_time = approve_apply_time
        return self

    def build(self) -> "UserOut":
        return self._user_out
