# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetBadgeGrantRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.badge_id: Optional[str] = None
        self.grant_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetBadgeGrantRequestBuilder":
        return GetBadgeGrantRequestBuilder()


class GetBadgeGrantRequestBuilder(object):

    def __init__(self) -> None:
        get_badge_grant_request = GetBadgeGrantRequest()
        get_badge_grant_request.http_method = HttpMethod.GET
        get_badge_grant_request.uri = "/open-apis/admin/v1/badges/:badge_id/grants/:grant_id"
        get_badge_grant_request.token_types = {AccessTokenType.TENANT}
        self._get_badge_grant_request: GetBadgeGrantRequest = get_badge_grant_request

    def user_id_type(self, user_id_type: str) -> "GetBadgeGrantRequestBuilder":
        self._get_badge_grant_request.user_id_type = user_id_type
        self._get_badge_grant_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetBadgeGrantRequestBuilder":
        self._get_badge_grant_request.department_id_type = department_id_type
        self._get_badge_grant_request.add_query("department_id_type", department_id_type)
        return self

    def badge_id(self, badge_id: str) -> "GetBadgeGrantRequestBuilder":
        self._get_badge_grant_request.badge_id = badge_id
        self._get_badge_grant_request.paths["badge_id"] = str(badge_id)
        return self

    def grant_id(self, grant_id: str) -> "GetBadgeGrantRequestBuilder":
        self._get_badge_grant_request.grant_id = grant_id
        self._get_badge_grant_request.paths["grant_id"] = str(grant_id)
        return self

    def build(self) -> GetBadgeGrantRequest:
        return self._get_badge_grant_request
