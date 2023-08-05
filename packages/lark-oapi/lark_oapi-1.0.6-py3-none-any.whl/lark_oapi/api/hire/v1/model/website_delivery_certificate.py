# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .website_delivery_customized_data import WebsiteDeliveryCustomizedData


class WebsiteDeliveryCertificate(object):
    _types = {
        "customized_data": List[WebsiteDeliveryCustomizedData],
        "desc": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.customized_data: Optional[List[WebsiteDeliveryCustomizedData]] = None
        self.desc: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryCertificateBuilder":
        return WebsiteDeliveryCertificateBuilder()


class WebsiteDeliveryCertificateBuilder(object):
    def __init__(self) -> None:
        self._website_delivery_certificate = WebsiteDeliveryCertificate()

    def customized_data(self,
                        customized_data: List[WebsiteDeliveryCustomizedData]) -> "WebsiteDeliveryCertificateBuilder":
        self._website_delivery_certificate.customized_data = customized_data
        return self

    def desc(self, desc: str) -> "WebsiteDeliveryCertificateBuilder":
        self._website_delivery_certificate.desc = desc
        return self

    def name(self, name: str) -> "WebsiteDeliveryCertificateBuilder":
        self._website_delivery_certificate.name = name
        return self

    def build(self) -> "WebsiteDeliveryCertificate":
        return self._website_delivery_certificate
