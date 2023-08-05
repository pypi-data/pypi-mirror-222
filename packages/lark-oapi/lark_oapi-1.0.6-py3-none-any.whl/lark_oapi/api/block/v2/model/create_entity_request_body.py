# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateEntityRequestBody(object):
    _types = {
        "title": str,
        "block_type_id": str,
        "source_data": str,
        "source_meta": str,
        "version": int,
        "source_link": str,
        "owner": str,
        "extra": str,
        "i18n_summary": str,
        "i18n_preview": str,
        "summary": str,
        "preview": str,
    }

    def __init__(self, d=None):
        self.title: Optional[str] = None
        self.block_type_id: Optional[str] = None
        self.source_data: Optional[str] = None
        self.source_meta: Optional[str] = None
        self.version: Optional[int] = None
        self.source_link: Optional[str] = None
        self.owner: Optional[str] = None
        self.extra: Optional[str] = None
        self.i18n_summary: Optional[str] = None
        self.i18n_preview: Optional[str] = None
        self.summary: Optional[str] = None
        self.preview: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateEntityRequestBodyBuilder":
        return CreateEntityRequestBodyBuilder()


class CreateEntityRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_entity_request_body = CreateEntityRequestBody()

    def title(self, title: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.title = title
        return self

    def block_type_id(self, block_type_id: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.block_type_id = block_type_id
        return self

    def source_data(self, source_data: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.source_data = source_data
        return self

    def source_meta(self, source_meta: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.source_meta = source_meta
        return self

    def version(self, version: int) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.version = version
        return self

    def source_link(self, source_link: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.source_link = source_link
        return self

    def owner(self, owner: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.owner = owner
        return self

    def extra(self, extra: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.extra = extra
        return self

    def i18n_summary(self, i18n_summary: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.i18n_summary = i18n_summary
        return self

    def i18n_preview(self, i18n_preview: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.i18n_preview = i18n_preview
        return self

    def summary(self, summary: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.summary = summary
        return self

    def preview(self, preview: str) -> "CreateEntityRequestBodyBuilder":
        self._create_entity_request_body.preview = preview
        return self

    def build(self) -> "CreateEntityRequestBody":
        return self._create_entity_request_body
