# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Cash(object):
    _types = {
        "currency_type": str,
        "amount": int,
    }

    def __init__(self, d=None):
        self.currency_type: Optional[str] = None
        self.amount: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CashBuilder":
        return CashBuilder()


class CashBuilder(object):
    def __init__(self) -> None:
        self._cash = Cash()

    def currency_type(self, currency_type: str) -> "CashBuilder":
        self._cash.currency_type = currency_type
        return self

    def amount(self, amount: int) -> "CashBuilder":
        self._cash.amount = amount
        return self

    def build(self) -> "Cash":
        return self._cash
