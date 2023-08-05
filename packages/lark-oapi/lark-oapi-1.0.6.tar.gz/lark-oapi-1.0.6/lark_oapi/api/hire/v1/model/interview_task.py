# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class InterviewTask(object):
    _types = {
        "id": str,
        "job_id": str,
        "talent_id": str,
        "application_id": str,
        "activity_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.activity_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewTaskBuilder":
        return InterviewTaskBuilder()


class InterviewTaskBuilder(object):
    def __init__(self) -> None:
        self._interview_task = InterviewTask()

    def id(self, id: str) -> "InterviewTaskBuilder":
        self._interview_task.id = id
        return self

    def job_id(self, job_id: str) -> "InterviewTaskBuilder":
        self._interview_task.job_id = job_id
        return self

    def talent_id(self, talent_id: str) -> "InterviewTaskBuilder":
        self._interview_task.talent_id = talent_id
        return self

    def application_id(self, application_id: str) -> "InterviewTaskBuilder":
        self._interview_task.application_id = application_id
        return self

    def activity_status(self, activity_status: int) -> "InterviewTaskBuilder":
        self._interview_task.activity_status = activity_status
        return self

    def build(self) -> "InterviewTask":
        return self._interview_task
