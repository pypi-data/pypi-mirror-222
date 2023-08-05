# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .code_name_object import CodeNameObject
from .i18n import I18n


class Location(object):
    _types = {
        "id": str,
        "name": I18n,
        "district": CodeNameObject,
        "city": CodeNameObject,
        "state": CodeNameObject,
        "country": CodeNameObject,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.district: Optional[CodeNameObject] = None
        self.city: Optional[CodeNameObject] = None
        self.state: Optional[CodeNameObject] = None
        self.country: Optional[CodeNameObject] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LocationBuilder":
        return LocationBuilder()


class LocationBuilder(object):
    def __init__(self) -> None:
        self._location = Location()

    def id(self, id: str) -> "LocationBuilder":
        self._location.id = id
        return self

    def name(self, name: I18n) -> "LocationBuilder":
        self._location.name = name
        return self

    def district(self, district: CodeNameObject) -> "LocationBuilder":
        self._location.district = district
        return self

    def city(self, city: CodeNameObject) -> "LocationBuilder":
        self._location.city = city
        return self

    def state(self, state: CodeNameObject) -> "LocationBuilder":
        self._location.state = state
        return self

    def country(self, country: CodeNameObject) -> "LocationBuilder":
        self._location.country = country
        return self

    def active_status(self, active_status: int) -> "LocationBuilder":
        self._location.active_status = active_status
        return self

    def build(self) -> "Location":
        return self._location
