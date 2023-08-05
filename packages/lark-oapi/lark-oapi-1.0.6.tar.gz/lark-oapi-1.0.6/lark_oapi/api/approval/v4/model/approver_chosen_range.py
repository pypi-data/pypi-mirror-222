# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApproverChosenRange(object):
    _types = {
        "approver_range_type": int,
        "approver_range_ids": List[str],
    }

    def __init__(self, d=None):
        self.approver_range_type: Optional[int] = None
        self.approver_range_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApproverChosenRangeBuilder":
        return ApproverChosenRangeBuilder()


class ApproverChosenRangeBuilder(object):
    def __init__(self) -> None:
        self._approver_chosen_range = ApproverChosenRange()

    def approver_range_type(self, approver_range_type: int) -> "ApproverChosenRangeBuilder":
        self._approver_chosen_range.approver_range_type = approver_range_type
        return self

    def approver_range_ids(self, approver_range_ids: List[str]) -> "ApproverChosenRangeBuilder":
        self._approver_chosen_range.approver_range_ids = approver_range_ids
        return self

    def build(self) -> "ApproverChosenRange":
        return self._approver_chosen_range
