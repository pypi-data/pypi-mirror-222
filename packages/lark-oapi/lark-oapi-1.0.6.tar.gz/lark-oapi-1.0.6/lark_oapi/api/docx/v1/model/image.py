# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Image(object):
    _types = {
        "width": int,
        "height": int,
        "token": str,
        "align": int,
    }

    def __init__(self, d=None):
        self.width: Optional[int] = None
        self.height: Optional[int] = None
        self.token: Optional[str] = None
        self.align: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageBuilder":
        return ImageBuilder()


class ImageBuilder(object):
    def __init__(self) -> None:
        self._image = Image()

    def width(self, width: int) -> "ImageBuilder":
        self._image.width = width
        return self

    def height(self, height: int) -> "ImageBuilder":
        self._image.height = height
        return self

    def token(self, token: str) -> "ImageBuilder":
        self._image.token = token
        return self

    def align(self, align: int) -> "ImageBuilder":
        self._image.align = align
        return self

    def build(self) -> "Image":
        return self._image
