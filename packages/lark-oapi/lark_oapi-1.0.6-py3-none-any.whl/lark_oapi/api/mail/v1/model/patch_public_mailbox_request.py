# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .public_mailbox import PublicMailbox


class PatchPublicMailboxRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.public_mailbox_id: Optional[str] = None
        self.request_body: Optional[PublicMailbox] = None

    @staticmethod
    def builder() -> "PatchPublicMailboxRequestBuilder":
        return PatchPublicMailboxRequestBuilder()


class PatchPublicMailboxRequestBuilder(object):

    def __init__(self) -> None:
        patch_public_mailbox_request = PatchPublicMailboxRequest()
        patch_public_mailbox_request.http_method = HttpMethod.PATCH
        patch_public_mailbox_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id"
        patch_public_mailbox_request.token_types = {AccessTokenType.TENANT}
        self._patch_public_mailbox_request: PatchPublicMailboxRequest = patch_public_mailbox_request

    def public_mailbox_id(self, public_mailbox_id: str) -> "PatchPublicMailboxRequestBuilder":
        self._patch_public_mailbox_request.public_mailbox_id = public_mailbox_id
        self._patch_public_mailbox_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def request_body(self, request_body: PublicMailbox) -> "PatchPublicMailboxRequestBuilder":
        self._patch_public_mailbox_request.request_body = request_body
        self._patch_public_mailbox_request.body = request_body
        return self

    def build(self) -> PatchPublicMailboxRequest:
        return self._patch_public_mailbox_request
