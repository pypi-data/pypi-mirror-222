# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListJobRequirementSchemaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListJobRequirementSchemaRequestBuilder":
        return ListJobRequirementSchemaRequestBuilder()


class ListJobRequirementSchemaRequestBuilder(object):

    def __init__(self) -> None:
        list_job_requirement_schema_request = ListJobRequirementSchemaRequest()
        list_job_requirement_schema_request.http_method = HttpMethod.GET
        list_job_requirement_schema_request.uri = "/open-apis/hire/v1/job_requirement_schemas"
        list_job_requirement_schema_request.token_types = {AccessTokenType.TENANT}
        self._list_job_requirement_schema_request: ListJobRequirementSchemaRequest = list_job_requirement_schema_request

    def page_token(self, page_token: str) -> "ListJobRequirementSchemaRequestBuilder":
        self._list_job_requirement_schema_request.page_token = page_token
        self._list_job_requirement_schema_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListJobRequirementSchemaRequestBuilder":
        self._list_job_requirement_schema_request.page_size = page_size
        self._list_job_requirement_schema_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListJobRequirementSchemaRequest:
        return self._list_job_requirement_schema_request
