# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateAccessTokenRequestBody(object):
    _types = {
        "grant_type": str,
        "code": str,
    }

    def __init__(self, d=None):
        self.grant_type: Optional[str] = None
        self.code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAccessTokenRequestBodyBuilder":
        return CreateAccessTokenRequestBodyBuilder()


class CreateAccessTokenRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_access_token_request_body = CreateAccessTokenRequestBody()

    def grant_type(self, grant_type: str) -> "CreateAccessTokenRequestBodyBuilder":
        self._create_access_token_request_body.grant_type = grant_type
        return self

    def code(self, code: str) -> "CreateAccessTokenRequestBodyBuilder":
        self._create_access_token_request_body.code = code
        return self

    def build(self) -> "CreateAccessTokenRequestBody":
        return self._create_access_token_request_body
