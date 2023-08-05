# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetSubdivisionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.subdivision_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetSubdivisionRequestBuilder":
        return GetSubdivisionRequestBuilder()


class GetSubdivisionRequestBuilder(object):

    def __init__(self) -> None:
        get_subdivision_request = GetSubdivisionRequest()
        get_subdivision_request.http_method = HttpMethod.GET
        get_subdivision_request.uri = "/open-apis/corehr/v1/subdivisions/:subdivision_id"
        get_subdivision_request.token_types = {AccessTokenType.TENANT}
        self._get_subdivision_request: GetSubdivisionRequest = get_subdivision_request

    def subdivision_id(self, subdivision_id: str) -> "GetSubdivisionRequestBuilder":
        self._get_subdivision_request.subdivision_id = subdivision_id
        self._get_subdivision_request.paths["subdivision_id"] = str(subdivision_id)
        return self

    def build(self) -> GetSubdivisionRequest:
        return self._get_subdivision_request
