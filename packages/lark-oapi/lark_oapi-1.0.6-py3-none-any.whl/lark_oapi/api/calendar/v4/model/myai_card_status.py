# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MyaiCardStatus(object):
    _types = {
        "from_status": str,
        "to_status": str,
    }

    def __init__(self, d=None):
        self.from_status: Optional[str] = None
        self.to_status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyaiCardStatusBuilder":
        return MyaiCardStatusBuilder()


class MyaiCardStatusBuilder(object):
    def __init__(self) -> None:
        self._myai_card_status = MyaiCardStatus()

    def from_status(self, from_status: str) -> "MyaiCardStatusBuilder":
        self._myai_card_status.from_status = from_status
        return self

    def to_status(self, to_status: str) -> "MyaiCardStatusBuilder":
        self._myai_card_status.to_status = to_status
        return self

    def build(self) -> "MyaiCardStatus":
        return self._myai_card_status
