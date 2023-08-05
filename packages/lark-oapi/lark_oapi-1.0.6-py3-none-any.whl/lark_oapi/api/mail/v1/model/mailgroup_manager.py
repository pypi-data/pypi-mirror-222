# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MailgroupManager(object):
    _types = {
        "user_id": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MailgroupManagerBuilder":
        return MailgroupManagerBuilder()


class MailgroupManagerBuilder(object):
    def __init__(self) -> None:
        self._mailgroup_manager = MailgroupManager()

    def user_id(self, user_id: str) -> "MailgroupManagerBuilder":
        self._mailgroup_manager.user_id = user_id
        return self

    def build(self) -> "MailgroupManager":
        return self._mailgroup_manager
