# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApplicationJobAddress(object):
    _types = {
        "id": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationJobAddressBuilder":
        return ApplicationJobAddressBuilder()


class ApplicationJobAddressBuilder(object):
    def __init__(self) -> None:
        self._application_job_address = ApplicationJobAddress()

    def id(self, id: str) -> "ApplicationJobAddressBuilder":
        self._application_job_address.id = id
        return self

    def name(self, name: str) -> "ApplicationJobAddressBuilder":
        self._application_job_address.name = name
        return self

    def en_name(self, en_name: str) -> "ApplicationJobAddressBuilder":
        self._application_job_address.en_name = en_name
        return self

    def build(self) -> "ApplicationJobAddress":
        return self._application_job_address
