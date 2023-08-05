# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_daily_shift import UserDailyShift


class BatchCreateUserDailyShiftResponseBody(object):
    _types = {
        "user_daily_shifts": List[UserDailyShift],
    }

    def __init__(self, d=None):
        self.user_daily_shifts: Optional[List[UserDailyShift]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateUserDailyShiftResponseBodyBuilder":
        return BatchCreateUserDailyShiftResponseBodyBuilder()


class BatchCreateUserDailyShiftResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_user_daily_shift_response_body = BatchCreateUserDailyShiftResponseBody()

    def user_daily_shifts(self,
                          user_daily_shifts: List[UserDailyShift]) -> "BatchCreateUserDailyShiftResponseBodyBuilder":
        self._batch_create_user_daily_shift_response_body.user_daily_shifts = user_daily_shifts
        return self

    def build(self) -> "BatchCreateUserDailyShiftResponseBody":
        return self._batch_create_user_daily_shift_response_body
