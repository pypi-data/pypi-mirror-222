# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RemoveTasklistTaskRequestBody(object):
    _types = {
        "tasklist_guid": str,
    }

    def __init__(self, d=None):
        self.tasklist_guid: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemoveTasklistTaskRequestBodyBuilder":
        return RemoveTasklistTaskRequestBodyBuilder()


class RemoveTasklistTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._remove_tasklist_task_request_body = RemoveTasklistTaskRequestBody()

    def tasklist_guid(self, tasklist_guid: str) -> "RemoveTasklistTaskRequestBodyBuilder":
        self._remove_tasklist_task_request_body.tasklist_guid = tasklist_guid
        return self

    def build(self) -> "RemoveTasklistTaskRequestBody":
        return self._remove_tasklist_task_request_body
