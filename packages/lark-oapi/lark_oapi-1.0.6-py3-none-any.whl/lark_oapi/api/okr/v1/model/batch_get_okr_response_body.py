# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .okr_batch import OkrBatch


class BatchGetOkrResponseBody(object):
    _types = {
        "okr_list": List[OkrBatch],
    }

    def __init__(self, d=None):
        self.okr_list: Optional[List[OkrBatch]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetOkrResponseBodyBuilder":
        return BatchGetOkrResponseBodyBuilder()


class BatchGetOkrResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_okr_response_body = BatchGetOkrResponseBody()

    def okr_list(self, okr_list: List[OkrBatch]) -> "BatchGetOkrResponseBodyBuilder":
        self._batch_get_okr_response_body.okr_list = okr_list
        return self

    def build(self) -> "BatchGetOkrResponseBody":
        return self._batch_get_okr_response_body
