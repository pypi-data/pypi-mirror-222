# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Member(object):
    _types = {
        "member_type": str,
        "member_id": str,
        "member_role": str,
    }

    def __init__(self, d=None):
        self.member_type: Optional[str] = None
        self.member_id: Optional[str] = None
        self.member_role: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MemberBuilder":
        return MemberBuilder()


class MemberBuilder(object):
    def __init__(self) -> None:
        self._member = Member()

    def member_type(self, member_type: str) -> "MemberBuilder":
        self._member.member_type = member_type
        return self

    def member_id(self, member_id: str) -> "MemberBuilder":
        self._member.member_id = member_id
        return self

    def member_role(self, member_role: str) -> "MemberBuilder":
        self._member.member_role = member_role
        return self

    def build(self) -> "Member":
        return self._member
