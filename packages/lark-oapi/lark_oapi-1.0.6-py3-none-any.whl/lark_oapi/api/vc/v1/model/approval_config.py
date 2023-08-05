# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .subscribe_user import SubscribeUser


class ApprovalConfig(object):
    _types = {
        "approval_switch": int,
        "approval_condition": int,
        "meeting_duration": float,
        "approvers": List[SubscribeUser],
    }

    def __init__(self, d=None):
        self.approval_switch: Optional[int] = None
        self.approval_condition: Optional[int] = None
        self.meeting_duration: Optional[float] = None
        self.approvers: Optional[List[SubscribeUser]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalConfigBuilder":
        return ApprovalConfigBuilder()


class ApprovalConfigBuilder(object):
    def __init__(self) -> None:
        self._approval_config = ApprovalConfig()

    def approval_switch(self, approval_switch: int) -> "ApprovalConfigBuilder":
        self._approval_config.approval_switch = approval_switch
        return self

    def approval_condition(self, approval_condition: int) -> "ApprovalConfigBuilder":
        self._approval_config.approval_condition = approval_condition
        return self

    def meeting_duration(self, meeting_duration: float) -> "ApprovalConfigBuilder":
        self._approval_config.meeting_duration = meeting_duration
        return self

    def approvers(self, approvers: List[SubscribeUser]) -> "ApprovalConfigBuilder":
        self._approval_config.approvers = approvers
        return self

    def build(self) -> "ApprovalConfig":
        return self._approval_config
