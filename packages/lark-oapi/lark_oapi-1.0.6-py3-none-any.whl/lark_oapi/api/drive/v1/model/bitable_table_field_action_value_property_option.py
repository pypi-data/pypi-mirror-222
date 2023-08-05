# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BitableTableFieldActionValuePropertyOption(object):
    _types = {
        "name": str,
        "id": str,
        "color": int,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.id: Optional[str] = None
        self.color: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitableTableFieldActionValuePropertyOptionBuilder":
        return BitableTableFieldActionValuePropertyOptionBuilder()


class BitableTableFieldActionValuePropertyOptionBuilder(object):
    def __init__(self) -> None:
        self._bitable_table_field_action_value_property_option = BitableTableFieldActionValuePropertyOption()

    def name(self, name: str) -> "BitableTableFieldActionValuePropertyOptionBuilder":
        self._bitable_table_field_action_value_property_option.name = name
        return self

    def id(self, id: str) -> "BitableTableFieldActionValuePropertyOptionBuilder":
        self._bitable_table_field_action_value_property_option.id = id
        return self

    def color(self, color: int) -> "BitableTableFieldActionValuePropertyOptionBuilder":
        self._bitable_table_field_action_value_property_option.color = color
        return self

    def build(self) -> "BitableTableFieldActionValuePropertyOption":
        return self._bitable_table_field_action_value_property_option
