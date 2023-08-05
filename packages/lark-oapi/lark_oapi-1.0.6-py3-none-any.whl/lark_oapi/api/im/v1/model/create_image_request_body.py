# Code generated by Lark OpenAPI.

from typing import *
from typing import IO

from lark_oapi.core.construct import init


class CreateImageRequestBody(object):
    _types = {
        "image_type": str,
        "image": IO[Any],
    }

    def __init__(self, d=None):
        self.image_type: Optional[str] = None
        self.image: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateImageRequestBodyBuilder":
        return CreateImageRequestBodyBuilder()


class CreateImageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_image_request_body = CreateImageRequestBody()

    def image_type(self, image_type: str) -> "CreateImageRequestBodyBuilder":
        self._create_image_request_body.image_type = image_type
        return self

    def image(self, image: IO[Any]) -> "CreateImageRequestBodyBuilder":
        self._create_image_request_body.image = image
        return self

    def build(self) -> "CreateImageRequestBody":
        return self._create_image_request_body
