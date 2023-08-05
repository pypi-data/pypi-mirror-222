# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Style(object):
    _types = {
        "range": str,
        "styles": List[list],
    }

    def __init__(self, d=None):
        self.range: Optional[str] = None
        self.styles: Optional[List[list]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StyleBuilder":
        return StyleBuilder()


class StyleBuilder(object):
    def __init__(self) -> None:
        self._style = Style()

    def range(self, range: str) -> "StyleBuilder":
        self._style.range = range
        return self

    def styles(self, styles: List[list]) -> "StyleBuilder":
        self._style.styles = styles
        return self

    def build(self) -> "Style":
        return self._style
