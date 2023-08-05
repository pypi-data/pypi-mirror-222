# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .prehire_create import PrehireCreate


class CreatePreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[PrehireCreate] = None

    @staticmethod
    def builder() -> "CreatePreHireRequestBuilder":
        return CreatePreHireRequestBuilder()


class CreatePreHireRequestBuilder(object):

    def __init__(self) -> None:
        create_pre_hire_request = CreatePreHireRequest()
        create_pre_hire_request.http_method = HttpMethod.POST
        create_pre_hire_request.uri = "/open-apis/corehr/v2/pre_hires"
        create_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._create_pre_hire_request: CreatePreHireRequest = create_pre_hire_request

    def request_body(self, request_body: PrehireCreate) -> "CreatePreHireRequestBuilder":
        self._create_pre_hire_request.request_body = request_body
        self._create_pre_hire_request.body = request_body
        return self

    def build(self) -> CreatePreHireRequest:
        return self._create_pre_hire_request
