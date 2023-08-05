# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum


class WorkEmail(object):
    _types = {
        "email": str,
        "email_usage": Enum,
    }

    def __init__(self, d=None):
        self.email: Optional[str] = None
        self.email_usage: Optional[Enum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkEmailBuilder":
        return WorkEmailBuilder()


class WorkEmailBuilder(object):
    def __init__(self) -> None:
        self._work_email = WorkEmail()

    def email(self, email: str) -> "WorkEmailBuilder":
        self._work_email.email = email
        return self

    def email_usage(self, email_usage: Enum) -> "WorkEmailBuilder":
        self._work_email.email_usage = email_usage
        return self

    def build(self) -> "WorkEmail":
        return self._work_email
