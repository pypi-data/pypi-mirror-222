# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .collaborator import Collaborator
from .due import Due
from .follower import Follower
from .origin import Origin


class Task(object):
    _types = {
        "id": str,
        "summary": str,
        "description": str,
        "complete_time": int,
        "creator_id": str,
        "extra": str,
        "create_time": int,
        "update_time": int,
        "due": Due,
        "origin": Origin,
        "can_edit": bool,
        "custom": str,
        "source": int,
        "followers": List[Follower],
        "collaborators": List[Collaborator],
        "collaborator_ids": List[str],
        "follower_ids": List[str],
        "repeat_rule": str,
        "rich_summary": str,
        "rich_description": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.summary: Optional[str] = None
        self.description: Optional[str] = None
        self.complete_time: Optional[int] = None
        self.creator_id: Optional[str] = None
        self.extra: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.due: Optional[Due] = None
        self.origin: Optional[Origin] = None
        self.can_edit: Optional[bool] = None
        self.custom: Optional[str] = None
        self.source: Optional[int] = None
        self.followers: Optional[List[Follower]] = None
        self.collaborators: Optional[List[Collaborator]] = None
        self.collaborator_ids: Optional[List[str]] = None
        self.follower_ids: Optional[List[str]] = None
        self.repeat_rule: Optional[str] = None
        self.rich_summary: Optional[str] = None
        self.rich_description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskBuilder":
        return TaskBuilder()


class TaskBuilder(object):
    def __init__(self) -> None:
        self._task = Task()

    def id(self, id: str) -> "TaskBuilder":
        self._task.id = id
        return self

    def summary(self, summary: str) -> "TaskBuilder":
        self._task.summary = summary
        return self

    def description(self, description: str) -> "TaskBuilder":
        self._task.description = description
        return self

    def complete_time(self, complete_time: int) -> "TaskBuilder":
        self._task.complete_time = complete_time
        return self

    def creator_id(self, creator_id: str) -> "TaskBuilder":
        self._task.creator_id = creator_id
        return self

    def extra(self, extra: str) -> "TaskBuilder":
        self._task.extra = extra
        return self

    def create_time(self, create_time: int) -> "TaskBuilder":
        self._task.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "TaskBuilder":
        self._task.update_time = update_time
        return self

    def due(self, due: Due) -> "TaskBuilder":
        self._task.due = due
        return self

    def origin(self, origin: Origin) -> "TaskBuilder":
        self._task.origin = origin
        return self

    def can_edit(self, can_edit: bool) -> "TaskBuilder":
        self._task.can_edit = can_edit
        return self

    def custom(self, custom: str) -> "TaskBuilder":
        self._task.custom = custom
        return self

    def source(self, source: int) -> "TaskBuilder":
        self._task.source = source
        return self

    def followers(self, followers: List[Follower]) -> "TaskBuilder":
        self._task.followers = followers
        return self

    def collaborators(self, collaborators: List[Collaborator]) -> "TaskBuilder":
        self._task.collaborators = collaborators
        return self

    def collaborator_ids(self, collaborator_ids: List[str]) -> "TaskBuilder":
        self._task.collaborator_ids = collaborator_ids
        return self

    def follower_ids(self, follower_ids: List[str]) -> "TaskBuilder":
        self._task.follower_ids = follower_ids
        return self

    def repeat_rule(self, repeat_rule: str) -> "TaskBuilder":
        self._task.repeat_rule = repeat_rule
        return self

    def rich_summary(self, rich_summary: str) -> "TaskBuilder":
        self._task.rich_summary = rich_summary
        return self

    def rich_description(self, rich_description: str) -> "TaskBuilder":
        self._task.rich_description = rich_description
        return self

    def build(self) -> "Task":
        return self._task
