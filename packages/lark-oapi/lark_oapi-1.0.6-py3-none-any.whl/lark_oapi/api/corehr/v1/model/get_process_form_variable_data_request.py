# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetProcessFormVariableDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.process_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetProcessFormVariableDataRequestBuilder":
        return GetProcessFormVariableDataRequestBuilder()


class GetProcessFormVariableDataRequestBuilder(object):

    def __init__(self) -> None:
        get_process_form_variable_data_request = GetProcessFormVariableDataRequest()
        get_process_form_variable_data_request.http_method = HttpMethod.GET
        get_process_form_variable_data_request.uri = "/open-apis/corehr/v1/processes/:process_id/form_variable_data"
        get_process_form_variable_data_request.token_types = {AccessTokenType.TENANT}
        self._get_process_form_variable_data_request: GetProcessFormVariableDataRequest = get_process_form_variable_data_request

    def process_id(self, process_id: str) -> "GetProcessFormVariableDataRequestBuilder":
        self._get_process_form_variable_data_request.process_id = process_id
        self._get_process_form_variable_data_request.paths["process_id"] = str(process_id)
        return self

    def build(self) -> GetProcessFormVariableDataRequest:
        return self._get_process_form_variable_data_request
