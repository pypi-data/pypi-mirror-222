# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .code_name_object import CodeNameObject
from .i18n import I18n


class CommonAddress(object):
    _types = {
        "id": str,
        "name": I18n,
        "district": CodeNameObject,
        "city": CodeNameObject,
        "state": CodeNameObject,
        "country": CodeNameObject,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.district: Optional[CodeNameObject] = None
        self.city: Optional[CodeNameObject] = None
        self.state: Optional[CodeNameObject] = None
        self.country: Optional[CodeNameObject] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommonAddressBuilder":
        return CommonAddressBuilder()


class CommonAddressBuilder(object):
    def __init__(self) -> None:
        self._common_address = CommonAddress()

    def id(self, id: str) -> "CommonAddressBuilder":
        self._common_address.id = id
        return self

    def name(self, name: I18n) -> "CommonAddressBuilder":
        self._common_address.name = name
        return self

    def district(self, district: CodeNameObject) -> "CommonAddressBuilder":
        self._common_address.district = district
        return self

    def city(self, city: CodeNameObject) -> "CommonAddressBuilder":
        self._common_address.city = city
        return self

    def state(self, state: CodeNameObject) -> "CommonAddressBuilder":
        self._common_address.state = state
        return self

    def country(self, country: CodeNameObject) -> "CommonAddressBuilder":
        self._common_address.country = country
        return self

    def build(self) -> "CommonAddress":
        return self._common_address
