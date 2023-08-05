# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BaseCountry(object):
    _types = {
        "zh_name": str,
        "en_name": str,
        "code": str,
        "location_type": int,
    }

    def __init__(self, d=None):
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.code: Optional[str] = None
        self.location_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BaseCountryBuilder":
        return BaseCountryBuilder()


class BaseCountryBuilder(object):
    def __init__(self) -> None:
        self._base_country = BaseCountry()

    def zh_name(self, zh_name: str) -> "BaseCountryBuilder":
        self._base_country.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "BaseCountryBuilder":
        self._base_country.en_name = en_name
        return self

    def code(self, code: str) -> "BaseCountryBuilder":
        self._base_country.code = code
        return self

    def location_type(self, location_type: int) -> "BaseCountryBuilder":
        self._base_country.location_type = location_type
        return self

    def build(self) -> "BaseCountry":
        return self._base_country
