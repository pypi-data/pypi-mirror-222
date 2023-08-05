# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AuditAndroidContext(object):
    _types = {
        "udid": str,
        "did": str,
        "app_ver": str,
        "ver": str,
        "region": str,
        "id_i": str,
        "id_r": str,
        "hw_brand": str,
        "hw_manuf": str,
        "wifip": str,
        "route_iip": str,
        "route_gip": str,
        "env_su": str,
        "env_tz": str,
        "env_ml": str,
        "location": str,
        "active_ip": str,
        "active_ip_detail": str,
        "cell_base_station": str,
        "i_p": str,
    }

    def __init__(self, d=None):
        self.udid: Optional[str] = None
        self.did: Optional[str] = None
        self.app_ver: Optional[str] = None
        self.ver: Optional[str] = None
        self.region: Optional[str] = None
        self.id_i: Optional[str] = None
        self.id_r: Optional[str] = None
        self.hw_brand: Optional[str] = None
        self.hw_manuf: Optional[str] = None
        self.wifip: Optional[str] = None
        self.route_iip: Optional[str] = None
        self.route_gip: Optional[str] = None
        self.env_su: Optional[str] = None
        self.env_tz: Optional[str] = None
        self.env_ml: Optional[str] = None
        self.location: Optional[str] = None
        self.active_ip: Optional[str] = None
        self.active_ip_detail: Optional[str] = None
        self.cell_base_station: Optional[str] = None
        self.i_p: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditAndroidContextBuilder":
        return AuditAndroidContextBuilder()


class AuditAndroidContextBuilder(object):
    def __init__(self) -> None:
        self._audit_android_context = AuditAndroidContext()

    def udid(self, udid: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.udid = udid
        return self

    def did(self, did: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.did = did
        return self

    def app_ver(self, app_ver: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.app_ver = app_ver
        return self

    def ver(self, ver: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.ver = ver
        return self

    def region(self, region: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.region = region
        return self

    def id_i(self, id_i: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.id_i = id_i
        return self

    def id_r(self, id_r: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.id_r = id_r
        return self

    def hw_brand(self, hw_brand: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.hw_brand = hw_brand
        return self

    def hw_manuf(self, hw_manuf: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.hw_manuf = hw_manuf
        return self

    def wifip(self, wifip: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.wifip = wifip
        return self

    def route_iip(self, route_iip: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.route_iip = route_iip
        return self

    def route_gip(self, route_gip: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.route_gip = route_gip
        return self

    def env_su(self, env_su: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.env_su = env_su
        return self

    def env_tz(self, env_tz: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.env_tz = env_tz
        return self

    def env_ml(self, env_ml: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.env_ml = env_ml
        return self

    def location(self, location: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.location = location
        return self

    def active_ip(self, active_ip: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.active_ip = active_ip
        return self

    def active_ip_detail(self, active_ip_detail: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.active_ip_detail = active_ip_detail
        return self

    def cell_base_station(self, cell_base_station: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.cell_base_station = cell_base_station
        return self

    def i_p(self, i_p: str) -> "AuditAndroidContextBuilder":
        self._audit_android_context.i_p = i_p
        return self

    def build(self) -> "AuditAndroidContext":
        return self._audit_android_context
