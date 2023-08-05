# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MultiLanguage(object):
    _types = {
        "language": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.language: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MultiLanguageBuilder":
        return MultiLanguageBuilder()


class MultiLanguageBuilder(object):
    def __init__(self) -> None:
        self._multi_language = MultiLanguage()

    def language(self, language: str) -> "MultiLanguageBuilder":
        self._multi_language.language = language
        return self

    def value(self, value: str) -> "MultiLanguageBuilder":
        self._multi_language.value = value
        return self

    def build(self) -> "MultiLanguage":
        return self._multi_language
