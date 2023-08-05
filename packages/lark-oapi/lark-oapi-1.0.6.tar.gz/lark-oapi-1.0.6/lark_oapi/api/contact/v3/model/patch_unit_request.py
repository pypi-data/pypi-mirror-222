# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_unit_request_body import PatchUnitRequestBody


class PatchUnitRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.unit_id: Optional[str] = None
        self.request_body: Optional[PatchUnitRequestBody] = None

    @staticmethod
    def builder() -> "PatchUnitRequestBuilder":
        return PatchUnitRequestBuilder()


class PatchUnitRequestBuilder(object):

    def __init__(self) -> None:
        patch_unit_request = PatchUnitRequest()
        patch_unit_request.http_method = HttpMethod.PATCH
        patch_unit_request.uri = "/open-apis/contact/v3/unit/:unit_id"
        patch_unit_request.token_types = {AccessTokenType.TENANT}
        self._patch_unit_request: PatchUnitRequest = patch_unit_request

    def unit_id(self, unit_id: str) -> "PatchUnitRequestBuilder":
        self._patch_unit_request.unit_id = unit_id
        self._patch_unit_request.paths["unit_id"] = str(unit_id)
        return self

    def request_body(self, request_body: PatchUnitRequestBody) -> "PatchUnitRequestBuilder":
        self._patch_unit_request.request_body = request_body
        self._patch_unit_request.body = request_body
        return self

    def build(self) -> PatchUnitRequest:
        return self._patch_unit_request
