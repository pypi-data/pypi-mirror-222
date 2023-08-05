# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchDeleteFunctionalRoleMemberRequestBody(object):
    _types = {
        "members": List[str],
    }

    def __init__(self, d=None):
        self.members: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteFunctionalRoleMemberRequestBodyBuilder":
        return BatchDeleteFunctionalRoleMemberRequestBodyBuilder()


class BatchDeleteFunctionalRoleMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_delete_functional_role_member_request_body = BatchDeleteFunctionalRoleMemberRequestBody()

    def members(self, members: List[str]) -> "BatchDeleteFunctionalRoleMemberRequestBodyBuilder":
        self._batch_delete_functional_role_member_request_body.members = members
        return self

    def build(self) -> "BatchDeleteFunctionalRoleMemberRequestBody":
        return self._batch_delete_functional_role_member_request_body
