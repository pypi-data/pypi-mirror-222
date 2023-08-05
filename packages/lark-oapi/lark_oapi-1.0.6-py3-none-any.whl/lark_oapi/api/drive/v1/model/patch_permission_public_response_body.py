# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .permission_public import PermissionPublic


class PatchPermissionPublicResponseBody(object):
    _types = {
        "permission_public": PermissionPublic,
    }

    def __init__(self, d=None):
        self.permission_public: Optional[PermissionPublic] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchPermissionPublicResponseBodyBuilder":
        return PatchPermissionPublicResponseBodyBuilder()


class PatchPermissionPublicResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_permission_public_response_body = PatchPermissionPublicResponseBody()

    def permission_public(self, permission_public: PermissionPublic) -> "PatchPermissionPublicResponseBodyBuilder":
        self._patch_permission_public_response_body.permission_public = permission_public
        return self

    def build(self) -> "PatchPermissionPublicResponseBody":
        return self._patch_permission_public_response_body
