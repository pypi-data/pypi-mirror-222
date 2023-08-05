# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ExternalApplication(object):
    _types = {
        "id": str,
        "external_id": str,
        "job_recruitment_type": int,
        "job_title": str,
        "resume_source": str,
        "stage": str,
        "talent_id": str,
        "termination_reason": str,
        "delivery_type": int,
        "modify_time": int,
        "termination_type": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.external_id: Optional[str] = None
        self.job_recruitment_type: Optional[int] = None
        self.job_title: Optional[str] = None
        self.resume_source: Optional[str] = None
        self.stage: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.termination_reason: Optional[str] = None
        self.delivery_type: Optional[int] = None
        self.modify_time: Optional[int] = None
        self.termination_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalApplicationBuilder":
        return ExternalApplicationBuilder()


class ExternalApplicationBuilder(object):
    def __init__(self) -> None:
        self._external_application = ExternalApplication()

    def id(self, id: str) -> "ExternalApplicationBuilder":
        self._external_application.id = id
        return self

    def external_id(self, external_id: str) -> "ExternalApplicationBuilder":
        self._external_application.external_id = external_id
        return self

    def job_recruitment_type(self, job_recruitment_type: int) -> "ExternalApplicationBuilder":
        self._external_application.job_recruitment_type = job_recruitment_type
        return self

    def job_title(self, job_title: str) -> "ExternalApplicationBuilder":
        self._external_application.job_title = job_title
        return self

    def resume_source(self, resume_source: str) -> "ExternalApplicationBuilder":
        self._external_application.resume_source = resume_source
        return self

    def stage(self, stage: str) -> "ExternalApplicationBuilder":
        self._external_application.stage = stage
        return self

    def talent_id(self, talent_id: str) -> "ExternalApplicationBuilder":
        self._external_application.talent_id = talent_id
        return self

    def termination_reason(self, termination_reason: str) -> "ExternalApplicationBuilder":
        self._external_application.termination_reason = termination_reason
        return self

    def delivery_type(self, delivery_type: int) -> "ExternalApplicationBuilder":
        self._external_application.delivery_type = delivery_type
        return self

    def modify_time(self, modify_time: int) -> "ExternalApplicationBuilder":
        self._external_application.modify_time = modify_time
        return self

    def termination_type(self, termination_type: str) -> "ExternalApplicationBuilder":
        self._external_application.termination_type = termination_type
        return self

    def build(self) -> "ExternalApplication":
        return self._external_application
