# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .national_id_type import NationalIdType


class CreateNationalIdTypeResponseBody(object):
    _types = {
        "national_id_type": NationalIdType,
    }

    def __init__(self, d=None):
        self.national_id_type: Optional[NationalIdType] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateNationalIdTypeResponseBodyBuilder":
        return CreateNationalIdTypeResponseBodyBuilder()


class CreateNationalIdTypeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_national_id_type_response_body = CreateNationalIdTypeResponseBody()

    def national_id_type(self, national_id_type: NationalIdType) -> "CreateNationalIdTypeResponseBodyBuilder":
        self._create_national_id_type_response_body.national_id_type = national_id_type
        return self

    def build(self) -> "CreateNationalIdTypeResponseBody":
        return self._create_national_id_type_response_body
