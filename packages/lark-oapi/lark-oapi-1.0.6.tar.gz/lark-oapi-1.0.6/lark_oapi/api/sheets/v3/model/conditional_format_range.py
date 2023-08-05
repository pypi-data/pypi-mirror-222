# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ConditionalFormatRange(object):
    _types = {
        "sheet_id": str,
        "start_row_index": int,
        "end_row_index": int,
        "start_column_index": int,
        "end_column_index": int,
    }

    def __init__(self, d=None):
        self.sheet_id: Optional[str] = None
        self.start_row_index: Optional[int] = None
        self.end_row_index: Optional[int] = None
        self.start_column_index: Optional[int] = None
        self.end_column_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConditionalFormatRangeBuilder":
        return ConditionalFormatRangeBuilder()


class ConditionalFormatRangeBuilder(object):
    def __init__(self) -> None:
        self._conditional_format_range = ConditionalFormatRange()

    def sheet_id(self, sheet_id: str) -> "ConditionalFormatRangeBuilder":
        self._conditional_format_range.sheet_id = sheet_id
        return self

    def start_row_index(self, start_row_index: int) -> "ConditionalFormatRangeBuilder":
        self._conditional_format_range.start_row_index = start_row_index
        return self

    def end_row_index(self, end_row_index: int) -> "ConditionalFormatRangeBuilder":
        self._conditional_format_range.end_row_index = end_row_index
        return self

    def start_column_index(self, start_column_index: int) -> "ConditionalFormatRangeBuilder":
        self._conditional_format_range.start_column_index = start_column_index
        return self

    def end_column_index(self, end_column_index: int) -> "ConditionalFormatRangeBuilder":
        self._conditional_format_range.end_column_index = end_column_index
        return self

    def build(self) -> "ConditionalFormatRange":
        return self._conditional_format_range
