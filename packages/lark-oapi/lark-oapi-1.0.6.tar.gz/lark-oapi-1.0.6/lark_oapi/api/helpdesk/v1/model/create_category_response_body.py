# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .category import Category


class CreateCategoryResponseBody(object):
    _types = {
        "category": Category,
    }

    def __init__(self, d=None):
        self.category: Optional[Category] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCategoryResponseBodyBuilder":
        return CreateCategoryResponseBodyBuilder()


class CreateCategoryResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_category_response_body = CreateCategoryResponseBody()

    def category(self, category: Category) -> "CreateCategoryResponseBodyBuilder":
        self._create_category_response_body.category = category
        return self

    def build(self) -> "CreateCategoryResponseBody":
        return self._create_category_response_body
