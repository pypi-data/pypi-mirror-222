# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application import Application


class GetApplicationResponseBody(object):
    _types = {
        "app": Application,
    }

    def __init__(self, d=None):
        self.app: Optional[Application] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetApplicationResponseBodyBuilder":
        return GetApplicationResponseBodyBuilder()


class GetApplicationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_application_response_body = GetApplicationResponseBody()

    def app(self, app: Application) -> "GetApplicationResponseBodyBuilder":
        self._get_application_response_body.app = app
        return self

    def build(self) -> "GetApplicationResponseBody":
        return self._get_application_response_body
