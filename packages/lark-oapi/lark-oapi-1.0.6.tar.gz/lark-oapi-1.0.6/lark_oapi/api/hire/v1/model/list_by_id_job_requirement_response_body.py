# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_requirement_dto import JobRequirementDto


class ListByIdJobRequirementResponseBody(object):
    _types = {
        "items": List[JobRequirementDto],
    }

    def __init__(self, d=None):
        self.items: Optional[List[JobRequirementDto]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListByIdJobRequirementResponseBodyBuilder":
        return ListByIdJobRequirementResponseBodyBuilder()


class ListByIdJobRequirementResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_by_id_job_requirement_response_body = ListByIdJobRequirementResponseBody()

    def items(self, items: List[JobRequirementDto]) -> "ListByIdJobRequirementResponseBodyBuilder":
        self._list_by_id_job_requirement_response_body.items = items
        return self

    def build(self) -> "ListByIdJobRequirementResponseBody":
        return self._list_by_id_job_requirement_response_body
