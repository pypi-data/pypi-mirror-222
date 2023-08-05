# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .transfer_info import TransferInfo


class CreateJobChangeResponseBody(object):
    _types = {
        "job_change_id": str,
        "employment_id": str,
        "status": str,
        "transfer_type_unique_identifier": str,
        "transfer_reason_unique_identifier": str,
        "process_id": str,
        "effective_date": str,
        "created_time": str,
        "transfer_info": TransferInfo,
    }

    def __init__(self, d=None):
        self.job_change_id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.status: Optional[str] = None
        self.transfer_type_unique_identifier: Optional[str] = None
        self.transfer_reason_unique_identifier: Optional[str] = None
        self.process_id: Optional[str] = None
        self.effective_date: Optional[str] = None
        self.created_time: Optional[str] = None
        self.transfer_info: Optional[TransferInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateJobChangeResponseBodyBuilder":
        return CreateJobChangeResponseBodyBuilder()


class CreateJobChangeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_job_change_response_body = CreateJobChangeResponseBody()

    def job_change_id(self, job_change_id: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.job_change_id = job_change_id
        return self

    def employment_id(self, employment_id: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.employment_id = employment_id
        return self

    def status(self, status: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.status = status
        return self

    def transfer_type_unique_identifier(self,
                                        transfer_type_unique_identifier: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.transfer_type_unique_identifier = transfer_type_unique_identifier
        return self

    def transfer_reason_unique_identifier(self,
                                          transfer_reason_unique_identifier: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.transfer_reason_unique_identifier = transfer_reason_unique_identifier
        return self

    def process_id(self, process_id: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.process_id = process_id
        return self

    def effective_date(self, effective_date: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.effective_date = effective_date
        return self

    def created_time(self, created_time: str) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.created_time = created_time
        return self

    def transfer_info(self, transfer_info: TransferInfo) -> "CreateJobChangeResponseBodyBuilder":
        self._create_job_change_response_body.transfer_info = transfer_info
        return self

    def build(self) -> "CreateJobChangeResponseBody":
        return self._create_job_change_response_body
