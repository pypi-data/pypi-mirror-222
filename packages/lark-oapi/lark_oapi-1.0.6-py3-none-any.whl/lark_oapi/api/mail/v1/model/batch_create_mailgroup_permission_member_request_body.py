# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .mailgroup_permission_member import MailgroupPermissionMember


class BatchCreateMailgroupPermissionMemberRequestBody(object):
    _types = {
        "items": List[MailgroupPermissionMember],
    }

    def __init__(self, d=None):
        self.items: Optional[List[MailgroupPermissionMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateMailgroupPermissionMemberRequestBodyBuilder":
        return BatchCreateMailgroupPermissionMemberRequestBodyBuilder()


class BatchCreateMailgroupPermissionMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_mailgroup_permission_member_request_body = BatchCreateMailgroupPermissionMemberRequestBody()

    def items(self, items: List[MailgroupPermissionMember]) -> "BatchCreateMailgroupPermissionMemberRequestBodyBuilder":
        self._batch_create_mailgroup_permission_member_request_body.items = items
        return self

    def build(self) -> "BatchCreateMailgroupPermissionMemberRequestBody":
        return self._batch_create_mailgroup_permission_member_request_body
