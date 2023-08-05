# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class OffboardingReason(object):
    _types = {
        "offboarding_reason_unique_identifier": str,
        "name": List[I18n],
        "active": bool,
        "parent_offboarding_reason_unique_identifier": str,
        "created_time": str,
        "updated_time": str,
    }

    def __init__(self, d=None):
        self.offboarding_reason_unique_identifier: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.parent_offboarding_reason_unique_identifier: Optional[str] = None
        self.created_time: Optional[str] = None
        self.updated_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OffboardingReasonBuilder":
        return OffboardingReasonBuilder()


class OffboardingReasonBuilder(object):
    def __init__(self) -> None:
        self._offboarding_reason = OffboardingReason()

    def offboarding_reason_unique_identifier(self,
                                             offboarding_reason_unique_identifier: str) -> "OffboardingReasonBuilder":
        self._offboarding_reason.offboarding_reason_unique_identifier = offboarding_reason_unique_identifier
        return self

    def name(self, name: List[I18n]) -> "OffboardingReasonBuilder":
        self._offboarding_reason.name = name
        return self

    def active(self, active: bool) -> "OffboardingReasonBuilder":
        self._offboarding_reason.active = active
        return self

    def parent_offboarding_reason_unique_identifier(self,
                                                    parent_offboarding_reason_unique_identifier: str) -> "OffboardingReasonBuilder":
        self._offboarding_reason.parent_offboarding_reason_unique_identifier = parent_offboarding_reason_unique_identifier
        return self

    def created_time(self, created_time: str) -> "OffboardingReasonBuilder":
        self._offboarding_reason.created_time = created_time
        return self

    def updated_time(self, updated_time: str) -> "OffboardingReasonBuilder":
        self._offboarding_reason.updated_time = updated_time
        return self

    def build(self) -> "OffboardingReason":
        return self._offboarding_reason
