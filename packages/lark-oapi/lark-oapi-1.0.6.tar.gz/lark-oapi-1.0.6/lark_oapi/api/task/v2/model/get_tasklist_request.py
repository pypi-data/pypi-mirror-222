# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetTasklistRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.tasklist_guid: Optional[str] = None

    @staticmethod
    def builder() -> "GetTasklistRequestBuilder":
        return GetTasklistRequestBuilder()


class GetTasklistRequestBuilder(object):

    def __init__(self) -> None:
        get_tasklist_request = GetTasklistRequest()
        get_tasklist_request.http_method = HttpMethod.GET
        get_tasklist_request.uri = "/open-apis/task/v2/tasklists/:tasklist_guid"
        get_tasklist_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_tasklist_request: GetTasklistRequest = get_tasklist_request

    def user_id_type(self, user_id_type: str) -> "GetTasklistRequestBuilder":
        self._get_tasklist_request.user_id_type = user_id_type
        self._get_tasklist_request.add_query("user_id_type", user_id_type)
        return self

    def tasklist_guid(self, tasklist_guid: str) -> "GetTasklistRequestBuilder":
        self._get_tasklist_request.tasklist_guid = tasklist_guid
        self._get_tasklist_request.paths["tasklist_guid"] = str(tasklist_guid)
        return self

    def build(self) -> GetTasklistRequest:
        return self._get_tasklist_request
