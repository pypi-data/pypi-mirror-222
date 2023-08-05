# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offer_schema_detail import OfferSchemaDetail


class GetOfferSchemaResponseBody(object):
    _types = {
        "id": str,
        "scenario": int,
        "version": int,
        "object_list": List[OfferSchemaDetail],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.scenario: Optional[int] = None
        self.version: Optional[int] = None
        self.object_list: Optional[List[OfferSchemaDetail]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetOfferSchemaResponseBodyBuilder":
        return GetOfferSchemaResponseBodyBuilder()


class GetOfferSchemaResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_offer_schema_response_body = GetOfferSchemaResponseBody()

    def id(self, id: str) -> "GetOfferSchemaResponseBodyBuilder":
        self._get_offer_schema_response_body.id = id
        return self

    def scenario(self, scenario: int) -> "GetOfferSchemaResponseBodyBuilder":
        self._get_offer_schema_response_body.scenario = scenario
        return self

    def version(self, version: int) -> "GetOfferSchemaResponseBodyBuilder":
        self._get_offer_schema_response_body.version = version
        return self

    def object_list(self, object_list: List[OfferSchemaDetail]) -> "GetOfferSchemaResponseBodyBuilder":
        self._get_offer_schema_response_body.object_list = object_list
        return self

    def build(self) -> "GetOfferSchemaResponseBody":
        return self._get_offer_schema_response_body
