# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_app_usage import ApplicationAppUsage


class ApplicationDepartmentAppUsage(object):
    _types = {
        "department_id": str,
        "app": List[ApplicationAppUsage],
        "gadget": List[ApplicationAppUsage],
        "webapp": List[ApplicationAppUsage],
        "bot": List[ApplicationAppUsage],
    }

    def __init__(self, d=None):
        self.department_id: Optional[str] = None
        self.app: Optional[List[ApplicationAppUsage]] = None
        self.gadget: Optional[List[ApplicationAppUsage]] = None
        self.webapp: Optional[List[ApplicationAppUsage]] = None
        self.bot: Optional[List[ApplicationAppUsage]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationDepartmentAppUsageBuilder":
        return ApplicationDepartmentAppUsageBuilder()


class ApplicationDepartmentAppUsageBuilder(object):
    def __init__(self) -> None:
        self._application_department_app_usage = ApplicationDepartmentAppUsage()

    def department_id(self, department_id: str) -> "ApplicationDepartmentAppUsageBuilder":
        self._application_department_app_usage.department_id = department_id
        return self

    def app(self, app: List[ApplicationAppUsage]) -> "ApplicationDepartmentAppUsageBuilder":
        self._application_department_app_usage.app = app
        return self

    def gadget(self, gadget: List[ApplicationAppUsage]) -> "ApplicationDepartmentAppUsageBuilder":
        self._application_department_app_usage.gadget = gadget
        return self

    def webapp(self, webapp: List[ApplicationAppUsage]) -> "ApplicationDepartmentAppUsageBuilder":
        self._application_department_app_usage.webapp = webapp
        return self

    def bot(self, bot: List[ApplicationAppUsage]) -> "ApplicationDepartmentAppUsageBuilder":
        self._application_department_app_usage.bot = bot
        return self

    def build(self) -> "ApplicationDepartmentAppUsage":
        return self._application_department_app_usage
