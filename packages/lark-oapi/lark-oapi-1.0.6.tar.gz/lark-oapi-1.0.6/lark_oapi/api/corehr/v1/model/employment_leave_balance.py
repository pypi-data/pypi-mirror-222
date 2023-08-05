# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .leave_balance import LeaveBalance


class EmploymentLeaveBalance(object):
    _types = {
        "employment_id": str,
        "employment_name": List[I18n],
        "as_of_date": str,
        "leave_balance_list": List[LeaveBalance],
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.employment_name: Optional[List[I18n]] = None
        self.as_of_date: Optional[str] = None
        self.leave_balance_list: Optional[List[LeaveBalance]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmploymentLeaveBalanceBuilder":
        return EmploymentLeaveBalanceBuilder()


class EmploymentLeaveBalanceBuilder(object):
    def __init__(self) -> None:
        self._employment_leave_balance = EmploymentLeaveBalance()

    def employment_id(self, employment_id: str) -> "EmploymentLeaveBalanceBuilder":
        self._employment_leave_balance.employment_id = employment_id
        return self

    def employment_name(self, employment_name: List[I18n]) -> "EmploymentLeaveBalanceBuilder":
        self._employment_leave_balance.employment_name = employment_name
        return self

    def as_of_date(self, as_of_date: str) -> "EmploymentLeaveBalanceBuilder":
        self._employment_leave_balance.as_of_date = as_of_date
        return self

    def leave_balance_list(self, leave_balance_list: List[LeaveBalance]) -> "EmploymentLeaveBalanceBuilder":
        self._employment_leave_balance.leave_balance_list = leave_balance_list
        return self

    def build(self) -> "EmploymentLeaveBalance":
        return self._employment_leave_balance
