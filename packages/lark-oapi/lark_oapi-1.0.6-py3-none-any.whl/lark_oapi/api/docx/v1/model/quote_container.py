# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class QuoteContainer(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QuoteContainerBuilder":
        return QuoteContainerBuilder()


class QuoteContainerBuilder(object):
    def __init__(self) -> None:
        self._quote_container = QuoteContainer()

    def build(self) -> "QuoteContainer":
        return self._quote_container
