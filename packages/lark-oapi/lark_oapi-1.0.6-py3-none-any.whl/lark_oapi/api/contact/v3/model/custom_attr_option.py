# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CustomAttrOption(object):
    _types = {
        "id": str,
        "value": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.value: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomAttrOptionBuilder":
        return CustomAttrOptionBuilder()


class CustomAttrOptionBuilder(object):
    def __init__(self) -> None:
        self._custom_attr_option = CustomAttrOption()

    def id(self, id: str) -> "CustomAttrOptionBuilder":
        self._custom_attr_option.id = id
        return self

    def value(self, value: str) -> "CustomAttrOptionBuilder":
        self._custom_attr_option.value = value
        return self

    def name(self, name: str) -> "CustomAttrOptionBuilder":
        self._custom_attr_option.name = name
        return self

    def build(self) -> "CustomAttrOption":
        return self._custom_attr_option
