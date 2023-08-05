# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Document(object):
    _types = {
        "document_id": str,
        "revision_id": int,
        "title": str,
    }

    def __init__(self, d=None):
        self.document_id: Optional[str] = None
        self.revision_id: Optional[int] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocumentBuilder":
        return DocumentBuilder()


class DocumentBuilder(object):
    def __init__(self) -> None:
        self._document = Document()

    def document_id(self, document_id: str) -> "DocumentBuilder":
        self._document.document_id = document_id
        return self

    def revision_id(self, revision_id: int) -> "DocumentBuilder":
        self._document.revision_id = revision_id
        return self

    def title(self, title: str) -> "DocumentBuilder":
        self._document.title = title
        return self

    def build(self) -> "Document":
        return self._document
