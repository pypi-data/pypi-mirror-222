# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .okr_name import OkrName


class OkrSimple(object):
    _types = {
        "name": OkrName,
        "okr_id": str,
        "period_id": str,
        "period_type": str,
    }

    def __init__(self, d=None):
        self.name: Optional[OkrName] = None
        self.okr_id: Optional[str] = None
        self.period_id: Optional[str] = None
        self.period_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrSimpleBuilder":
        return OkrSimpleBuilder()


class OkrSimpleBuilder(object):
    def __init__(self) -> None:
        self._okr_simple = OkrSimple()

    def name(self, name: OkrName) -> "OkrSimpleBuilder":
        self._okr_simple.name = name
        return self

    def okr_id(self, okr_id: str) -> "OkrSimpleBuilder":
        self._okr_simple.okr_id = okr_id
        return self

    def period_id(self, period_id: str) -> "OkrSimpleBuilder":
        self._okr_simple.period_id = period_id
        return self

    def period_type(self, period_type: str) -> "OkrSimpleBuilder":
        self._okr_simple.period_type = period_type
        return self

    def build(self) -> "OkrSimple":
        return self._okr_simple
