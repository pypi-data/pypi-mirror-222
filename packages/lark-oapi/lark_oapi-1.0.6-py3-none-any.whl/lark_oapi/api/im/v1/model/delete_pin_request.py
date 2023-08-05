# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeletePinRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.message_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeletePinRequestBuilder":
        return DeletePinRequestBuilder()


class DeletePinRequestBuilder(object):

    def __init__(self) -> None:
        delete_pin_request = DeletePinRequest()
        delete_pin_request.http_method = HttpMethod.DELETE
        delete_pin_request.uri = "/open-apis/im/v1/pins/:message_id"
        delete_pin_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_pin_request: DeletePinRequest = delete_pin_request

    def message_id(self, message_id: str) -> "DeletePinRequestBuilder":
        self._delete_pin_request.message_id = message_id
        self._delete_pin_request.paths["message_id"] = str(message_id)
        return self

    def build(self) -> DeletePinRequest:
        return self._delete_pin_request
