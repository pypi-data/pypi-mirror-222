# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .user_auth_data_relation import UserAuthDataRelation


class BindUserAuthDataRelationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[UserAuthDataRelation] = None

    @staticmethod
    def builder() -> "BindUserAuthDataRelationRequestBuilder":
        return BindUserAuthDataRelationRequestBuilder()


class BindUserAuthDataRelationRequestBuilder(object):

    def __init__(self) -> None:
        bind_user_auth_data_relation_request = BindUserAuthDataRelationRequest()
        bind_user_auth_data_relation_request.http_method = HttpMethod.POST
        bind_user_auth_data_relation_request.uri = "/open-apis/mdm/v1/user_auth_data_relations/bind"
        bind_user_auth_data_relation_request.token_types = {AccessTokenType.TENANT}
        self._bind_user_auth_data_relation_request: BindUserAuthDataRelationRequest = bind_user_auth_data_relation_request

    def user_id_type(self, user_id_type: str) -> "BindUserAuthDataRelationRequestBuilder":
        self._bind_user_auth_data_relation_request.user_id_type = user_id_type
        self._bind_user_auth_data_relation_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: UserAuthDataRelation) -> "BindUserAuthDataRelationRequestBuilder":
        self._bind_user_auth_data_relation_request.request_body = request_body
        self._bind_user_auth_data_relation_request.body = request_body
        return self

    def build(self) -> BindUserAuthDataRelationRequest:
        return self._bind_user_auth_data_relation_request
