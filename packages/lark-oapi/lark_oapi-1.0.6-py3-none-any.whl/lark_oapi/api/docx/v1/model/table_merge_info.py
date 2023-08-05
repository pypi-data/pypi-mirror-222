# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TableMergeInfo(object):
    _types = {
        "row_span": int,
        "col_span": int,
    }

    def __init__(self, d=None):
        self.row_span: Optional[int] = None
        self.col_span: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TableMergeInfoBuilder":
        return TableMergeInfoBuilder()


class TableMergeInfoBuilder(object):
    def __init__(self) -> None:
        self._table_merge_info = TableMergeInfo()

    def row_span(self, row_span: int) -> "TableMergeInfoBuilder":
        self._table_merge_info.row_span = row_span
        return self

    def col_span(self, col_span: int) -> "TableMergeInfoBuilder":
        self._table_merge_info.col_span = col_span
        return self

    def build(self) -> "TableMergeInfo":
        return self._table_merge_info
