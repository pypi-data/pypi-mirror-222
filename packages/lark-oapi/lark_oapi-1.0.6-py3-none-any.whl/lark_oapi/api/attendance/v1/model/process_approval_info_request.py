# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .process_approval_info_request_body import ProcessApprovalInfoRequestBody


class ProcessApprovalInfoRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ProcessApprovalInfoRequestBody] = None

    @staticmethod
    def builder() -> "ProcessApprovalInfoRequestBuilder":
        return ProcessApprovalInfoRequestBuilder()


class ProcessApprovalInfoRequestBuilder(object):

    def __init__(self) -> None:
        process_approval_info_request = ProcessApprovalInfoRequest()
        process_approval_info_request.http_method = HttpMethod.POST
        process_approval_info_request.uri = "/open-apis/attendance/v1/approval_infos/process"
        process_approval_info_request.token_types = {AccessTokenType.TENANT}
        self._process_approval_info_request: ProcessApprovalInfoRequest = process_approval_info_request

    def request_body(self, request_body: ProcessApprovalInfoRequestBody) -> "ProcessApprovalInfoRequestBuilder":
        self._process_approval_info_request.request_body = request_body
        self._process_approval_info_request.body = request_body
        return self

    def build(self) -> ProcessApprovalInfoRequest:
        return self._process_approval_info_request
