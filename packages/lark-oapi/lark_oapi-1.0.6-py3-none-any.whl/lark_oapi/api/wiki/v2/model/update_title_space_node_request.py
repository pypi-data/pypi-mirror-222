# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_title_space_node_request_body import UpdateTitleSpaceNodeRequestBody


class UpdateTitleSpaceNodeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.space_id: Optional[int] = None
        self.node_token: Optional[str] = None
        self.request_body: Optional[UpdateTitleSpaceNodeRequestBody] = None

    @staticmethod
    def builder() -> "UpdateTitleSpaceNodeRequestBuilder":
        return UpdateTitleSpaceNodeRequestBuilder()


class UpdateTitleSpaceNodeRequestBuilder(object):

    def __init__(self) -> None:
        update_title_space_node_request = UpdateTitleSpaceNodeRequest()
        update_title_space_node_request.http_method = HttpMethod.POST
        update_title_space_node_request.uri = "/open-apis/wiki/v2/spaces/:space_id/nodes/:node_token/update_title"
        update_title_space_node_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._update_title_space_node_request: UpdateTitleSpaceNodeRequest = update_title_space_node_request

    def space_id(self, space_id: int) -> "UpdateTitleSpaceNodeRequestBuilder":
        self._update_title_space_node_request.space_id = space_id
        self._update_title_space_node_request.paths["space_id"] = str(space_id)
        return self

    def node_token(self, node_token: str) -> "UpdateTitleSpaceNodeRequestBuilder":
        self._update_title_space_node_request.node_token = node_token
        self._update_title_space_node_request.paths["node_token"] = str(node_token)
        return self

    def request_body(self, request_body: UpdateTitleSpaceNodeRequestBody) -> "UpdateTitleSpaceNodeRequestBuilder":
        self._update_title_space_node_request.request_body = request_body
        self._update_title_space_node_request.body = request_body
        return self

    def build(self) -> UpdateTitleSpaceNodeRequest:
        return self._update_title_space_node_request
