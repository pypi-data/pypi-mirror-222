# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UploadPersonResponseBody(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadPersonResponseBodyBuilder":
        return UploadPersonResponseBodyBuilder()


class UploadPersonResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_person_response_body = UploadPersonResponseBody()

    def id(self, id: str) -> "UploadPersonResponseBodyBuilder":
        self._upload_person_response_body.id = id
        return self

    def build(self) -> "UploadPersonResponseBody":
        return self._upload_person_response_body
