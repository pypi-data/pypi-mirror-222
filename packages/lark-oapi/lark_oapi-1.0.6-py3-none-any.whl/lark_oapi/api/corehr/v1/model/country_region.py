# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class CountryRegion(object):
    _types = {
        "id": str,
        "name": List[I18n],
        "alpha_3_code": str,
        "alpha_2_code": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.alpha_3_code: Optional[str] = None
        self.alpha_2_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CountryRegionBuilder":
        return CountryRegionBuilder()


class CountryRegionBuilder(object):
    def __init__(self) -> None:
        self._country_region = CountryRegion()

    def id(self, id: str) -> "CountryRegionBuilder":
        self._country_region.id = id
        return self

    def name(self, name: List[I18n]) -> "CountryRegionBuilder":
        self._country_region.name = name
        return self

    def alpha_3_code(self, alpha_3_code: str) -> "CountryRegionBuilder":
        self._country_region.alpha_3_code = alpha_3_code
        return self

    def alpha_2_code(self, alpha_2_code: str) -> "CountryRegionBuilder":
        self._country_region.alpha_2_code = alpha_2_code
        return self

    def build(self) -> "CountryRegion":
        return self._country_region
