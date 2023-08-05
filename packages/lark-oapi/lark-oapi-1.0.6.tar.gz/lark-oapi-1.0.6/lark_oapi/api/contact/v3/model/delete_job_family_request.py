# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteJobFamilyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_family_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteJobFamilyRequestBuilder":
        return DeleteJobFamilyRequestBuilder()


class DeleteJobFamilyRequestBuilder(object):

    def __init__(self) -> None:
        delete_job_family_request = DeleteJobFamilyRequest()
        delete_job_family_request.http_method = HttpMethod.DELETE
        delete_job_family_request.uri = "/open-apis/contact/v3/job_families/:job_family_id"
        delete_job_family_request.token_types = {AccessTokenType.TENANT}
        self._delete_job_family_request: DeleteJobFamilyRequest = delete_job_family_request

    def job_family_id(self, job_family_id: str) -> "DeleteJobFamilyRequestBuilder":
        self._delete_job_family_request.job_family_id = job_family_id
        self._delete_job_family_request.paths["job_family_id"] = str(job_family_id)
        return self

    def build(self) -> DeleteJobFamilyRequest:
        return self._delete_job_family_request
