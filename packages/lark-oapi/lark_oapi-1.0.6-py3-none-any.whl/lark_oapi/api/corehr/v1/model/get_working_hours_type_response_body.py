# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .working_hours_type import WorkingHoursType


class GetWorkingHoursTypeResponseBody(object):
    _types = {
        "working_hours_type": WorkingHoursType,
    }

    def __init__(self, d=None):
        self.working_hours_type: Optional[WorkingHoursType] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetWorkingHoursTypeResponseBodyBuilder":
        return GetWorkingHoursTypeResponseBodyBuilder()


class GetWorkingHoursTypeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_working_hours_type_response_body = GetWorkingHoursTypeResponseBody()

    def working_hours_type(self, working_hours_type: WorkingHoursType) -> "GetWorkingHoursTypeResponseBodyBuilder":
        self._get_working_hours_type_response_body.working_hours_type = working_hours_type
        return self

    def build(self) -> "GetWorkingHoursTypeResponseBody":
        return self._get_working_hours_type_response_body
