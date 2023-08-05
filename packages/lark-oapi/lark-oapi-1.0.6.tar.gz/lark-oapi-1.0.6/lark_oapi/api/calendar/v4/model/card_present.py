# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CardPresent(object):
    _types = {
        "body": str,
        "interactable": bool,
        "type": str,
        "operation_type": str,
        "callback_info": str,
    }

    def __init__(self, d=None):
        self.body: Optional[str] = None
        self.interactable: Optional[bool] = None
        self.type: Optional[str] = None
        self.operation_type: Optional[str] = None
        self.callback_info: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CardPresentBuilder":
        return CardPresentBuilder()


class CardPresentBuilder(object):
    def __init__(self) -> None:
        self._card_present = CardPresent()

    def body(self, body: str) -> "CardPresentBuilder":
        self._card_present.body = body
        return self

    def interactable(self, interactable: bool) -> "CardPresentBuilder":
        self._card_present.interactable = interactable
        return self

    def type(self, type: str) -> "CardPresentBuilder":
        self._card_present.type = type
        return self

    def operation_type(self, operation_type: str) -> "CardPresentBuilder":
        self._card_present.operation_type = operation_type
        return self

    def callback_info(self, callback_info: str) -> "CardPresentBuilder":
        self._card_present.callback_info = callback_info
        return self

    def build(self) -> "CardPresent":
        return self._card_present
