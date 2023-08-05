# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Gadget(object):
    _types = {
        "enable_pc_mode": int,
        "schema_urls": List[str],
        "pc_use_mobile_pkg": bool,
        "pc_version": str,
        "mobile_version": str,
        "mobile_min_lark_version": str,
        "pc_min_lark_version": str,
    }

    def __init__(self, d=None):
        self.enable_pc_mode: Optional[int] = None
        self.schema_urls: Optional[List[str]] = None
        self.pc_use_mobile_pkg: Optional[bool] = None
        self.pc_version: Optional[str] = None
        self.mobile_version: Optional[str] = None
        self.mobile_min_lark_version: Optional[str] = None
        self.pc_min_lark_version: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GadgetBuilder":
        return GadgetBuilder()


class GadgetBuilder(object):
    def __init__(self) -> None:
        self._gadget = Gadget()

    def enable_pc_mode(self, enable_pc_mode: int) -> "GadgetBuilder":
        self._gadget.enable_pc_mode = enable_pc_mode
        return self

    def schema_urls(self, schema_urls: List[str]) -> "GadgetBuilder":
        self._gadget.schema_urls = schema_urls
        return self

    def pc_use_mobile_pkg(self, pc_use_mobile_pkg: bool) -> "GadgetBuilder":
        self._gadget.pc_use_mobile_pkg = pc_use_mobile_pkg
        return self

    def pc_version(self, pc_version: str) -> "GadgetBuilder":
        self._gadget.pc_version = pc_version
        return self

    def mobile_version(self, mobile_version: str) -> "GadgetBuilder":
        self._gadget.mobile_version = mobile_version
        return self

    def mobile_min_lark_version(self, mobile_min_lark_version: str) -> "GadgetBuilder":
        self._gadget.mobile_min_lark_version = mobile_min_lark_version
        return self

    def pc_min_lark_version(self, pc_min_lark_version: str) -> "GadgetBuilder":
        self._gadget.pc_min_lark_version = pc_min_lark_version
        return self

    def build(self) -> "Gadget":
        return self._gadget
