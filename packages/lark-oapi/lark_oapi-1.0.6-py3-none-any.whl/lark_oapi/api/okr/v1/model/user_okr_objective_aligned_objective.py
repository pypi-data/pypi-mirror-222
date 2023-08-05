# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_okr_objective_aligned_objective_owner import UserOkrObjectiveAlignedObjectiveOwner


class UserOkrObjectiveAlignedObjective(object):
    _types = {
        "id": str,
        "okr_id": str,
        "owner": UserOkrObjectiveAlignedObjectiveOwner,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.okr_id: Optional[str] = None
        self.owner: Optional[UserOkrObjectiveAlignedObjectiveOwner] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserOkrObjectiveAlignedObjectiveBuilder":
        return UserOkrObjectiveAlignedObjectiveBuilder()


class UserOkrObjectiveAlignedObjectiveBuilder(object):
    def __init__(self) -> None:
        self._user_okr_objective_aligned_objective = UserOkrObjectiveAlignedObjective()

    def id(self, id: str) -> "UserOkrObjectiveAlignedObjectiveBuilder":
        self._user_okr_objective_aligned_objective.id = id
        return self

    def okr_id(self, okr_id: str) -> "UserOkrObjectiveAlignedObjectiveBuilder":
        self._user_okr_objective_aligned_objective.okr_id = okr_id
        return self

    def owner(self, owner: UserOkrObjectiveAlignedObjectiveOwner) -> "UserOkrObjectiveAlignedObjectiveBuilder":
        self._user_okr_objective_aligned_objective.owner = owner
        return self

    def build(self) -> "UserOkrObjectiveAlignedObjective":
        return self._user_okr_objective_aligned_objective
