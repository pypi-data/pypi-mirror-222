# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .employee_type_enum import EmployeeTypeEnum


class P2ContactEmployeeTypeEnumCreatedV3Data(object):
    _types = {
        "new_enum": EmployeeTypeEnum,
    }

    def __init__(self, d=None):
        self.new_enum: Optional[EmployeeTypeEnum] = None
        init(self, d, self._types)


class P2ContactEmployeeTypeEnumCreatedV3(EventContext):
    _types = {
        "event": P2ContactEmployeeTypeEnumCreatedV3Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ContactEmployeeTypeEnumCreatedV3Data] = None
        init(self, d, self._types)
