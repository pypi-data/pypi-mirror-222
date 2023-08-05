# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_flow import UserFlow


class TaskResult(object):
    _types = {
        "check_in_record_id": str,
        "check_in_record": UserFlow,
        "check_out_record_id": str,
        "check_out_record": UserFlow,
        "check_in_result": str,
        "check_out_result": str,
        "check_in_result_supplement": str,
        "check_out_result_supplement": str,
        "check_in_shift_time": str,
        "check_out_shift_time": str,
        "task_shift_type": int,
    }

    def __init__(self, d=None):
        self.check_in_record_id: Optional[str] = None
        self.check_in_record: Optional[UserFlow] = None
        self.check_out_record_id: Optional[str] = None
        self.check_out_record: Optional[UserFlow] = None
        self.check_in_result: Optional[str] = None
        self.check_out_result: Optional[str] = None
        self.check_in_result_supplement: Optional[str] = None
        self.check_out_result_supplement: Optional[str] = None
        self.check_in_shift_time: Optional[str] = None
        self.check_out_shift_time: Optional[str] = None
        self.task_shift_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskResultBuilder":
        return TaskResultBuilder()


class TaskResultBuilder(object):
    def __init__(self) -> None:
        self._task_result = TaskResult()

    def check_in_record_id(self, check_in_record_id: str) -> "TaskResultBuilder":
        self._task_result.check_in_record_id = check_in_record_id
        return self

    def check_in_record(self, check_in_record: UserFlow) -> "TaskResultBuilder":
        self._task_result.check_in_record = check_in_record
        return self

    def check_out_record_id(self, check_out_record_id: str) -> "TaskResultBuilder":
        self._task_result.check_out_record_id = check_out_record_id
        return self

    def check_out_record(self, check_out_record: UserFlow) -> "TaskResultBuilder":
        self._task_result.check_out_record = check_out_record
        return self

    def check_in_result(self, check_in_result: str) -> "TaskResultBuilder":
        self._task_result.check_in_result = check_in_result
        return self

    def check_out_result(self, check_out_result: str) -> "TaskResultBuilder":
        self._task_result.check_out_result = check_out_result
        return self

    def check_in_result_supplement(self, check_in_result_supplement: str) -> "TaskResultBuilder":
        self._task_result.check_in_result_supplement = check_in_result_supplement
        return self

    def check_out_result_supplement(self, check_out_result_supplement: str) -> "TaskResultBuilder":
        self._task_result.check_out_result_supplement = check_out_result_supplement
        return self

    def check_in_shift_time(self, check_in_shift_time: str) -> "TaskResultBuilder":
        self._task_result.check_in_shift_time = check_in_shift_time
        return self

    def check_out_shift_time(self, check_out_shift_time: str) -> "TaskResultBuilder":
        self._task_result.check_out_shift_time = check_out_shift_time
        return self

    def task_shift_type(self, task_shift_type: int) -> "TaskResultBuilder":
        self._task_result.task_shift_type = task_shift_type
        return self

    def build(self) -> "TaskResult":
        return self._task_result
