# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_update_document_block_request_body import BatchUpdateDocumentBlockRequestBody


class BatchUpdateDocumentBlockRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.document_revision_id: Optional[int] = None
        self.client_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.document_id: Optional[str] = None
        self.request_body: Optional[BatchUpdateDocumentBlockRequestBody] = None

    @staticmethod
    def builder() -> "BatchUpdateDocumentBlockRequestBuilder":
        return BatchUpdateDocumentBlockRequestBuilder()


class BatchUpdateDocumentBlockRequestBuilder(object):

    def __init__(self) -> None:
        batch_update_document_block_request = BatchUpdateDocumentBlockRequest()
        batch_update_document_block_request.http_method = HttpMethod.PATCH
        batch_update_document_block_request.uri = "/open-apis/docx/v1/documents/:document_id/blocks/batch_update"
        batch_update_document_block_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._batch_update_document_block_request: BatchUpdateDocumentBlockRequest = batch_update_document_block_request

    def document_revision_id(self, document_revision_id: int) -> "BatchUpdateDocumentBlockRequestBuilder":
        self._batch_update_document_block_request.document_revision_id = document_revision_id
        self._batch_update_document_block_request.add_query("document_revision_id", document_revision_id)
        return self

    def client_token(self, client_token: str) -> "BatchUpdateDocumentBlockRequestBuilder":
        self._batch_update_document_block_request.client_token = client_token
        self._batch_update_document_block_request.add_query("client_token", client_token)
        return self

    def user_id_type(self, user_id_type: str) -> "BatchUpdateDocumentBlockRequestBuilder":
        self._batch_update_document_block_request.user_id_type = user_id_type
        self._batch_update_document_block_request.add_query("user_id_type", user_id_type)
        return self

    def document_id(self, document_id: str) -> "BatchUpdateDocumentBlockRequestBuilder":
        self._batch_update_document_block_request.document_id = document_id
        self._batch_update_document_block_request.paths["document_id"] = str(document_id)
        return self

    def request_body(self,
                     request_body: BatchUpdateDocumentBlockRequestBody) -> "BatchUpdateDocumentBlockRequestBuilder":
        self._batch_update_document_block_request.request_body = request_body
        self._batch_update_document_block_request.body = request_body
        return self

    def build(self) -> BatchUpdateDocumentBlockRequest:
        return self._batch_update_document_block_request
