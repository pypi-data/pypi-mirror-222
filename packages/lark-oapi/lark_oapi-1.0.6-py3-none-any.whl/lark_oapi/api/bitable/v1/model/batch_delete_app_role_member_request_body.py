# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_role_member_id import AppRoleMemberId


class BatchDeleteAppRoleMemberRequestBody(object):
    _types = {
        "member_list": List[AppRoleMemberId],
    }

    def __init__(self, d=None):
        self.member_list: Optional[List[AppRoleMemberId]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteAppRoleMemberRequestBodyBuilder":
        return BatchDeleteAppRoleMemberRequestBodyBuilder()


class BatchDeleteAppRoleMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_delete_app_role_member_request_body = BatchDeleteAppRoleMemberRequestBody()

    def member_list(self, member_list: List[AppRoleMemberId]) -> "BatchDeleteAppRoleMemberRequestBodyBuilder":
        self._batch_delete_app_role_member_request_body.member_list = member_list
        return self

    def build(self) -> "BatchDeleteAppRoleMemberRequestBody":
        return self._batch_delete_app_role_member_request_body
