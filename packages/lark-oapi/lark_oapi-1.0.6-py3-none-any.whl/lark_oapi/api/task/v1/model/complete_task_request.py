# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class CompleteTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_id: Optional[str] = None

    @staticmethod
    def builder() -> "CompleteTaskRequestBuilder":
        return CompleteTaskRequestBuilder()


class CompleteTaskRequestBuilder(object):

    def __init__(self) -> None:
        complete_task_request = CompleteTaskRequest()
        complete_task_request.http_method = HttpMethod.POST
        complete_task_request.uri = "/open-apis/task/v1/tasks/:task_id/complete"
        complete_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._complete_task_request: CompleteTaskRequest = complete_task_request

    def task_id(self, task_id: str) -> "CompleteTaskRequestBuilder":
        self._complete_task_request.task_id = task_id
        self._complete_task_request.paths["task_id"] = str(task_id)
        return self

    def build(self) -> CompleteTaskRequest:
        return self._complete_task_request
