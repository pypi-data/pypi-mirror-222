# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ScanWifiInfo(object):
    _types = {
        "ssid": str,
        "bssid": str,
    }

    def __init__(self, d=None):
        self.ssid: Optional[str] = None
        self.bssid: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScanWifiInfoBuilder":
        return ScanWifiInfoBuilder()


class ScanWifiInfoBuilder(object):
    def __init__(self) -> None:
        self._scan_wifi_info = ScanWifiInfo()

    def ssid(self, ssid: str) -> "ScanWifiInfoBuilder":
        self._scan_wifi_info.ssid = ssid
        return self

    def bssid(self, bssid: str) -> "ScanWifiInfoBuilder":
        self._scan_wifi_info.bssid = bssid
        return self

    def build(self) -> "ScanWifiInfo":
        return self._scan_wifi_info
