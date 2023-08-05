# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Dummy(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DummyBuilder":
        return DummyBuilder()


class DummyBuilder(object):
    def __init__(self) -> None:
        self._dummy = Dummy()

    def id(self, id: str) -> "DummyBuilder":
        self._dummy.id = id
        return self

    def build(self) -> "Dummy":
        return self._dummy
