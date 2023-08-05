# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteLeaveGrantingRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.leave_granting_record_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteLeaveGrantingRecordRequestBuilder":
        return DeleteLeaveGrantingRecordRequestBuilder()


class DeleteLeaveGrantingRecordRequestBuilder(object):

    def __init__(self) -> None:
        delete_leave_granting_record_request = DeleteLeaveGrantingRecordRequest()
        delete_leave_granting_record_request.http_method = HttpMethod.DELETE
        delete_leave_granting_record_request.uri = "/open-apis/corehr/v1/leave_granting_records/:leave_granting_record_id"
        delete_leave_granting_record_request.token_types = {AccessTokenType.TENANT}
        self._delete_leave_granting_record_request: DeleteLeaveGrantingRecordRequest = delete_leave_granting_record_request

    def leave_granting_record_id(self, leave_granting_record_id: str) -> "DeleteLeaveGrantingRecordRequestBuilder":
        self._delete_leave_granting_record_request.leave_granting_record_id = leave_granting_record_id
        self._delete_leave_granting_record_request.paths["leave_granting_record_id"] = str(leave_granting_record_id)
        return self

    def build(self) -> DeleteLeaveGrantingRecordRequest:
        return self._delete_leave_granting_record_request
