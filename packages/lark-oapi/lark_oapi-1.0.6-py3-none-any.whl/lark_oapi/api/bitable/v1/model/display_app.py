# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DisplayApp(object):
    _types = {
        "app_token": str,
        "name": str,
        "revision": int,
        "is_advanced": bool,
    }

    def __init__(self, d=None):
        self.app_token: Optional[str] = None
        self.name: Optional[str] = None
        self.revision: Optional[int] = None
        self.is_advanced: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DisplayAppBuilder":
        return DisplayAppBuilder()


class DisplayAppBuilder(object):
    def __init__(self) -> None:
        self._display_app = DisplayApp()

    def app_token(self, app_token: str) -> "DisplayAppBuilder":
        self._display_app.app_token = app_token
        return self

    def name(self, name: str) -> "DisplayAppBuilder":
        self._display_app.name = name
        return self

    def revision(self, revision: int) -> "DisplayAppBuilder":
        self._display_app.revision = revision
        return self

    def is_advanced(self, is_advanced: bool) -> "DisplayAppBuilder":
        self._display_app.is_advanced = is_advanced
        return self

    def build(self) -> "DisplayApp":
        return self._display_app
