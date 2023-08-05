# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .extend_field import ExtendField


class VendorAddress(object):
    _types = {
        "id": int,
        "country": str,
        "province": str,
        "city": str,
        "county": str,
        "address": str,
        "extend_info": List[ExtendField],
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.country: Optional[str] = None
        self.province: Optional[str] = None
        self.city: Optional[str] = None
        self.county: Optional[str] = None
        self.address: Optional[str] = None
        self.extend_info: Optional[List[ExtendField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VendorAddressBuilder":
        return VendorAddressBuilder()


class VendorAddressBuilder(object):
    def __init__(self) -> None:
        self._vendor_address = VendorAddress()

    def id(self, id: int) -> "VendorAddressBuilder":
        self._vendor_address.id = id
        return self

    def country(self, country: str) -> "VendorAddressBuilder":
        self._vendor_address.country = country
        return self

    def province(self, province: str) -> "VendorAddressBuilder":
        self._vendor_address.province = province
        return self

    def city(self, city: str) -> "VendorAddressBuilder":
        self._vendor_address.city = city
        return self

    def county(self, county: str) -> "VendorAddressBuilder":
        self._vendor_address.county = county
        return self

    def address(self, address: str) -> "VendorAddressBuilder":
        self._vendor_address.address = address
        return self

    def extend_info(self, extend_info: List[ExtendField]) -> "VendorAddressBuilder":
        self._vendor_address.extend_info = extend_info
        return self

    def build(self) -> "VendorAddress":
        return self._vendor_address
