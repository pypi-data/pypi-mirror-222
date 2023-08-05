# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchGetIdUserRequestBody(object):
    _types = {
        "emails": List[str],
        "mobiles": List[str],
    }

    def __init__(self, d=None):
        self.emails: Optional[List[str]] = None
        self.mobiles: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetIdUserRequestBodyBuilder":
        return BatchGetIdUserRequestBodyBuilder()


class BatchGetIdUserRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_id_user_request_body = BatchGetIdUserRequestBody()

    def emails(self, emails: List[str]) -> "BatchGetIdUserRequestBodyBuilder":
        self._batch_get_id_user_request_body.emails = emails
        return self

    def mobiles(self, mobiles: List[str]) -> "BatchGetIdUserRequestBodyBuilder":
        self._batch_get_id_user_request_body.mobiles = mobiles
        return self

    def build(self) -> "BatchGetIdUserRequestBody":
        return self._batch_get_id_user_request_body
