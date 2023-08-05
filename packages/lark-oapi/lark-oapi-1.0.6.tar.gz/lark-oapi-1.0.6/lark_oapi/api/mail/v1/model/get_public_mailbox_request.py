# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetPublicMailboxRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.public_mailbox_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetPublicMailboxRequestBuilder":
        return GetPublicMailboxRequestBuilder()


class GetPublicMailboxRequestBuilder(object):

    def __init__(self) -> None:
        get_public_mailbox_request = GetPublicMailboxRequest()
        get_public_mailbox_request.http_method = HttpMethod.GET
        get_public_mailbox_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id"
        get_public_mailbox_request.token_types = {AccessTokenType.TENANT}
        self._get_public_mailbox_request: GetPublicMailboxRequest = get_public_mailbox_request

    def public_mailbox_id(self, public_mailbox_id: str) -> "GetPublicMailboxRequestBuilder":
        self._get_public_mailbox_request.public_mailbox_id = public_mailbox_id
        self._get_public_mailbox_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def build(self) -> GetPublicMailboxRequest:
        return self._get_public_mailbox_request
