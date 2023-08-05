# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offer_schema_detail import OfferSchemaDetail


class OfferSchema(object):
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
    def builder() -> "OfferSchemaBuilder":
        return OfferSchemaBuilder()


class OfferSchemaBuilder(object):
    def __init__(self) -> None:
        self._offer_schema = OfferSchema()

    def id(self, id: str) -> "OfferSchemaBuilder":
        self._offer_schema.id = id
        return self

    def scenario(self, scenario: int) -> "OfferSchemaBuilder":
        self._offer_schema.scenario = scenario
        return self

    def version(self, version: int) -> "OfferSchemaBuilder":
        self._offer_schema.version = version
        return self

    def object_list(self, object_list: List[OfferSchemaDetail]) -> "OfferSchemaBuilder":
        self._offer_schema.object_list = object_list
        return self

    def build(self) -> "OfferSchema":
        return self._offer_schema
