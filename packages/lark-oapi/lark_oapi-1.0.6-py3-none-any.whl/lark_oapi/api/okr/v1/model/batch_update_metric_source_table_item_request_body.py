# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .metric_item_request import MetricItemRequest


class BatchUpdateMetricSourceTableItemRequestBody(object):
    _types = {
        "items": List[MetricItemRequest],
    }

    def __init__(self, d=None):
        self.items: Optional[List[MetricItemRequest]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchUpdateMetricSourceTableItemRequestBodyBuilder":
        return BatchUpdateMetricSourceTableItemRequestBodyBuilder()


class BatchUpdateMetricSourceTableItemRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_update_metric_source_table_item_request_body = BatchUpdateMetricSourceTableItemRequestBody()

    def items(self, items: List[MetricItemRequest]) -> "BatchUpdateMetricSourceTableItemRequestBodyBuilder":
        self._batch_update_metric_source_table_item_request_body.items = items
        return self

    def build(self) -> "BatchUpdateMetricSourceTableItemRequestBody":
        return self._batch_update_metric_source_table_item_request_body
