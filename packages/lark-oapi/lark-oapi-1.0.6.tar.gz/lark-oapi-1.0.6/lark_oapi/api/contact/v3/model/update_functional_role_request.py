# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_functional_role_request_body import UpdateFunctionalRoleRequestBody


class UpdateFunctionalRoleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.role_id: Optional[str] = None
        self.request_body: Optional[UpdateFunctionalRoleRequestBody] = None

    @staticmethod
    def builder() -> "UpdateFunctionalRoleRequestBuilder":
        return UpdateFunctionalRoleRequestBuilder()


class UpdateFunctionalRoleRequestBuilder(object):

    def __init__(self) -> None:
        update_functional_role_request = UpdateFunctionalRoleRequest()
        update_functional_role_request.http_method = HttpMethod.PUT
        update_functional_role_request.uri = "/open-apis/contact/v3/functional_roles/:role_id"
        update_functional_role_request.token_types = {AccessTokenType.TENANT}
        self._update_functional_role_request: UpdateFunctionalRoleRequest = update_functional_role_request

    def role_id(self, role_id: str) -> "UpdateFunctionalRoleRequestBuilder":
        self._update_functional_role_request.role_id = role_id
        self._update_functional_role_request.paths["role_id"] = str(role_id)
        return self

    def request_body(self, request_body: UpdateFunctionalRoleRequestBody) -> "UpdateFunctionalRoleRequestBuilder":
        self._update_functional_role_request.request_body = request_body
        self._update_functional_role_request.body = request_body
        return self

    def build(self) -> UpdateFunctionalRoleRequest:
        return self._update_functional_role_request
