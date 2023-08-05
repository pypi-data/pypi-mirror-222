# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job import Job


class PatchJobResponseBody(object):
    _types = {
        "job": Job,
    }

    def __init__(self, d=None):
        self.job: Optional[Job] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchJobResponseBodyBuilder":
        return PatchJobResponseBodyBuilder()


class PatchJobResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_job_response_body = PatchJobResponseBody()

    def job(self, job: Job) -> "PatchJobResponseBodyBuilder":
        self._patch_job_response_body.job = job
        return self

    def build(self) -> "PatchJobResponseBody":
        return self._patch_job_response_body
