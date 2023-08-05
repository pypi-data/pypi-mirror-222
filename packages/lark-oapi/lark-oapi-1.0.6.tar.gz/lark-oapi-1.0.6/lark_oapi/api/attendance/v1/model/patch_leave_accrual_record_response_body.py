# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .leave_accrual_record import LeaveAccrualRecord


class PatchLeaveAccrualRecordResponseBody(object):
    _types = {
        "record": LeaveAccrualRecord,
    }

    def __init__(self, d=None):
        self.record: Optional[LeaveAccrualRecord] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchLeaveAccrualRecordResponseBodyBuilder":
        return PatchLeaveAccrualRecordResponseBodyBuilder()


class PatchLeaveAccrualRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_leave_accrual_record_response_body = PatchLeaveAccrualRecordResponseBody()

    def record(self, record: LeaveAccrualRecord) -> "PatchLeaveAccrualRecordResponseBodyBuilder":
        self._patch_leave_accrual_record_response_body.record = record
        return self

    def build(self) -> "PatchLeaveAccrualRecordResponseBody":
        return self._patch_leave_accrual_record_response_body
