# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UsageTrendItem(object):
    _types = {
        "timestamp": int,
        "page_view": int,
        "unique_visitor": int,
    }

    def __init__(self, d=None):
        self.timestamp: Optional[int] = None
        self.page_view: Optional[int] = None
        self.unique_visitor: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UsageTrendItemBuilder":
        return UsageTrendItemBuilder()


class UsageTrendItemBuilder(object):
    def __init__(self) -> None:
        self._usage_trend_item = UsageTrendItem()

    def timestamp(self, timestamp: int) -> "UsageTrendItemBuilder":
        self._usage_trend_item.timestamp = timestamp
        return self

    def page_view(self, page_view: int) -> "UsageTrendItemBuilder":
        self._usage_trend_item.page_view = page_view
        return self

    def unique_visitor(self, unique_visitor: int) -> "UsageTrendItemBuilder":
        self._usage_trend_item.unique_visitor = unique_visitor
        return self

    def build(self) -> "UsageTrendItem":
        return self._usage_trend_item
