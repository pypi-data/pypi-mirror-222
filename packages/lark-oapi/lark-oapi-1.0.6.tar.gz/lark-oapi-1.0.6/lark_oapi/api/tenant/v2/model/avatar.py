# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Avatar(object):
    _types = {
        "avatar_origin": str,
        "avatar_72": str,
        "avatar_240": str,
        "avatar_640": str,
    }

    def __init__(self, d=None):
        self.avatar_origin: Optional[str] = None
        self.avatar_72: Optional[str] = None
        self.avatar_240: Optional[str] = None
        self.avatar_640: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AvatarBuilder":
        return AvatarBuilder()


class AvatarBuilder(object):
    def __init__(self) -> None:
        self._avatar = Avatar()

    def avatar_origin(self, avatar_origin: str) -> "AvatarBuilder":
        self._avatar.avatar_origin = avatar_origin
        return self

    def avatar_72(self, avatar_72: str) -> "AvatarBuilder":
        self._avatar.avatar_72 = avatar_72
        return self

    def avatar_240(self, avatar_240: str) -> "AvatarBuilder":
        self._avatar.avatar_240 = avatar_240
        return self

    def avatar_640(self, avatar_640: str) -> "AvatarBuilder":
        self._avatar.avatar_640 = avatar_640
        return self

    def build(self) -> "Avatar":
        return self._avatar
