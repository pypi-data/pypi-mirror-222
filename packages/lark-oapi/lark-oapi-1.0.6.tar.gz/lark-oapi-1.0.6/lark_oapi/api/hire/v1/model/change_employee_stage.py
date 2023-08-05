# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .employee_conversion_info import EmployeeConversionInfo
from .employee_overboard_info import EmployeeOverboardInfo


class ChangeEmployeeStage(object):
    _types = {
        "operation": int,
        "conversion_info": EmployeeConversionInfo,
        "overboard_info": EmployeeOverboardInfo,
    }

    def __init__(self, d=None):
        self.operation: Optional[int] = None
        self.conversion_info: Optional[EmployeeConversionInfo] = None
        self.overboard_info: Optional[EmployeeOverboardInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChangeEmployeeStageBuilder":
        return ChangeEmployeeStageBuilder()


class ChangeEmployeeStageBuilder(object):
    def __init__(self) -> None:
        self._change_employee_stage = ChangeEmployeeStage()

    def operation(self, operation: int) -> "ChangeEmployeeStageBuilder":
        self._change_employee_stage.operation = operation
        return self

    def conversion_info(self, conversion_info: EmployeeConversionInfo) -> "ChangeEmployeeStageBuilder":
        self._change_employee_stage.conversion_info = conversion_info
        return self

    def overboard_info(self, overboard_info: EmployeeOverboardInfo) -> "ChangeEmployeeStageBuilder":
        self._change_employee_stage.overboard_info = overboard_info
        return self

    def build(self) -> "ChangeEmployeeStage":
        return self._change_employee_stage
