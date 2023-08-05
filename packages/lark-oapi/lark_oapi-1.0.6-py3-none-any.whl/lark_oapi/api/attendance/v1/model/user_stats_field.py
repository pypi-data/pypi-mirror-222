# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .field import Field


class UserStatsField(object):
    _types = {
        "stats_type": str,
        "user_id": str,
        "fields": List[Field],
    }

    def __init__(self, d=None):
        self.stats_type: Optional[str] = None
        self.user_id: Optional[str] = None
        self.fields: Optional[List[Field]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserStatsFieldBuilder":
        return UserStatsFieldBuilder()


class UserStatsFieldBuilder(object):
    def __init__(self) -> None:
        self._user_stats_field = UserStatsField()

    def stats_type(self, stats_type: str) -> "UserStatsFieldBuilder":
        self._user_stats_field.stats_type = stats_type
        return self

    def user_id(self, user_id: str) -> "UserStatsFieldBuilder":
        self._user_stats_field.user_id = user_id
        return self

    def fields(self, fields: List[Field]) -> "UserStatsFieldBuilder":
        self._user_stats_field.fields = fields
        return self

    def build(self) -> "UserStatsField":
        return self._user_stats_field
