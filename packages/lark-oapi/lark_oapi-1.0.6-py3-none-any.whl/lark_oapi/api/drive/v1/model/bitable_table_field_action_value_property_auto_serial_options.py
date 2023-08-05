# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BitableTableFieldActionValuePropertyAutoSerialOptions(object):
    _types = {
        "type": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitableTableFieldActionValuePropertyAutoSerialOptionsBuilder":
        return BitableTableFieldActionValuePropertyAutoSerialOptionsBuilder()


class BitableTableFieldActionValuePropertyAutoSerialOptionsBuilder(object):
    def __init__(self) -> None:
        self._bitable_table_field_action_value_property_auto_serial_options = BitableTableFieldActionValuePropertyAutoSerialOptions()

    def type(self, type: str) -> "BitableTableFieldActionValuePropertyAutoSerialOptionsBuilder":
        self._bitable_table_field_action_value_property_auto_serial_options.type = type
        return self

    def value(self, value: str) -> "BitableTableFieldActionValuePropertyAutoSerialOptionsBuilder":
        self._bitable_table_field_action_value_property_auto_serial_options.value = value
        return self

    def build(self) -> "BitableTableFieldActionValuePropertyAutoSerialOptions":
        return self._bitable_table_field_action_value_property_auto_serial_options
