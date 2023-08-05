# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OkrName(object):
    _types = {
        "zh": str,
        "en": str,
    }

    def __init__(self, d=None):
        self.zh: Optional[str] = None
        self.en: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrNameBuilder":
        return OkrNameBuilder()


class OkrNameBuilder(object):
    def __init__(self) -> None:
        self._okr_name = OkrName()

    def zh(self, zh: str) -> "OkrNameBuilder":
        self._okr_name.zh = zh
        return self

    def en(self, en: str) -> "OkrNameBuilder":
        self._okr_name.en = en
        return self

    def build(self) -> "OkrName":
        return self._okr_name
