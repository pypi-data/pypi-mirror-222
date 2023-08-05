# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ContentColor(object):
    _types = {
        "red": int,
        "green": int,
        "blue": int,
        "alpha": float,
    }

    def __init__(self, d=None):
        self.red: Optional[int] = None
        self.green: Optional[int] = None
        self.blue: Optional[int] = None
        self.alpha: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentColorBuilder":
        return ContentColorBuilder()


class ContentColorBuilder(object):
    def __init__(self) -> None:
        self._content_color = ContentColor()

    def red(self, red: int) -> "ContentColorBuilder":
        self._content_color.red = red
        return self

    def green(self, green: int) -> "ContentColorBuilder":
        self._content_color.green = green
        return self

    def blue(self, blue: int) -> "ContentColorBuilder":
        self._content_color.blue = blue
        return self

    def alpha(self, alpha: float) -> "ContentColorBuilder":
        self._content_color.alpha = alpha
        return self

    def build(self) -> "ContentColor":
        return self._content_color
