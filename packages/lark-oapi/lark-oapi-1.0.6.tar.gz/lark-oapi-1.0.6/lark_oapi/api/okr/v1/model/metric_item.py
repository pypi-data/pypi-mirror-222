# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .metric_unit import MetricUnit


class MetricItem(object):
    _types = {
        "metric_item_id": str,
        "user_id": str,
        "period_id": str,
        "metric_unit": MetricUnit,
        "metric_initial_value": float,
        "metric_target_value": float,
        "metric_current_value": float,
        "supported_user_id": str,
        "kr_id": str,
        "updated_at": int,
        "updated_by": str,
    }

    def __init__(self, d=None):
        self.metric_item_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.period_id: Optional[str] = None
        self.metric_unit: Optional[MetricUnit] = None
        self.metric_initial_value: Optional[float] = None
        self.metric_target_value: Optional[float] = None
        self.metric_current_value: Optional[float] = None
        self.supported_user_id: Optional[str] = None
        self.kr_id: Optional[str] = None
        self.updated_at: Optional[int] = None
        self.updated_by: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MetricItemBuilder":
        return MetricItemBuilder()


class MetricItemBuilder(object):
    def __init__(self) -> None:
        self._metric_item = MetricItem()

    def metric_item_id(self, metric_item_id: str) -> "MetricItemBuilder":
        self._metric_item.metric_item_id = metric_item_id
        return self

    def user_id(self, user_id: str) -> "MetricItemBuilder":
        self._metric_item.user_id = user_id
        return self

    def period_id(self, period_id: str) -> "MetricItemBuilder":
        self._metric_item.period_id = period_id
        return self

    def metric_unit(self, metric_unit: MetricUnit) -> "MetricItemBuilder":
        self._metric_item.metric_unit = metric_unit
        return self

    def metric_initial_value(self, metric_initial_value: float) -> "MetricItemBuilder":
        self._metric_item.metric_initial_value = metric_initial_value
        return self

    def metric_target_value(self, metric_target_value: float) -> "MetricItemBuilder":
        self._metric_item.metric_target_value = metric_target_value
        return self

    def metric_current_value(self, metric_current_value: float) -> "MetricItemBuilder":
        self._metric_item.metric_current_value = metric_current_value
        return self

    def supported_user_id(self, supported_user_id: str) -> "MetricItemBuilder":
        self._metric_item.supported_user_id = supported_user_id
        return self

    def kr_id(self, kr_id: str) -> "MetricItemBuilder":
        self._metric_item.kr_id = kr_id
        return self

    def updated_at(self, updated_at: int) -> "MetricItemBuilder":
        self._metric_item.updated_at = updated_at
        return self

    def updated_by(self, updated_by: str) -> "MetricItemBuilder":
        self._metric_item.updated_by = updated_by
        return self

    def build(self) -> "MetricItem":
        return self._metric_item
