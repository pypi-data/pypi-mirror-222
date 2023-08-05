# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteShiftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.shift_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteShiftRequestBuilder":
        return DeleteShiftRequestBuilder()


class DeleteShiftRequestBuilder(object):

    def __init__(self) -> None:
        delete_shift_request = DeleteShiftRequest()
        delete_shift_request.http_method = HttpMethod.DELETE
        delete_shift_request.uri = "/open-apis/attendance/v1/shifts/:shift_id"
        delete_shift_request.token_types = {AccessTokenType.TENANT}
        self._delete_shift_request: DeleteShiftRequest = delete_shift_request

    def shift_id(self, shift_id: str) -> "DeleteShiftRequestBuilder":
        self._delete_shift_request.shift_id = shift_id
        self._delete_shift_request.paths["shift_id"] = str(shift_id)
        return self

    def build(self) -> DeleteShiftRequest:
        return self._delete_shift_request
