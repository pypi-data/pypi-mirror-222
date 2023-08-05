# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class NativeRegion(object):
    _types = {
        "iso_code": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.iso_code: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NativeRegionBuilder":
        return NativeRegionBuilder()


class NativeRegionBuilder(object):
    def __init__(self) -> None:
        self._native_region = NativeRegion()

    def iso_code(self, iso_code: str) -> "NativeRegionBuilder":
        self._native_region.iso_code = iso_code
        return self

    def name(self, name: str) -> "NativeRegionBuilder":
        self._native_region.name = name
        return self

    def build(self) -> "NativeRegion":
        return self._native_region
