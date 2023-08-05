# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_data import JobData


class EmployeeJobData(object):
    _types = {
        "employment_id": str,
        "job_datas": List[JobData],
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.job_datas: Optional[List[JobData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeJobDataBuilder":
        return EmployeeJobDataBuilder()


class EmployeeJobDataBuilder(object):
    def __init__(self) -> None:
        self._employee_job_data = EmployeeJobData()

    def employment_id(self, employment_id: str) -> "EmployeeJobDataBuilder":
        self._employee_job_data.employment_id = employment_id
        return self

    def job_datas(self, job_datas: List[JobData]) -> "EmployeeJobDataBuilder":
        self._employee_job_data.job_datas = job_datas
        return self

    def build(self) -> "EmployeeJobData":
        return self._employee_job_data
