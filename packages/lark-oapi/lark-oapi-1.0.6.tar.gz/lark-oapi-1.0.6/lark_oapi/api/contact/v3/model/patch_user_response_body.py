# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user import User


class PatchUserResponseBody(object):
    _types = {
        "user": User,
    }

    def __init__(self, d=None):
        self.user: Optional[User] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchUserResponseBodyBuilder":
        return PatchUserResponseBodyBuilder()


class PatchUserResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_user_response_body = PatchUserResponseBody()

    def user(self, user: User) -> "PatchUserResponseBodyBuilder":
        self._patch_user_response_body.user = user
        return self

    def build(self) -> "PatchUserResponseBody":
        return self._patch_user_response_body
