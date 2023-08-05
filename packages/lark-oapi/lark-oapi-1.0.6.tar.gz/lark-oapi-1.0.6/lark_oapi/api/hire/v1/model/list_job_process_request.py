# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListJobProcessRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobProcessRequestBuilder":
        return ListJobProcessRequestBuilder()


class ListJobProcessRequestBuilder(object):

    def __init__(self) -> None:
        list_job_process_request = ListJobProcessRequest()
        list_job_process_request.http_method = HttpMethod.GET
        list_job_process_request.uri = "/open-apis/hire/v1/job_processes"
        list_job_process_request.token_types = {AccessTokenType.TENANT}
        self._list_job_process_request: ListJobProcessRequest = list_job_process_request

    def page_size(self, page_size: int) -> "ListJobProcessRequestBuilder":
        self._list_job_process_request.page_size = page_size
        self._list_job_process_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListJobProcessRequestBuilder":
        self._list_job_process_request.page_token = page_token
        self._list_job_process_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListJobProcessRequest:
        return self._list_job_process_request
