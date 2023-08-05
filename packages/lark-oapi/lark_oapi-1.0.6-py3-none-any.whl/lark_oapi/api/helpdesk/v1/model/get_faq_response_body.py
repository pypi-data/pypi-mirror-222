# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .faq import Faq


class GetFaqResponseBody(object):
    _types = {
        "faq": Faq,
    }

    def __init__(self, d=None):
        self.faq: Optional[Faq] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetFaqResponseBodyBuilder":
        return GetFaqResponseBodyBuilder()


class GetFaqResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_faq_response_body = GetFaqResponseBody()

    def faq(self, faq: Faq) -> "GetFaqResponseBodyBuilder":
        self._get_faq_response_body.faq = faq
        return self

    def build(self) -> "GetFaqResponseBody":
        return self._get_faq_response_body
